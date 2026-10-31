"""Checks catalog.json for the public Durweg catalog (Durweg plan v1.1 D4).

For every entry: the name and fields are valid; the repository is on GitHub and public; it has
a README and a LICENSE; its workflow.json is valid for Durweg and the files it names exist. Run in CI on every pull request:
    python tools/check_catalog.py <folder with a checkout of musetee/durweg>
"""

import json
import re
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

NAME = re.compile(r"^[a-z0-9][a-z0-9-]*$")
URL = re.compile(r"^https://github\.com/([A-Za-z0-9-]+/[A-Za-z0-9._-]+?)(?:\.git)?$")


def public(repo):
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}", headers={"User-Agent": "durweg-catalog"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:          # no token: only public ones answer
            return not json.load(r).get("private", True)
    except OSError:
        return False


def main(durweg):
    sys.path.insert(0, str(Path(durweg).resolve()))
    from durweg import workflow
    data = json.loads(Path("catalog.json").read_text(encoding="utf-8"))
    problems = []
    if data.get("format") != 1 or not isinstance(data.get("workflows"), dict):
        print('catalog.json: needs {"format": 1, "workflows": {...}}')
        return 1
    for name, e in sorted(data["workflows"].items()):
        where = f"{name}:"
        if not NAME.match(name):
            problems.append(f"{where} names use lower-case letters, digits and -")
            continue
        if not isinstance(e, dict) or not all(isinstance(e.get(k), str) and e[k] for k in ("title", "summary", "url")):
            problems.append(f"{where} needs title, summary and url")
            continue
        m = URL.match(e["url"])
        if not m:
            problems.append(f"{where} url must be https://github.com/<owner>/<repo>(.git)")
            continue
        if not public(m.group(1)):
            problems.append(f"{where} {m.group(1)} is not a public GitHub repository")
            continue
        with tempfile.TemporaryDirectory() as tmp:
            r = subprocess.run(["git", "clone", "-q", "--depth", "1", e["url"], tmp + "/w"], capture_output=True, text=True)
            if r.returncode != 0:
                problems.append(f"{where} cannot be cloned: {r.stderr.strip()[-200:]}")
                continue
            w = Path(tmp) / "w"
            if not any((w / f).is_file() for f in ("README.md", "README", "README_cn.md")):
                problems.append(f"{where} has no README.md")
            if not any((w / f).is_file() for f in ("LICENSE", "LICENSE.md", "LICENSE.txt")):
                problems.append(f"{where} has no LICENSE")
            try:
                wf = workflow.load(w)
                workflow.snapshot_sources(wf)      # the skill folder, snapshot files and gate scripts exist
            except Exception as ex:                                  # a WfError, or anything else
                problems.append(f"{where} workflow.json is not valid: {ex}")
        print(f"checked {name}")
    for p in problems:
        print("PROBLEM", p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
