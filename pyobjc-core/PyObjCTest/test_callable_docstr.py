from PyObjCTools.TestSupport import *

import sys

from objc import _callable_docstr as mod
import objc


class TestDescribeType (TestCase):
    def test_basic_types(self):
        self.assertEqual(mod.describe_type(objc._C_VOID), "void")
        self.assertEqual(mod.describe_type(objc._C_INT), "int")
        self.assertEqual(mod.describe_type(objc._C_UINT), "unsigned int")
        self.assertEqual(mod.describe_type(objc._C_CHR), "char")
        self.assertEqual(mod.describe_type(objc._C_UCHR), "unsigned char")
        self.assertEqual(mod.describe_type(objc._C_SHT), "short")
        self.assertEqual(mod.describe_type(objc._C_USHT), "unsigned short")
        self.assertEqual(mod.describe_type(objc._C_LNG), "long")
        self.assertEqual(mod.describe_type(objc._C_ULNG), "unsigned long")
        self.assertEqual(mod.describe_type(objc._C_LNG_LNG), "long long")
        self.assertEqual(mod.describe_type(objc._C_ULNG_LNG), "unsigned long long")
        self.assertEqual(mod.describe_type(objc._C_FLT), "float")
        self.assertEqual(mod.describe_type(objc._C_DBL), "double")
        self.assertEqual(mod.describe_type(objc._C_ID), "id")
        self.assertEqual(mod.describe_type(objc._C_CLASS), "Class")
        self.assertEqual(mod.describe_type(objc._C_SEL), "SEL")
        self.assertEqual(mod.describe_type(objc._C_CHARPTR), "char*")
        self.assertEqual(mod.describe_type(objc._C_BOOL), "bool")

        # PyObjC specials:
        self.assertEqual(mod.describe_type(objc._C_CHAR_AS_INT), "int8_t")
        self.assertEqual(mod.describe_type(objc._C_CHAR_AS_TEXT), "char")
        self.assertEqual(mod.describe_type(objc._C_UNICHAR), "UniChar")
        self.assertEqual(mod.describe_type(objc._C_NSBOOL), "BOOL")


    def test_inout(self):
        self.assertEqual(mod.describe_type(objc._C_IN + objc._C_PTR + objc._C_INT), "in int*")
        self.assertEqual(mod.describe_type(objc._C_OUT + objc._C_PTR + objc._C_INT), "out int*")
        self.assertEqual(mod.describe_type(objc._C_INOUT + objc._C_PTR + objc._C_INT), "inout int*")

        # Nonsense, but should give a sane result anway:
        self.assertEqual(mod.describe_type(objc._C_OUT + objc._C_IN + objc._C_PTR + objc._C_INT), "out in int*")

    def test_pointers(self):
        self.assertEqual(mod.describe_type(objc._C_CHARPTR), "char*")
        self.assertEqual(mod.describe_type(objc._C_PTR + objc._C_CHR), "char*")
        self.assertEqual(mod.describe_type(objc._C_PTR + objc._C_PTR + objc._C_FLT), "float**")
        self.assertEqual(mod.describe_type(objc._C_PTR + objc._C_STRUCT_B + b'hello=' + objc._C_INT + objc._C_STRUCT_E), "struct hello*")

        # XXX: Register an opaque pointer and use that

    def test_callable(self):
        self.assertEqual(mod.describe_type(objc._C_ID + b'?'), "<BLOCK>")
        self.assertEqual(mod.describe_type(objc._C_PTR + b'?'), "<FUNCTION>")

    def test_array(self):
        self.assertEqual(mod.describe_type(objc._C_ARY_B + b"42" + objc._C_INT), "int[42]")
        self.assertEqual(mod.describe_type(objc._C_ARY_B + b"42" + objc._C_PTR + objc._C_INT), "int*[42]")

    def test_struct(self):
        self.assertEqual(mod.describe_type(objc._C_STRUCT_B + b"=" + objc._C_ID + objc._C_STRUCT_E), "struct <?>")
        self.assertEqual(mod.describe_type(objc._C_STRUCT_B + b"name=" + objc._C_ID + objc._C_INT + objc._C_STRUCT_E), "struct name")
        self.assertEqual(mod.describe_type(objc._C_STRUCT_B + b"name=\"field\"" + objc._C_ID + b'"field2"' + objc._C_INT + objc._C_STRUCT_E), "struct name")

        # XXX: Register a struct type and use that.

    def test_union(self):
        self.assertEqual(mod.describe_type(objc._C_UNION_B + b"=" + objc._C_ID + objc._C_UNION_E), "union <?>")
        self.assertEqual(mod.describe_type(objc._C_UNION_B + b"name=" + objc._C_ID + objc._C_INT + objc._C_UNION_E), "union name")
        self.assertEqual(mod.describe_type(objc._C_UNION_B + b"name=\"field\"" + objc._C_ID + b'"field2"' + objc._C_INT + objc._C_UNION_E), "union name")

class TestDescribeCallable (TestCase):
    def test_missing(self):
        self.fail()

    def test_docattr(self):
        # Check that someFunction.__doc__ == describe_callable(someFunction),
        # and likewise for a class and instance selector.
        self.fail()

if sys.version_info[:2] >= (3, 3):
    class TestCallableSignature (TestCase):
        def test_missing(self):
            self.fail()


        def test_signatureattr(self):
            # Check that someFunction.__signature__ == desribe_signature(someFunction),
            # and likewise for a class and instance selectors.
            self.fail()

if __name__ == "__main__":
    main()
