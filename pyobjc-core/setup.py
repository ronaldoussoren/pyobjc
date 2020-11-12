import glob
import os
import plistlib
import shlex
import tempfile
import sys
import subprocess
import warnings
from setuptools import Extension, setup
from setuptools.command import build_ext, build_py, egg_info, install_lib, test
from distutils import log
from distutils.errors import DistutilsError, DistutilsPlatformError, DistutilsSetupError
from distutils.sysconfig import get_config_var as _get_config_var
from distutils.sysconfig import get_config_vars

from pkg_resources import add_activation_listener, normalize_path, require, working_set


def get_config_var(var):
    return _get_config_var(var) or ""


# We need at least Python 3.6
MIN_PYTHON = (3, 6)

if sys.version_info < MIN_PYTHON:
    vstr = ".".join(map(str, MIN_PYTHON))
    raise SystemExit("PyObjC: Need at least Python " + vstr)

#
#
# Compiler arguments
#
#


def get_os_level():
    pl = plistlib.readPlist("/System/Library/CoreServices/SystemVersion.plist")
    v = pl["ProductVersion"]
    return ".".join(v.split(".")[:2])


def get_sdk_level(sdk):
    if sdk == "/":
        return get_os_level()

    sdk = sdk.rstrip("/")
    sdkname = os.path.basename(sdk)
    assert sdkname.startswith("MacOSX")
    assert sdkname.endswith(".sdk")
    if sdkname == "MacOSX.sdk":
        try:
            pl = plistlib.readPlist(os.path.join(sdk, "SDKSettings.plist"))
            return pl["Version"]
        except Exception:
            raise SystemExit("Cannot determine SDK version")
    else:
        return sdkname[6:-4]


# CFLAGS for the objc._objc extension:
CFLAGS = [
    "-g",
    "-fexceptions",
    # Loads of warning flags
    "-Wall",
    "-Wstrict-prototypes",
    "-Wmissing-prototypes",
    "-Wformat=2",
    "-W",
    "-Wpointer-arith",
    "-Wmissing-declarations",
    "-Wnested-externs",
    "-W",
    "-Wno-import",
    "-Wno-unknown-pragmas",
    "-Wshorten-64-to-32",
    # "-fsanitize=address", "-fsanitize=undefined", "-fno-sanitize=vptr",
    # "--analyze",
    "-Werror",
    "-I/usr/include/ffi",
]

# CFLAGS for other (test) extensions:
EXT_CFLAGS = CFLAGS + ["-IModules/objc"]

# LDFLAGS for the objc._objc extension
OBJC_LDFLAGS = [
    "-framework",
    "CoreFoundation",
    "-framework",
    "Foundation",
    "-framework",
    "Carbon",
    "-fvisibility=protected",
    "-g",
    "-lffi",
    # "-fsanitize=address", "-fsanitize=undefined", "-fno-sanitize=vptr",
    # "-O3",
]


#
#
# Adjust distutils CFLAGS:
#
# - PyObjC won't work when compiled with -O0
# - To make it easier to debug reduce optimization level
#   to -O1 when building with a --with-pydebug build of Python
# - Set optimization to -O4 with normal builds of Python,
#   enables link-time optimization with clang and appears to
#   be (slightly) faster.
#


if "-O0" in get_config_var("CFLAGS"):
    # -O0 doesn't work with some (older?) compilers, unconditionally
    # change -O0 to -O1 to work around that issue.
    print("Change -O0 to -O1 (-O0 miscompiles libffi)")
    config_vars = get_config_vars()
    for k in config_vars:
        if isinstance(config_vars[k], str) and "-O0" in config_vars[k]:
            config_vars[k] = config_vars[k].replace("-O0", "-O1")


if get_config_var("Py_DEBUG"):
    # Running with Py_DEBUG, reduce optimization level
    # to make it easier to debug the code.
    cfg_vars = get_config_vars()
    for k in vars:
        if isinstance(cfg_vars[k], str) and "-O2" in cfg_vars[k]:
            cfg_vars[k] = cfg_vars[k].replace("-O2", "-O1 -g")
        elif isinstance(cfg_vars[k], str) and "-O3" in cfg_vars[k]:
            cfg_vars[k] = cfg_vars[k].replace("-O3", "-O1 -g")

