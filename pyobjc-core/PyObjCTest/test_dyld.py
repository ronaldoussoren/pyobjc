import os
import objc
import sys
import subprocess

import objc._dyld as dyld
from PyObjCTools.TestSupport import (
    TestCase,
    os_release,
    os_level_key,
    min_os_level,
    max_os_level,
)


class TestDyld(TestCase):
    def setUp(self):
        self.orig_environ = os.environ
        os.environ = os.environ.copy()  # noqa: B003

    def tearDown(self):
        os.environ = self.orig_environ  # noqa: B003

    def test_inject_suffixes(self):
        if "DYLD_IMAGE_SUFFIX" in os.environ:
            del os.environ["DYLD_IMAGE_SUFFIX"]

        # No suffix
        paths = [
            "/usr/lib/libSystem.dylib",
            "/lib/libfoo.3.dylib",
            "/System/Library/Frameworks/CorePython.framework/Versions/B/CorePython",
            "/System/Library/Frameworks/CorePython.framework/CorePython",
        ]
        self.assertEqual(list(dyld.inject_suffixes(iter(paths))), paths)
        self.assertIs(dyld.inject_suffixes(paths), paths)

        os.environ["DYLD_IMAGE_SUFFIX"] = "_DEBUG"
        self.maxDiff = None
        self.assertEqual(
            list(dyld.inject_suffixes(iter(paths))),
            [
                "/usr/lib/libSystem_DEBUG.dylib",
                "/usr/lib/libSystem.dylib",
                "/lib/libfoo.3_DEBUG.dylib",
                "/lib/libfoo.3.dylib",
                "/System/Library/Frameworks/CorePython.framework/Versions/B/CorePython_DEBUG",
                "/System/Library/Frameworks/CorePython.framework/Versions/B/CorePython",
                "/System/Library/Frameworks/CorePython.framework/CorePython_DEBUG",
                "/System/Library/Frameworks/CorePython.framework/CorePython",
            ],
        )

    def test_ensure_unicode(self):
        v = dyld.ensure_unicode("foo")
        self.assertIsInstance(v, str)
        self.assertEqual(v, "foo")

        v = dyld.ensure_unicode(b"foo")
        self.assertIsInstance(v, str)
        self.assertEqual(v, "foo")

        v = dyld.ensure_unicode(b"foo".decode("utf-8"))
        self.assertIsInstance(v, str)
        self.assertEqual(v, "foo")

        with self.assertRaises(UnicodeError):
            dyld.ensure_unicode(b"\xff\xff")

    @max_os_level("10.15")
    def test_contains_path_old_os(self):
        self.assertFalse(
            objc._dyld_shared_cache_contains_path("/usr/lib/libSystem.dylib")
        )

    @min_os_level("11.0")
    def test_contains_path_new_os(self):
        self.assertTrue(
            objc._dyld_shared_cache_contains_path("/usr/lib/libSystem.dylib")
        )

        if os.path.exists("/Library/Frameworks/Python.framework"):
            self.assertFalse(
                objc._dyld_shared_cache_contains_path(
                    os.path.realpath(
                        "/Library/Frameworks/Python.framework/Versions/Current/Python"
                    )
                )
            )

    def test_contains_path_invalid(self):
        with self.assertRaisesRegex(TypeError, "Expecting a string"):
            objc._dyld_shared_cache_contains_path(42)

        with self.assertRaisesRegex(
            UnicodeEncodeError, "'utf-8' codec can't encode characters .*"
        ):
            objc._dyld_shared_cache_contains_path("\ud800\udc00")

    def test_dyld_library(self):
        for k in (
            "DYLD_LIBRARY_PATH",
            "DYLD_FALLBACK_LIBRARY_PATH",
            "DYLD_IMAGE_SUFFIX",
        ):
            if k in os.environ:
                del os.environ[k]

        orig_exists = os.path.exists
        orig__dyld_shared_cache_contains_path = dyld._dyld_shared_cache_contains_path
        try:
            os.path.exists = lambda fn: lst.append(fn)
            dyld._dyld_shared_cache_contains_path = lambda fn: False

            lst = []
            with self.assertRaises(ValueError):
                result = dyld.dyld_library(
                    "/usr/lib/libSystem.dylib", "libXSystem.dylib"
                )
                print("Found", result)
            self.assertEqual(
                lst,
                [
                    "/usr/lib/libSystem.dylib",
                    os.path.expanduser("~/lib/libXSystem.dylib"),
                    "/usr/local/lib/libXSystem.dylib",
                    "/lib/libXSystem.dylib",
                    "/usr/lib/libXSystem.dylib",
                ],
            )

            os.environ["DYLD_IMAGE_SUFFIX"] = "_debug"
            lst = []
            with self.assertRaises(ValueError):
                dyld.dyld_library(
                    "/usr/lib/libSystem.dylib",
                    "libXSystem.dylib",
                )
            self.assertEqual(
                lst,
                [
                    "/usr/lib/libSystem_debug.dylib",
                    "/usr/lib/libSystem.dylib",
                    os.path.expanduser("~/lib/libXSystem_debug.dylib"),
                    os.path.expanduser("~/lib/libXSystem.dylib"),
                    "/usr/local/lib/libXSystem_debug.dylib",
                    "/usr/local/lib/libXSystem.dylib",
                    "/lib/libXSystem_debug.dylib",
                    "/lib/libXSystem.dylib",
                    "/usr/lib/libXSystem_debug.dylib",
                    "/usr/lib/libXSystem.dylib",
                ],
            )

            del os.environ["DYLD_IMAGE_SUFFIX"]

            os.environ["DYLD_LIBRARY_PATH"] = "/slib:/usr/slib"
            lst = []
            with self.assertRaises(ValueError):
                dyld.dyld_library(
                    "/usr/lib/libSystem.dylib",
                    "libXSystem.dylib",
                )
            self.assertEqual(
                lst,
                [
                    "/slib/libXSystem.dylib",
                    "/usr/slib/libXSystem.dylib",
                    "/usr/lib/libSystem.dylib",
                    os.path.expanduser("~/lib/libXSystem.dylib"),
                    "/usr/local/lib/libXSystem.dylib",
                    "/lib/libXSystem.dylib",
                    "/usr/lib/libXSystem.dylib",
                ],
            )
            del os.environ["DYLD_LIBRARY_PATH"]

            os.environ["DYLD_FALLBACK_LIBRARY_PATH"] = "/slib:/usr/slib"
            lst = []
            with self.assertRaises(ValueError):
                dyld.dyld_library(
                    "/usr/lib/libSystem.dylib",
                    "libXSystem.dylib",
                )
            self.assertEqual(
                lst,
                [
                    "/usr/lib/libSystem.dylib",
                    "/slib/libXSystem.dylib",
                    "/usr/slib/libXSystem.dylib",
                ],
            )
            del os.environ["DYLD_FALLBACK_LIBRARY_PATH"]

            os.environ["DYLD_LIBRARY_PATH"] = "/lib2:/lib3"
            os.environ["DYLD_FALLBACK_LIBRARY_PATH"] = "/lib4:/lib5"
            os.environ["DYLD_IMAGE_SUFFIX"] = "_profile"

            lst = []
            with self.assertRaises(ValueError):
                dyld.dyld_library(
                    "/usr/lib/libSystem.dylib",
                    "libXSystem.dylib",
                )
            self.assertEqual(
                lst,
                [
                    "/lib2/libXSystem_profile.dylib",
                    "/lib2/libXSystem.dylib",
                    "/lib3/libXSystem_profile.dylib",
                    "/lib3/libXSystem.dylib",
                    "/usr/lib/libSystem_profile.dylib",
                    "/usr/lib/libSystem.dylib",
                    "/lib4/libXSystem_profile.dylib",
                    "/lib4/libXSystem.dylib",
                    "/lib5/libXSystem_profile.dylib",
                    "/lib5/libXSystem.dylib",
                ],
            )
            del os.environ["DYLD_LIBRARY_PATH"]
            del os.environ["DYLD_FALLBACK_LIBRARY_PATH"]
            del os.environ["DYLD_IMAGE_SUFFIX"]

        finally:
            os.path.exists = orig_exists
            dyld._dyld_shared_cache_contains_path = (
                orig__dyld_shared_cache_contains_path
            )

        self.assertEqual(
            dyld.dyld_library("/usr/lib/libSystem.dylib", "libXSystem.dylib"),
            "/usr/lib/libSystem.dylib",
        )

        if os.path.exists("/Library/Frameworks/Python.framework"):
            # Test using a non-system path, to ensure we hit a code path that doesn't find the
            # library in the shared library cache
            libdir = os.environ["DYLD_LIBRARY_PATH"] = (
                f"/Library/Frameworks/Python.framework/Versions/{sys.version_info[0]}.{sys.version_info[1]}/lib"
            )
            self.assertEqual(
                dyld.dyld_library("libcrypto.dylib", "libcrypto.dylib"),
                f"{libdir}/libcrypto.dylib",
            )

        # When the 'command line tools for xcode' are not installed
        # there is no debug version of libsystem in the system wide
        # library directory. In that case we look in the SDK instead.
        if os.path.exists("/usr/lib/libSystem_debug.dylib"):
            os.environ["DYLD_IMAGE_SUFFIX"] = "_debug"
            self.assertEqual(
                dyld.dyld_library("/usr/lib/libSystem.dylib", "libSystem.dylib"),
                "/usr/lib/libSystem_debug.dylib",
            )

        else:
            p = subprocess.check_output(["xcrun", "--show-sdk-path"]).strip()
            os.environ["DYLD_LIBRARY_PATH"] = os.path.join(
                p.decode("utf-8"), "usr", "lib"
            )
            os.environ["DYLD_IMAGE_SUFFIX"] = "_debug"

            # The OSX 10.11 SDK no longer contains ".dylib" files, which
            # makes the test useless when running up-to-date
            # tools on OSX 10.10 or later.
            if os_level_key(os_release()) < os_level_key("10.10"):
                self.assertEqual(
                    dyld.dyld_library("/usr/lib/libSystem.dylib", "libSystem.dylib"),
                    os.path.join(
                        os.environ["DYLD_LIBRARY_PATH"], "libSystem_debug.dylib"
                    ),
                )

    def test_dyld_framework(self):
        for k in (
            "DYLD_FRAMEWORK_PATH",
            "DYLD_FALLBACK_FRAMEWORK_PATH",
            "DYLD_IMAGE_SUFFIX",
        ):
            if k in os.environ:
                del os.environ[k]

        orig = os.path.exists
        try:
            os.path.exists = lambda fn: lst.append(fn)

            self.maxDiff = None

            lst = []
            with self.assertRaises(ImportError):
                dyld.dyld_framework(
                    "/System/Library/Cocoa.framework/Cocoa",
                    "XCocoa",
                )
            self.assertEqual(
                lst,
                [
                    "/System/Library/Cocoa.framework/Cocoa",
                    os.path.expanduser("~/Library/Frameworks/XCocoa.framework/XCocoa"),
                    "/Library/Frameworks/XCocoa.framework/XCocoa",
                    "/Network/Library/Frameworks/XCocoa.framework/XCocoa",
                    "/System/Library/Frameworks/XCocoa.framework/XCocoa",
                ],
            )

            os.environ["DYLD_IMAGE_SUFFIX"] = "_profile"
            lst = []
            with self.assertRaises(ImportError):
                dyld.dyld_framework(
                    "/System/Library/Cocoa.framework/Cocoa",
                    "XCocoa",
                )
            self.assertEqual(
                lst,
                [
                    "/System/Library/Cocoa.framework/Cocoa_profile",
                    "/System/Library/Cocoa.framework/Cocoa",
                    os.path.expanduser(
                        "~/Library/Frameworks/XCocoa.framework/XCocoa_profile"
                    ),
                    os.path.expanduser("~/Library/Frameworks/XCocoa.framework/XCocoa"),
                    "/Library/Frameworks/XCocoa.framework/XCocoa_profile",
                    "/Library/Frameworks/XCocoa.framework/XCocoa",
                    "/Network/Library/Frameworks/XCocoa.framework/XCocoa_profile",
                    "/Network/Library/Frameworks/XCocoa.framework/XCocoa",
                    "/System/Library/Frameworks/XCocoa.framework/XCocoa_profile",
                    "/System/Library/Frameworks/XCocoa.framework/XCocoa",
                ],
            )
            del os.environ["DYLD_IMAGE_SUFFIX"]

            os.environ["DYLD_FRAMEWORK_PATH"] = "/Projects/Frameworks:/Company"
            lst = []
            with self.assertRaises(ImportError):
                dyld.dyld_framework(
                    "/System/Library/Cocoa.framework/Cocoa",
                    "XCocoa",
                )
            self.assertEqual(
                lst,
                [
                    "/Projects/Frameworks/XCocoa.framework/XCocoa",
                    "/Company/XCocoa.framework/XCocoa",
                    "/System/Library/Cocoa.framework/Cocoa",
                    os.path.expanduser("~/Library/Frameworks/XCocoa.framework/XCocoa"),
                    "/Library/Frameworks/XCocoa.framework/XCocoa",
                    "/Network/Library/Frameworks/XCocoa.framework/XCocoa",
                    "/System/Library/Frameworks/XCocoa.framework/XCocoa",
                ],
            )
            del os.environ["DYLD_FRAMEWORK_PATH"]

            os.environ["DYLD_FALLBACK_FRAMEWORK_PATH"] = "/Projects/Frameworks:/Company"
            lst = []
            with self.assertRaises(ImportError):
                dyld.dyld_framework(
                    "/System/Library/Cocoa.framework/Cocoa",
                    "XCocoa",
                )
            self.assertEqual(
                lst,
                [
                    "/System/Library/Cocoa.framework/Cocoa",
                    "/Projects/Frameworks/XCocoa.framework/XCocoa",
                    "/Company/XCocoa.framework/XCocoa",
                ],
            )
            del os.environ["DYLD_FALLBACK_FRAMEWORK_PATH"]

            os.environ["DYLD_FRAMEWORK_PATH"] = "/Prefix1:/Prefix2"
            os.environ["DYLD_FALLBACK_FRAMEWORK_PATH"] = "/Suffix1:/Suffix2"
            os.environ["DYLD_IMAGE_SUFFIX"] = "_debug"

            lst = []
            with self.assertRaises(ImportError):
                dyld.dyld_framework(
                    "/System/Library/Cocoa.framework/Cocoa",
                    "XCocoa",
                    "B",
                )
            self.assertEqual(
                lst,
                [
                    "/Prefix1/XCocoa.framework/Versions/B/XCocoa_debug",
                    "/Prefix1/XCocoa.framework/Versions/B/XCocoa",
                    "/Prefix2/XCocoa.framework/Versions/B/XCocoa_debug",
                    "/Prefix2/XCocoa.framework/Versions/B/XCocoa",
                    "/System/Library/Cocoa.framework/Cocoa_debug",
                    "/System/Library/Cocoa.framework/Cocoa",
                    "/Suffix1/XCocoa.framework/Versions/B/XCocoa_debug",
                    "/Suffix1/XCocoa.framework/Versions/B/XCocoa",
                    "/Suffix2/XCocoa.framework/Versions/B/XCocoa_debug",
                    "/Suffix2/XCocoa.framework/Versions/B/XCocoa",
                ],
            )
            del os.environ["DYLD_FRAMEWORK_PATH"]
            del os.environ["DYLD_FALLBACK_FRAMEWORK_PATH"]
            del os.environ["DYLD_IMAGE_SUFFIX"]

        finally:
            os.path.exists = orig

        self.assertEqual(
            dyld.dyld_framework("/System/Library/Cocoa.framework/Cocoa", "Cocoa"),
            "/System/Library/Frameworks/Cocoa.framework/Cocoa",
        )
        self.assertEqual(
            dyld.dyld_framework("/System/Library/Cocoa.framework/Cocoa", "Cocoa", "A"),
            "/System/Library/Frameworks/Cocoa.framework/Versions/A/Cocoa",
        )

        if os.path.exists("/Library/Frameworks/Python.framework"):
            py_ver = ".".join(map(str, sys.version_info[:2]))
            self.assertEqual(
                dyld.dyld_framework(
                    "/Library/Python.framework/Python", "Python", py_ver
                ),
                f"/Library/Frameworks/Python.framework/Versions/{py_ver}/Python",
            )

    def test_dyld_find(self):
        self.assertEqual(
            dyld.dyld_find("Cocoa.framework"),
            "/System/Library/Frameworks/Cocoa.framework/Cocoa",
        )
        self.assertEqual(dyld.dyld_find("libSystem.dylib"), "/usr/lib/libSystem.dylib")

    def test_pathForFramework(self):
        self.assertEqual(
            dyld.pathForFramework("Cocoa.framework"),
            "/System/Library/Frameworks/Cocoa.framework",
        )
        with self.assertRaisesRegex(ImportError, "Framework Foo could not be found"):
            # ^^^^ XXX: I don't like this exception, but it is public API by now.
            dyld.pathForFramework("Foo.framework")
