#!/usr/bin/env python3
import subprocess
import os.path
import sys

try:
    import nuitka  # noqa: F401
except ImportError:
    raise SystemExit("This script requires installing 'nuitka' first")


subprocess.check_call(
    [
        sys.executable,
        "-mnuitka",
        "--run",
        "--standalone",
        "--include-package=PyObjCTest",
        "--include-package-data=PyObjCTest",
        os.path.join(os.path.dirname(__file__), "runtests.py"),
    ],
    cwd=os.path.dirname(os.path.dirname(__file__)),
    env={
        "PYTHONPATH": os.path.dirname(os.path.dirname(__file__)),
    },
)
