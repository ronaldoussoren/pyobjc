import objc
import objc._objc
from PyObjCTools.TestSupport import TestCase

NSObject = objc.lookUpClass("NSObject")
NSURL = objc.lookUpClass("NSURL")


class TestMethodResolution(TestCase):
    def test_super_object(self):
        if getattr(objc._objc, "pep447", False):
            self.assertIs(objc.super, super)
        else:
            self.assertIsSubclass(objc.super, super)

    def test_loading_categories(self):
        obj = NSObject.alloc().init()
        url = NSURL.alloc().initWithString_("http://www.python.org/")
        self.assertIsInstance(obj, NSObject)
        self.assertIsInstance(url, NSObject)
        self.assertIsInstance(url, NSURL)

        with self.assertRaisesRegex(
            AttributeError, "'NSObject' object has no attribute 'oc_method1'"
        ):
            obj.oc_method1
        with self.assertRaisesRegex(
            AttributeError, "'NSObject' object has no attribute 'ocmethod2'"
        ):
            obj.ocmethod2

        # Check that a category was added to NSObject, and that
        # it can be used for NSURL objects as well.
        # NOTE: Don't check resolution of NSURL.ocmethod2 to ensure
        #       that resolution even works when there'd be a cache.
        import PyObjCTest.methres1  # noqa: F401

        self.assertEqual(obj.oc_method1(), "NSObject.oc_method1")
        self.assertEqual(obj.ocmethod2(), "NSObject.ocmethod2")
        self.assertEqual(url.oc_method1(), "NSObject.oc_method1")
        # self.assertEqual(url.ocmethod2(), 'NSObject.ocmethod2')
        self.assertEqual(super(NSURL, url).oc_method1(), "NSObject.oc_method1")
        # self.assertEqual(super(NSURL, url).ocmethod2(), 'NSObject.ocmethod2')

        # Load an NSURL category and check that it is used.
        import PyObjCTest.methres2  # noqa: F401

        self.assertEqual(obj.oc_method1(), "NSObject.oc_method1")
        self.assertEqual(obj.ocmethod2(), "NSObject.ocmethod2")
        self.assertEqual(url.oc_method1(), "NSURL.oc_method1")
        self.assertEqual(url.ocmethod2(), "NSURL.ocmethod2")
        self.assertEqual(super(NSURL, url).oc_method1(), "NSObject.oc_method1")
        self.assertEqual(super(NSURL, url).ocmethod2(), "NSObject.ocmethod2")
