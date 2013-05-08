import weakref
from PyObjCTools.TestSupport import *
from PyObjCTest.fnd import NSObject, NSArray, NSAutoreleasePool

class OC_WeakrefTest1 (NSObject):
    pass

class OC_WeakrefTest2 (OC_WeakrefTest1):
    pass

class TestWeakrefs (TestCase):
    def testPureObjC(self):
        o = NSObject.new()
        self.assertRaises(TypeError, weakref.ref, o)

    def testFirstGenPython(self):
        o = OC_WeakrefTest1.new()
        self.assertRaises(TypeError, weakref.ref, o)

    def testSecondGenPython(self):
        o = OC_WeakrefTest2.new()
        self.assertRaises(TypeError, weakref.ref, o)


class TestObjCWeakRef (TestCase):
    @min_os_level('10.7')
    def test_weakref_to_python(self):
        self.assertRaises(TypeError,  objc.WeakRef, 1)
        self.assertRaises(TypeError,  objc.WeakRef, "hello")
        self.assertRaises(TypeError,  objc.WeakRef, b"hello")
        self.assertRaises(TypeError,  objc.WeakRef, b"hello".decode('utf-8'))
        self.assertRaises(TypeError,  objc.WeakRef, [])
        self.assertRaises(TypeError,  objc.WeakRef, self)

    @min_os_level('10.7')
    def test_weakref_to_objc(self):

        pool = NSAutoreleasePool.alloc().init()

        o = NSObject.alloc().init()
        a = NSArray.arrayWithObject_(o)

        r = objc.WeakRef(o)
        self.assertIs(r(), o)

        del o
        del pool
        pool = NSAutoreleasePool.alloc().init()

        self.assertIsInstance(r(), NSObject)
        del a

        del pool
        self.assertIs(r(), None)


if __name__ == "__main__":
    main()
