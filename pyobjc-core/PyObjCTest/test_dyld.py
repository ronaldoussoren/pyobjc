from PyObjCTools.TestSupport import *
import os

import objc._dyld as dyld

try:
    unicode
except NameError:
    unicode = str


class TestDyld (TestCase):
    def setUp(self):
        self.orig_environ = os.environ
        os.environ = os.environ.copy()

    def tearDown(self):
        os.environ = self.orig_environ

    def test_inject_suffixes(self):
        if 'DYLD_IMAGE_SUFFIX' in os.environ:
            del os.environ['DYLD_IMAGE_SUFFIX']


        # No suffix
        paths = [ '/usr/lib/libSystem.dylib',
                '/lib/libfoo.3.dylib',
                '/System/Library/Frameworks/CorePython.framework/Versions/B/CorePython',
                '/System/Library/Frameworks/CorePython.framework/CorePython',
        ]
        self.assertEqual(list(dyld.inject_suffixes(iter(paths))), paths)
        self.assertIs(dyld.inject_suffixes(paths), paths)

        os.environ['DYLD_IMAGE_SUFFIX'] = '_DEBUG'
        self.maxDiff = None
        self.assertEqual(list(dyld.inject_suffixes(iter(paths))), [
                '/usr/lib/libSystem_DEBUG.dylib',
                '/usr/lib/libSystem.dylib',
                '/lib/libfoo.3_DEBUG.dylib',
                '/lib/libfoo.3.dylib',
                '/System/Library/Frameworks/CorePython.framework/Versions/B/CorePython_DEBUG',
                '/System/Library/Frameworks/CorePython.framework/Versions/B/CorePython',
                '/System/Library/Frameworks/CorePython.framework/CorePython_DEBUG',
                '/System/Library/Frameworks/CorePython.framework/CorePython',
        ])


    def test_ensure_unicode(self):
        v = dyld.ensure_unicode("foo")
        self.assertIsInstance(v, unicode)
        self.assertEqual(v, b"foo".decode("utf-8"))

        v = dyld.ensure_unicode(b"foo")
        self.assertIsInstance(v, unicode)
        self.assertEqual(v, b"foo".decode("utf-8"))

        v = dyld.ensure_unicode(b"foo".decode("utf-8"))
        self.assertIsInstance(v, unicode)
        self.assertEqual(v, b"foo".decode("utf-8"))

        self.assertRaises(UnicodeError, dyld.ensure_unicode, b"\xff\xff")

    def test_dyld_library(self):
        for k in ('DYLD_LIBRARY_PATH', 'DYLD_FALLBACK_LIBRARY_PATH', 'DYLD_IMAGE_SUFFIX'):
            if k in os.environ:
                del os.environ[k]

        orig = os.path.exists
        try:
            os.path.exists = lambda fn: l.append(fn)

            l = []
            self.assertRaises(ValueError, dyld.dyld_library, '/usr/lib/libSystem.dylib', 'libXSystem.dylib')
            self.assertEqual(l, [
                '/usr/lib/libSystem.dylib',
                os.path.expanduser('~/lib/libXSystem.dylib'),
                '/usr/local/lib/libXSystem.dylib',
                '/lib/libXSystem.dylib',
                '/usr/lib/libXSystem.dylib',
            ])

            os.environ['DYLD_IMAGE_SUFFIX'] = '_debug'
            l = []
            self.assertRaises(ValueError, dyld.dyld_library, '/usr/lib/libSystem.dylib', 'libXSystem.dylib')
            self.assertEqual(l, [
                '/usr/lib/libSystem_debug.dylib',
                '/usr/lib/libSystem.dylib',
                os.path.expanduser('~/lib/libXSystem_debug.dylib'),
                os.path.expanduser('~/lib/libXSystem.dylib'),
                '/usr/local/lib/libXSystem_debug.dylib',
                '/usr/local/lib/libXSystem.dylib',
                '/lib/libXSystem_debug.dylib',
                '/lib/libXSystem.dylib',
                '/usr/lib/libXSystem_debug.dylib',
                '/usr/lib/libXSystem.dylib',
            ])

            del os.environ['DYLD_IMAGE_SUFFIX']

            os.environ['DYLD_LIBRARY_PATH'] = '/slib:/usr/slib'
            l = []
            self.assertRaises(ValueError, dyld.dyld_library, '/usr/lib/libSystem.dylib', 'libXSystem.dylib')
            self.assertEqual(l, [
                '/slib/libXSystem.dylib',
                '/usr/slib/libXSystem.dylib',
                '/usr/lib/libSystem.dylib',
                os.path.expanduser('~/lib/libXSystem.dylib'),
                '/usr/local/lib/libXSystem.dylib',
                '/lib/libXSystem.dylib',
                '/usr/lib/libXSystem.dylib',
            ])
            del os.environ['DYLD_LIBRARY_PATH']

            os.environ['DYLD_FALLBACK_LIBRARY_PATH'] = '/slib:/usr/slib'
            l = []
            self.assertRaises(ValueError, dyld.dyld_library, '/usr/lib/libSystem.dylib', 'libXSystem.dylib')
            self.assertEqual(l, [
                '/usr/lib/libSystem.dylib',
                '/slib/libXSystem.dylib',
                '/usr/slib/libXSystem.dylib',
            ])
            del os.environ['DYLD_FALLBACK_LIBRARY_PATH']

            os.environ['DYLD_LIBRARY_PATH'] = "/lib2:/lib3"
            os.environ['DYLD_FALLBACK_LIBRARY_PATH'] = "/lib4:/lib5"
            os.environ['DYLD_IMAGE_SUFFIX'] = "_profile"

            l = []
            self.assertRaises(ValueError, dyld.dyld_library, '/usr/lib/libSystem.dylib', 'libXSystem.dylib')
            self.assertEqual(l, [
                '/lib2/libXSystem_profile.dylib',
                '/lib2/libXSystem.dylib',
                '/lib3/libXSystem_profile.dylib',
                '/lib3/libXSystem.dylib',
                '/usr/lib/libSystem_profile.dylib',
                '/usr/lib/libSystem.dylib',
                '/lib4/libXSystem_profile.dylib',
                '/lib4/libXSystem.dylib',
                '/lib5/libXSystem_profile.dylib',
                '/lib5/libXSystem.dylib',
            ])
            del os.environ['DYLD_LIBRARY_PATH']
            del os.environ['DYLD_FALLBACK_LIBRARY_PATH']
            del os.environ['DYLD_IMAGE_SUFFIX']

        finally:
            os.path.exists = orig


        self.assertEqual(dyld.dyld_library('/usr/lib/libSystem.dylib', 'libXSystem.dylib'), '/usr/lib/libSystem.dylib')

        os.environ['DYLD_IMAGE_SUFFIX'] = "_debug"
        self.assertEqual(dyld.dyld_library('/usr/lib/libSystem.dylib', 'libSystem.dylib'), '/usr/lib/libSystem_debug.dylib')

    def test_dyld_framework(self):
        for k in ('DYLD_FRAMEWORK_PATH', 'DYLD_FALLBACK_FRAMEWORK_PATH', 'DYLD_IMAGE_SUFFIX'):
            if k in os.environ:
                del os.environ[k]

        orig = os.path.exists
        try:
            os.path.exists = lambda fn: l.append(fn)

            self.maxDiff = None

            l = []
            self.assertRaises(ImportError, dyld.dyld_framework, "/System/Library/Cocoa.framework/Cocoa", "XCocoa")
            self.assertEqual(l, [
                "/System/Library/Cocoa.framework/Cocoa",
                os.path.expanduser("~/Library/Frameworks/XCocoa.framework/XCocoa"),
                "/Library/Frameworks/XCocoa.framework/XCocoa",
                "/Network/Library/Frameworks/XCocoa.framework/XCocoa",
                "/System/Library/Frameworks/XCocoa.framework/XCocoa",
            ])

            os.environ["DYLD_IMAGE_SUFFIX"] = "_profile"
            l = []
            self.assertRaises(ImportError, dyld.dyld_framework, "/System/Library/Cocoa.framework/Cocoa", "XCocoa")
            self.assertEqual(l, [
                "/System/Library/Cocoa.framework/Cocoa_profile",
                "/System/Library/Cocoa.framework/Cocoa",
                os.path.expanduser("~/Library/Frameworks/XCocoa.framework/XCocoa_profile"),
                os.path.expanduser("~/Library/Frameworks/XCocoa.framework/XCocoa"),
                "/Library/Frameworks/XCocoa.framework/XCocoa_profile",
                "/Library/Frameworks/XCocoa.framework/XCocoa",
                "/Network/Library/Frameworks/XCocoa.framework/XCocoa_profile",
                "/Network/Library/Frameworks/XCocoa.framework/XCocoa",
                "/System/Library/Frameworks/XCocoa.framework/XCocoa_profile",
                "/System/Library/Frameworks/XCocoa.framework/XCocoa",
            ])
            del os.environ["DYLD_IMAGE_SUFFIX"]

            os.environ["DYLD_FRAMEWORK_PATH"] = "/Projects/Frameworks:/Company"
            l = []
            self.assertRaises(ImportError, dyld.dyld_framework, "/System/Library/Cocoa.framework/Cocoa", "XCocoa")
            self.assertEqual(l, [
                "/Projects/Frameworks/XCocoa.framework/XCocoa",
                "/Company/XCocoa.framework/XCocoa",
                "/System/Library/Cocoa.framework/Cocoa",
                os.path.expanduser("~/Library/Frameworks/XCocoa.framework/XCocoa"),
                "/Library/Frameworks/XCocoa.framework/XCocoa",
                "/Network/Library/Frameworks/XCocoa.framework/XCocoa",
                "/System/Library/Frameworks/XCocoa.framework/XCocoa",
            ])
            del os.environ["DYLD_FRAMEWORK_PATH"]

            os.environ["DYLD_FALLBACK_FRAMEWORK_PATH"] = "/Projects/Frameworks:/Company"
            l = []
            self.assertRaises(ImportError, dyld.dyld_framework, "/System/Library/Cocoa.framework/Cocoa", "XCocoa")
            self.assertEqual(l, [
                "/System/Library/Cocoa.framework/Cocoa",
                "/Projects/Frameworks/XCocoa.framework/XCocoa",
                "/Company/XCocoa.framework/XCocoa",
            ])
            del os.environ["DYLD_FALLBACK_FRAMEWORK_PATH"]

            os.environ["DYLD_FRAMEWORK_PATH"] = "/Prefix1:/Prefix2"
            os.environ["DYLD_FALLBACK_FRAMEWORK_PATH"] = "/Suffix1:/Suffix2"
            os.environ["DYLD_IMAGE_SUFFIX"] = "_debug"

            l = []
            self.assertRaises(ImportError, dyld.dyld_framework, "/System/Library/Cocoa.framework/Cocoa", "XCocoa", "B")
            self.assertEqual(l, [
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
            ])
            del os.environ["DYLD_FRAMEWORK_PATH"]
            del os.environ["DYLD_FALLBACK_FRAMEWORK_PATH"]
            del os.environ["DYLD_IMAGE_SUFFIX"]


        finally:
            os.path.exists = orig

        self.assertEqual(dyld.dyld_framework("/System/Library/Cocoa.framework/Cocoa", "Cocoa"), "/System/Library/Frameworks/Cocoa.framework/Cocoa")
        self.assertEqual(dyld.dyld_framework("/System/Library/Cocoa.framework/Cocoa", "Cocoa", "A"), "/System/Library/Frameworks/Cocoa.framework/Versions/A/Cocoa")

    def test_readlink(self):
        # Some python versions had a readlink version that doesn't work with unicode
        # input, ensure that we're not one one of those
        self.assertEqual(os.path.realpath("/usr/lib/libSystem.dylib"), "/usr/lib/libSystem.B.dylib")
        self.assertEqual(os.path.realpath(b"/usr/lib/libSystem.dylib"), b"/usr/lib/libSystem.B.dylib")
        self.assertEqual(os.path.realpath(b"/usr/lib/libSystem.dylib".decode('utf-8')), b"/usr/lib/libSystem.B.dylib".decode('utf-8'))

    def test_dyld_find(self):
        self.assertEqual(dyld.dyld_find('Cocoa.framework'), '/System/Library/Frameworks/Cocoa.framework/Cocoa')
        self.assertEqual(dyld.dyld_find('libSystem.dylib'), '/usr/lib/libSystem.dylib')

    def test_pathForFramework(self):
        self.assertEqual(dyld.pathForFramework('Cocoa.framework'), '/System/Library/Frameworks/Cocoa.framework')
        self.assertRaises(ImportError, dyld.pathForFramework, 'Foo.framework')

if __name__ == "__main__":
    main()
