#!/usr/bin/env python

import ast
import contextlib
import glob
import os
import shutil
import subprocess
import sys
import tarfile

from setuptools import setup, Command
from setuptools.command import egg_info

VERSION = "8.4"

# Table with all framework wrappers and the OSX releases where they are
# first supported, and where support was removed. The introduced column
# is ``None`` when the framework is supported on OSX 10.4 or later. The
# removed column is ``None`` when the framework is present ont he latest
# supported OSX release.
FRAMEWORK_WRAPPERS = [
    # Name                      Introduced          Removed
    ("libdispatch", "10.8", None),
    ("Accessibility", "11.0", None),
    ("AdServices", "11.0", None),
    ("AdSupport", "10.14", None),
    ("AppTrackingTransparency", "11.0", None),
    ("AudioVideoBridging", "10.8", None),
    ("AuthenticationServices", "10.15", None),
    ("AutomaticAssessmentConfiguration", "10.15", None),
    ("AVKit", "10.9", None),
    ("AVFoundation", "10.7", None),
    ("Accounts", "10.8", None),
    ("AddressBook", None, None),
    ("AppleScriptKit", None, None),
    ("AppleScriptObjC", "10.6", None),
    ("ApplicationServices", None, None),
    ("Automator", None, None),
    ("BusinessChat", "10.14", None),
    ("CFNetwork", None, None),
    ("CalendarStore", "10.5", None),
    ("CallKit", "11.0", None),
    ("ClassKit", "11.0", None),
    ("CloudKit", "10.10", None),
    ("Cocoa", None, None),
    ("Collaboration", "10.5", None),
    ("ColorSync", "10.13", None),
    ("Contacts", "10.11", None),
    ("ContactsUI", "10.11", None),
    ("CoreAudio", None, None),
    ("CoreAudioKit", None, None),
    ("CoreBluetooth", "10.10", None),
    ("CoreData", None, None),
    ("CoreHaptics", "10.15", None),
    ("CoreLocation", "10.6", None),
    ("CoreMedia", "10.7", None),
    ("CoreMediaIO", "10.7", None),
    ("CoreMIDI", None, None),
    ("CoreML", "10.13", None),
    ("CoreMotion", "10.15", None),
    ("CoreServices", None, None),
    ("CoreSpotlight", "10.13", None),
    ("CoreText", None, None),
    ("CoreWLAN", "10.6", None),
    ("CryptoTokenKit", "10.10", None),
    ("DataDetection", "12.0", None),
    ("DeviceCheck", "10.15", None),
    ("DictionaryServices", "10.5", None),
    ("DiscRecording", None, None),
    ("DiscRecordingUI", None, None),
    ("DiskArbitration", None, None),
    ("DVDPlayback", None, None),
    ("EventKit", "10.8", None),
    ("ExceptionHandling", None, None),
    ("ExecutionPolicy", "10.15", None),
    ("ExternalAccessory", "10.13", None),
    ("FileProvider", "10.15", None),
    ("FileProviderUI", "10.15", None),
    ("FSEvents", "10.5", None),
    ("FinderSync", "10.10", None),
    ("GameCenter", "10.8", None),
    ("GameController", "10.9", None),
    ("IMServicePlugIn", "10.7", None),
    ("InputMethodKit", "10.5", None),
    ("ImageCaptureCore", "10.6", None),
    ("Intents", "10.12", None),
    ("IntentsUI", "12.0", None),
    ("InstallerPlugins", None, None),
    ("InstantMessage", "10.5", None),
    # ("IOBluetooth", "10.2", None),
    # ("IOBluetoothUI", "10.2", None),
    ("IOSurface", "10.6", None),
    ("KernelManagement", "11.0", None),
    ("LatentSemanticMapping", None, None),
    ("LaunchServices", None, None),
    ("LinkPresentation", "10.15", None),
    ("LocalAuthentication", "10.10", None),
    ("LocalAuthenticationEmbeddedUI", "12.0", None),
    ("MailKit", "12.0", None),
    ("MapKit", "10.9", None),
    ("MediaAccessibility", "10.9", None),
    ("MediaLibrary", "10.9", None),
    ("MediaPlayer", "10.12", None),
    ("MediaToolbox", "10.9", None),
    ("Message", None, "10.9"),
    ("Metal", "10.11", None),
    ("MetalKit", "10.11", None),
    ("MetalPerformanceShaders", "10.13", None),
    ("MetalPerformanceShadersGraph", "11.0", None),
    ("MetricKit", "12.0", None),
    ("MLCompute", "11.0", None),
    ("ModelIO", "10.11", None),
    ("MultipeerConnectivity", "10.10", None),
    ("NaturalLanguage", "10.14", None),
    ("NetFS", "10.6", None),
    ("Network", "10.14", None),
    ("NetworkExtension", "10.11", None),
    ("NotificationCenter", "10.10", None),
    ("OpenDirectory", "10.6", None),
    ("OSAKit", None, None),
    ("OSLog", "10.15", None),
    ("PassKit", "11.0", None),
    ("PencilKit", "10.15", None),
    ("Photos", "10.11", None),
    ("PhotosUI", "10.11", None),
    ("PreferencePanes", None, None),
    ("PubSub", "10.5", "10.14"),
    ("PushKit", "10.15", None),
    ("Quartz", None, None),
    ("QuickLookThumbnailing", "10.15", None),
    ("ReplayKit", "11.0", None),
    ("SafariServices", "10.11", None),
    ("ScreenSaver", None, None),
    ("ScreenTime", "11.0", None),
    ("ScriptingBridge", "10.5", None),
    ("Security", None, None),
    ("SecurityFoundation", None, None),
    ("SecurityInterface", None, None),
    ("SearchKit", None, None),
    ("ServerNotification", "10.6", "10.9"),
    ("ServiceManagement", "10.6", None),
    ("ShazamKit", "12.0", None),
    ("Social", "10.8", None),
    ("Speech", "10.15", None),
    ("SpriteKit", "10.9", None),
    ("StoreKit", "10.7", None),
    ("SyncServices", None, None),
    ("SystemConfiguration", None, None),
    ("WebKit", None, None),
    ("GameKit", "10.8", None),
    ("GameplayKit", "10.11", None),
    ("SceneKit", "10.7", None),
    ("SoundAnalysis", "10.15", None),
    ("ScreenCaptureKit", "12.3", None),
    ("SystemExtensions", "10.15", None),
    ("UniformTypeIdentifiers", "11.0", None),
    ("UserNotifications", "10.14", None),
    ("UserNotificationsUI", "11.0", None),
    ("VideoSubscriberAccount", "10.14", None),
    ("VideoToolbox", "10.8", None),
    ("Virtualization", "11.0", None),
    ("Vision", "10.13", None),
    # iTunes library is shipped with iTunes, not part of macOS 'core'
    # Requires iTunes 11 or later, which is not available on 10.5
    ("iTunesLibrary", "10.6", None),
]

