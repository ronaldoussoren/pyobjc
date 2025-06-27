import inspect

import objc
from objc import _callable_docstr as mod
from PyObjCTools.TestSupport import TestCase

NSArray = objc.lookUpClass("NSArray")


class TestDescribeType(TestCase):
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
        self.assertEqual(
            mod.describe_type(objc._C_IN + objc._C_PTR + objc._C_INT), "in int*"
        )
        self.assertEqual(
            mod.describe_type(objc._C_OUT + objc._C_PTR + objc._C_INT), "out int*"
        )
        self.assertEqual(
            mod.describe_type(objc._C_INOUT + objc._C_PTR + objc._C_INT), "inout int*"
        )

        # Nonsense, but should give a sane result anway:
        self.assertEqual(
            mod.describe_type(objc._C_OUT + objc._C_IN + objc._C_PTR + objc._C_INT),
            "out in int*",
        )

    def test_pointers(self):
        self.assertEqual(mod.describe_type(objc._C_CHARPTR), "char*")
        self.assertEqual(mod.describe_type(objc._C_PTR + objc._C_CHR), "char*")
        self.assertEqual(
            mod.describe_type(objc._C_PTR + objc._C_PTR + objc._C_FLT), "float**"
        )
        self.assertEqual(
            mod.describe_type(
                objc._C_PTR
                + objc._C_STRUCT_B
                + b"hello="
                + objc._C_INT
                + objc._C_STRUCT_E
            ),
            "hello*",
        )

        _ = objc.createOpaquePointerType("NamedPointer", b"^{NamedTestPointer1=}")
        self.assertEqual(mod.describe_type(b"^{NamedTestPointer1=}"), "NamedPointer")

    def test_unknown(self):
        self.assertEqual(mod.describe_type(b"?"), "<?>")
        self.assertEqual(mod.describe_type(b"X"), "<?>")

    def test_callable(self):
        self.assertEqual(mod.describe_type(objc._C_ID + b"?"), "<BLOCK>")
        self.assertEqual(mod.describe_type(objc._C_PTR + b"?"), "<FUNCTION>")

    def test_array(self):
        self.assertEqual(
            mod.describe_type(objc._C_ARY_B + b"42" + objc._C_INT), "int[42]"
        )
        self.assertEqual(
            mod.describe_type(objc._C_ARY_B + b"42" + objc._C_PTR + objc._C_INT),
            "int*[42]",
        )

    def test_struct(self):
        self.assertEqual(
            mod.describe_type(objc._C_STRUCT_B + b"=" + objc._C_ID + objc._C_STRUCT_E),
            "struct <?>",
        )
        self.assertEqual(
            mod.describe_type(objc._C_STRUCT_B + objc._C_STRUCT_E), "struct <?>"
        )
        self.assertEqual(
            mod.describe_type(
                objc._C_STRUCT_B
                + b"name="
                + objc._C_ID
                + objc._C_INT
                + objc._C_STRUCT_E
            ),
            "name",
        )
        self.assertEqual(
            mod.describe_type(
                objc._C_STRUCT_B
                + b'name="field"'
                + objc._C_ID
                + b'"field2"'
                + objc._C_INT
                + objc._C_STRUCT_E
            ),
            "name",
        )

        _ = objc.createStructType(
            "NamedTestStruct", b'{NamedTestStruct1="a"i"b"i}', None
        )
        self.assertEqual(mod.describe_type(b"{NamedTestStruct1=ii}"), "NamedTestStruct")

        self.assertEqual(
            mod.describe_type(
                objc._C_STRUCT_B + b"Bar.Struct=" + objc._C_ID + objc._C_STRUCT_E
            ),
            "Struct",
        )

    def test_union(self):
        self.assertEqual(
            mod.describe_type(objc._C_UNION_B + b"=" + objc._C_ID + objc._C_UNION_E),
            "union <?>",
        )
        self.assertEqual(
            mod.describe_type(objc._C_UNION_B + objc._C_UNION_E), "union <?>"
        )
        self.assertEqual(
            mod.describe_type(
                objc._C_UNION_B + b"name=" + objc._C_ID + objc._C_INT + objc._C_UNION_E
            ),
            "union name",
        )
        self.assertEqual(
            mod.describe_type(
                objc._C_UNION_B
                + b'name="field"'
                + objc._C_ID
                + b'"field2"'
                + objc._C_INT
                + objc._C_UNION_E
            ),
            "union name",
        )

    def test_vector(self):
        self.assertEqual(mod.describe_type(b"<2f>"), "simd_float2")
        self.assertEqual(mod.describe_type(b"<4i>"), "simd_int4")
        self.assertEqual(mod.describe_type(b"<3S>"), "simd_ushort3")


