"""
Common definitions for
- collect-dist-archives
- update-system-dependencies
- run-test-suite
"""

import contextlib
import os
import shutil
import subprocess
import time
from _topsort import topological_sort


PY_VERSIONS = ["3.8", "3.9", "3.10", "3.11", "3.12", "3.13", "3.13t"]

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
    return (
        subprocess.check_output(
            ["git", "describe", "--abbrev=12", "--always", "--dirty=+"], cwd=TOP_DIR
        )
        .decode("utf-8")
        .strip()
    )


def repository_commit_state():
    summary = subprocess.check_output(["git", "status"], cwd=TOP_DIR).decode("utf-8")
    for ln in summary.splitlines():
        if "Changes not staged for commit" in ln:
            return "(dirty)"
    return "(clean)"


def xcode_version():
    try:
        data = subprocess.check_output(["xcodebuild", "-version"])
        data = data.decode("utf-8")
        lines = data.splitlines()
        assert len(lines) >= 2
        return f"{lines[0]} ({lines[-1]})"

    except subprocess.CalledProcessError:
        return "Xcode not installed (cmd line tools)"


def py_version(ver):
    return (
        subprocess.check_output(
            [f"python{ver}", "-c", "import sys; print(sys.version)"]
        )
        .decode("utf-8")
        .splitlines()[0]
    )


def system_report(path, py_versions):
    with open(path, "w") as fp:
        fp.write(f"Build at:           {time.ctime()}\n")
        fp.write(f"macOS version:      {mac_ver()}\n")
        fp.write(f"Xcode version:      {xcode_version()}\n")
        fp.write(f"ID of checkout:     {repository_id()}\n")
        fp.write(f"Status of checkout: {repository_commit_state()}\n")
        fp.write("\n")

        for ver in py_versions:
            fp.write(f"Python {ver}:         {py_version(ver)}\n")


def _install_virtualenv_software(interpreter):
    subprocess.check_call([interpreter, "-mpip", "install", "-U", "pip"])
    subprocess.check_call([interpreter, "-mpip", "install", "-U", "setuptools"])
    subprocess.check_call([interpreter, "-mpip", "install", "-U", "wheel"])

    if b"PythonT.framework" not in subprocess.check_output(
        [interpreter, "-c", "import sys; print(sys.base_prefix)"]
    ):
        # Twine doesn't install for me with the free threaded build due to missing build dependencies
        subprocess.check_call([interpreter, "-mpip", "install", "-U", "twine"])


@contextlib.contextmanager
def virtualenv(interpreter):
    if os.path.exists("test-env"):
        shutil.rmtree("test-env")

    subprocess.check_call([interpreter, "-mvenv", "test-env"])

    path = "test-env/bin/python"
    if not os.path.exists(path):
        raise RuntimeError(f"VirtualEnv incomplete, no {path}")

    try:
        _install_virtualenv_software(path)
        yield os.path.abspath(path)

    finally:
        print("CLEANUP")
        shutil.rmtree("test-env")


def variants(
    ver, permitted_variants=("64bit", "x86_64", "arm64", "intel", "universal2")
):
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


def sort_framework_wrappers():
    """
    Returns a list of framework wrappers in the order they should
    be build in.
    """
    frameworks = []
    partial_order = []

    for subdir in os.listdir(TOP_DIR):
        if not subdir.startswith("pyobjc-framework-"):
            continue

        setup = os.path.join(TOP_DIR, subdir, "setup.py")

        requires = None
        with open(setup) as fp:
            for ln in fp:
                if requires is None:
                    if ln.strip().startswith("install_requires"):
                        requires = []

                        if "]" in ln:
                            # Dependencies on a single line
                            start = ln.find("[")
                            deps = ln[start + 1 :].strip().split(",")
                            for d in deps:
                                d = d.strip()[1:]
                                if d.startswith("pyobjc-framework-"):
                                    d = d.split(">")[0]
                                    requires.append(d)
                else:
                    if ln.strip().startswith("]"):
                        break

                    dep = ln.strip()[1:-1]
                    if dep.startswith("pyobjc-framework"):
                        dep = dep.split(">")[0]
                        requires.append(dep)

        frameworks.append(subdir)
        for dep in requires:
            partial_order.append((dep, subdir))

    frameworks = topological_sort(frameworks, partial_order)
    return frameworks
