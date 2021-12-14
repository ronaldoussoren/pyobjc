import objc

# from objc import super
from PyObjCTools.TestSupport import TestCase
from PyObjCTest.helpernsobject import OC_AllocRaises

NSObject = objc.lookUpClass("NSObject")


class TestNSOBjectSupport(TestCase):
    def test_invalid_alloc(self):
        with self.assertRaisesRegex(TypeError, ".*expected no arguments, got 1"):
            NSObject.alloc(42)

    def test_invalid_cls(self):
        with self.assertRaisesRegex(
            TypeError, "Expecting instance of NSObject as self, got one of int"
        ):
            type(NSObject).__dict__["alloc"](42)

    def test_alloc_raises(self):
        with self.assertRaisesRegex(objc.error, "SomeException - Some Reason"):
            OC_AllocRaises.alloc().init()

        imp = OC_AllocRaises.methodForSelector_("alloc")

        with self.assertRaisesRegex(objc.error, "SomeException - Some Reason"):
            imp(OC_AllocRaises)

    def test_invalid_dealloc(self):
        o = NSObject.alloc().init()
        with self.assertRaisesRegex(TypeError, ".*expected no arguments, got 1"):
            o.dealloc(42)

    def test_invalid_retain(self):
        o = NSObject.alloc().init()
        with self.assertRaisesRegex(TypeError, ".*expected no arguments, got 1"):
            o.retain(42)

    def test_invalid_release(self):
        o = NSObject.alloc().init()
        with self.assertRaisesRegex(TypeError, ".*expected no arguments, got 1"):
            o.release(42)

    def test_retain_release(self):
        o = NSObject.alloc().init()
        start = o.retainCount()

        o.retain()
        self.assertEqual(o.retainCount(), start + 1)

        o.release()
        self.assertEqual(o.retainCount(), start)

        imp_ret = o.methodForSelector_("retain")
        imp_rel = o.methodForSelector_("release")

        imp_ret(o)
        self.assertEqual(o.retainCount(), start + 1)

        imp_rel(o)
        self.assertEqual(o.retainCount(), start)
