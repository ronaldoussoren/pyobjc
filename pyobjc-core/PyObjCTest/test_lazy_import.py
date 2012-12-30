from PyObjCTools.TestSupport import *

import objc._lazyimport as lazyimport
import objc
import sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a


class TestLazyImport (TestCase):
    def test_exports(self):
        self.assertIs(objc.ObjCLazyModule, lazyimport.ObjCLazyModule)
        self.assertTrue(issubclass(objc.ObjCLazyModule, type(objc)))


    def test_getattr_map(self):
        o = lazyimport.GetAttrMap(sys)
        self.assertEqual(o['path'], sys.path)
        self.assertEqual(o['version'], sys.version)
        self.assertRaises(KeyError, o.__getitem__, 'nosuchkey')

    def test_load_bundle(self):
        NSBundle = objc.lookUpClass('NSBundle')

        # _objc is linked with Foundation, hence should be able to load without
        # providing a valid path
        o = lazyimport._loadBundle('Foundation', 'com.apple.Foundation', '/dev/null')
        self.assertIsInstance(o, NSBundle)
        self.assertEqual(o.bundleIdentifier(), 'com.apple.Foundation')
        self.assertTrue(o.isLoaded())

        # Load using path
        o = lazyimport._loadBundle('AppKit', None, '/System/Library/Frameworks/AppKit.framework')
        o.load()
        self.assertEqual(o.bundleIdentifier(), 'com.apple.AppKit')
        self.assertTrue(o.isLoaded())


        # Should not be loaded yet, hence fallback from identifier to path
        o = lazyimport._loadBundle('PreferencePanes', 'com.apple.frameworks.preferencepanes', '/System/Library/Frameworks/PreferencePanes.framework')
        o.load()
        self.assertEqual(o.bundleIdentifier(), 'com.apple.frameworks.preferencepanes')
        self.assertTrue(o.isLoaded())



    def no_test_all_types(self):
        # NOTE: Test isn't ready yet
        # Note: this test uses the real functions, other tests can (and will) mock 
        #       functions in objc._objc to test failure condictions, but the full
        #       API stack should be used in at least one testcase.
        metadict = {
            'constants': '$NSAFMCharacterSet$NSAFMDescender$',
            'constants_dicts': { 
                'NSAFMAscender': b'@',
            },
            'enums': '$NSAWTEventType@16$NSAboveBottom@4$NSAboveTop@1$',

            'functions': {
                'NSRectClipList': (
                    sel32or64(b'v^{_NSRect={_NSPoint=ff}{_NSSize=ff}}i', b'v^{CGRect={CGPoint=dd}{CGSize=dd}}q'), 
                    '', 
                    {
                        'arguments': {
                            0: {
                                'c_array_length_in_arg': 1, 
                                'type_modifier': b'n'
                            }
                        }
                    }
                ),
            },
            'aliases': {
                'doc_string': '__doc__',
            },
            'expressions': {
                'mysum': 'NSAWTEventType + NSAboveBottom + 3',
            }
        }

        initial_dict = {
                '__doc__': 'AppKit test module',
        }

        mod = objc.ObjCLazyModule ('AppKit', None, '/System/Library/Frameworks/AppKit.framework', metadict, None,
                initial_dict, ())
        self.assertIsInstance(mod, objc.ObjCLazyModule)

        self.assertEqual(mod.__doc__, initial_dict['__doc__'])
        self.assertEqual(mod.doc_string, initial_dict['__doc__'])
        self.assertIsInstance(mod.NSAFMCharacterSet, objc.objc_object)
        self.assertIsInstance(mod.NSAFMDescender, objc.objc_object)
        self.assertIsInstance(mod.NSAFMAscender, objc.objc_object)
        self.assertEqual(mod.NSAWTEventType, 16)
        self.assertEqual(mod.NSAboveBottom, 4)
        self.assertEqual(mod.NSAboveTop, 1)
        self.assertIsInstance(mod.NSRectClipList, objc.function)
        self.assertEqual(mod.NSRectClipList.__name__, 'NSRectClipList')
        self.assertArgLengthInArg(mod.NSRectClipList, 0, 1)
        self.assertEqual(mod.mysum, mod.NSAWTEventType + mod.NSAboveBottom + 3)


    def test_hack(self):
        # This is not really a test, but ensures that the code is at 
        # least exercised a little. 
        # There still have to be real tests...
        try:
            import CoreFoundation
            import Foundation
            import AppKit
        except ImportError:
            return

        CoreFoundation.__all__
        Foundation.__all__
        AppKit.__all__
        dir(Foundation)

        try:
            import Quartz
        except ImportError:
            return

        Quartz.__all__


       
    # XXX: add tests for the rest of the module
    # - metadict with/without various elements (that is, with/without 'misc', 'constants', ...)
    # - metadict with invalid data
    # - verify that look-ups are done in the expected order (and document?)
    # - dotted name ('Quartz.CoreGraphics')
    # - test with frameworkIdentifier == frameworkPath == None (both with and without a parents. 
    # - test with protocols in metadict

if __name__ == "__main__":
    main()
