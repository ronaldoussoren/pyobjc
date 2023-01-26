from PyObjCTools.TestSupport import TestCase, pyobjc_options
from PyObjCTest.test_metadata_function import (
    returnUnionArray,
    union_SomeUnion,
    returnPointerArray,
    makeVoidPArrayOf_,
)

# , return2ndPointerArray
import objc

# XXX: Most tests for varlist are curerently in test_metadata.py, to be moved


class TestVarlistVarious(TestCase):
    def test_cannot_create(self):
        with self.assertRaisesRegex(
            TypeError, "cannot create 'objc.varlist' instances"
        ):
            objc.varlist()

    def test_array_of_union(self):
        # Unions are barely supported by PyObjC...
        res = returnUnionArray()
        self.assertIsInstance(res, objc.varlist)
        self.assertEqual(res.__typestr__, union_SomeUnion)

        with self.assertRaisesRegex(ValueError, "depythonifying 'union', got 'int'"):
            res[0] = 42

        with self.assertRaisesRegex(ValueError, "depythonifying 'union', got 'int'"):
            res[0:1] = (42,)

    def test_array_of_void(self):
        res = makeVoidPArrayOf_(4)
        self.assertIsInstance(res, objc.varlist)
        self.assertEqual(res.__typestr__, objc._C_CHAR_AS_TEXT)

        self.assertIsInstance(res[0], bytes)

    def test_array_of_unknown_pointer(self):
        res = returnPointerArray()
        self.assertIsInstance(res, objc.varlist)
        self.assertEqual(res.__typestr__, b"^{UnknownLabel=ii}")

        with pyobjc_options(unknown_pointer_raises=True):
            with self.assertRaisesRegex(
                objc.UnknownPointerError, r"pointer of type \^{UnknownLabel=ii}"
            ):
                res[0]

            with self.assertRaisesRegex(
                objc.UnknownPointerError, r"pointer of type \^{UnknownLabel=ii}"
            ):
                res[0:1]

            with self.assertRaisesRegex(
                objc.UnknownPointerError, r"pointer of type \^{UnknownLabel=ii}"
            ):
                res.as_tuple(2)


# XXX: This test cannot work, the type signature is valildated when the function object is created...
#      It may be possible to trigger this by using the ObjC runtime API to add a method to a class from C.
#
#    def test_invalid_signature(self):
#        with self.assertRaisesRegex(objc.internal_error, "Invalid struct definition in type signature: {UnknownLabel=ii"):
#            res = return2ndPointerArray()
