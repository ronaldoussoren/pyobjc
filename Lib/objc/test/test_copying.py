import unittest
import objc

NSObject = objc.lookUpClass("NSObject")
NSAutoreleasePool = objc.lookUpClass("NSAutoreleasePool")
from objc.test.copying import OC_CopyHelper, OC_CopyBase

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

    def copyWithZone_(self, zone):
        other = super(OC_TestCopy4, self).copyWithZone_(zone)
        other.x = self.x
        other.y = self.y
        other.z = "hello"
        return other

class TestNSCopying (unittest.TestCase):
    def testCopyingWithoutSuperFromObjC(self):
        self.assert_(not OC_TestCopy1.copyWithZone_.isClassMethod)

        p = NSAutoreleasePool.alloc().init()
        o = OC_CopyHelper.doCopySetup_(OC_TestCopy1)
        del p

        self.assertEquals(o.x, 42)
        self.assertEquals(o.y, 24)
        self.assertRaises(AttributeError, getattr, o, 'z')

    def testCopyingWithSuperFromObjC(self):
        self.assert_(not OC_CopyBase.copyWithZone_.isClassMethod)
        self.assert_(not OC_TestCopy2.copyWithZone_.isClassMethod)
        self.assert_(not OC_TestCopy3.copyWithZone_.isClassMethod)
        self.assert_(not OC_TestCopy4.copyWithZone_.isClassMethod)

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
        self.assert_(not OC_TestCopy1.copyWithZone_.isClassMethod)

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

        self.assert_(not OC_CopyBase.copyWithZone_.isClassMethod)
        self.assert_(not OC_TestCopy2.copyWithZone_.isClassMethod)
        self.assert_(not OC_TestCopy3.copyWithZone_.isClassMethod)
        self.assert_(not OC_TestCopy4.copyWithZone_.isClassMethod)

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

if __name__ == "__main__":
    unittest.main()