MACOS_TO_DARWIN = {
    "10.2": "6.0",
    "10.3": "7.0",
    "10.4": "8.0",
    "10.5": "9.0",
    "10.6": "10.0",
    "10.7": "11.0",
    "10.8": "12.0",
    "10.9": "13.0",
    "10.10": "14.0",
    "10.11": "15.0",
    "10.12": "16.0",
    "10.13": "17.0",
    "10.14": "18.0",
    "10.15": "19.0",
    "11.0": "20.0",
    "12.0": "21.0",
    "12.3": "21.3",
}


BASE_REQUIRES = ["pyobjc-core==" + VERSION]


def version_key(version):
    return tuple(int(x) for x in version.split("."))


def framework_requires(include_all=False):
    if sys.platform != "darwin":
        raise SystemExit("ERROR: Requires macOS to install or build")

    result = []

    for name, introduced, removed in FRAMEWORK_WRAPPERS:

        marker = []
        if introduced is not None:
            marker.append(f'platform_release>="{MACOS_TO_DARWIN[introduced]}"')

        if removed is not None:
            marker.append(f'platform_release<"{MACOS_TO_DARWIN[removed]}"')

        if marker:
            marker = ";{}".format(" and ".join(marker))
        else:
            marker = ""

        if include_all:
            result.append(f"pyobjc-framework-{name}=={VERSION}")
        else:
            result.append(f"pyobjc-framework-{name}=={VERSION}{marker}")

    return result


