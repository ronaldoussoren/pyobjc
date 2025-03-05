"""
Generic setup.py file for PyObjC framework wrappers.

This file should only be changed in pyobjc-core and then copied
to all framework wrappers.

To change this file:
    - Change the copy in pyobjc-core/Tools/pyobjc_setup.py
    - Run development-support/update-shared-files
"""

__all__ = ("setup", "Extension", "Command")

import os
import pkg_resources
import plistlib
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import textwrap
import time
import unittest
from fnmatch import fnmatch
from sysconfig import get_config_var, get_config_vars
from setuptools import Command
from setuptools import Extension as _Extension
from setuptools import setup as _setup
from setuptools.command import build_ext, build_py, develop, egg_info, install_lib

from distutils import log
from distutils.errors import DistutilsError, DistutilsPlatformError

try:
    from setuptools.command import install
except ImportError:
    from distutils.command import install

try:
    from setuptools.command import build
except ImportError:
    from distutils.command import build


class oc_build_py(build_py.build_py):
    def build_packages(self):
        log.info("overriding build_packages to copy PyObjCTest")
        p = self.packages
        self.packages = list(self.packages) + ["PyObjCTest"]
        try:
            build_py.build_py.build_packages(self)
        finally:
            self.packages = p


REPO_NAME = "pyobjc"


class oc_egg_info(egg_info.egg_info):
    def run(self):
        egg_info.egg_info.run(self)
        self.write_build_info()

        path = os.path.join(self.egg_info, "PKG-INFO")
        with open(path) as fp:
            contents = fp.read()

        first, middle, last = contents.partition("\n\n")

        with open(path, "w") as fp:
            fp.write(first)
            fp.write(
                "\nProject-URL: Documentation, "
                "https://%s.readthedocs.io/en/latest/\n" % (REPO_NAME,)
            )
            fp.write(
                "Project-URL: Issue tracker, "
                "https://github.com/ronaldoussoren/%s/issues\n" % (REPO_NAME,)
            )
            fp.write(
                "Project-URL: Repository, "
                "https://github.com/ronaldoussoren/%s" % (REPO_NAME,)
            )
            fp.write(middle)
            fp.write(last)

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

        sdk_root = get_sdk()
        if sdk_root is None:
            sdk_root = subprocess.check_output(
                ["xcrun", "-sdk", "macosx", "--show-sdk-path"], text=True
            ).strip()
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


