try:
    import ctypes
except ImportError:
    ctypes = None

import objc
from PyObjCTest.pointersupport import object_capsule, opaque_capsule, OC_PointerSupport
from PyObjCTools.TestSupport import TestCase, skipUnless

OpaqueType = objc.createOpaquePointerType("OpaqueType", b"^{OpaqueType}", None)


class TestProxySupport(TestCase):
    def test_cobject_roundtrip(self):
        arr = objc.lookUpClass("NSArray").array()

        p = arr.__cobject__()
        self.assertEqual(type(p).__name__, "PyCapsule")
        self.assertIn("objc.__object__", repr(p))
        # Note:

        v = objc.objc_object(cobject=p)
        self.assertIs(v, arr)

        with self.assertRaisesRegex(
            TypeError,
            r"('cobject2' is an invalid keyword argument for this function)|"
            r"(this function got an unexpected keyword argument 'cobject2'.)",
        ):
            objc.objc_object(cobject2=p)

    def test_cobject_for_nil(self):
        arr = objc.lookUpClass("NSArray").alloc()
        arr.init()
        with self.assertRaisesRegex(
            AttributeError, "cannot access attribute '__cobject__' of NIL"
        ):
            self.assertIs(arr.__cobject__(), None)

    def test_no__new__(self):
        with self.assertRaisesRegex(
            TypeError, "Use class methods to instantiate new Objective-C objects"
        ):
            objc.objc_object()

    @skipUnless(ctypes is not None, "requires ctypes")
    def test_voidp_roundtrip(self):
        arr = objc.lookUpClass("NSArray").array()

        p = arr.__c_void_p__()
        self.assertIsInstance(p, ctypes.c_void_p)
        self.assertEqual(p.value, objc.pyobjc_id(arr))

        v = objc.objc_object(c_void_p=p)
        self.assertIs(v, arr)

        class B:
            pass

        v = objc.objc_object(c_void_p=p.value)
        self.assertIs(v, arr)

        q = arr.__cobject__()

        with self.assertRaisesRegex(
            TypeError, "Pass either cobject or c_void_p, but not both"
        ):
            objc.objc_object(c_void_p=p, cobject=q)

        with self.assertRaisesRegex(
            AttributeError, "'str' object has no attribute 'value'"
        ):
            objc.objc_object(c_void_p="pointer!")

        b = B()
        b.value = "pointer"
        with self.assertRaisesRegex(ValueError, "c_void_p.value is not an integer"):
            objc.objc_object(c_void_p=b)

    @skipUnless(ctypes is not None, "requires ctypes")
    def test_voidp_for_nil(self):
        arr = objc.lookUpClass("NSArray").alloc()
        arr.init()
        with self.assertRaisesRegex(
            AttributeError, "cannot access attribute '__c_void_p__' of NIL"
        ):
            self.assertIs(arr.__c_void_p__(), None)

    @skipUnless(ctypes is not None, "requires ctypes")
    def test_voidp_using_ctypes(self):
        lib = ctypes.CDLL(
            "/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation"
        )
        func = lib.CFStringCreateWithCString
        func.restype = ctypes.c_void_p
        func.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]

        kCFStringEncodingISOLatin1 = 0x0201
        ct_obj = func(None, b"hello world", kCFStringEncodingISOLatin1)

        value = objc.objc_object(c_void_p=ct_obj)
        self.assertIsInstance(value, objc.pyobjc_unicode)
        self.assertEqual(objc.pyobjc_id(value.nsstring()), ct_obj)

    def test_pyobjc_id_invalid(self):
        with self.assertRaisesRegex(
            TypeError,
            r"(function missing required argument 'obj' \(pos 1\))|(Required argument 'obj' \(pos 1\) not found)",
        ):
            objc.pyobjc_id()

        with self.assertRaisesRegex(TypeError, r"not an Objective-C object"):
            objc.pyobjc_id(42)

    def test_opaque_capsule(self):
        cap = opaque_capsule()

        value = OpaqueType(cobject=cap)
        self.assertIsInstance(value, OpaqueType)
        self.assertEqual(value.__pointer__, 1234)

        with self.assertRaisesRegex(
            ValueError, "PyCapsule_GetPointer called with incorrect name"
        ):
            OpaqueType(cobject=object_capsule())
        with self.assertRaisesRegex(TypeError, "cobject' argument is not a PyCapsule"):
            OpaqueType(cobject=42)

    @skipUnless(ctypes is not None, "requires ctypes")
    def test_opaque_ctypes(self):
        ptr = ctypes.c_void_p(0xABCD)

        value = OpaqueType(c_void_p=ptr)
        self.assertIsInstance(value, OpaqueType)
        self.assertEqual(value.__pointer__, 0xABCD)

        value = OpaqueType(c_void_p=0xDEFA)
        self.assertIsInstance(value, OpaqueType)
        self.assertEqual(value.__pointer__, 0xDEFA)

    def test_object_capsule(self):
        NSObject = objc.lookUpClass("NSObject")
        cap = object_capsule()

        value = NSObject(cobject=cap)
        self.assertIsInstance(value, NSObject)

        with self.assertRaisesRegex(
            ValueError, "PyCapsule_GetPointer called with incorrect name"
        ):
            NSObject(cobject=opaque_capsule())
        with self.assertRaisesRegex(TypeError, "cobject' argument is not a PyCapsule"):
            NSObject(cobject=42)


