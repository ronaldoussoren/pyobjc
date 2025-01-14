import glob
import os
import re
import plistlib
import shlex
import tempfile
import sys
import subprocess
import textwrap
import warnings
from setuptools import Extension, setup, Command
from setuptools.command import build_ext, build_py, egg_info, install_lib
from distutils import log
from distutils.errors import DistutilsError, DistutilsPlatformError, DistutilsSetupError
from distutils.sysconfig import get_config_var as _get_config_var
from distutils.sysconfig import get_config_vars

from pkg_resources import add_activation_listener, normalize_path, require, working_set


def get_config_var(var):
    return _get_config_var(var) or ""


# We need at least Python 3.9
MIN_PYTHON = (3, 9)

if sys.version_info < MIN_PYTHON:
    vstr = ".".join(map(str, MIN_PYTHON))
    raise SystemExit("PyObjC: Need at least Python " + vstr)

#
#
# Compiler arguments
#
#


def get_os_level():
    with open("/System/Library/CoreServices/SystemVersion.plist", "rb") as fp:
        pl = plistlib.load(fp)
    v = pl["ProductVersion"]
    return ".".join(v.split(".")[:2])


def get_sdk_level(sdk):
    if sdk == "/":
        return get_os_level()

    sdk = sdk.rstrip("/")
    sdkname = os.path.basename(sdk)
    assert sdkname.startswith("MacOSX")
    assert sdkname.endswith(".sdk")

    settings_path = os.path.join(sdk, "SDKSettings.plist")
    if os.path.exists(settings_path):
        try:
            with open(os.path.join(sdk, "SDKSettings.plist"), "rb") as fp:
                pl = plistlib.load(fp)
            return pl["Version"]
        except Exception:
            raise SystemExit("Cannot determine SDK version")
    else:
        version_part = sdkname[6:-4]
        assert version_part
        return version_part


# CFLAGS for the objc._objc extension:
CFLAGS = [
    "-g",
    "-fexceptions",
    # Explicitly opt-out of ARC
    "-fno-objc-arc",
    # Loads of warning flags
    "-Wall",
    # "-Wextra",
    # "-Wpedantic",
    "-Wno-variadic-macros",
    "-Wstrict-prototypes",
    "-Wbad-function-cast",
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
    "-fvisibility=hidden",
    # "-O0",
    "-g",
    # "-O0",
    # "-O3",
    # "-flto=thin",
    # XXX: Use object_path_lto (during linking?)
    "-UNDEBUG",
]

# CFLAGS for other (test) extensions:
EXT_CFLAGS = CFLAGS + ["-IModules/objc"]

# LDFLAGS for the objc._objc extension
OBJC_LDFLAGS = [
    "-framework",
    "CoreFoundation",
    "-framework",
    "Foundation",
    # "-fvisibility=protected",
    "-g",
    "-lffi",
    # "-fsanitize=address", "-fsanitize=undefined", "-fno-sanitize=vptr",
    "-fvisibility=hidden",
    # "-O0",
    "-g",
    # "-O3",
    # "-flto=thin",
    "-fexceptions",
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


# if "-O0" in get_config_var("CFLAGS"):
#    # -O0 doesn't work with some (older?) compilers, unconditionally
#    # change -O0 to -O1 to work around that issue.
#    print("Change -O0 to -O1 (-O0 miscompiles libffi)")
#    config_vars = get_config_vars()
#    for k in config_vars:
#        if isinstance(config_vars[k], str) and "-O0" in config_vars[k]:
#            config_vars[k] = config_vars[k].replace("-O0", "-O1")


if get_config_var("Py_DEBUG"):
    # Running with Py_DEBUG, reduce optimization level
    # to make it easier to debug the code.
    cfg_vars = get_config_vars()
    for k in cfg_vars:
        if isinstance(cfg_vars[k], str) and "-O2" in cfg_vars[k]:
            cfg_vars[k] = cfg_vars[k].replace("-O2", "-O1 -g")
        elif isinstance(cfg_vars[k], str) and "-O3" in cfg_vars[k]:
            cfg_vars[k] = cfg_vars[k].replace("-O3", "-O1 -g")

# else:
#    # Enable -O3, which enables link-time optimization with
#    # clang. This appears to have a positive effect on performance.
#    cfg_vars = get_config_vars()
#    for k in cfg_vars:
#        if isinstance(cfg_vars[k], str) and "-O2" in cfg_vars[k]:
#            cfg_vars[k] = cfg_vars[k].replace("-O2", "-O3")
#        elif isinstance(cfg_vars[k], str) and "-O3" in cfg_vars[k]:
#            cfg_vars[k] = cfg_vars[k].replace("-O3", "-O3")


# XXX: bug in CPython 3.4 repository leaks unwanted compiler flag into distutils.
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


class oc_test(Command):
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
            log.info(f"removing installed {dirname!r} from sys.path before testing")
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
        require(f"{ei_cmd.egg_name}=={ei_cmd.egg_version}")

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

            if self.verbose and self.verbosity < 3:
                runner = unittest.TextTestRunner(verbosity=3)
            else:
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
            print(f"SUMMARY: {summary}")

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

        self.write_build_info()

        egg_info.egg_info.run(self)

        path = os.path.join(self.egg_info, "PKG-INFO")
        with open(path) as fp:
            contents = fp.read()

        first, middle, last = contents.partition("\n\n")

        with open(path, "w") as fp:
            fp.write(first)
            fp.write(
                "\nProject-URL: Documentation, https://pyobjc.readthedocs.io/en/latest/\n"
            )
            fp.write(
                "Project-URL: Issue tracker, https://github.com/ronaldoussoren/pyobjc/issues\n"
            )
            fp.write(
                "Project-URL: Repository, https://github.com/ronaldoussoren/pyobjc"
            )
            fp.write(middle)
            fp.write(last)

    def write_header(self, basename, filename):
        with open(os.path.join("Modules/objc/", os.path.basename(basename))) as fp:
            data = fp.read()
        if not self.dry_run:
            if not os.path.exists(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename))

        self.write_file(basename, filename, data)

    def write_build_info(self):
        macos_version = subprocess.check_output(
            ["sw_vers", "-productversion"], text=True
        ).strip()
        macos_build = subprocess.check_output(
            ["sw_vers", "-buildversion"], text=True
        ).strip()
        clang_version = (
            subprocess.check_output(["clang", "--version"], text=True)
            .splitlines()[0]
            .strip()
        )

        sdk_root = self.get_finalized_command("build_ext").sdk_root
        sdk_info = os.path.join(sdk_root, "SDKSettings.plist")
        if os.path.exists(sdk_info):
            pl = plistlib.load(open(sdk_info, "rb"))
            sdk_version = pl["DisplayName"]
        else:
            sdk_version = os.path.basename(sdk_root)

        build_info = textwrap.dedent(
            f"""\
            macOS {macos_version} ({macos_build})
            {clang_version}
            SDK: {sdk_version}
            """
        )

        self.write_file(
            "pyobjc-build-info.txt",
            os.path.join(self.egg_info, "pyobjc-build-info.txt"),
            build_info,
        )


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
            if "-flto=thin" in CFLAGS:
                cflags.remove("-flto=thin")
                CFLAGS.remove("-flto=thin")
                EXT_CFLAGS.remove("-flto=thin")
                OBJC_LDFLAGS.remove("-flto=thin")
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
            "'{}' --version 2>/dev/null".format(cc.replace("'", "'\"'\"'"))
        ) as fp:
            data = fp.read()
        if "llvm-gcc" in data:
            cc = None

    if cc is not None and not _working_compiler(cc):
        cc = None

    if cc is None:
        # Default compiler is not usable, try finding 'clang'
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
            cc = f"{p} {cc}"

    if cc != oldcc:
        log.info(f"Use '{cc}' instead of '{oldcc}' as the compiler")

        config_vars = get_config_vars()
        for env in ("BLDSHARED", "LDSHARED", "CC", "CXX"):
            if env in config_vars and env not in os.environ:
                split = config_vars[env].split()
                split[0] = cc if env != "CXX" else cc + "++"
                config_vars[env] = " ".join(split)

    cflags = get_config_var("CFLAGS")
    if re.search(r"-arch\s+i386", cflags) is not None:
        raise DistutilsPlatformError("i386 (32-bit) is not supported by PyObjC")

    if re.search(r"-arch\s+ppc", cflags) is not None:
        raise DistutilsPlatformError("PowerPC is not supported by PyObjC")


