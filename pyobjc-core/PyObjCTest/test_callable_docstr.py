from PyObjCTools.TestSupport import *

import sys
import inspect

from objc import _callable_docstr as mod
import objc

NSArray = objc.lookUpClass('NSArray')

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

        handle = objc.createOpaquePointerType("NamedPointer", b"^{NamedTestPointer1=}")
        self.assertEqual(mod.describe_type(b"^{NamedTestPointer1=}"), "NamedPointer")

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

        strType = objc.createStructType("NamedTestStruct", b'{NamedTestStruct1="a"i"b"i}', None)
        self.assertEqual(mod.describe_type(b'{NamedTestStruct1=ii}'), "NamedTestStruct")

    def test_union(self):
        self.assertEqual(mod.describe_type(objc._C_UNION_B + b"=" + objc._C_ID + objc._C_UNION_E), "union <?>")
        self.assertEqual(mod.describe_type(objc._C_UNION_B + b"name=" + objc._C_ID + objc._C_INT + objc._C_UNION_E), "union name")
        self.assertEqual(mod.describe_type(objc._C_UNION_B + b"name=\"field\"" + objc._C_ID + b'"field2"' + objc._C_INT + objc._C_UNION_E), "union name")

class TestDescribeCallable (TestCase):
    def test_not_for_regular_types(self):
        self.assertRaises(AttributeError, mod.describe_callable, 42)
        self.assertRaises(AttributeError, mod.describe_callable, int)
        self.assertRaises(AttributeError, mod.describe_callable, dir)
        self.assertRaises(AttributeError, mod.describe_callable, lambda x: x*2)

    def test_sel(self):
        # Basicly just test that this calls the metadata function
        self.fail()

    def test_func(self):
        # Basicly just test that this calls the metadata function
        self.fail()

    def test_metadata(self):
        # Add variants for the various types of metadata.
        self.fail()

    def test_docattr(self):
        # Check that someFunction.__doc__ == describe_callable(someFunction),
        # and likewise for a class and instance selector.
        self.assertEqual(NSArray.arrayWithObjects_.__doc__, mod.describe_callable(NSArray.arrayWithObjects_))
        self.assertEqual(NSArray.array.__doc__, mod.describe_callable(NSArray.array))

        # TODO: Same for functions

if sys.version_info[:2] >= (3, 3):
    class TestCallableSignature (TestCase):
        def test_function(self):
            self.fail()

            # Also: Check that someFunction.__signature__ == desribe_signature(someFunction),
            # and likewise for a class and instance selectors.
            self.fail()

        def test_selector(self):
            m = NSArray.array
            self.assertEqual(m.__signature__, mod.callable_signature(m))

            sig = m.__signature__
            self.assertIsInstance(sig, inspect.Signature)
            self.assertEqual(len(sig.parameters), 0)

            m = NSArray.arrayWithObjects_
            sig = m.__signature__
            self.assertIsInstance(sig, inspect.Signature)
            self.assertEqual(len(sig.parameters), 1)
            self.assertEqual(sig.parameters['arg0'], inspect.Parameter('arg0', inspect.Parameter.POSITIONAL_ONLY))

            m = NSArray.indexOfObject_inRange_
            sig = m.__signature__
            self.assertIsInstance(sig, inspect.Signature)
            self.assertEqual(len(sig.parameters), 2)
            self.assertEqual(sig.parameters['arg0'], inspect.Parameter('arg0', inspect.Parameter.POSITIONAL_ONLY))
            self.assertEqual(sig.parameters['arg1'], inspect.Parameter('arg1', inspect.Parameter.POSITIONAL_ONLY))
            self.assertEqual(list(sig.parameters), ['arg0', 'arg1'])

        def test_not_for_regular_types(self):
            self.assertRaises(AttributeError, mod.callable_signature, 42)
            self.assertRaises(AttributeError, mod.callable_signature, int)
            self.assertRaises(AttributeError, mod.callable_signature, dir)
            self.assertRaises(AttributeError, mod.callable_signature, lambda x: x*2)

if __name__ == "__main__":
    main()
