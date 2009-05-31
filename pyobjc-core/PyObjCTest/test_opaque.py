from PyObjCTools.TestSupport import *
import objc
from PyObjCTest.opaque import *

class TestFromPython (TestCase):
    def testBasic (self):
        tp = objc.createOpaquePointerType(
                "BarHandle", BarEncoded, "BarHandle doc")

        self.assert_(isinstance(tp, type))

        f = OC_OpaqueTest.createBarWithFirst_andSecond_(1.0, 4.5)
        self.assert_( isinstance(f, tp) )
        x = OC_OpaqueTest.getFirst_(f)
        self.assertEquals(x, 1.0)
        x = OC_OpaqueTest.getSecond_(f)
        self.assertEquals(x, 4.5)

        # NULL pointer is converted to None
        self.assertEquals(OC_OpaqueTest.nullBar(), None)


class TestFromC (TestCase):
    def testMutable(self):
        self.assert_( isinstance(FooHandle, type) )

        def create(cls, value):
            return OC_OpaqueTest.createFoo_(value)
        FooHandle.create = classmethod(create)
        FooHandle.delete = lambda self: OC_OpaqueTest.deleteFoo_(self)
        FooHandle.get = lambda self: OC_OpaqueTest.getValueOf_(self)
        FooHandle.set = lambda self, v: OC_OpaqueTest.setValue_forFoo_(v, self)

        self.assert_( hasattr(FooHandle, 'create') )
        self.assert_( hasattr(FooHandle, 'delete') )
        
        f = FooHandle.create(42)
        self.assert_( isinstance(f, FooHandle) )
        self.assertEquals( f.get(), 42 )

        f.set(f.get() + 20)
        self.assertEquals( f.get(), 62 )

        FooHandle.__int__ = lambda self: self.get()
        FooHandle.__getitem__ = lambda self, x: self.get() * x
        
        self.assertEquals(int(f), 62)
        self.assertEquals(f[4], 4 * 62)

    def testBasic(self):
        f = OC_OpaqueTest.createFoo_(99)
        self.assert_( isinstance(f, FooHandle) )
        self.assertEquals( OC_OpaqueTest.getValueOf_(f), 99 )

        self.assert_( hasattr(f, "__pointer__") )
        self.assert_( isinstance(f.__pointer__, (int, long)) )

        # NULL pointer is converted to None
        self.assertEquals(OC_OpaqueTest.nullFoo(), None)

        # There is no exposed type object that for PyCObject, test the
        # type name instead
        self.assertEquals( type(f.__cobject__()).__name__, 'PyCObject' )

        # Check round tripping through a PyCObject.
        co = f.__cobject__()
        g = FooHandle(co)
        self.assertEquals(f.__pointer__, g.__pointer__)

if __name__ == "__main__":
    main()
