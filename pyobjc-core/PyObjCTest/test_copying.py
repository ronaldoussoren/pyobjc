import copy

import objc
from objc import super  # noqa: A004
from PyObjCTest.copying import OC_CopyBase, OC_CopyHelper, OC_CopyFails
from PyObjCTools.TestSupport import TestCase

NSObject = objc.lookUpClass("NSObject")
NSAutoreleasePool = objc.lookUpClass("NSAutoreleasePool")


def funcattr(**kwds):
    def annotate(func):
        for k, v in kwds.items():
            setattr(func, k, v)
        return func

    return annotate


class OC_TestCopy1(NSObject):
    def init(self):
        self = objc.super(OC_TestCopy1, self).init()
        if self is not None:
            self.x = 1
            self.y = 2
        return self

    def modify(self):
        self.x = 42
        self.y = 24
        self.z = 0

    @funcattr(occlass="OC_TestCopy1")
    def copyWithZone_(self, zone):
        other = OC_TestCopy1.allocWithZone_(zone).init()
        other.x = self.x
        other.y = self.y
        return other

    # Argh, copyWithZone_ is a classmethod by default unless the
    # superclass implements  -copyWithZone:
    copyWithZone_ = objc.selector(
        copyWithZone_, signature=NSObject.copyWithZone_.signature, isClassMethod=False
    )


# OC_CopyBase.initWithInt_
class OC_TestCopy2(OC_CopyBase):
    x = objc.ivar()  # type=objc._C_INT)

    def init(self):
        self = objc.super(OC_TestCopy2, self).initWithInt_(10)
        if self is not None:
            self.x = 1
            self.y = 2
        return self

    def modify(self):
        self.setIntVal_(40)
        self.x = 42
        self.y = 24
        self.z = 0


class OC_TestCopy3(OC_CopyBase):
    __slots__ = "x y".split()

    def init(self):
        self = objc.super(OC_TestCopy3, self).initWithInt_(10)
        if self is not None:
            self.x = 1
            self.y = 2
        return self

    def modify(self):
        self.setIntVal_(40)
        self.x = 42
        self.y = 24


class OC_TestCopy4(OC_CopyBase):
    def init(self):
        self = objc.super(OC_TestCopy4, self).initWithInt_(10)
        if self is None:
            return None

        self.x = 1
        self.y = 2
        return self

    def modify(self):
        self.setIntVal_(40)
        self.x = 42
        self.y = 24
        self.z = 0

    @funcattr(occlass="OC_TestCopy4")
    def copyWithZone_(self, zone):
        other = super().copyWithZone_(zone)
        other.x = self.x
        other.y = self.y
        other.z = "hello"
        return other


class TestNSCopyingHelper(NSObject):
    def copyWithZone_(self, zone):
        return 42


