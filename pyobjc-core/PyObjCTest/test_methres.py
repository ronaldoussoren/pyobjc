from PyObjCTools.TestSupport import *

import objc

NSObject = objc.lookUpClass('NSObject')
NSURL = objc.lookUpClass('NSURL')

class TestMethodResolution (TestCase):
    def test_loading_categories(self):
        obj = NSObject.alloc().init()
        url = NSURL.alloc().initWithString_("http://www.python.org/")
        self.assertIsInstance(obj, NSObject)
        self.assertIsInstance(url, NSObject)
        self.assertIsInstance(url, NSURL)

        self.assertRaises(AttributeError, getattr, obj, 'oc_method1')
        self.assertRaises(AttributeError, getattr, obj, 'ocmethod2')

        # Check that a category was added to NSObject, and that
        # it can be used for NSURL objects as well.
        # NOTE: Don't check resolution of NSURL.ocmethod2 to ensure
        #       that resolution even works when there'd be a cache.
        import PyObjCTest.methres1
        self.assertEqual(obj.oc_method1(), 'NSObject.oc_method1')
        self.assertEqual(obj.ocmethod2(), 'NSObject.ocmethod2')
        self.assertEqual(url.oc_method1(), 'NSObject.oc_method1')
        #self.assertEqual(url.ocmethod2(), 'NSObject.ocmethod2')
        self.assertEqual(super(NSURL, url).oc_method1(), 'NSObject.oc_method1')
        #self.assertEqual(super(NSURL, url).ocmethod2(), 'NSObject.ocmethod2')

        # Load an NSURL category and check that it is used.
        import PyObjCTest.methres2
        self.assertEqual(obj.oc_method1(), 'NSObject.oc_method1')
        self.assertEqual(obj.ocmethod2(), 'NSObject.ocmethod2')
        self.assertEqual(url.oc_method1(), 'NSURL.oc_method1')
        self.assertEqual(url.ocmethod2(), 'NSURL.ocmethod2')
        self.assertEqual(super(NSURL, url).oc_method1(), 'NSObject.oc_method1')
        self.assertEqual(super(NSURL, url).ocmethod2(), 'NSObject.ocmethod2')


if __name__ == "__main__":
    main()
