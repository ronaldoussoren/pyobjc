#!/usr/bin/env python3
import subprocess
import sys
import pathlib

MYDIR = pathlib.Path(__file__).parent
ROOT = MYDIR.parent

try:
    import nuitka  # noqa: F401
except ImportError:
    raise SystemExit("This script requires installing 'nuitka' first")

print(sys.executable)
subprocess.check_call(
    [
        sys.executable,
        "-mnuitka",
        "--run",
        "--standalone",
        "--include-package=PyObjCTest",
        "--include-package-data=PyObjCTest",
        MYDIR / "runtests.py",
    ],
    cwd=ROOT,
    env={"PYTHONPATH": str(ROOT)},
)