class TestNSCopying(TestCase):
    def testCopyingRegr20090327(self):
        self.assertFalse(TestNSCopyingHelper.new().copyWithZone_.isClassMethod)
        o = TestNSCopyingHelper.alloc().init()
        v = o.copyWithZone_(None)
        self.assertEqual(v, 42)

    def testCopyingWithoutSuperFromObjC(self):
        v = OC_TestCopy1.alloc().init()
        self.assertFalse(v.copyWithZone_.isClassMethod)
        self.assertEqual(v.copyWithZone_.callable.occlass, "OC_TestCopy1")
        del v

        p = NSAutoreleasePool.alloc().init()
        o = OC_CopyHelper.doCopySetup_(OC_TestCopy1)
        del p

        self.assertEqual(o.x, 42)
        self.assertEqual(o.y, 24)
        with self.assertRaisesRegex(
            AttributeError, "OC_TestCopy1' object has no attribute 'z'"
        ):
            o.z

    def testCopyingWithSuperFromObjC(self):
        o = OC_CopyBase.alloc().init()
        self.assertFalse(o.copyWithZone_.isClassMethod)
        del o

        o = OC_TestCopy2.alloc().init()
        self.assertFalse(o.copyWithZone_.isClassMethod)
        del o

        o = OC_TestCopy3.alloc().init()
        self.assertFalse(o.copyWithZone_.isClassMethod)
        del o

        o = OC_TestCopy4.alloc().init()
        self.assertEqual(o.copyWithZone_.callable.occlass, "OC_TestCopy4")
        del o

        p = NSAutoreleasePool.alloc().init()
        o = OC_CopyHelper.doCopySetup_(OC_TestCopy2)
        del p

        self.assertEqual(o.x, 42)
        self.assertEqual(o.y, 24)
        self.assertEqual(o.intVal(), 40)

        p = NSAutoreleasePool.alloc().init()
        o = OC_CopyHelper.doCopySetup_(OC_TestCopy3)
        del p

        self.assertEqual(o.x, 42)
        self.assertEqual(o.y, 24)
        self.assertEqual(o.intVal(), 40)

        p = NSAutoreleasePool.alloc().init()
        o = OC_CopyHelper.doCopySetup_(OC_TestCopy4)
        del p

        self.assertEqual(o.x, 42)
        self.assertEqual(o.y, 24)
        self.assertEqual(o.z, "hello")
        self.assertEqual(o.intVal(), 40)

    def testCopyingWithoutSuper(self):
        v = OC_TestCopy1.alloc().init()
        self.assertFalse(v.copyWithZone_.isClassMethod)
        self.assertEqual(v.copyWithZone_.callable.occlass, "OC_TestCopy1")
        del v

        v = OC_TestCopy1.alloc().init()
        v.modify()

        p = NSAutoreleasePool.alloc().init()
        o = v.copy()
        v.x = 20
        del v
        del p

        self.assertEqual(o.x, 42)
        self.assertEqual(o.y, 24)
        with self.assertRaisesRegex(
            AttributeError, "OC_TestCopy1' object has no attribute 'z'"
        ):
            o.z

    def testCopyingWithSuper(self):
        o = OC_CopyBase.alloc().init()
        self.assertFalse(o.copyWithZone_.isClassMethod)
        del o

        o = OC_TestCopy2.alloc().init()
        self.assertFalse(o.copyWithZone_.isClassMethod)
        del o

        o = OC_TestCopy3.alloc().init()
        self.assertFalse(o.copyWithZone_.isClassMethod)
        del o

        o = OC_TestCopy4.alloc().init()
        self.assertEqual(o.copyWithZone_.callable.occlass, "OC_TestCopy4")
        del o

        with objc.autorelease_pool():
            v = OC_TestCopy2.alloc().init()
            v.modify()

            o = v.copy()
            v.x = 20
            del v

        self.assertEqual(o.x, 42)
        self.assertEqual(o.y, 24)
        self.assertEqual(o.intVal(), 40)

        with objc.autorelease_pool():
            v = OC_TestCopy3.alloc().init()
            v.modify()

            o = v.copy()
            v.x = 20
            del v

        self.assertEqual(o.x, 42)
        self.assertEqual(o.y, 24)
        self.assertEqual(o.intVal(), 40)

        with objc.autorelease_pool():
            v = OC_TestCopy4.alloc().init()
            v.modify()

            o = v.copy()
            v.x = 20
            del v

        self.assertEqual(o.z, "hello")
        self.assertEqual(o.y, 24)
        self.assertEqual(o.x, 42)
        self.assertEqual(o.intVal(), 40)


NSMutableArray = objc.lookUpClass("NSMutableArray")


class TestPyCopyObjC(TestCase):
    # Testcases that ensure that copy.copy works
    # with Objective-C objects as well.

    def testCopyArray(self):
        a = NSMutableArray.arrayWithArray_(["a", "b", "c"])
        self.assertIsInstance(a, NSMutableArray)

        b = copy.copy(a)
        self.assertIsInstance(b, NSMutableArray)
        self.assertEqual(list(a), list(b))


class TestCopyingFailsWithPython(OC_CopyFails):
    def copy(self):
        self = super().copy()
        if self is None:
            return None

        self.key = 42
        return self

    def copyWithZone_(self, zone):
        self = super().copyWithZone_(zone)
        if self is None:
            return None

        self.key = 21
        return self


class TestCopyingFails(TestCase):
    def test_native(self):
        o = OC_CopyFails.alloc().init()

        self.assertIs(o.copy(), None)
        self.assertIs(o.copyWithZone_(None), None)

    def test_python(self):
        o = TestCopyingFailsWithPython.alloc().init()
        self.assertIs(o.copy(), None)
        self.assertIs(o.copyWithZone_(None), None)
