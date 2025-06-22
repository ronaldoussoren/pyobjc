"""
The implementation for the install.py and develop.py
scripts in the root of the repository.
"""

import os
import plistlib
import shlex
import shutil
import subprocess
import sys
from sysconfig import get_config_var
from _common_definitions import RED, BOLD, RESET, sort_framework_wrappers

TOPDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_os_level() -> str:
    with open("/System/Library/CoreServices/SystemVersion.plist", "rb") as fp:
        pl = plistlib.load(fp)
    v = pl["ProductVersion"]
    return ".".join(v.split(".")[:2])


def get_sdk_level() -> str | None:
    cflags = get_config_var("CFLAGS")
    cflags = shlex.split(cflags)
    for i, val in enumerate(cflags):
        if val == "-isysroot":
            sdk = cflags[i + 1]
            break
    else:
        return None

    if sdk == "/":
        return get_os_level()

    sdkname = os.path.basename(sdk)
    assert sdkname.startswith("MacOSX")
    assert sdkname.endswith(".sdk")

    settings_path = os.path.join(sdk, "SDKSettings.plist")
    if os.path.exists(settings_path):
        try:
            with open(os.path.join(sdk, "SDKSettings.plist"), "rb") as fp:
                pl = plistlib.load(fp)
            assert isinstance(pl["Version"], str)
            return pl["Version"]
        except Exception:
            raise SystemExit("Cannot determine SDK version")
    else:
        version_part = sdkname[6:-4]
        assert version_part != ""
        return version_part


def build_project(project: str, extra_arg: str | None) -> bool:
    proj_dir = os.path.join(TOPDIR, project)

    # First ask distutils to clean up
    print(f"Cleaning {project!r} using {sys.executable!r}")
    status = subprocess.call([sys.executable, "setup.py", "clean"], cwd=proj_dir)
    if status != 0:
        print(f"{RED}Cleaning of {project!r} failed, status {status}{RESET}")
        return False

    # Explicitly remove the 'build' directory, just in case...
    if os.path.exists(os.path.join(proj_dir, "build")):
        shutil.rmtree(os.path.join(proj_dir, "build"))

    print(f"Installing {project!r} using {sys.executable!r}, {extra_arg}")
    status = subprocess.call(
        [
            sys.executable,
            "-mpip",
            "install",
            "--no-cache-dir",
        ]
        + ([extra_arg, "."] if extra_arg is not None else ["."]),
        cwd=proj_dir,
    )

    if status != 0:
        print(f"{RED}Installing {project!r} failed (status {status}){RESET}")
        return False

    return True


def version_key(version: str) -> tuple[int, ...]:
    return tuple(int(x) for x in version.split("."))


def main(extra_arg: str | None = None) -> None:
    if sys.platform != "darwin":
        print("{RED}PyObjC requires macOS{RESET}")
        sys.exit(1)

    subprocess.check_call(
        [sys.executable, "-mpip", "install", "-U", "setuptools", "pip", "wheel"]
    )

    all_projects = ["pyobjc-core"] + sort_framework_wrappers()
    for idx, project in enumerate(all_projects):
        print()
        print(
            f"{BOLD}{idx + 1}/{len(all_projects)}: Building project {project!r}{RESET}"
        )
        print()
        if not build_project(project, extra_arg):
            print(f"{RED}Cannot build one of the projects, bailing out{RESET}")
            sys.exit(1)
