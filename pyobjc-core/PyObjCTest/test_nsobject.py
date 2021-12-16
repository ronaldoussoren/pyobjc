import objc
import os
import tempfile

# from objc import super
from PyObjCTools.TestSupport import TestCase
from PyObjCTest.helpernsobject import OC_AllocRaises, OC_RefcountRaises
from objc import super  # noqa: F401

NSObject = objc.lookUpClass("NSObject")


class SomeException(Exception):
    pass


class Py_AllocRaises(NSObject):
    @classmethod
    def alloc(cls):
        raise SomeException("alloc")


class Py_RefCountRaises(NSObject):
    def init(self):
        self.scenario = 0
        return self

    # XXX: For some reason super() doens't work
    #      to resolve these methods, to be fixed...

    def retain(self):
        if self.scenario == 1:
            self.scenario = 0
            raise SomeException("retain")
        return NSObject.__dict__["retain"](self)
        # return super.retain()

    def release(self):
        if self.scenario == 2:
            self.scenario = 0
            raise SomeException("release")
        return NSObject.__dict__["release"](self)
        # return super.release()

    def dealloc(self):
        # print("dealloc", self.scenario)
        if self.scenario == 3:
            self.scenario = 0
            raise SomeException("dealloc")
        return NSObject.__dict__["dealloc"](self)
        # return super.dealloc()


class TestNSObjectSupport(TestCase):
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

        # Note: the code below just tests error paths and
        # is not in any way representative of normal code.

        o = OC_RefcountRaises.alloc().init()

        o.setScenario_(1)
        with self.assertRaisesRegex(objc.error, "SomeException - Some Reason"):
            o.retain()

        o.setScenario_(2)
        with self.assertRaisesRegex(objc.error, "SomeException - Some Reason"):
            o.release()

        o.setScenario_(3)
        orig = os.dup(2)

        with tempfile.TemporaryFile() as stream:
            os.dup2(stream.fileno(), 2)
            try:
                del o

            finally:
                os.dup2(orig, 2)

            stream.seek(0)
            capture = stream.read().decode()

        self.assertIn("Exception during dealloc of proxy: Some Reason", capture)

        o = OC_RefcountRaises.alloc().init()
        o.setScenario_(3)
        with self.assertRaisesRegex(objc.error, "SomeException - Some Reason"):
            o.dealloc()

    def test_python_alloc_raises(self):
        with self.assertRaisesRegex(SomeException, "alloc"):
            Py_AllocRaises.alloc()

    def test_python_retain_release(self):
        obj = Py_RefCountRaises.alloc().init()

        obj.retain()
        obj.release()

        obj.scenario = 1
        with self.assertRaisesRegex(SomeException, "retain"):
            obj.retain()

        obj.scenario = 2
        with self.assertRaisesRegex(SomeException, "release"):
            obj.release()

        obj.scenario = 3
        with self.assertRaisesRegex(SomeException, "dealloc"):
            obj.dealloc()

        return

        # XXX: raising in dealloc hangs the interpreter

        obj.scenario = 3
        orig = os.dup(2)

        with tempfile.TemporaryFile() as stream:
            os.dup2(stream.fileno(), 2)
            try:
                del obj

            finally:
                os.dup2(orig, 2)

            stream.seek(0)
            capture = stream.read().decode()

        self.assertIn("Exception during dealloc of proxy: Some Reason", capture)
