from PyObjCTools.TestSupport import *
import objc
import objc._convenience as convenience

class TestConvenienceHelpers (TestCase):
    def test_add_for_selector(self):
        methods = [
            ('add', lambda self, x: self.testMethod_(x))
        ]

        with filterWarnings("error", DeprecationWarning):
            self.assertRaises(DeprecationWarning, objc.addConvenienceForSelector, b'testMethod:', methods)
            if b'testMethod' in convenience._CONVENIENCE_METHODS:
                del convenience._CONVENIENCE_METHODS[b'testMethods:']

        with filterWarnings("ignore", DeprecationWarning):
            self.assertNotIn(b'testMethod:', convenience._CONVENIENCE_METHODS)
            try:
                objc.addConvenienceForSelector(b'testMethod:', methods)

                self.assertEqual(convenience._CONVENIENCE_METHODS[b'testMethod:'], methods)

            finally:
                if b'testMethod' in convenience._CONVENIENCE_METHODS:
                    del convenience._CONVENIENCE_METHODS[b'testMethods:']


    def test_add_for_class(self):
        self.assertNotIn("MyObject", convenience.CLASS_METHODS)

        methods = [
            ('info', lambda self: self.description())
        ]

        try:
            objc.addConvenienceForClass("MyObject", methods)
            self.assertEqual(convenience.CLASS_METHODS["MyObject"], methods)

        finally:
            if 'MyObject' in convenience.CLASS_METHODS:
                del convenience.CLASS_METHODS["MyObject"]



class TestBasicConveniences (TestCase):
    def testBundleForClass(self):
        orig = convenience.currentBundle
        try:
            the_bundle = object()
            def currentBundle():
                return the_bundle
            convenience.currentBundle = currentBundle

            class OC_Test_Basic_Convenience_1 (objc.lookUpClass("NSObject")):
                pass

            self.assertIs(OC_Test_Basic_Convenience_1.bundleForClass(), the_bundle)
        finally:
            convenience.currentBundle = orig

    def test_kvc_helper(self):
        o = objc.lookUpClass('NSURL').URLWithString_('http://www.python.org/')
        self.assertEqual(o.host(), 'www.python.org')

        self.assertEqual(o._.host, 'www.python.org')
        self.assertEqual(o._['host'], 'www.python.org')
        self.assertRaises(TypeError, lambda: o._[42])
        self.assertEqual(repr(o._), '<KVC accessor for %r>'%(o,))
        self.assertRaises(AttributeError, getattr, o._, 'nosuchattr')
        self.assertRaises(TypeError, o._.__setitem__, 42) 

        o = objc.lookUpClass('NSMutableDictionary').dictionary()
        o._.key1 = 1
        o._['key2'] = 2

        self.assertEqual(o, {'key1': 1, 'key2': 2 })
        self.assertRaises(AttributeError, o._.nosuchattr)
        self.assertRaises(TypeError, o._.__setitem__, 42) 



# TODO: Explicit tests for add_convenience_methods.

if __name__ == "__main__":
    main()