else:
    # Enable -O4, which enables link-time optimization with
    # clang. This appears to have a positive effect on performance.
    cfg_vars = get_config_vars()
    for k in cfg_vars:
        if isinstance(cfg_vars[k], str) and "-O2" in cfg_vars[k]:
            cfg_vars[k] = cfg_vars[k].replace("-O2", "-O3")
        elif isinstance(cfg_vars[k], str) and "-O3" in cfg_vars[k]:
            cfg_vars[k] = cfg_vars[k].replace("-O3", "-O3")


# XXX: bug in CPython 3.4 repository leaks unwanted compiler flag into disutils.
cfg_vars = get_config_vars()
for k in cfg_vars:
    if (
        isinstance(cfg_vars[k], str)
        and "-Werror=declaration-after-statement" in cfg_vars[k]
    ):
        cfg_vars[k] = cfg_vars[k].replace("-Werror=declaration-after-statement", "")


#
#
# Custom distutils commands
#
#


def verify_platform():
    if sys.platform != "darwin":
        raise DistutilsPlatformError("PyObjC requires macOS to build")

    if sys.version_info[:2] < MIN_PYTHON:
        raise DistutilsPlatformError(
            "PyObjC requires Python {} or later to build".format(".".join(MIN_PYTHON))
        )

    if hasattr(sys, "pypy_version_info"):
        print("WARNING: PyPy is not a supported platform for PyObjC")


class oc_build_py(build_py.build_py):
    def run(self):
        verify_platform()
        build_py.build_py.run(self)

    def build_packages(self):
        log.info("Overriding build_packages to copy PyObjCTest")
        p = self.packages
        self.packages = list(self.packages) + ["PyObjCTest"]
        try:
            build_py.build_py.build_packages(self)
        finally:
            self.packages = p


class oc_test(test.test):
    description = "run test suite"
    user_options = [("verbosity=", None, "print what tests are run")]

    def initialize_options(self):
        self.verbosity = "1"

    def finalize_options(self):
        if isinstance(self.verbosity, str):
            self.verbosity = int(self.verbosity)

    def cleanup_environment(self):
        add_activation_listener(lambda dist: dist.activate())

        ei_cmd = self.get_finalized_command("egg_info")
        egg_name = ei_cmd.egg_name.replace("-", "_")

        to_remove = []
        for dirname in sys.path:
            bn = os.path.basename(dirname)
            if bn.startswith(egg_name + "-"):
                to_remove.append(dirname)

        for dirname in to_remove:
            log.info("removing installed %r from sys.path before testing" % (dirname,))
            sys.path.remove(dirname)

        working_set.__init__(sys.path)

    def add_project_to_sys_path(self):
        from pkg_resources import working_set

        self.reinitialize_command("egg_info")
        self.run_command("egg_info")
        self.reinitialize_command("build_ext", inplace=1)
        self.run_command("build_ext")

        self.__old_path = sys.path[:]
        self.__old_modules = sys.modules.copy()

        if "PyObjCTools" in sys.modules:
            del sys.modules["PyObjCTools"]

        ei_cmd = self.get_finalized_command("egg_info")
        sys.path.insert(0, normalize_path(ei_cmd.egg_base))
        sys.path.insert(1, os.path.dirname(__file__))

        add_activation_listener(lambda dist: dist.activate())
        working_set.__init__()
        require("%s==%s" % (ei_cmd.egg_name, ei_cmd.egg_version))

        from PyObjCTools import TestSupport

        if os.path.realpath(os.path.dirname(TestSupport.__file__)) != os.path.realpath(
            "Lib/PyObjCTools"
        ):
            raise DistutilsError(
                "Setting up test environment failed for 'PyObjCTools.TestSupport'"
            )

        import objc

        if os.path.realpath(os.path.dirname(objc.__file__)) != os.path.realpath(
            "Lib/objc"
        ):
            raise DistutilsError("Setting up test environment failed for 'objc'")

    def remove_from_sys_path(self):
        from pkg_resources import working_set

        sys.path[:] = self.__old_path
        sys.modules.clear()
        sys.modules.update(self.__old_modules)
        working_set.__init__()

    def run(self):
        verify_platform()

        import unittest

        # Ensure that build directory is on sys.path (py3k)
        self.cleanup_environment()
        self.add_project_to_sys_path()

        from PyObjCTest.loader import makeTestSuite

        warnings.simplefilter("error")

        try:
            suite = makeTestSuite()

            runner = unittest.TextTestRunner(verbosity=self.verbosity)
            result = runner.run(suite)

            # Print out summary. This is a structured format that
            # should make it easy to use this information in scripts.
            summary = {
                "count": result.testsRun,
                "fails": len(result.failures),
                "errors": len(result.errors),
                "xfails": len(getattr(result, "expectedFailures", [])),
                "xpass": len(getattr(result, "expectedSuccesses", [])),
                "skip": len(getattr(result, "skipped", [])),
            }
            print("SUMMARY: %s" % (summary,))

            if not result.wasSuccessful():
                raise DistutilsError("some tests failed")

        finally:
            self.remove_from_sys_path()


