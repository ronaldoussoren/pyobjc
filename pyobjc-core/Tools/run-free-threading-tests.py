#!/usr/bin/env python
"""
Run the various tests in the free-threading
directory and report on the results.
"""
import pathlib
import subprocess
import sys

test_dir = pathlib.Path(__file__).resolve().parent / "free-threading"

failed = []
for script in test_dir.iterdir():
    if script.name in ("_tools.py", "__pycache__"):
        continue
    print(script)
    print("=" * len(str(script)))
    print()
    try:
        subprocess.check_call([sys.executable, str(script)])
    except subprocess.CalledProcessError:
        failed.append(script)

if failed:
    print()
    print(f"{len(failed)} scripts failed")

else:
    print("")
    print("OK: all scripts successful")
