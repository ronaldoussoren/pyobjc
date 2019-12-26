"""
Common definitions for
- collect-dist-archives
- update-system-dependencies
- run-test-suite
"""

import os
import subprocess
import contextlib
import shutil
import time

PY_VERSIONS = [
    "3.6",
    "3.7",
    "3.8",
    "3.9",
]

TOP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DIST_DIR = os.path.join(TOP_DIR, "distribution-dir")

_basedir = os.path.dirname(os.path.abspath(__file__))
TEST_STATE_DIR = os.path.join(TOP_DIR, "test-results", "state")
TEST_REPORT_DIR = os.path.join(TOP_DIR, "test-results", "html")
TEST_TMPL_DIR = os.path.join(_basedir, "templates")
TEST_STATIC_DIR = os.path.join(_basedir, "static")


def mac_ver():
    # Return a macOS version string that includes the Build ID
    info = {}
    for ln in subprocess.check_output("sw_vers").decode("utf-8").splitlines():
        key, value = ln.split(":", 1)
        key = key.strip()
        value = value.strip()
        info[key] = value

    return "{ProductVersion} ({BuildVersion})".format(**info)


def repository_id():
    return subprocess.check_output(["hg", "id"], cwd=TOP_DIR).decode("utf-8").strip()


def repository_commit_state():
    summary = subprocess.check_output(["hg", "summary"], cwd=TOP_DIR).decode("utf-8")
    for ln in summary.splitlines():
        if ln.startswith("commit:"):
            return ln

    raise RuntimeError("Cannot find commit status")


def xcode_version():
    data = subprocess.check_output(["xcodebuild", "-version"])
    data = data.decode("utf-8")
    lines = data.splitlines()
    assert len(lines) >= 2
    return "{} ({})".format(lines[0], lines[-1])


def py_version(ver):
    return (
        subprocess.check_output(
            ["python{}".format(ver), "-c", "import sys; print(sys.version)"]
        )
        .decode("utf-8")
        .splitlines()[0]
    )


def system_report(path, py_versions):
    with open(path, "w") as fp:
        fp.write("Build at:           {}\n".format(time.ctime()))
        fp.write("macOS version:      {}\n".format(mac_ver()))
        fp.write("Xcode version:      {}\n".format(xcode_version()))
        fp.write("ID of checkout:     {}\n".format(repository_id()))
        fp.write("Status of checkout: {}\n".format(repository_commit_state()))
        fp.write("\n")

        for ver in py_versions:
            fp.write("Python {}:         {}\n".format(ver, py_version(ver)))


def _install_virtualenv(interpreter):
    subprocess.check_call([interpreter, "-mpip", "install", "-U", "pip"])
    subprocess.check_call([interpreter, "-mpip", "install", "-U", "setuptools"])
    subprocess.check_call([interpreter, "-mpip", "install", "-U", "virtualenv"])
    subprocess.check_call([interpreter, "-mpip", "install", "-U", "wheel"])


@contextlib.contextmanager
def virtualenv(interpreter):
    if os.path.exists("test-env"):
        shutil.rmtree("test-env")

    _install_virtualenv(interpreter)

    subprocess.check_call([interpreter, "-mvirtualenv", "test-env"])
    if not os.path.exists("test-env/bin/python"):
        raise RuntimeError("VirtualEnv incomplete")

    try:
        yield os.path.abspath("test-env/bin/python")

    finally:
        print("CLEANUP")
        shutil.rmtree("test-env")


def variants(ver, permitted_variants={"64bit"}):
    if os.path.islink(
        os.path.join("/Library/Frameworks/Python.framework/Versions", ver)
    ):

        result = []
        for nm in os.listdir("/Library/Frameworks/Python.framework/Versions"):
            if nm == ver:
                continue

            v, _, s = nm.partition("-")

            if permitted_variants and s not in permitted_variants:
                continue
            if v == ver:
                result.append(nm)

        if result:
            return result

    return [ver]


def setup_variant(ver, variant):
    if ver == variant:
        return

    tgt = os.path.join("/Library/Frameworks/Python.framework/Versions", ver)

    if os.path.exists(tgt):
        os.unlink(tgt)

    os.symlink(variant, tgt)
