import objc
import sys
import ctypes
from PyObjCTest.opaque import OC_OpaqueTest, BarEncoded, FooEncoded, traverse
from PyObjCTools.TestSupport import TestCase

FooHandle = objc.createOpaquePointerType("FooHandle", FooEncoded, "FooHandle doc")

BarHandle = objc.createOpaquePointerType("Mod.BarHandle", BarEncoded, "BarHandle doc")


class TestFromPython(TestCase):
    def testBasic(self):
        self.assertIsInstance(BarHandle, type)
        self.assertEqual(BarHandle.__module__, "Mod")
        self.assertEqual(repr(BarHandle), "<class 'Mod.BarHandle'>")

        f = OC_OpaqueTest.createBarWithFirst_andSecond_(1.0, 4.5)
        self.assertIsInstance(f, BarHandle)
        x = OC_OpaqueTest.getFirst_(f)
        self.assertEqual(x, 1.0)
        x = OC_OpaqueTest.getSecond_(f)
        self.assertEqual(x, 4.5)

        # NULL pointer is converted to None
        self.assertEqual(OC_OpaqueTest.nullBar(), None)

    def testSubclassing(self):
        self.assertEqual(BarHandle.__name__, "BarHandle")

        with self.assertRaisesRegex(
            TypeError, "type 'Mod.BarHandle' is not an acceptable base type"
        ):

            class Subclass1(BarHandle):
                pass

    def testNaming(self):

        self.assertIsInstance(BarHandle, type)
        self.assertEqual(BarHandle.__module__, "Mod")
        self.assertEqual(BarHandle.__name__, "BarHandle")
        self.assertEqual(BarHandle.__qualname__, "BarHandle")
        self.assertEqual(repr(BarHandle), "<class 'Mod.BarHandle'>")

    def testDoc(self):
        self.assertEqual(BarHandle.__doc__, "BarHandle doc")

        docstr = None
        tp = objc.createOpaquePointerType("Mod.BarHandle2", b"^{TestDoc2=}", docstr)
        self.assertEqual(tp.__doc__, None)


class TestFromC(TestCase):
    def testMutable(self):
        self.assertIsInstance(FooHandle, type)

        def create(cls, value):
            return OC_OpaqueTest.createFoo_(value)

        FooHandle.create = classmethod(create)
        FooHandle.delete = lambda self: OC_OpaqueTest.deleteFoo_(self)
        FooHandle.get = lambda self: OC_OpaqueTest.getValueOf_(self)
        FooHandle.set = lambda self, v: OC_OpaqueTest.setValue_forFoo_(v, self)

        self.assertHasAttr(FooHandle, "create")
        self.assertHasAttr(FooHandle, "delete")

        f = FooHandle.create(42)
        self.assertIsInstance(f, FooHandle)
        self.assertEqual(f.get(), 42)

        f.set(f.get() + 20)
        self.assertEqual(f.get(), 62)

        FooHandle.__int__ = lambda self: self.get()
        FooHandle.__getitem__ = lambda self, x: self.get() * x

        self.assertEqual(int(f), 62)
        self.assertEqual(f[4], 4 * 62)

    def testBasic(self):
        f = OC_OpaqueTest.createFoo_(99)
        self.assertIsInstance(f, FooHandle)
        self.assertEqual(OC_OpaqueTest.getValueOf_(f), 99)

        self.assertHasAttr(f, "__pointer__")
        self.assertIsInstance(f.__pointer__, int)

        # NULL pointer is converted to None
        self.assertEqual(OC_OpaqueTest.nullFoo(), None)

        # There is no exposed type object that for PyCObject, test the
        # type name instead
        self.assertEqual(type(f.__cobject__()).__name__, "PyCapsule")

        # Check round tripping through a PyCObject.
        co = f.__cobject__()
        g = FooHandle(cobject=co)
        self.assertEqual(f.__pointer__, g.__pointer__)

        # Check roundtripping to a c_void_p
        cptr = f.__c_void_p__()
        self.assertIsInstance(cptr, ctypes.c_void_p)
        g = FooHandle(c_void_p=cptr)
        self.assertEqual(f.__pointer__, g.__pointer__)

        # Check that NULL pointers result in None
        cptr = ctypes.c_voidp(0)
        g = FooHandle(c_void_p=cptr)
        self.assertIs(g, None)

        g = FooHandle(c_void_p=0)
        self.assertIs(g, None)

    def test_sizeof(self):
        # XXX: Test is suboptimal, but code looks ok...
        f = OC_OpaqueTest.createFoo_(99)
        self.assertIsInstance(f, FooHandle)
        self.assertIsInstance(f.__sizeof__(), int)

    def test_invalid_creation(self):
        with self.assertRaisesRegex(
            TypeError,
            r"('invalid' is an invalid keyword argument for this function)|"
            r"(this function got an unexpected keyword argument 'invalid')",
        ):
            FooHandle(invalid=42)

        with self.assertRaisesRegex(TypeError, "'cobject' argument is not a PyCapsule"):
            FooHandle(42)

        with self.assertRaisesRegex(
            OverflowError, "Python int too large to convert to C unsigned long"
        ):
            FooHandle(c_void_p=2**65 + 3)

        with self.assertRaisesRegex(
            AttributeError, "'str' object has no attribute 'value'"
        ):
            FooHandle(c_void_p="hello")

        class Pointer:
            value = "hello"

        with self.assertRaisesRegex(TypeError, "c_void_p.value is not an integer"):
            FooHandle(c_void_p=Pointer())

        f = OC_OpaqueTest.createFoo_(99)
        with self.assertRaisesRegex(
            TypeError, "pass 'cobject' or 'c_void_p', not both"
        ):
            FooHandle(cobject=f.__cobject__(), c_void_p=f.__c_void_p__())

        with self.assertRaisesRegex(TypeError, "Cannot create objc.FooHandle objects"):
            FooHandle()

        with self.assertRaisesRegex(
            ValueError, "PyCapsule_GetPointer called with incorrect name"
        ):
            FooHandle(cobject=objc.__C_API__)

    def test_too_long_name(self):
        with self.assertRaisesRegex(ValueError, "dotless name is too long"):
            objc.createOpaquePointerType("BarHandle" * 100, BarEncoded, "BarHandle doc")

    def test_invalid_arguments(self):
        with self.assertRaisesRegex(TypeError, "missing required argument"):
            objc.createOpaquePointerType()

    def test_invalid_opaque_arg(self):
        with self.assertRaisesRegex(
            TypeError, "Need instance of objc.FooHandle, got instance of int"
        ):
            OC_OpaqueTest.deleteFoo_(42)

    def test_traverse(self):
        # XXX: Need to investigate how to trigger a traverse call
        f = OC_OpaqueTest.createFoo_(99)
        r = traverse(f)
        if sys.version_info[:2] < (3, 9):
            self.assertEqual(r, [])
        else:
            self.assertEqual(r, [type(f)])
