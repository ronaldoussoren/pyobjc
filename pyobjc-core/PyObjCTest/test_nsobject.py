import objc
import os
import tempfile

# from objc import super
from PyObjCTools.TestSupport import TestCase
from PyObjCTest.helpernsobject import OC_AllocRaises, OC_RefcountRaises
from objc import super  # noqa: A004
from .test_metadata import NoObjCClass

NSObject = objc.lookUpClass("NSObject")

objc.registerMetaDataForSelector(
    b"OC_AllocRaises", b"invokeAlloc:", {"retval": {"already_retained": True}}
)


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
    def alloc(cls):
        return super().alloc()

    def retain(self):
        if self.scenario == 1:
            self.scenario = 0
            raise SomeException("retain")
        elif self.scenario == 4:
            self.scenario = 0
            return NoObjCClass()
        r = super().retain()
        return r

    def release(self):
        if self.scenario == 2:
            self.scenario = 0
            raise SomeException("release")
        elif self.scenario == 5:
            self.scenario = 0
            return 1
        r = super().release()
        return r

    def dealloc(self):
        if self.scenario == 3:
            self.scenario = 0
            raise SomeException("dealloc")
        r = super().dealloc()
        return r


class Py_DeallocReturns(NSObject):
    def dealloc(self):
        super().dealloc()
        return 42


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

    def test_dealloc_returns_value(self):
        o = Py_DeallocReturns.alloc().init()
        orig = os.dup(2)

        with tempfile.TemporaryFile() as stream:
            os.dup2(stream.fileno(), 2)
            try:
                del o

            finally:
                os.dup2(orig, 2)

            stream.seek(0)
            capture = stream.read().decode()

        self.assertIn("dealloc should return None, returned instance of int", capture)

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

        return

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

        imp = o.methodForSelector_("retain")
        o.setScenario_(1)
        with self.assertRaisesRegex(objc.error, "SomeException - Some Reason"):
            imp(o)

        o.setScenario_(2)
        with self.assertRaisesRegex(objc.error, "SomeException - Some Reason"):
            o.release()

        imp = o.methodForSelector_("release")
        o.setScenario_(2)
        with self.assertRaisesRegex(objc.error, "SomeException - Some Reason"):
            imp(o)

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

        # XXX: Not sure why, but calling o.dealloc() before  'with tempfile...'
        #      causes a crash.
        o = OC_RefcountRaises.alloc().init()
        o.setScenario_(3)
        with self.assertRaisesRegex(objc.error, "SomeException - Some Reason"):
            o.dealloc()

        o = OC_RefcountRaises.alloc().init()
        o.setScenario_(3)
        imp = o.methodForSelector_(b"dealloc")
        with self.assertRaisesRegex(objc.error, "SomeException - Some Reason"):
            imp(o)

    def test_python_alloc_raises(self):
        with self.assertRaisesRegex(SomeException, "alloc"):
            OC_AllocRaises.invokeAlloc_(Py_AllocRaises)

    def test_python_alloc(self):
        count = 0

        class Py_AllocPasses(NSObject):
            @classmethod
            def alloc(cls):
                nonlocal count
                count += 1
                return super().alloc()

        v = OC_AllocRaises.invokeAlloc_(Py_AllocPasses).init()
        self.assertIsInstance(v, Py_AllocPasses)
        self.assertEqual(count, 1)

    def test_alloc_returns_invalid(self):
        class Py_AllocReturnsInvalid(NSObject):
            def alloc(cls):
                return NoObjCClass()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            OC_AllocRaises.invokeAlloc_(Py_AllocReturnsInvalid).init()

    def test_python_retain_release(self):
        obj = Py_RefCountRaises.alloc().init()

        obj.retain()
        obj.release()

        obj.scenario = 1
        with self.assertRaisesRegex(SomeException, "retain"):
            OC_AllocRaises.invoke_on_(b"retain", obj)

        obj.scenario = 2
        with self.assertRaisesRegex(SomeException, "release"):
            OC_AllocRaises.invoke_on_(b"release", obj)

        obj.scenario = 4
        with self.assertRaisesRegex(TypeError, "proxy"):
            OC_AllocRaises.invoke_on_(b"retain", obj)

        obj.scenario = 5
        with self.assertRaisesRegex(TypeError, "release should return None"):
            OC_AllocRaises.invoke_on_(b"release", obj)

        orig = os.dup(2)
        obj.scenario = 3
        with tempfile.TemporaryFile() as stream:
            os.dup2(stream.fileno(), 2)
            try:
                del obj

            finally:
                os.dup2(orig, 2)

            stream.seek(0)
            capture = stream.read().decode()

        self.assertIn("Exception during dealloc of proxy: ", capture)
        self.assertIn("PyObjCTest.test_nsobject.SomeException", capture)
