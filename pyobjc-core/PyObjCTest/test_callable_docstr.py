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

    def test_unknown(self):
        self.assertEqual(mod.describe_type(b'?'), '<?>')
        self.assertEqual(mod.describe_type(b'X'), '<?>')

    def test_callable(self):
        self.assertEqual(mod.describe_type(objc._C_ID + b'?'), "<BLOCK>")
        self.assertEqual(mod.describe_type(objc._C_PTR + b'?'), "<FUNCTION>")

    def test_array(self):
        self.assertEqual(mod.describe_type(objc._C_ARY_B + b"42" + objc._C_INT), "int[42]")
        self.assertEqual(mod.describe_type(objc._C_ARY_B + b"42" + objc._C_PTR + objc._C_INT), "int*[42]")

    def test_struct(self):
        self.assertEqual(mod.describe_type(objc._C_STRUCT_B + b"=" + objc._C_ID + objc._C_STRUCT_E), "struct <?>")
        self.assertEqual(mod.describe_type(objc._C_STRUCT_B + objc._C_STRUCT_E), "struct <?>")
        self.assertEqual(mod.describe_type(objc._C_STRUCT_B + b"name=" + objc._C_ID + objc._C_INT + objc._C_STRUCT_E), "struct name")
        self.assertEqual(mod.describe_type(objc._C_STRUCT_B + b"name=\"field\"" + objc._C_ID + b'"field2"' + objc._C_INT + objc._C_STRUCT_E), "struct name")

        strType = objc.createStructType("NamedTestStruct", b'{NamedTestStruct1="a"i"b"i}', None)
        self.assertEqual(mod.describe_type(b'{NamedTestStruct1=ii}'), "NamedTestStruct")

    def test_union(self):
        self.assertEqual(mod.describe_type(objc._C_UNION_B + b"=" + objc._C_ID + objc._C_UNION_E), "union <?>")
        self.assertEqual(mod.describe_type(objc._C_UNION_B + objc._C_UNION_E), "union <?>")
        self.assertEqual(mod.describe_type(objc._C_UNION_B + b"name=" + objc._C_ID + objc._C_INT + objc._C_UNION_E), "union name")
        self.assertEqual(mod.describe_type(objc._C_UNION_B + b"name=\"field\"" + objc._C_ID + b'"field2"' + objc._C_INT + objc._C_UNION_E), "union name")

