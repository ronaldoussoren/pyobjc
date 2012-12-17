from PyObjCTools.TestSupport import *
import objc, sys
from PyObjCTest.opaque import *

class TestFromPython (TestCase):
    def testBasic (self):
        tp = objc.createOpaquePointerType(
                "BarHandle", BarEncoded, "BarHandle doc")

        self.assertIsInstance(tp, type)

        f = OC_OpaqueTest.createBarWithFirst_andSecond_(1.0, 4.5)
        self.assertIsInstance(f, tp)
        x = OC_OpaqueTest.getFirst_(f)
        self.assertEqual(x, 1.0)
        x = OC_OpaqueTest.getSecond_(f)
        self.assertEqual(x, 4.5)

        # NULL pointer is converted to None
        self.assertEqual(OC_OpaqueTest.nullBar(), None)


class TestFromC (TestCase):
    def testMutable(self):
        self.assertIsInstance(FooHandle, type)

        def create(cls, value):
            return OC_OpaqueTest.createFoo_(value)
        FooHandle.create = classmethod(create)
        FooHandle.delete = lambda self: OC_OpaqueTest.deleteFoo_(self)
        FooHandle.get = lambda self: OC_OpaqueTest.getValueOf_(self)
        FooHandle.set = lambda self, v: OC_OpaqueTest.setValue_forFoo_(v, self)

        self.assertHasAttr(FooHandle, 'create')
        self.assertHasAttr(FooHandle, 'delete')

        f = FooHandle.create(42)
        self.assertIsInstance(f, FooHandle)
        self.assertEqual( f.get(), 42 )

        f.set(f.get() + 20)
        self.assertEqual( f.get(), 62 )

        FooHandle.__int__ = lambda self: self.get()
        FooHandle.__getitem__ = lambda self, x: self.get() * x

        self.assertEqual(int(f), 62)
        self.assertEqual(f[4], 4 * 62)

    def testBasic(self):
        f = OC_OpaqueTest.createFoo_(99)
        self.assertIsInstance(f, FooHandle)
        self.assertEqual( OC_OpaqueTest.getValueOf_(f), 99 )

        self.assertHasAttr(f, "__pointer__")
        if sys.version_info[0] == 2:
            self.assertIsInstance(f.__pointer__, (int, long))
        else:
            self.assertIsInstance(f.__pointer__, int)

        # NULL pointer is converted to None
        self.assertEqual(OC_OpaqueTest.nullFoo(), None)

        # There is no exposed type object that for PyCObject, test the
        # type name instead
        if sys.version_info[0] == 2 and sys.version_info[1] < 7:
            self.assertEqual( type(f.__cobject__()).__name__, 'PyCObject' )
        else:
            self.assertEqual( type(f.__cobject__()).__name__, 'PyCapsule' )

        # Check round tripping through a PyCObject.
        co = f.__cobject__()
        g = FooHandle(co)
        self.assertEqual(f.__pointer__, g.__pointer__)

if __name__ == "__main__":
    main()