class oc_egg_info(egg_info.egg_info):
    # This is a workaround for a bug in setuptools: I'd like
    # to use the 'egg_info.writers' entry points in the setup()
    # call, but those don't work when also using a package_base
    # argument as we do.
    # (issue 123 in the distribute tracker)
    def run(self):
        verify_platform()

        self.mkpath(self.egg_info)

        for hdr in ("pyobjc-compat.h", "pyobjc-api.h"):
            fn = os.path.join("include", hdr)

            self.write_header(fn, os.path.join(self.egg_info, fn))

        egg_info.egg_info.run(self)

        path = os.path.join(self.egg_info, "PKG-INFO")
        with open(path, "a+") as fp:
            fp.write(
                "Project-URL: Documentation, https://pyobjc.readthedocs.io/en/latest/\n"
            )
            fp.write(
                "Project-URL: Issue tracker, https://github.com/ronaldoussoren/pyobjc/issues\n"
            )
            fp.write(
                "Project-URL: Repository, https://github.com/ronaldoussoren/pyobjc\n"
            )

    def write_header(self, basename, filename):
        with open(os.path.join("Modules/objc/", os.path.basename(basename)), "r") as fp:
            data = fp.read()
        if not self.dry_run:
            if not os.path.exists(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename))

        self.write_file(basename, filename, data)


class oc_install_lib(install_lib.install_lib):
    def run(self):
        verify_platform()
        install_lib.install_lib.run(self)

    def get_exclusions(self):
        result = install_lib.install_lib.get_exclusions(self)
        if hasattr(install_lib, "_install_lib"):
            outputs = install_lib._install_lib.get_outputs(self)
        else:
            outputs = install_lib.orig.install_lib.get_outputs(self)

        exclusions = {}
        for fn in outputs:
            if "PyObjCTest" in fn:
                exclusions[fn] = 1

        for fn in os.listdir("PyObjCTest"):
            exclusions[os.path.join("PyObjCTest", fn)] = 1
            exclusions[os.path.join(self.install_dir, "PyObjCTest", fn)] = 1

        result.update(exclusions)
        return result


def _find_executable(executable):
    if os.path.isfile(executable):
        return executable

    else:
        for p in os.environ["PATH"].split(os.pathsep):
            f = os.path.join(p, executable)
            if os.path.isfile(f):
                return executable
    return None


