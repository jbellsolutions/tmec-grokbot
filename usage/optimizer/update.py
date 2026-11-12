#!/usr/bin/env python3
"""The optimizer's one tool: apply an optimization update to an installed GrokBot pack, idempotently.

    python3 update.py apply <unpacked-update-dir>   copy only what's new (with a backup), print the chat steps
    python3 update.py check                         download the latest update; print "NEW <version>" or nothing
    python3 update.py init                          record the installed version (fresh installs)
    python3 update.py done <step-id>                mark a chat step done so it is never repeated
    python3 update.py status                        installed version, pending chat steps

Stdlib only. It touches only files listed in the update (inside the pack's repo folder) and its own state
file. It never sends, posts, spends, deletes outside its backup folder, or changes a schedule. Anything an
update marks "ask" is printed as an item for the owner, never done.
"""
import hashlib
import json
import os
import shutil
import sys
import tempfile
import urllib.request
import zipfile
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent            # <repo>/usage/optimizer, or the same path inside an unpacked update
CFG = json.loads((HERE / "config.json").read_text()) if (HERE / "config.json").exists() else {}
REPO = Path(os.environ.get("OPTIMIZER_REPO") or CFG.get("repo") or HERE.parent.parent)
WS = Path(os.environ.get("OPTIMIZER_WORKSPACE") or CFG.get("workspace") or REPO.parent)
STATE = WS / "state" / "optimizer-state.json"
UA = "usage-optimizer/1.0"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text())
    return {"version": None, "done": [], "history": []}


def save_state(s):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(s, indent=1))


def vkey(v):
    return tuple(int(x) if x.isdigit() else 0 for x in (v or "0").split("."))


def log(line):
    d = WS / "log"
    d.mkdir(parents=True, exist_ok=True)
    with open(d / f"runs-{datetime.now():%Y-%m}.md", "a") as f:
        f.write(f"{datetime.now():%Y-%m-%d %H:%M} · Optimizer · {line}\n")


def cmd_init():
    s = load_state()
    v = (REPO / "PACK-VERSION").read_text().strip() if (REPO / "PACK-VERSION").exists() else None
    s["version"] = s.get("version") or v
    save_state(s)
    print(f"optimizer: installed version recorded ({s['version']})")


def cmd_check():
    url = CFG.get("update_url")
    if not url:
        return  # no public update channel for this pack: updates arrive by paste only
    s = load_state()
    with tempfile.TemporaryDirectory() as t:
        z = Path(t) / "u.zip"
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=60) as r:
            z.write_bytes(r.read())
        with zipfile.ZipFile(z) as zf:
            meta = json.loads(zf.read(next(n for n in zf.namelist() if n.endswith("update.json"))))
    if vkey(meta["version"]) > vkey(s.get("version")):
        print(f"NEW {meta['version']}")


def cmd_apply(src):
    src = Path(src)
    meta = json.loads((src / "update.json").read_text())
    s = load_state()
    ver = meta["version"]
    backup = WS / "state" / "optimizer-backups" / ver
    changed, same = [], 0
    for f in meta["files"]:
        new = src / "files" / f["path"]
        dst = REPO / f["path"]
        if dst.exists() and sha(dst) == f["sha256"]:
            same += 1
            continue
        if dst.exists():
            (backup / f["path"]).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(dst, backup / f["path"])
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(new, dst)
        changed.append(f["path"])
    # this file may itself have been updated; config.json survives because updates never ship it
    s["version"] = ver if vkey(ver) > vkey(s.get("version")) else s.get("version")
    s["history"].append({"version": ver, "at": datetime.now().isoformat(timespec="seconds"), "changed": len(changed)})
    save_state(s)
    steps = [st for st in meta.get("steps", []) if st["id"] not in s["done"]]
    log(f"EXECUTED · update {ver}: {len(changed)} files changed, {same} already current, {len(steps)} chat steps")
    print(f"UPDATE {ver}: {len(changed)} files changed, {same} already current. Backup: {backup if changed else 'none needed'}")
    for p in changed[:40]:
        print(f"  changed {p}")
    if not steps:
        print("CHAT STEPS: none. Done.")
        return
    print("CHAT STEPS (do each, then run: python3 usage/optimizer/update.py done <id>):")
    for st in steps:
        print(f"- [{st['id']}] ({st.get('kind', 'do')}) {st['text']}")


def cmd_done(step):
    s = load_state()
    if step not in s["done"]:
        s["done"].append(step)
    save_state(s)
    print(f"optimizer: {step} done")


def cmd_status():
    s = load_state()
    print(json.dumps({"version": s.get("version"), "updates": s.get("history", [])[-3:], "done_steps": len(s.get("done", [])),
                      "update_url": CFG.get("update_url")}, indent=1))


def main():
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    {"init": lambda: cmd_init(), "check": lambda: cmd_check(), "status": lambda: cmd_status(),
     "apply": lambda: cmd_apply(a[1]), "done": lambda: cmd_done(a[1])}.get(a[0], lambda: sys.exit(__doc__))()


if __name__ == "__main__":
    main()
