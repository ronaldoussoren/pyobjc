from PyObjCTools.TestSupport import *
import objc

NSObject = objc.lookUpClass("NSObject")
NSAutoreleasePool = objc.lookUpClass("NSAutoreleasePool")
from PyObjCTest.copying import OC_CopyHelper, OC_CopyBase

def funcattr(**kwds):
    def annotate(func):
        for k, v in kwds.iteritems():
            setattr(func, k, v)
        return func
    return annotate

class OC_TestCopy1 (NSObject):
    def init(self):
        self = super(OC_TestCopy1, self).init()
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
    copyWithZone_ = objc.selector(copyWithZone_, 
            signature=NSObject.copyWithZone_.signature, 
            isClassMethod=False)

class OC_TestCopy2 (OC_CopyBase):
    def init(self):
        self = super(OC_TestCopy2, self).initWithInt_(10)
        if self is not None:
            self.x = 1
            self.y = 2
        return self

    def modify(self):
        self.setIntVal_(40)
        self.x = 42
        self.y = 24
        self.z = 0

class OC_TestCopy3 (OC_CopyBase):
    __slots__ = 'x y'.split()

    def init(self):
        self = super(OC_TestCopy3, self).initWithInt_(10)
        if self is not None:
            self.x = 1
            self.y = 2
        return self

    def modify(self):
        self.setIntVal_(40)
        self.x = 42
        self.y = 24

class OC_TestCopy4 (OC_CopyBase):
    def init(self):
        self = super(OC_TestCopy4, self).initWithInt_(10)
        if self is not None:
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
        other = super(OC_TestCopy4, self).copyWithZone_(zone)
        other.x = self.x
        other.y = self.y
        other.z = "hello"
        return other

class TestNSCopyingHelper (NSObject):
    def copyWithZone_(self, zone):
        return 42

class TestNSCopying (TestCase):
    def testCopyingRegr20090327(self):
        o = TestNSCopyingHelper.alloc().init()
        v = o.copyWithZone_(None)
        self.failUnlessEqual(v, 42)

    def testCopyingWithoutSuperFromObjC(self):
        v = OC_TestCopy1.alloc().init()
        self.assert_(not v.copyWithZone_.isClassMethod)
        self.assertEquals(v.copyWithZone_.callable.occlass, "OC_TestCopy1")
        del v

        p = NSAutoreleasePool.alloc().init()
        o = OC_CopyHelper.doCopySetup_(OC_TestCopy1)
        del p

        self.assertEquals(o.x, 42)
        self.assertEquals(o.y, 24)
        self.assertRaises(AttributeError, getattr, o, 'z')

    def testCopyingWithSuperFromObjC(self):
        o = OC_CopyBase.alloc().init()
        self.assert_(not o.copyWithZone_.isClassMethod)
        del o

        o = OC_TestCopy2.alloc().init()
        self.assert_(not o.copyWithZone_.isClassMethod)
        del o

        o = OC_TestCopy3.alloc().init()
        self.assert_(not o.copyWithZone_.isClassMethod)
        del o

        o = OC_TestCopy4.alloc().init()
        self.assertEquals(o.copyWithZone_.callable.occlass, "OC_TestCopy4")
        del o

        p = NSAutoreleasePool.alloc().init()
        o = OC_CopyHelper.doCopySetup_(OC_TestCopy2)
        del p

        self.assertEquals(o.x, 42)
        self.assertEquals(o.y, 24)
        self.assertEquals(o.intVal(), 40)

        p = NSAutoreleasePool.alloc().init()
        o = OC_CopyHelper.doCopySetup_(OC_TestCopy3)
        del p

        self.assertEquals(o.x, 42)
        self.assertEquals(o.y, 24)
        self.assertEquals(o.intVal(), 40)

        p = NSAutoreleasePool.alloc().init()
        o = OC_CopyHelper.doCopySetup_(OC_TestCopy4)
        del p

        self.assertEquals(o.x, 42)
        self.assertEquals(o.y, 24)
        self.assertEquals(o.z, "hello")
        self.assertEquals(o.intVal(), 40)

    def testCopyingWithoutSuper(self):
        v = OC_TestCopy1.alloc().init()
        self.assert_(not v.copyWithZone_.isClassMethod)
        self.assertEquals(v.copyWithZone_.callable.occlass, "OC_TestCopy1")
        del v

        v = OC_TestCopy1.alloc().init()
        v.modify()

        p = NSAutoreleasePool.alloc().init()
        o = v.copy()
        v.x = 20
        del v
        del p

        self.assertEquals(o.x, 42)
        self.assertEquals(o.y, 24)
        self.assertRaises(AttributeError, getattr, o, 'z')

    def testCopyingWithSuper(self):
        o = OC_CopyBase.alloc().init()
        self.assert_(not o.copyWithZone_.isClassMethod)
        del o

        o = OC_TestCopy2.alloc().init()
        self.assert_(not o.copyWithZone_.isClassMethod)
        del o

        o = OC_TestCopy3.alloc().init()
        self.assert_(not o.copyWithZone_.isClassMethod)
        del o

        o = OC_TestCopy4.alloc().init()
        self.assertEquals(o.copyWithZone_.callable.occlass, "OC_TestCopy4")
        del o

        p = NSAutoreleasePool.alloc().init()
        v = OC_TestCopy2.alloc().init()
        v.modify()

        o = v.copy()
        v.x = 20
        del v
        del p

        self.assertEquals(o.x, 42)
        self.assertEquals(o.y, 24)
        self.assertEquals(o.intVal(), 40)

        p = NSAutoreleasePool.alloc().init()
        v = OC_TestCopy3.alloc().init()
        v.modify()

        o = v.copy()
        v.x = 20
        del v
        del p

        self.assertEquals(o.x, 42)
        self.assertEquals(o.y, 24)
        self.assertEquals(o.intVal(), 40)

        p = NSAutoreleasePool.alloc().init()
        v = OC_TestCopy4.alloc().init()
        v.modify()

        o = v.copy()
        v.x = 20
        del v
        del p

        self.assertEquals(o.z, "hello")
        self.assertEquals(o.y, 24)
        self.assertEquals(o.x, 42)
        self.assertEquals(o.intVal(), 40)


NSMutableArray = objc.lookUpClass("NSMutableArray")
import copy

class TestPyCopyObjC (TestCase):
    # Testcases that ensure that copy.copy works
    # with Objective-C objects as well.

    def testCopyArray(self):
        a = NSMutableArray.arrayWithArray_(['a', 'b', 'c'])
        self.assert_(isinstance(a, NSMutableArray))

        b = copy.copy(a)
        self.assert_(isinstance(b, NSMutableArray))
        self.assert_(list(a) == list(b))


if __name__ == "__main__":
    main()