class TestDescribeCallable (TestCase):

    def setUp(self):
        dct = {}
        func = objc.loadBundleFunctions(None, dct, [
            ('NSTemporaryDirectory', objc._C_ID),
            ('NSSearchPathForDirectoriesInDomains', objc._C_ID + objc._C_NSUInteger + objc._C_NSUInteger + objc._C_NSBOOL),
        ])
        self.NSTemporaryDirectory = dct['NSTemporaryDirectory']
        self.NSSearchPathForDirectoriesInDomains = dct['NSSearchPathForDirectoriesInDomains']

    def test_not_for_regular_types(self):
        self.assertRaises(AttributeError, mod.describe_callable, 42)
        self.assertRaises(AttributeError, mod.describe_callable, int)
        self.assertRaises(AttributeError, mod.describe_callable, dir)
        self.assertRaises(AttributeError, mod.describe_callable, lambda x: x*2)

    def test_sel_func(self):
        # Basicly just test that mod.describe_callable calls
        # mod.describe_callable_metadata with the right arguments.
        orig = mod.describe_callable_metadata
        try:
            recording = []
            def record(*args, **kwds):
                recording.append((args, kwds))
                return 42
            mod.describe_callable_metadata = record

            self.assertEqual(mod.describe_callable(NSArray.array), 42)
            self.assertEqual(mod.describe_callable(self.NSTemporaryDirectory), 42)
            self.assertEqual(recording, [
                ((NSArray.array.__name__, NSArray.array.__metadata__()), dict(ismethod=True)),
                ((self.NSTemporaryDirectory.__name__, self.NSTemporaryDirectory.__metadata__()), dict(ismethod=False)),
            ])

        finally:
            mod.describe_callable_metadata = orig

    def test_metadata_header_func(self):
        # Add variants for the various types of metadata.
        self.assertEqual(mod.describe_callable_metadata('array', {'arguments':[], 'retval': { 'type': b'v'}}, ismethod=False), 'void array(void);')
        self.assertEqual(mod.describe_callable_metadata('array', {'arguments':[ {'type': b'i' }, {'type': b'f'} ], 'retval': { 'type': b'v'}}, ismethod=False), 'void array(int arg0, float arg1);')
        self.assertEqual(mod.describe_callable_metadata('array', {'variadic': 1, 'arguments':[ {'type': b'i' }, {'type': b'f'} ], 'retval': { 'type': b'v'}}, ismethod=False), 'void array(int arg0, float arg1, ...);')

        # This is metadata is nonsense (C doesn't allow variadic functions where all arguments are variadic)
        self.assertEqual(mod.describe_callable_metadata('array', {'variadic':1 , 'arguments':[], 'retval': { 'type': b'v'}}, ismethod=False), 'void array(, ...);')

    def test_metadata_header_sel(self):
        self.assertEqual(mod.describe_callable_metadata('array', {'classmethod': 1, 'arguments':[ {'type': b'@'}, {'type': b':' }], 'retval': { 'type': b'v'}}, ismethod=True), '+ (void)array;')
        self.assertEqual(mod.describe_callable_metadata('array', {'classmethod': 0, 'arguments':[ {'type': b'@'}, {'type': b':' }], 'retval': { 'type': b'v'}}, ismethod=True), '- (void)array;')
        self.assertEqual(mod.describe_callable_metadata('initWithObjects:', {'classmethod': 0, 'arguments':[ {'type': b'@'}, {'type': b':' }, {'type': b'f'}], 'retval': { 'type': b'v'}}, ismethod=True),
            '- (void)initWithObjects:(float)arg0;')
        self.assertEqual(mod.describe_callable_metadata('initWithObjects:length:', {'classmethod': 0, 'arguments':[ {'type': b'@'}, {'type': b':' }, {'type': b'f'}, {'type': b'@'}], 'retval': { 'type': b'v'}}, ismethod=True),
            '- (void)initWithObjects:(float)arg0 length:(id)arg1;')
        self.assertEqual(mod.describe_callable_metadata('initWithObjects:', {'classmethod': 0, 'variadic': 1, 'arguments':[ {'type': b'@'}, {'type': b':' }, {'type': b'f'}], 'retval': { 'type': b'v'}}, ismethod=True),
            '- (void)initWithObjects:(float)arg0, ...;')

        # This metadata is nonsense, but shouldn't cause problems
        self.assertEqual(mod.describe_callable_metadata('array', {'classmethod': 0, 'variadic': 1, 'arguments':[ {'type': b'@'}, {'type': b':' }], 'retval': { 'type': b'v'}}, ismethod=True), '- (void)array, ...;')

    def test_metadata_special_arguments(self):
        # - in/out/inout
        # - function pointers
        # - block pointers
        # - array arguments (fixed size, size in argument(s), ...)
        # - 1, 2 special arguments
        # - printf_format
        # - description of variadic arguments
        # ...
        self.fail()

    def test_docattr(self):
        # Check that someFunction.__doc__ == describe_callable(someFunction),
        # and likewise for a class and instance selector.
        self.assertEqual(NSArray.arrayWithObjects_.__doc__, mod.describe_callable(NSArray.arrayWithObjects_))
        self.assertEqual(NSArray.array.__doc__, mod.describe_callable(NSArray.array))

        self.assertEqual(self.NSTemporaryDirectory.__doc__, mod.describe_callable(self.NSTemporaryDirectory))
        self.assertEqual(self.NSSearchPathForDirectoriesInDomains.__doc__, mod.describe_callable(self.NSSearchPathForDirectoriesInDomains))


if sys.version_info[:2] >= (3, 3):
    class TestCallableSignature (TestCase):
        def test_function(self):
            dct = {}
            func = objc.loadBundleFunctions(None, dct, [
                ('NSTemporaryDirectory', objc._C_ID),
                ('NSSearchPathForDirectoriesInDomains', objc._C_ID + objc._C_NSUInteger + objc._C_NSUInteger + objc._C_NSBOOL),
            ])
            NSTemporaryDirectory = dct['NSTemporaryDirectory']
            NSSearchPathForDirectoriesInDomains = dct['NSSearchPathForDirectoriesInDomains']

            self.assertEqual(NSTemporaryDirectory.__signature__, mod.callable_signature(NSTemporaryDirectory))
            self.assertEqual(NSSearchPathForDirectoriesInDomains.__signature__, mod.callable_signature(NSSearchPathForDirectoriesInDomains))

            sig = NSTemporaryDirectory.__signature__
            self.assertIsInstance(sig, inspect.Signature)
            self.assertEqual(len(sig.parameters), 0)

            sig = NSSearchPathForDirectoriesInDomains.__signature__
            self.assertIsInstance(sig, inspect.Signature)
            self.assertEqual(len(sig.parameters), 3)
            self.assertEqual(sig.parameters['arg0'], inspect.Parameter('arg0', inspect.Parameter.POSITIONAL_ONLY))
            self.assertEqual(sig.parameters['arg1'], inspect.Parameter('arg1', inspect.Parameter.POSITIONAL_ONLY))
            self.assertEqual(sig.parameters['arg2'], inspect.Parameter('arg2', inspect.Parameter.POSITIONAL_ONLY))
            self.assertEqual(list(sig.parameters), ['arg0', 'arg1', 'arg2'])

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