class oc_build_ext(build_ext.build_ext):
    user_options = build_ext.build_ext.user_options + [
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
        ("no-lto", None, "Disable LTO"),
        ("no-warnings-as-errors", None, "Don't treat compiler errors as warnings"),
    ]

    def initialize_options(self):
        build_ext.build_ext.initialize_options(self)
        self.deployment_target = None
        self.sdk_root = None
        self.no_lto = False
        self.no_warnings_as_errors = False

    def finalize_options(self):
        build_ext.build_ext.finalize_options(self)
        if self.no_lto:
            for var in CFLAGS, EXT_CFLAGS, OBJC_LDFLAGS:
                to_remove = []
                for idx, val in enumerate(var):
                    if val == "-O3" or val.startswith("-flto"):
                        to_remove.append(idx)
                for idx in to_remove[::-1]:
                    del var[idx]

        if self.no_warnings_as_errors:
            CFLAGS.remove("-Werror")
            EXT_CFLAGS.remove("-Werror")

        self.sdk_root = os.environ.get("SDKROOT", None)
        if self.sdk_root is None:
            if os.path.exists("/usr/bin/xcrun"):
                self.sdk_root = subprocess.check_output(
                    ["/usr/bin/xcrun", "-sdk", "macosx", "--show-sdk-path"],
                    text=True,
                ).strip()

                if not self.sdk_root:
                    # With command line tools the value can be empty
                    self.sdk_root = "/"

            else:
                self.sdk_root = "/"

        if not os.path.exists(self.sdk_root):
            raise DistutilsSetupError(f"SDK root {self.sdk_root!r} does not exist")

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
            % (tuple(map(int, get_sdk_level(self.sdk_root).split(".")[:2])))
        )
        EXT_CFLAGS.append(
            "-DPyObjC_BUILD_RELEASE=%02d%02d"
            % (tuple(map(int, get_sdk_level(self.sdk_root).split(".")[:2])))
        )

        if tuple(map(int, get_sdk_level(self.sdk_root).split("."))) < (10, 14):
            # XXX: Not sure where the cut-off is, but older compilers warn
            #      about unused parameters for objc methods even with the right
            #      __attribute__.
            CFLAGS.append("-Wno-unused-parameter")

        _fixup_compiler(
            use_ccache="PYOBJC_USE_CCACHE" in os.environ
            or any(cmd in sys.argv for cmd in ["develop", "test"])
        )

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
    metadata (at least those parts that can be configured statically).
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
    fp = open("Modules/objc/pyobjc.h")
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
        for test_source in glob.glob(os.path.join("Modules", "objc", "test", "*.[mc]"))
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