objc.loadBundleFunctions(
    None,
    globals(),
    [
        ("CFStringGetTypeID", b"Q"),
        ("CFAllocatorGetTypeID", b"Q"),
    ],
)

objc.registerCFSignature(
    "CFStringRef", b"^{__CFString=}", CFStringGetTypeID(), "NSString"  # noqa: F821
)
objc.registerCFSignature(
    "CFAllocatorRef", b"^{__CFAllocator=}", CFAllocatorGetTypeID()  # noqa: F821
)

objc.registerMetaDataForSelector(
    b"OC_PointerSupport", b"getClass", {"retval": {"type": b"^{objc_class=}"}}
)
objc.registerMetaDataForSelector(
    b"OC_PointerSupport", b"className:", {"arguments": {2: {"type": b"^{objc_class=}"}}}
)


class TestMiscTypes(TestCase):
    def test_pyobject(self):
        v = OC_PointerSupport.getObjectLen_([1, 2, 3])
        self.assertEqual(v, 3)

        v = OC_PointerSupport.getObjectLen_(
            [
                1,
            ]
        )
        self.assertEqual(v, 1)

        v = OC_PointerSupport.getNone()
        self.assertIs(v, None)

    def test_class_alias(self):
        self.assertEqual(
            OC_PointerSupport.getClass.__metadata__()["retval"]["type"],
            b"^{objc_class=}",
        )
        self.assertEqual(
            OC_PointerSupport.className_.__metadata__()["arguments"][2]["type"],
            b"^{objc_class=}",
        )
        self.assertEqual(
            OC_PointerSupport.className_(objc.lookUpClass("NSObject")), "NSObject"
        )
        self.assertEqual(OC_PointerSupport.getClass(), OC_PointerSupport)

    def test_string_ref(self):
        v1 = OC_PointerSupport.getString()
        self.assertEqual(v1, "a static string")

        v2 = OC_PointerSupport.getString()
        self.assertEqual(v2, "a static string")

        self.assertEqual(
            objc.pyobjc_id(v1.__pyobjc_object__), objc.pyobjc_id(v2.__pyobjc_object__)
        )
        self.assertEqual(v1, v2)

    def test_context(self):
        v1 = OC_PointerSupport.getContext()
        v2 = OC_PointerSupport.getContext()

        self.assertIs(v1, v2)