# Some PyPI stuff
LONG_DESCRIPTION = """
PyObjC is a bridge between Python and Objective-C.  It allows full
featured Cocoa applications to be written in pure Python.  It is also
easy to use other frameworks containing Objective-C class libraries
from Python and to mix in Objective-C, C and C++ source.

This package is a pseudo-package that will install all pyobjc related
packages (that is, pyobjc-core as well as wrappers for frameworks on
macOS)

Project links
-------------

* `Documentation <https://pyobjc.readthedocs.io/en/latest/>`_
* `Issue Tracker <https://github.com/ronaldoussoren/pyobjc/issues>`_
* `Repository <https://github.com/ronaldoussoren/pyobjc/>`_
"""


CLASSIFIERS = list(
    filter(
        None,
        """
Development Status :: 5 - Production/Stable
Environment :: Console
Environment :: MacOS X :: Cocoa
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Natural Language :: English
Operating System :: MacOS :: MacOS X
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Programming Language :: Python :: 3.10
Programming Language :: Objective C
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Software Development :: User Interfaces
""".splitlines(),
    )
)

_SETUP_KEYS = (
    "name",
    "description",
    "min_os_level",
    "max_os_level",
    "packages",
    "namespace_packages",
    "ext_modules",
    "version",
    "install_requires",
    "long_description",
    "options",
)
_SETUP_OPTIONAL = (
    "min_os_level",
    "max_os_level",
    "ext_modules",
    "namespace_packages",
    "options",
)


def same_order(lst1, lst2):
    idx = 0
    for k in lst1:
        try:
            while lst2[idx] != k:
                idx += 1
        except IndexError:
            return False
    return True


@contextlib.contextmanager
def cwd(path):
    cur = os.getcwd()
    try:
        os.chdir(path)

        yield

    finally:
        os.chdir(cur)