class TestDescribeCallable(TestCase):
    def setUp(self):
        dct = {}
        objc.loadBundleFunctions(
            None,
            dct,
            [
                ("NSTemporaryDirectory", objc._C_ID),
                (
                    "NSSearchPathForDirectoriesInDomains",
                    objc._C_ID
                    + objc._C_NSUInteger
                    + objc._C_NSUInteger
                    + objc._C_NSBOOL,
                ),
            ],
        )
        self.NSTemporaryDirectory = dct["NSTemporaryDirectory"]
        self.NSSearchPathForDirectoriesInDomains = dct[
            "NSSearchPathForDirectoriesInDomains"
        ]

    def test_not_for_regular_types(self):
        self.assertIs(mod.describe_callable(42), None)
        self.assertIs(mod.describe_callable(int), None)
        self.assertIs(mod.describe_callable(dir), None)
        self.assertIs(mod.describe_callable(lambda x: x * 2), None)

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
            self.assertEqual(
                recording,
                [
                    (
                        (NSArray.array.__name__, NSArray.array.__metadata__()),
                        {"ismethod": True},
                    ),
                    (
                        (
                            self.NSTemporaryDirectory.__name__,
                            self.NSTemporaryDirectory.__metadata__(),
                        ),
                        {"ismethod": False},
                    ),
                ],
            )

        finally:
            mod.describe_callable_metadata = orig

    def test_metadata_header_func(self):
        # Add variants for the various types of metadata.
        self.assertEqual(
            mod.describe_callable_metadata(
                "array", {"arguments": [], "retval": {"type": b"v"}}, ismethod=False
            ),
            "void array(void);",
        )
        self.assertEqual(
            mod.describe_callable_metadata(
                "array",
                {
                    "arguments": [{"type": b"i"}, {"type": b"f"}],
                    "retval": {"type": b"v"},
                },
                ismethod=False,
            ),
            "void array(int arg0, float arg1);",
        )
        self.assertEqual(
            mod.describe_callable_metadata(
                "array",
                {
                    "variadic": 1,
                    "arguments": [{"type": b"i"}, {"type": b"f"}],
                    "retval": {"type": b"v"},
                },
                ismethod=False,
            ),
            "void array(int arg0, float arg1, ...);",
        )

        # This is metadata is nonsense (C doesn't allow variadic
        # functions where all arguments are variadic)
        self.assertEqual(
            mod.describe_callable_metadata(
                "array",
                {"variadic": 1, "arguments": [], "retval": {"type": b"v"}},
                ismethod=False,
            ),
            "void array(, ...);",
        )

    def test_metadata_header_sel(self):
        self.assertEqual(
            mod.describe_callable_metadata(
                "array",
                {
                    "classmethod": 1,
                    "arguments": [{"type": b"@"}, {"type": b":"}],
                    "retval": {"type": b"v"},
                },
                ismethod=True,
            ),
            "+ (void)array;",
        )
        self.assertEqual(
            mod.describe_callable_metadata(
                "array",
                {
                    "classmethod": 0,
                    "arguments": [{"type": b"@"}, {"type": b":"}],
                    "retval": {"type": b"v"},
                },
                ismethod=True,
            ),
            "- (void)array;",
        )
        self.assertEqual(
            mod.describe_callable_metadata(
                "initWithObjects:",
                {
                    "classmethod": 0,
                    "arguments": [{"type": b"@"}, {"type": b":"}, {"type": b"f"}],
                    "retval": {"type": b"v"},
                },
                ismethod=True,
            ),
            "- (void)initWithObjects:(float)arg0;",
        )
        self.assertEqual(
            mod.describe_callable_metadata(
                "initWithObjects:length:",
                {
                    "classmethod": 0,
                    "arguments": [
                        {"type": b"@"},
                        {"type": b":"},
                        {"type": b"f"},
                        {"type": b"@"},
                    ],
                    "retval": {"type": b"v"},
                },
                ismethod=True,
            ),
            "- (void)initWithObjects:(float)arg0 length:(id)arg1;",
        )
        self.assertEqual(
            mod.describe_callable_metadata(
                "initWithObjects:",
                {
                    "classmethod": 0,
                    "variadic": 1,
                    "arguments": [{"type": b"@"}, {"type": b":"}, {"type": b"f"}],
                    "retval": {"type": b"v"},
                },
                ismethod=True,
            ),
            "- (void)initWithObjects:(float)arg0, ...;",
        )

        # This metadata is nonsense, but shouldn't cause problems
        self.assertEqual(
            mod.describe_callable_metadata(
                "array",
                {
                    "classmethod": 0,
                    "variadic": 1,
                    "arguments": [{"type": b"@"}, {"type": b":"}],
                    "retval": {"type": b"v"},
                },
                ismethod=True,
            ),
            "- (void)array, ...;",
        )

    def test_metadata_special_arguments(self):
        # - in/out/inout
        self.assertEqual(
            mod.describe_callable_metadata(
                "array",
                {"arguments": [{"type": b"nf"}], "retval": {"type": b"v"}},
                ismethod=False,
            ),
            "void array(in float arg0);\n\narg0: pass-by-reference in argument",
        )
        self.assertEqual(
            mod.describe_callable_metadata(
                "array",
                {"arguments": [{"type": b"Nf"}], "retval": {"type": b"v"}},
                ismethod=False,
            ),
            "void array(inout float arg0);\n\narg0: pass-by-reference inout argument",
        )
        self.assertEqual(
            mod.describe_callable_metadata(
                "array",
                {"arguments": [{"type": b"of"}], "retval": {"type": b"v"}},
                ismethod=False,
            ),
            "void array(out float arg0);\n\narg0: pass-by-reference out argument",
        )
        self.assertEqual(
            mod.describe_callable_metadata(
                "array",
                {"arguments": [{"type": b"rf"}], "retval": {"type": b"v"}},
                ismethod=False,
            ),
            "void array(const float arg0);",
        )
        self.assertEqual(
            mod.describe_callable_metadata(
                "array",
                {
                    "arguments": [{"type": b"of"}, {"type": b"ni"}],
                    "retval": {"type": b"v"},
                },
                ismethod=False,
            ),
            "void array(out float arg0, in int arg1);\n\n"
            "arg0: pass-by-reference out argument\n"
            "arg1: pass-by-reference in argument",
        )

        self.assertEqual(
            mod.describe_callable_metadata(
                "array:",
                {
                    "classmethod": False,
                    "arguments": [{"type": b"@"}, {"type": b":"}, {"type": b"nf"}],
                    "retval": {"type": b"v"},
                },
                ismethod=True,
            ),
            "- (void)array:(in float)arg0;\n\narg0: pass-by-reference in argument",
        )

        # - function pointers (simple and nested)
        self.assertEqual(
            mod.describe_callable_metadata(
                "function",
                {
                    "arguments": [
                        {
                            "type": b"^?",
                            "callable": {"retval": {"type": b"i"}, "arguments": []},
                        }
                    ],
                    "retval": {"type": b"v"},
                },
                ismethod=False,
            ),
            "void function(<FUNCTION> arg0);\n\narg0: int callback(void);",
        )

        self.assertEqual(
            mod.describe_callable_metadata(
                "function",
                {
                    "arguments": [
                        {
                            "type": b"^?",
                            "callable": {
                                "retval": {"type": b"i"},
                                "arguments": [{"type": b"f"}, {"type": b"d"}],
                            },
                        }
                    ],
                    "retval": {"type": b"v"},
                },
                ismethod=False,
            ),
            "void function(<FUNCTION> arg0);\n\narg0: int callback(float arg0, double arg1);",
        )

        self.maxDiff = None
        self.assertEqual(
            mod.describe_callable_metadata(
                "function",
                {
                    "arguments": [
                        {
                            "type": b"^?",
                            "callable": {
                                "retval": {"type": b"i"},
                                "arguments": [
                                    {
                                        "type": b"^?",
                                        "callable": {
                                            "retval": {"type": b"d"},
                                            "arguments": [
                                                {
                                                    "type": b"n@",
                                                    "c_array_length_in_arg": 1,
                                                },
                                                {"type": b"@"},
                                            ],
                                        },
                                    }
                                ],
                            },
                        }
                    ],
                    "retval": {"type": b"v"},
                },
                ismethod=False,
            ),
            "void function(<FUNCTION> arg0);\n\n"
            "arg0: int callback(<FUNCTION> arg0);\n\n"
            "    arg0: double callback(in id arg0, id arg1);\n\n"
            "        arg0: array with length in arg1",
        )

        # - block pointers (simple and nested)
        self.assertEqual(
            mod.describe_callable_metadata(
                "function",
                {
                    "arguments": [
                        {
                            "type": b"@?",
                            "callable": {"retval": {"type": b"i"}, "arguments": []},
                        }
                    ],
                    "retval": {"type": b"v"},
                },
                ismethod=False,
            ),
            "void function(<BLOCK> arg0);\n\narg0: int callback(void);",
        )

        self.assertEqual(
            mod.describe_callable_metadata(
                "performCallback:",
                {
                    "classmethod": False,
                    "arguments": [
                        {"type": b"@"},
                        {"type": b":"},
                        {
                            "type": b"@?",
                            "callable": {"retval": {"type": b"i"}, "arguments": []},
                        },
                    ],
                    "retval": {"type": b"v"},
                },
                ismethod=True,
            ),
            "- (void)performCallback:(<BLOCK>)arg0;\n\narg0: int callback(void);",
        )

        self.assertEqual(
            mod.describe_callable_metadata(
                "function",
                {
                    "arguments": [
                        {
                            "type": b"@?",
                            "callable": {
                                "retval": {"type": b"i"},
                                "arguments": [{"type": b"f"}, {"type": b"d"}],
                            },
                        }
                    ],
                    "retval": {"type": b"v"},
                },
                ismethod=False,
            ),
            "void function(<BLOCK> arg0);\n\narg0: int callback(float arg0, double arg1);",
        )

        self.maxDiff = None
        self.assertEqual(
            mod.describe_callable_metadata(
                "function",
                {
                    "arguments": [
                        {
                            "type": b"@?",
                            "callable": {
                                "retval": {"type": b"i"},
                                "arguments": [
                                    {
                                        "type": b"@?",
                                        "callable": {
                                            "retval": {"type": b"d"},
                                            "arguments": [
                                                {
                                                    "type": b"n@",
                                                    "c_array_length_in_arg": 1,
                                                },
                                                {"type": b"@"},
                                            ],
                                        },
                                    }
                                ],
                            },
                        }
                    ],
                    "retval": {"type": b"v"},
                },
                ismethod=False,
            ),
            "void function(<BLOCK> arg0);\n\n"
            "arg0: int callback(<BLOCK> arg0);\n\n"
            "    arg0: double callback(in id arg0, id arg1);\n\n"
            "        arg0: array with length in arg1",
        )

        # - variadic arguments
        self.assertEqual(
            mod.describe_callable_metadata(
                "printf",
                {
                    "variadic": True,
                    "c_array_delimited_by_null": True,
                    "arguments": [{"type": b"@"}],
                    "retval": {"type": b"v"},
                },
                ismethod=False,
            ),
            "void printf(id arg0, ...);\n\nVariadic arguments form an array of C type id",
        )
        self.assertEqual(
            mod.describe_callable_metadata(
                "printf",
                {
                    "variadic": True,
                    "c_array_delimited_by_null": True,
                    "arguments": [{"type": b"@"}, {"type": b"i"}],
                    "retval": {"type": b"v"},
                },
                ismethod=False,
            ),
            "void printf(id arg0, int arg1, ...);\n\n"
            "Variadic arguments form an array of C type int",
        )
        self.assertEqual(
            mod.describe_callable_metadata(
                "printf",
                {
                    "variadic": True,
                    "c_array_delimited_by_null": True,
                    "arguments": [{"type": b"n@"}, {"type": b"i"}],
                    "retval": {"type": b"v"},
                },
                ismethod=False,
            ),
            "void printf(in id arg0, int arg1, ...);\n\n"
            "arg0: pass-by-reference in argument\n"
            "Variadic arguments form an array of C type int",
        )

        # - printf_format
        self.assertEqual(
            mod.describe_callable_metadata(
                "printf",
                {
                    "variadic": True,
                    "arguments": [
                        {"type": b"n^" + objc._C_CHAR_AS_TEXT, "printf_format": True}
                    ],
                    "retval": {"type": b"v"},
                },
                ismethod=False,
            ),
            "void printf(in char* arg0, ...);\n\narg0: %-style format string",
        )
        self.assertEqual(
            mod.describe_callable_metadata(
                "printf",
                {
                    "variadic": True,
                    "arguments": [{"type": objc._C_CHARPTR, "printf_format": True}],
                    "retval": {"type": b"i"},
                },
                ismethod=False,
            ),
            "int printf(char* arg0, ...);\n\narg0: %-style format string",
        )
        self.assertEqual(
            mod.describe_callable_metadata(
                "printf:",
                {
                    "classmethod": False,
                    "variadic": True,
                    "arguments": [
                        {"type": b"@"},
                        {"type": b":"},
                        {"type": objc._C_CHARPTR, "printf_format": True},
                    ],
                    "retval": {"type": b"i"},
                },
                ismethod=True,
            ),
            "- (int)printf:(char*)arg0, ...;\n\narg0: %-style format string",
        )

        # - description of variadic arguments
        self.assertEqual(
            mod.describe_callable_metadata(
                "array",
                {"arguments": [{"type": b"ni"}], "retval": {"type": b"v"}},
                ismethod=False,
            ),
            "void array(in int arg0);\n\narg0: pass-by-reference in argument",
        )
        self.assertEqual(
            mod.describe_callable_metadata(
                "array",
                {
                    "arguments": [{"type": b"ni", "c_array_length_in_arg": 2}],
                    "retval": {"type": b"v"},
                },
                ismethod=False,
            ),
            "void array(in int arg0);\n\narg0: array with length in arg2",
        )
        self.assertEqual(
            mod.describe_callable_metadata(
                "array",
                {
                    "arguments": [{"type": b"ni", "c_array_length_in_arg": (2, 3)}],
                    "retval": {"type": b"v"},
                },
                ismethod=False,
            ),
            "void array(in int arg0);\n\n"
            "arg0: array with length on input in arg2, and output in arg3",
        )
        self.assertEqual(
            mod.describe_callable_metadata(
                "array",
                {
                    "arguments": [
                        {
                            "type": b"ni",
                            "c_array_length_in_arg": 2,
                            "c_array_length_in_result": True,
                        }
                    ],
                    "retval": {"type": b"v"},
                },
                ismethod=False,
            ),
            "void array(in int arg0);\n\n"
            "arg0: array with length on input in arg2, and output "
            "in return value",
        )
        self.assertEqual(
            mod.describe_callable_metadata(
                "array",
                {
                    "arguments": [{"type": b"ni", "c_array_length_in_result": True}],
                    "retval": {"type": b"v"},
                },
                ismethod=False,
            ),
            "void array(in int arg0);\n\narg0: array with length in return value",
        )
        self.assertEqual(
            mod.describe_callable_metadata(
                "array",
                {
                    "arguments": [{"type": b"ni", "c_array_of_fixed_length": 42}],
                    "retval": {"type": b"v"},
                },
                ismethod=False,
            ),
            "void array(in int arg0);\n\narg0: array with length 42",
        )
        self.assertEqual(
            mod.describe_callable_metadata(
                "array",
                {
                    "arguments": [{"type": b"ni", "c_array_of_variable_length": True}],
                    "retval": {"type": b"v"},
                },
                ismethod=False,
            ),
            "void array(in int arg0);\n\narg0: array with unknown length",
        )
        self.assertEqual(
            mod.describe_callable_metadata(
                "array",
                {
                    "arguments": [{"type": b"ni", "c_array_delimited_by_null": True}],
                    "retval": {"type": b"v"},
                },
                ismethod=False,
            ),
            "void array(in int arg0);\n\narg0: array (will be NULL terminated in C)",
        )

        self.assertEqual(
            mod.describe_callable_metadata(
                "array:",
                {
                    "classmethod": False,
                    "arguments": [
                        {"type": b"@"},
                        {"type": b":"},
                        {"type": b"ni", "c_array_length_in_arg": 2},
                    ],
                    "retval": {"type": b"v"},
                },
                ismethod=True,
            ),
            "- (void)array:(in int)arg0;\n\narg0: array with length in arg0",
        )
        self.assertEqual(
            mod.describe_callable_metadata(
                "array:",
                {
                    "classmethod": False,
                    "arguments": [
                        {"type": b"@"},
                        {"type": b":"},
                        {"type": b"ni", "c_array_length_in_arg": (2, 3)},
                    ],
                    "retval": {"type": b"v"},
                },
                ismethod=True,
            ),
            "- (void)array:(in int)arg0;\n\n"
            "arg0: array with length on input in arg0, and output in arg1",
        )
        self.assertEqual(
            mod.describe_callable_metadata(
                "array:",
                {
                    "classmethod": False,
                    "arguments": [
                        {"type": b"@"},
                        {"type": b":"},
                        {
                            "type": b"ni",
                            "c_array_length_in_arg": 2,
                            "c_array_length_in_result": True,
                        },
                    ],
                    "retval": {"type": b"v"},
                },
                ismethod=True,
            ),
            "- (void)array:(in int)arg0;\n\n"
            "arg0: array with length on input in arg0, and "
            "output in return value",
        )

        # - warnings
        self.assertEqual(
            mod.describe_callable_metadata(
                "array",
                {
                    "arguments": [],
                    "retval": {"type": b"v"},
                    "suggestion": "Please don't",
                },
                ismethod=False,
            ),
            "void array(void);\n\nWARNING: Please don't",
        )
        self.assertEqual(
            mod.describe_callable_metadata(
                "array",
                {
                    "arguments": [{"type": b"ni"}],
                    "retval": {"type": b"v"},
                    "suggestion": "Please don't",
                },
                ismethod=False,
            ),
            "void array(in int arg0);\n\n"
            "WARNING: Please don't\n\n"
            "arg0: pass-by-reference in argument",
        )

    def test_docattr(self):
        # Check that someFunction.__doc__ == describe_callable(someFunction),
        # and likewise for a class and instance selector.
        self.assertEqual(
            NSArray.arrayWithObjects_.__doc__,
            mod.describe_callable(NSArray.arrayWithObjects_),
        )
        self.assertEqual(NSArray.array.__doc__, mod.describe_callable(NSArray.array))

        self.assertEqual(
            self.NSTemporaryDirectory.__doc__,
            mod.describe_callable(self.NSTemporaryDirectory),
        )
        self.assertEqual(
            self.NSSearchPathForDirectoriesInDomains.__doc__,
            mod.describe_callable(self.NSSearchPathForDirectoriesInDomains),
        )

    def test_no_metadata(self):
        class M:
            __name__ = "foo"

            def __metadata__(self):
                raise objc.internal_error

        m = M()
        self.assertIs(mod.describe_callable(m), None)