def _working_compiler(executable):
    if executable == "xcrun":
        return True

    with tempfile.NamedTemporaryFile(mode="w", suffix=".c") as fp:
        fp.write("#include <stdarg.h>\nint main(void) { return 0; }\n")
        fp.flush()

        cflags = get_config_var("CFLAGS")
        cflags = shlex.split(cflags)
        cflags += CFLAGS

        p = subprocess.Popen(
            [executable, "-c", fp.name] + cflags,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = p.communicate()
        status = p.wait()
        if status != 0:
            return False

        binfile = fp.name[:-1] + "o"
        if os.path.exists(binfile):
            os.unlink(binfile)

        binfile = os.path.basename(binfile)
        if os.path.exists(binfile):
            os.unlink(binfile)

    return True


def _fixup_compiler(use_ccache):
    if "CC" in os.environ:
        # CC is in the environment, always use explicit
        # overrides.
        return

    try:
        # Newer version of python have support for dealing with
        # the compiler mess w.r.t. various versions of Apple's SDKs
        import _osx_support

        _osx_support.customize_compiler(get_config_vars())
    except (ImportError, AttributeError, KeyError):
        pass

    cc = oldcc = get_config_var("CC").split()[0]
    cc = _find_executable(cc)
    if cc is not None and os.path.basename(cc).startswith("gcc"):
        # Check if compiler is LLVM-GCC, that's known to
        # generate bad code.
        with os.popen(
            "'%s' --version 2>/dev/null" % (cc.replace("'", "'\"'\"'"),)
        ) as fp:
            data = fp.read()
        if "llvm-gcc" in data:
            cc = None

    if cc is not None and not _working_compiler(cc):

        cc = None

    if cc is None:
        # Default compiler is not useable, try finding 'clang'
        cc = _find_executable("clang")
        if cc is None:
            cc = os.popen("/usr/bin/xcrun -find clang").read()

    if not cc:
        raise DistutilsPlatformError("Cannot locate compiler candidate")

    if not _working_compiler(cc):
        raise DistutilsPlatformError("Cannot locate a working compiler")

    if use_ccache:
        p = _find_executable("ccache")
        if p is not None:
            log.info("Detected and using 'ccache'")
            cc = "%s %s" % (p, cc)

    if cc != oldcc:
        log.info("Use '%s' instead of '%s' as the compiler" % (cc, oldcc))

        config_vars = get_config_vars()
        for env in ("BLDSHARED", "LDSHARED", "CC", "CXX"):
            if env in config_vars and env not in os.environ:
                split = config_vars[env].split()
                split[0] = cc if env != "CXX" else cc + "++"
                config_vars[env] = " ".join(split)


class oc_build_ext(build_ext.build_ext):
    user_options = [
        (
            "deployment-target=",
            None,
            "deployment target to use (can also be set using ${MACOSX_DEPLOYMENT_TARGET})",
        ),
        (
            "sdk-root=",
            None,
            "Path to the SDK to use (can also be set using ${SDKROOT})",
        ),
    ]

    def initialize_options(self):
        build_ext.build_ext.initialize_options(self)
        self.deployment_target = None
        self.sdk_root = None

    def finalize_options(self):
        build_ext.build_ext.finalize_options(self)

        self.sdk_root = os.environ.get("SDKROOT", None)
        if self.sdk_root is None:
            if os.path.exists("/usr/bin/xcodebuild"):
                self.sdk_root = subprocess.check_output(
                    ["/usr/bin/xcrun", "-sdk", "macosx", "--show-sdk-path"],
                    universal_newlines=True,
                ).strip()

            else:
                self.sdk_root = "/"

        if not os.path.exists(self.sdk_root):
            raise DistutilsSetupError("SDK root %r does not exist" % (self.sdk_root,))

        if not os.path.exists(
            os.path.join(self.sdk_root, "usr/include/objc/runtime.h")
        ):
            if "-DNO_OBJC2_RUNTIME" not in CFLAGS:
                CFLAGS.append("-DNO_OBJC2_RUNTIME")
                EXT_CFLAGS.append("-DNO_OBJC2_RUNTIME")

    def run(self):
        verify_platform()

        if self.deployment_target is not None:
            os.environ["MACOSX_DEPLOYMENT_TARGET"] = self.deployment_target

        if self.sdk_root != "python":
            if "-isysroot" not in CFLAGS:
                CFLAGS.extend(["-isysroot", self.sdk_root])
                EXT_CFLAGS.extend(["-isysroot", self.sdk_root])
                OBJC_LDFLAGS.extend(["-isysroot", self.sdk_root])

        cflags = get_config_var("CFLAGS")
        if "-mno-fused-madd" in cflags:
            cflags = cflags.replace("-mno-fused-madd", "")
            get_config_vars()["CFLAGS"] = cflags

        CFLAGS.append(
            "-DPyObjC_BUILD_RELEASE=%02d%02d"
            % (tuple(map(int, get_sdk_level(self.sdk_root).split("."))))
        )
        EXT_CFLAGS.append(
            "-DPyObjC_BUILD_RELEASE=%02d%02d"
            % (tuple(map(int, get_sdk_level(self.sdk_root).split("."))))
        )

        _fixup_compiler(use_ccache=any(cmd in sys.argv for cmd in ["develop", "test"]))

        build_ext.build_ext.run(self)
        extensions = self.extensions
        self.extensions = [e for e in extensions if e.name.startswith("PyObjCTest")]
        self.copy_extensions_to_source()
        self.extensions = extensions


#
# Calculate package metadata
#


def parse_package_metadata():
    """
    Read the 'metadata' section of 'setup.cfg' to calculate the package
    metadata (at least those parts that can be configured staticly).
    """
    try:
        from ConfigParser import RawConfigParser
    except ImportError:
        from configparser import RawConfigParser

    cfg = RawConfigParser()
    cfg.optionxform = lambda x: x

    with open("setup.cfg") as fp:
        cfg.read_file(fp)

    metadata = {}
    for opt in cfg.options("x-metadata"):
        val = cfg.get("x-metadata", opt)
        if opt in ("classifiers",):
            metadata[opt] = [x for x in val.splitlines() if x]
        elif opt in ("long_description",):
            # In python 2.7 empty lines in the long description are handled incorrectly,
            # therefore setup.cfg uses '$' at the start of empty lines. Remove that
            # character from the description
            val = val[1:]
            val = val.replace("$", "")
            metadata[opt] = val

            # Add links to interesting location to the long_description
            metadata[opt] += "\n\nProject links\n"
            metadata[opt] += "-------------\n"
            metadata[opt] += "\n"
            metadata[
                opt
            ] += "* `Documentation <https://pyobjc.readthedocs.io/en/latest/>`_\n\n"
            metadata[
                opt
            ] += "* `Issue Tracker <https://github.com/ronaldoussoren/pyobjc/issues>`_\n\n"
            metadata[
                opt
            ] += "* `Repository <https://github.com/ronaldoussoren/pyobjc/>`_\n\n"

        elif opt in ("packages", "namespace_packages", "platforms", "keywords"):
            metadata[opt] = [x.strip() for x in val.split(",")]

        elif opt in ["zip-safe"]:
            metadata["zip_safe"] = int(val)
        else:
            metadata[opt] = val

    metadata["version"] = package_version()

    return metadata


def package_version():
    """
    Return the package version, the canonical location
    for the version is the main header file of the objc._objc
    extension.
    """
    fp = open("Modules/objc/pyobjc.h", "r")
    for ln in fp.readlines():
        if ln.startswith("#define OBJC_VERSION"):
            fp.close()
            return ln.split()[-1][1:-1]

    raise DistutilsSetupError("Version not found")


#
# Actually call the setup function.
#
# Note that all package metadata is stored in setup.cfg, except those
# bits that require Python code to calculate or are needed to control
# the working of distutils.
#

# Note: sorts source files with most recently modified
# first, gives faster feedback when working on source code.
sources = list(glob.glob(os.path.join("Modules", "objc", "*.m")))
sources.sort(key=lambda x: (-os.stat(x).st_mtime, x))
setup(
    ext_modules=[
        Extension(
            "objc._objc",
            sources,
            extra_compile_args=CFLAGS,
            extra_link_args=OBJC_LDFLAGS,
            depends=sources,
        ),
        Extension(
            "objc._machsignals",
            ["Modules/_machsignals.m"],
            extra_compile_args=EXT_CFLAGS,
            extra_link_args=OBJC_LDFLAGS,
        ),
    ]
    + [
        Extension(
            "PyObjCTest." + os.path.splitext(os.path.basename(test_source))[0],
            [test_source],
            extra_compile_args=EXT_CFLAGS,
            extra_link_args=OBJC_LDFLAGS,
        )
        for test_source in glob.glob(os.path.join("Modules", "objc", "test", "*.m"))
    ],
    cmdclass={
        "build_ext": oc_build_ext,
        "install_lib": oc_install_lib,
        "build_py": oc_build_py,
        "test": oc_test,
        "egg_info": oc_egg_info,
    },
    package_dir={"": "Lib", "PyObjCTest": "PyObjCTest"},
    options={"egg_info": {"egg_base": "Lib"}},
    **parse_package_metadata(),
)