class oc_test(Command):
    description = "run test suite"
    user_options = [("verbosity=", None, "print what tests are run")]

    def initialize_options(self):
        self.verbosity = 1

    def finalize_options(self):
        if isinstance(self.verbosity, str):
            self.verbosity = int(self.verbosity)

    def run(self):
        print("  validating framework list...")
        all_names = {
            nm.split("-")[-1]
            for nm in os.listdir("..")
            if nm.startswith("pyobjc-framework-")
        }
        configured_names = {x[0] for x in FRAMEWORK_WRAPPERS}
        failures = 0

        if all_names - configured_names:
            print(
                "Framework wrappers not mentioned in setup.py: %s"
                % (", ".join(sorted(all_names - configured_names)))
            )
            failures += 1
        if configured_names - all_names:
            print(
                "Framework mentioned in setup.py not in filesystem: %s"
                % (", ".join(sorted(configured_names - all_names)))
            )
            failures += 1

        print("  validating framework Modules/ directories...")
        header_files = ("pyobjc-api.h", "pyobjc-compat.h")
        templates = {}
        for fn in header_files:
            with open(os.path.join("../pyobjc-core/Modules/objc", fn), "rb") as fp:
                templates[fn] = fp.read()

        for nm in sorted(all_names):
            subdir = "../pyobjc-framework-" + nm + "/Modules"
            if not os.path.exists(subdir):
                continue

            for fn in header_files:
                if not os.path.exists(os.path.join(subdir, fn)):
                    print(f"Framework wrapper for {nm} does not contain {fn}")
                    failures += 1

                else:
                    with open(os.path.join(subdir, fn), "rb") as fp:
                        data = fp.read()

                    if data != templates[fn]:
                        print(f"Framework wrapper for {nm} contains stale {fn}")
                        failures += 1

        print("  validating framework setup files...")
        with open("../pyobjc-core/Tools/pyobjc_setup.py", "rb") as fp:
            pyobjc_setup = fp.read()

        for nm in sorted(all_names):
            subdir = "../pyobjc-framework-" + nm
            if not os.path.exists(os.path.join(subdir, "MANIFEST.in")):
                print("Framework wrapper for %s does not contain MANIFEST.in" % (nm))
                failures += 1

            if not os.path.exists(os.path.join(subdir, "License.txt")):
                print("Framework wrapper for %s does not contain MANIFEST.in" % (nm))
                failures += 1

            if not os.path.exists(os.path.join(subdir, "setup.py")):
                print("Framework wrapper for %s does not contain setup.py" % (nm))
                failures += 1

            if not os.path.exists(os.path.join(subdir, "pyobjc_setup.py")):
                print(
                    "Framework wrapper for %s does not contain pyobjc_setup.py" % (nm)
                )
                failures += 1

            else:
                with open(os.path.join(subdir, "pyobjc_setup.py"), "rb") as fp:
                    data = fp.read()
                if data != pyobjc_setup:
                    print(
                        "Framework wrapper for %s contains stale pyobjc_setup.py" % (nm)
                    )
                    failures += 1

            if not os.path.exists(os.path.join(subdir, "setup.py")):
                print("Framework wrapper for %s does not contain setup.py" % (nm))
                failures += 1
            else:
                with open(os.path.join(subdir, "setup.py")) as fp:
                    contents = fp.read()

                if "setup_requires" in contents:
                    print("Framework wrapper for %s has setup_requires" % (nm))
                    failures += 1

                a = compile(contents, subdir, "exec", ast.PyCF_ONLY_AST)
                try:
                    args = [v.arg for v in a.body[-1].value.keywords]

                    if a.body[-1].value.func.id != "setup":
                        print("Unexpected setup.py structure in wrapper for %s" % (nm))
                        failures += 1

                    elif a.body[-1].value.args:
                        print("Unexpected setup.py structure in wrapper for %s" % (nm))
                        failures += 1

                    for n in a.body:
                        if isinstance(n, ast.Assign):
                            if n.targets[0].id == "VERSION":
                                found_version = n.value.s

                except AttributeError:
                    print("Unexpected setup.py structure in wrapper for %s" % (nm))
                    failures += 1

                if not same_order(args, _SETUP_KEYS):
                    print(
                        "Unexpected order of setup.py keyword args in wrapper for %s"
                        % (nm,)
                    )
                    failures += 1

                for k in set(_SETUP_KEYS) - set(_SETUP_OPTIONAL):
                    if k not in args:
                        print(
                            "Missing %r in setup.py keyword args in wrapper for %s"
                            % (k, nm)
                        )
                        failures += 1

                if "ext_modules" not in args:
                    if os.path.exists(os.path.join(subdir, "Modules")):
                        print(
                            "No ext_modules in setup.py, but Modules subdir, "
                            "in wrapper for %s" % (nm,)
                        )
                        failures += 1

                if found_version != VERSION:
                    print(f"Bad version in wrapper for {nm}")
                    failures += 1

        print("  validating sdist archives...")
        devnull = open("/dev/null", "a")
        for nm in ("pyobjc", "pyobjc-core") + tuple(
            sorted(nm for nm in os.listdir("..") if nm.startswith("pyobjc-framework-"))
        ):
            print(f"    {nm}")
            subdir = os.path.join("..", nm)
            if os.path.exists(os.path.join(subdir, "dist")):
                shutil.rmtree(os.path.join(subdir, "dist"))

            p = subprocess.check_call(
                [sys.executable, "setup.py", "sdist"],
                cwd=subdir,
                stdout=devnull,
                stderr=devnull,
            )
            files = glob.glob(os.path.join(subdir, "dist", "*.tar.gz"))

            if not files:
                print(f"No sdist in {nm}")
                failures += 1

            elif len(files) > 1:
                print(f"Too many sdist in {nm}")
                failures += 1

            else:
                t = tarfile.open(files[0], "r:gz")
                for fn in t.getnames():
                    if fn.startswith("/"):
                        print(f"Absolute path in sdist for {nm}")
                        failures += 1

                    for p in (
                        "__pycache__",
                        ".pyc",
                        ".pyo",
                        ".so",
                        ".dSYM",
                        ".eggs",
                        ".app",
                        "/build/",
                        "/dist/",
                    ):

                        if p in fn:
                            print(f"Unwanted pattern {p!r} in sdist for {nm}: {fn}")
                            failures += 1

        print("  validating long description...")
        for nm in ("pyobjc", "pyobjc-core") + tuple(
            sorted(nm for nm in os.listdir("..") if nm.startswith("pyobjc-framework-"))
        ):
            subdir = os.path.join("..", nm)
            print(f"    {nm}")
            with cwd(subdir):
                try:
                    subprocess.check_output(
                        [sys.executable, "-mtwine", "check"] + glob.glob("dist/*")
                    )
                except subprocess.CalledProcessError as exc:
                    print("Twine failed for", nm, exc)
                    failures += 1

        filename = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "docs",
            "notes",
            "framework-wrappers.rst",
        )
        if not os.path.exists(filename):
            print("ERROR: framework-wrappers.rst not found")
            failures += 1

        else:
            frameworks = frameworks_in_table(filename)

            for fwk in os.listdir("/System/Library/Frameworks"):
                if not fwk.endswith(".framework"):
                    continue
                fwk, _ = os.path.splitext(fwk)
                if fwk not in frameworks:
                    print(f"Framework {fwk} not in framework-wrappers.rst")
                    failures += 1

        print(
            "SUMMARY: {'testSeconds': 0.0, 'count': 1, 'fails': %d, "
            "'errors': 0, 'xfails': 0, 'skip': 0, 'xpass': 0, }" % (failures,)
        )
        if failures:
            sys.exit(1)