class TestCallableSignature(TestCase):
    def test_function(self):
        dct = {}
        objc.loadBundleFunctions(
            None,
            dct,
            [
                ("NSTemporaryDirectory", objc._C_ID),
                (
                    "NSSearchPathForDirectoriesInDomains",
                    objc._C_ID
                    + objc._C_NSUInteger
                    + objc._C_NSUInteger
                    + objc._C_NSBOOL,
                ),
            ],
        )
        NSTemporaryDirectory = dct["NSTemporaryDirectory"]
        NSSearchPathForDirectoriesInDomains = dct["NSSearchPathForDirectoriesInDomains"]

        self.assertEqual(
            NSTemporaryDirectory.__signature__,
            mod.callable_signature(NSTemporaryDirectory),
        )
        self.assertEqual(
            NSSearchPathForDirectoriesInDomains.__signature__,
            mod.callable_signature(NSSearchPathForDirectoriesInDomains),
        )

        sig = NSTemporaryDirectory.__signature__
        self.assertIsInstance(sig, inspect.Signature)
        self.assertEqual(len(sig.parameters), 0)

        sig = NSSearchPathForDirectoriesInDomains.__signature__
        self.assertIsInstance(sig, inspect.Signature)
        self.assertEqual(len(sig.parameters), 3)
        self.assertEqual(
            sig.parameters["arg0"],
            inspect.Parameter("arg0", inspect.Parameter.POSITIONAL_ONLY),
        )
        self.assertEqual(
            sig.parameters["arg1"],
            inspect.Parameter("arg1", inspect.Parameter.POSITIONAL_ONLY),
        )
        self.assertEqual(
            sig.parameters["arg2"],
            inspect.Parameter("arg2", inspect.Parameter.POSITIONAL_ONLY),
        )
        self.assertEqual(list(sig.parameters), ["arg0", "arg1", "arg2"])

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
        self.assertEqual(
            sig.parameters["arg0"],
            inspect.Parameter("arg0", inspect.Parameter.POSITIONAL_ONLY),
        )

        m = NSArray.indexOfObject_inRange_
        sig = m.__signature__
        self.assertIsInstance(sig, inspect.Signature)
        self.assertEqual(len(sig.parameters), 2)
        self.assertEqual(
            sig.parameters["arg0"],
            inspect.Parameter("arg0", inspect.Parameter.POSITIONAL_ONLY),
        )
        self.assertEqual(
            sig.parameters["arg1"],
            inspect.Parameter("arg1", inspect.Parameter.POSITIONAL_ONLY),
        )
        self.assertEqual(list(sig.parameters), ["arg0", "arg1"])

    def test_not_for_regular_types(self):
        self.assertIs(mod.callable_signature(42), None)
        self.assertIs(mod.callable_signature(int), None)
        self.assertIs(mod.callable_signature(dir), None)
        self.assertIs(mod.callable_signature(lambda x: x * 2), None)

    def test_no_metadata(self):
        class M:
            __name__ = "foo"

            def __metadata__(self):
                raise objc.internal_error

        m = M()
        self.assertIs(mod.describe_callable(m), None)

        self.assertIs(mod.callable_signature(m), None)

    def test_introspect_doc(self):
        meth = NSArray.arrayWithArray_

        s = meth.__doc__
        self.assertIsInstance(s, str)

        orig = objc.options._callable_doc
        try:
            objc.options._callable_doc = None

            s = meth.__doc__
            self.assertIs(s, None)

            def raiser(func):
                raise RuntimeError

            objc.options._callable_doc = raiser

            with self.assertRaises(RuntimeError):
                s = meth.__doc__

        finally:
            objc.options._callable_doc = orig

    def test_introspect_signature(self):
        meth = NSArray.arrayWithArray_

        s = meth.__signature__
        self.assertIsInstance(s, inspect.Signature)

        orig = objc.options._callable_signature
        try:
            objc.options._callable_signature = None

            s = meth.__signature__
            self.assertIs(s, None)

            def raiser(func):
                raise RuntimeError

            objc.options._callable_signature = raiser

            with self.assertRaises(RuntimeError):
                s = meth.__signature__

        finally:
            objc.options._callable_signature = orig