class oc_test(Command):
    description = "run test suite"
    user_options = [("verbosity=", None, "print what tests are run")]

    def initialize_options(self):
        self.verbosity = "1"

    def finalize_options(self):
        if isinstance(self.verbosity, str):
            self.verbosity = int(self.verbosity)

    def cleanup_environment(self):
        from pkg_resources import add_activation_listener

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

        pkg_resources.working_set.__init__()

    def add_project_to_sys_path(self):
        from pkg_resources import normalize_path, add_activation_listener
        from pkg_resources import working_set, require

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

    def remove_from_sys_path(self):
        from pkg_resources import working_set

        sys.path[:] = self.__old_path
        sys.modules.clear()
        sys.modules.update(self.__old_modules)
        working_set.__init__()

    def run(self):
        self.cleanup_environment()
        self.add_project_to_sys_path()

        import warnings

        warnings.simplefilter("error")

        try:
            time_before = time.time()
            suite = makeTestSuite()

            if self.verbose and self.verbosity < 3:
                runner = unittest.TextTestRunner(verbosity=3)
            else:
                runner = unittest.TextTestRunner(verbosity=self.verbosity)
            result = runner.run(suite)

            time_after = time.time()

            # Print out summary. This is a structured format that
            # should make it easy to use this information in scripts.
            summary = {
                "count": result.testsRun,
                "fails": len(result.failures),
                "errors": len(result.errors),
                "xfails": len(getattr(result, "expectedFailures", [])),
                "xpass": len(getattr(result, "unexpectedSuccesses", [])),
                "skip=": len(getattr(result, "skipped", [])),
                "testSeconds": (time_after - time_before),
            }
            print(f"SUMMARY: {summary}")
            if not result.wasSuccessful():
                raise DistutilsError("some tests failed")

        finally:
            self.remove_from_sys_path()


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
Programming Language :: Python :: 3 :: Only
Programming Language :: Python :: 3.9
Programming Language :: Python :: 3.10
Programming Language :: Python :: 3.11
Programming Language :: Python :: 3.12
Programming Language :: Python :: 3.13
Programming Language :: Python :: 3.14
Programming Language :: Python :: Implementation :: CPython
Programming Language :: Objective C
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Software Development :: User Interfaces
""".splitlines(),
    )
)


def get_os_level():
    # Retrieve the productVersion by invoking sw_vers, code tries
    # to retrieve the version in-process will retrieve a compatibility
    # version when compiled with an SDK older than 11.0.
    v = (
        subprocess.check_output(["/usr/bin/sw_vers", "-productVersion"])
        .decode()
        .strip()
    )
    return ".".join(v.split(".")[:2])


def get_sdk():
    env_cflags = os.environ.get("CFLAGS", "")
    config_cflags = get_config_var("CFLAGS")
    sdk = None
    for cflags_str in [env_cflags, config_cflags]:
        cflags = shlex.split(cflags_str)
        for i, val in enumerate(cflags):
            if val == "-isysroot":
                sdk = cflags[i + 1]
                break
            elif val.find("-isysroot") == 0:
                sdk = val[len("-isysroot") :]
                break
        if sdk:
            break

    return sdk


def get_sdk_level():
    sdk = get_sdk()

    if not sdk:
        return None

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


class pyobjc_install_lib(install_lib.install_lib):
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

        exclusions["PyObjCTest"] = 1
        exclusions[os.path.join(self.install_dir, "PyObjCTest")] = 1
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
    with tempfile.NamedTemporaryFile(mode="w", suffix=".c") as fp:
        fp.write("#include <stdarg.h>\nint main(void) { return 0; }\n")
        fp.flush()

        cflags = get_config_var("CFLAGS")
        cflags = shlex.split(cflags)

        p = subprocess.Popen(
            [executable, "-c", fp.name] + cflags,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        status = p.wait()
        p.stdout.close()
        p.stderr.close()
        if status != 0:
            return False

        binfile = fp.name[:-1] + "o"
        if os.path.exists(binfile):
            os.unlink(binfile)

        binfile = os.path.basename(binfile)
        if os.path.exists(binfile):
            os.unlink(binfile)

    cflags = get_config_var("CFLAGS")
    if re.search(r"-arch\s+i386", cflags) is not None:
        raise DistutilsPlatformError("i386 (32-bit) is not supported by PyObjC")

    if re.search(r"-arch\s+ppc", cflags) is not None:
        raise DistutilsPlatformError("PowerPC is not supported by PyObjC")

    return True


def _fixup_compiler(use_ccache):
    if "CC" in os.environ:
        # CC is in the environment, always use explicit
        # overrides.
        return

    try:
        import _osx_support

        _osx_support.customize_compiler(get_config_vars())
    except (ImportError, NameError):
        pass

    cc = oldcc = get_config_var("CC").split()[0]
    cc = _find_executable(cc)
    if cc is not None and os.path.basename(cc).startswith("gcc"):
        # Check if compiler is LLVM-GCC, that's known to
        # generate bad code.
        data = os.popen(
            "'{}' --version 2>/dev/null".format(cc.replace("'", "'\"'\"'"))
        ).read()
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
        raise SystemExit("Cannot locate compiler candidate")

    if not _working_compiler(cc):
        raise SystemExit("Cannot locate a working compiler")

    if use_ccache:
        ccache = _find_executable("ccache")
        if ccache:
            cc = f"{ccache} {cc}"

    if cc != oldcc:
        print(f"Use '{cc}' instead of '{oldcc}' as the compiler")

        config_vars = get_config_vars()
        for env in ("BLDSHARED", "LDSHARED", "CC", "CXX"):
            if env in config_vars and env not in os.environ:
                split = config_vars[env].split()
                split[0] = cc if env != "CXX" else cc + "++"
                config_vars[env] = " ".join(split)


class pyobjc_build_ext(build_ext.build_ext):
    def run(self):
        _fixup_compiler("PYOBJC_USE_CCACHE" in os.environ)

        # Ensure that the PyObjC header files are available
        # in 2.3 and later the headers are in the egg,
        # before that we ship a copy.
        if os.path.exists("Modules") and not os.path.isfile("Modules/pyobjc-api.h"):
            (dist,) = pkg_resources.require("pyobjc-core")

            include_root = os.path.join(self.build_temp, "pyobjc-include")
            if os.path.exists(include_root):
                shutil.rmtree(include_root)

            os.makedirs(include_root)
            if dist.has_metadata("include"):
                for fn in dist.metadata_listdir("include"):
                    data = dist.get_metadata(f"include/{fn}")
                    fp = open(os.path.join(include_root, fn), "w")
                    try:
                        fp.write(data)
                    finally:
                        fp.close()

            else:
                raise SystemExit("pyobjc-core egg-info does not include header files")

            for e in self.extensions:
                if include_root not in e.include_dirs:
                    e.include_dirs.append(include_root)

        # Run the actual build
        build_ext.build_ext.run(self)

        # Then tweak the copy_extensions bit to ensure PyObjCTest gets
        # copied to the right place.
        extensions = self.extensions
        self.extensions = [e for e in extensions if e.name.startswith("PyObjCTest")]
        self.copy_extensions_to_source()
        self.extensions = extensions


def Extension(*args, **kwds):
    """
    Simple wrapper about distutils.core.Extension that adds additional PyObjC
    specific flags.
    """
    if sys.platform != "darwin":
        # Use a fake OS level on non-macOS platforms,
        # otherwise the error path in setup() is not triggered.
        os_level = "10.0"
    else:
        os_level = get_sdk_level()
        if os_level is None:
            os_level = get_os_level()

    cflags = []
    ldflags = []
    if "clang" in get_config_var("CC"):
        cflags.append("-Wno-deprecated-declarations")

    if sys.platform != "darwin":
        # See above
        sdk = "/"
    else:
        sdk = get_sdk()

    if not sdk:
        # We're likely on a system with the Xcode Command Line Tools.
        # Explicitly use the most recent SDK to avoid compile problems.
        data = subprocess.check_output(
            ["/usr/bin/xcrun", "-sdk", "macosx", "--show-sdk-path"],
            text=True,
        ).strip()

        if data:
            sdk_settings_path = os.path.join(data, "SDKSettings.plist")
            if os.path.exists(sdk_settings_path):
                with open(sdk_settings_path, "rb") as fp:
                    sdk_settings = plistlib.load(fp)
                version = sdk_settings["Version"]
            else:
                version = os.path.basename(data)[6:-4]

            cflags.append("-isysroot")
            cflags.append(data)
            cflags.append(
                "-DPyObjC_BUILD_RELEASE=%02d%02d"
                % (tuple(map(int, version.split(".")[:2])))
            )
        else:
            cflags.append(
                "-DPyObjC_BUILD_RELEASE=%02d%02d"
                % (tuple(map(int, os_level.split(".")[:2])))
            )

    else:
        cflags.append(
            "-DPyObjC_BUILD_RELEASE=%02d%02d"
            % (tuple(map(int, os_level.split(".")[:2])))
        )

    if os_level == "10.4":
        cflags.append("-DNO_OBJC2_RUNTIME")

    if "-Werror" not in cflags:
        cflags.append("-Werror")

    if get_config_var("Py_GIL_DISABLED"):
        cflags.append("-DPyObjC_GIL_DISABLED")

    if "extra_compile_args" in kwds:
        kwds["extra_compile_args"] = kwds["extra_compile_args"] + cflags
    else:
        kwds["extra_compile_args"] = cflags

    if "extra_link_args" in kwds:
        kwds["extra_link_args"] = kwds["extra_link_args"] + ldflags
    else:
        kwds["extra_link_args"] = ldflags

    return _Extension(*args, **kwds)


def _sort_key(version):
    return tuple(int(x) for x in version.split("."))


def setup(
    min_os_level=None,
    max_os_level=None,
    cmdclass=None,
    options={},  # noqa: M511, B006
    **kwds,
):
    k = kwds.copy()
    options = options.copy()

    os_level = get_sdk_level()
    if os_level is None:
        os_level = get_os_level()
    os_compatible = True
    if sys.platform != "darwin":
        os_compatible = False

    else:
        if min_os_level is not None:
            if _sort_key(os_level) < _sort_key(min_os_level):
                os_compatible = False
        if max_os_level is not None:
            if _sort_key(os_level) > _sort_key(max_os_level):
                os_compatible = False

    if cmdclass is None:
        cmdclass = {}
    else:
        cmdclass = cmdclass.copy()

    if os_compatible or ("bdist_wheel" in sys.argv and "ext_modules" not in k):
        cmdclass["build_ext"] = pyobjc_build_ext
        cmdclass["egg_info"] = oc_egg_info
        cmdclass["install_lib"] = pyobjc_install_lib
        cmdclass["test"] = oc_test
        cmdclass["build_py"] = oc_build_py

    else:
        if min_os_level is not None:
            if max_os_level is not None:
                msg = (
                    "This distribution is only supported on macOS "
                    "versions %s up to and including %s" % (min_os_level, max_os_level)
                )
            else:
                msg = "This distribution is only supported on macOS >= {}".format(
                    min_os_level,
                )
        elif max_os_level is not None:
            msg = "This distribution is only supported on macOS <= {}".format(
                max_os_level,
            )
        else:
            msg = "This distribution is only supported on macOS"

        def create_command_subclass(base_class):
            class subcommand(base_class):
                def run(self, msg=msg):
                    raise DistutilsPlatformError(msg)

            return subcommand

        class no_test(oc_test):
            def run(self, msg=msg):
                print(f"WARNING: {msg}\n")
                print(
                    "SUMMARY: {'testSeconds': 0.0, 'count': 0, 'fails': 0, "
                    "'errors': 0, 'xfails': 0, 'skip': 65, 'xpass': 0, "
                    "'message': %r }" % (msg,)
                )

        cmdclass["build"] = create_command_subclass(build.build)
        cmdclass["test"] = no_test
        cmdclass["install"] = create_command_subclass(install.install)
        cmdclass["install_lib"] = create_command_subclass(pyobjc_install_lib)
        cmdclass["develop"] = create_command_subclass(develop.develop)
        cmdclass["build_py"] = create_command_subclass(oc_build_py)

    if "ext_modules" not in k:
        # No extension modules, can build universal wheel
        options.update({"bdist_wheel": {"universal": 1}})

    plat_name = "MacOS X"
    plat_versions = []
    if min_os_level is not None and min_os_level == max_os_level:
        plat_versions.append(f"=={min_os_level}")
    else:
        if min_os_level is not None:
            plat_versions.append(f">={min_os_level}")
        if max_os_level is not None:
            plat_versions.append(f"<={max_os_level}")
    if plat_versions:
        plat_name += " ({})".format(", ".join(plat_versions))

    if os.path.isfile("Modules/pyobjc-api.h") or "ext_modules" not in k:
        if "setup_requires" in k:
            if len(k["setup_requires"]) == 1 and k["setup_requires"][0].startswith(
                "pyobjc-core"
            ):
                del k["setup_requires"]

    if "long_description" in k:
        k["long_description"] += "\n\nProject links\n"
        k["long_description"] += "-------------\n"
        k["long_description"] += "\n"
        k[
            "long_description"
        ] += "* `Documentation <https://{}.readthedocs.io/en/latest/>`_\n\n".format(
            REPO_NAME,
        )
        k[
            "long_description"
        ] += "* `Issue Tracker <https://github.com/ronaldoussoren/{}/issues>`_\n\n".format(
            REPO_NAME,
        )
        k[
            "long_description"
        ] += "* `Repository <https://github.com/ronaldoussoren/{}/>`_\n\n".format(
            REPO_NAME,
        )
        k["long_description_content_type"] = "text/x-rst; charset=UTF-8"

    if "bdist_wheel" in options:
        # Python 3.13 does not support the limited ABI for C extensions
        # when using a free threaded build.
        if get_config_var("Py_GIL_DISABLED"):
            del options["bdist_wheel"]

    _setup(
        cmdclass=cmdclass,
        author="Ronald Oussoren",
        author_email="pyobjc-dev@lists.sourceforge.net",
        url="https://github.com/ronaldoussoren/pyobjc",
        platforms=[plat_name],
        package_dir={"": "Lib", "PyObjCTest": "PyObjCTest"},
        dependency_links=[],
        package_data={"": ["*.bridgesupport"]},
        zip_safe=False,
        license="MIT License",
        classifiers=CLASSIFIERS,
        python_requires=">=3.9",
        keywords=["PyObjC"] + [p for p in k["packages"] if p not in ("PyObjCTools",)],
        options=options,
        **k,
    )


def recursiveGlob(root, pathPattern):
    """
    Recursively look for files matching 'pathPattern'. Return a list
    of matching files/directories.
    """
    result = []

    for rootpath, _dirnames, filenames in os.walk(root):
        for fn in filenames:
            if fnmatch(fn, pathPattern):
                result.append(os.path.join(rootpath, fn))
    return result


def importExternalTestCases(pathPattern="test_*.py", root=".", package=None):
    """
    Import all unittests in the PyObjC tree starting at 'root'
    """

    testFiles = recursiveGlob(root, pathPattern)
    testModules = [x[len(root) + 1 : -3].replace("/", ".") for x in testFiles]
    if package is not None:
        testModules = [(package + "." + m) for m in testModules]

    suites = []

    for modName in testModules:
        try:
            module = __import__(modName)
        except ImportError as msg:
            print(f"SKIP {modName}: {msg}")
            continue

        if "." in modName:
            for elem in modName.split(".")[1:]:
                module = getattr(module, elem)

        s = unittest.defaultTestLoader.loadTestsFromModule(module)
        suites.append(s)

    return unittest.TestSuite(suites)


gTopdir = os.path.dirname(__file__)


def makeTestSuite():
    plain_suite = importExternalTestCases(
        "test_*.py", os.path.join(gTopdir, "PyObjCTest"), package="PyObjCTest"
    )

    return plain_suite