def frameworks_in_table(filename):
    result = {}
    in_table = False
    with open(filename) as stream:

        for line in stream:
            if not in_table:
                if line.startswith("+--") or line.startswith("+=="):
                    in_table = True
                    continue

            else:
                if line.startswith("+--") or line.startswith("+=="):
                    continue
                elif not line.startswith("|"):
                    break

                cell = line.split("|")[1].strip()
                if not cell:
                    continue

                if "`" in cell:
                    cell = cell.split("`")[1].split()[0]
                    linked = True
                else:
                    linked = False

                result[cell] = linked
    return result


class oc_egg_info(egg_info.egg_info):
    def run(self):
        egg_info.egg_info.run(self)

        path = os.path.join(self.egg_info, "PKG-INFO")
        with open(path) as fp:
            contents = fp.read()

        first, middle, last = contents.partition("\n\n")

        with open(path, "w") as fp:
            fp.write(first)
            fp.write(
                "\nProject-URL: Documentation, "
                "https://pyobjc.readthedocs.io/en/latest/\n"
            )
            fp.write(
                "Project-URL: Issue tracker, "
                "https://github.com/ronaldoussoren/pyobjc/issues\n"
            )
            fp.write(
                "Project-URL: Repository, " "https://github.com/ronaldoussoren/pyobjc"
            )
            fp.write(middle)
            fp.write(last)


setup(
    name="pyobjc",
    version=VERSION,
    description="Python<->ObjC Interoperability Module",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst; charset=UTF-8",
    author="Ronald Oussoren",
    author_email="pyobjc-dev@lists.sourceforge.net",
    url="https://github.com/ronaldoussoren/pyobjc",
    platforms=["macOS"],
    packages=[],
    install_requires=BASE_REQUIRES + framework_requires(),
    extras_require={
        "allbindings": BASE_REQUIRES + framework_requires(include_all=True)
    },
    python_requires=">=3.6",
    setup_requires=[],
    classifiers=CLASSIFIERS,
    license="MIT License",
    zip_safe=True,
    # workaround for setuptools 0.6b4 bug
    dependency_links=[],
    keywords=["Objective-C", "bridge", "Cocoa"],
    cmdclass={"test": oc_test, "egg_info": oc_egg_info},
)
