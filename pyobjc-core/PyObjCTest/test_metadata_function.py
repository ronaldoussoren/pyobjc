"""
Tests for the new-style metadata format interface.

These tests are for global function
"""

import objc
from PyObjCTest.metadatafunction import function_list, union_SomeUnion
from PyObjCTools.TestSupport import TestCase

union_SomeUnion = union_SomeUnion.encode()

_FunctionTable = [
    (
        "makeArrayWithFormat_",
        b"@@",
        "",
        {"variadic": True, "arguments": {0: {"printf_format": True}}},
    ),
    (
        "makeArrayWithCFormat_",
        b"@*",
        "",
        {"variadic": True, "arguments": {0: {"printf_format": True}}},
    ),
    (
        "make4Tuple_",
        b"@^d",
        "",
        {
            "arguments": {
                0: {
                    "type_modifier": objc._C_IN,
                    "c_array_of_fixed_length": 4,
                    "null_accepted": False,
                }
            }
        },
    ),
    (
        "null4Tuple_",
        b"@^d",
        "",
        {
            "arguments": {
                0: {
                    "type_modifier": objc._C_IN,
                    "c_array_of_fixed_length": 4,
                    "null_accepted": True,
                }
            }
        },
    ),
    (
        "makeObjectArray_",
        b"@^@",
        "",
        {
            "arguments": {
                0: {
                    "type_modifier": objc._C_IN,
                    "c_array_delimited_by_null": True,
                    "null_accepted": False,
                }
            }
        },
    ),
    (
        "makeStringArray_",
        b"@^*",
        "",
        {
            "arguments": {
                0: {
                    "type_modifier": objc._C_IN,
                    "c_array_delimited_by_null": True,
                    "null_accepted": False,
                }
            }
        },
    ),
    (
        "nullStringArray_",
        b"@^*",
        "",
        {
            "arguments": {
                0: {
                    "type_modifier": objc._C_IN,
                    "c_array_delimited_by_null": True,
                    "null_accepted": True,
                }
            }
        },
    ),
    (
        "makeIntArray_count_",
        b"@^iI",
        "",
        {
            "arguments": {
                0: {
                    "type_modifier": objc._C_IN,
                    "c_array_length_in_arg": 1,
                    "null_accepted": False,
                }
            }
        },
    ),
    (
        "makeIntArray_countPtr_",
        b"@^i^I",
        "",
        {
            "arguments": {
                0: {
                    "type_modifier": objc._C_IN,
                    "c_array_length_in_arg": 1,
                    "null_accepted": False,
                },
                1: {"type_modifier": objc._C_IN},
            }
        },
    ),
    (
        "nullIntArray_count_",
        b"@^iI",
        "",
        {
            "arguments": {
                0: {
                    "type_modifier": objc._C_IN,
                    "c_array_length_in_arg": 1,
                    "null_accepted": True,
                }
            }
        },
    ),
    (
        "fillArray_uptoCount_",
        b"i^ii",
        "",
        {
            "arguments": {
                0: {
                    "type_modifier": objc._C_OUT,
                    "c_array_length_in_arg": 1,
                    "c_array_length_in_result": True,
                    "null_accepted": False,
                }
            }
        },
    ),
    (
        "fillArray_count_",
        b"v^ii",
        "",
        {
            "arguments": {
                0: {
                    "type_modifier": objc._C_OUT,
                    "c_array_length_in_arg": 1,
                    "null_accepted": False,
                }
            }
        },
    ),
    (
        "nullfillArray_count_",
        b"i^ii",
        "",
        {
            "arguments": {
                0: {
                    "type_modifier": objc._C_OUT,
                    "c_array_length_in_arg": 1,
                    "null_accepted": True,
                }
            }
        },
    ),
    (
        "maybeFillArray_",
        b"i^i",
        "",
        {
            "arguments": {
                0: {
                    "type_modifier": objc._C_OUT,
                    "c_array_of_fixed_length": 4,
                    "c_array_length_in_result": True,
                    "null_accepted": False,
                }
            }
        },
    ),
    (
        "fill4Tuple_",
        b"v^i",
        "",
        {
            "arguments": {
                0: {
                    "type_modifier": objc._C_OUT,
                    "c_array_of_fixed_length": 4,
                    "null_accepted": False,
                }
            }
        },
    ),
    (
        "nullfill4Tuple_",
        b"i^i",
        "",
        {
            "arguments": {
                0: {
                    "type_modifier": objc._C_OUT,
                    "c_array_of_fixed_length": 4,
                    "null_accepted": True,
                }
            }
        },
    ),
    (
        "fillStringArray_",
        b"i^*",
        "",
        {
            "arguments": {
                0: {
                    "type_modifier": objc._C_OUT,
                    "c_array_delimited_by_null": True,
                    "null_accepted": False,
                }
            }
        },
    ),
    (
        "nullfillStringArray_",
        b"i^*",
        "",
        {
            "arguments": {
                0: {
                    "type_modifier": objc._C_OUT,
                    "c_array_delimited_by_null": True,
                    "null_accepted": True,
                }
            }
        },
    ),
    (
        "reverseArray_uptoCount_",
        b"i^fi",
        "",
        {
            "arguments": {
                0: {
                    "type_modifier": objc._C_INOUT,
                    "c_array_length_in_arg": 1,
                    "c_array_length_in_result": True,
                    "null_accepted": False,
                }
            }
        },
    ),
    (
        "reverseArray_count_",
        b"v^fi",
        "",
        {
            "arguments": {
                0: {
                    "type_modifier": objc._C_INOUT,
                    "c_array_length_in_arg": 1,
                    "null_accepted": False,
                }
            }
        },
    ),
    (
        "nullreverseArray_count_",
        b"i^fi",
        "",
        {
            "arguments": {
                0: {
                    "type_modifier": objc._C_INOUT,
                    "c_array_length_in_arg": 1,
                    "null_accepted": True,
                }
            }
        },
    ),
    (
        "reverseStrings_",
        b"v^*",
        "",
        {
            "arguments": {
                0: {
                    "type_modifier": objc._C_INOUT,
                    "c_array_delimited_by_null": True,
                    "null_accepted": False,
                }
            }
        },
    ),
    (
        "nullreverseStrings_",
        b"i^*",
        "",
        {
            "arguments": {
                0: {
                    "type_modifier": objc._C_INOUT,
                    "c_array_delimited_by_null": True,
                    "null_accepted": True,
                }
            }
        },
    ),
    (
        "maybeReverseArray_",
        b"i^s",
        "",
        {
            "arguments": {
                0: {
                    "type_modifier": objc._C_INOUT,
                    "c_array_of_fixed_length": 4,
                    "c_array_length_in_result": True,
                    "null_accepted": False,
                }
            }
        },
    ),
    (
        "reverse4Tuple_",
        b"v^s",
        "",
        {
            "arguments": {
                0: {
                    "type_modifier": objc._C_INOUT,
                    "c_array_of_fixed_length": 4,
                    "null_accepted": False,
                }
            }
        },
    ),
    (
        "nullreverse4Tuple_",
        b"i^s",
        "",
        {
            "arguments": {
                0: {
                    "type_modifier": objc._C_INOUT,
                    "c_array_of_fixed_length": 4,
                    "null_accepted": True,
                }
            }
        },
    ),
    ("makeIntArrayOf5", b"^i", "", {"retval": {"c_array_of_fixed_length": 5}}),
    ("makeStringArray", b"^*", "", {"retval": {"c_array_delimited_by_null": True}}),
    ("makeIntArrayOf_", b"^ii", "", {"retval": {"c_array_length_in_arg": 0}}),
    ("nullIntArrayOf5", b"^i", "", {"retval": {"c_array_of_fixed_length": 5}}),
    ("nullStringArray", b"^*", "", {"retval": {"c_array_delimited_by_null": True}}),
    ("nullIntArrayOf_", b"^ii", "", {"retval": {"c_array_length_in_arg": 0}}),
    (
        "sumX_andY_",
        b"i^i^i",
        "",
        {
            "arguments": {
                0: {"type_modifier": objc._C_IN, "null_accepted": False},
                1: {"type_modifier": objc._C_IN, "null_accepted": False},
            }
        },
    ),
    (
        "divBy5_remainder_",
        b"ii^i",
        "",
        {"arguments": {1: {"type_modifier": objc._C_OUT, "null_accepted": False}}},
    ),
    (
        "swapX_andY_",
        b"v^d^d",
        "",
        {
            "arguments": {
                0: {"type_modifier": objc._C_INOUT, "null_accepted": False},
                1: {"type_modifier": objc._C_INOUT, "null_accepted": False},
            }
        },
    ),
    (
        "input_output_inputAndOutput_",
        b"@^i^i^i",
        "",
        {
            "arguments": {
                0: {"type_modifier": objc._C_IN, "null_accepted": True},
                1: {"type_modifier": objc._C_OUT, "null_accepted": True},
                2: {"type_modifier": objc._C_INOUT, "null_accepted": True},
            }
        },
    ),
    (
        "getDoubleFunc",
        b"^?",
        "",
        {
            "retval": {
                "callable": {
                    "retval": {"type": objc._C_INT},
                    "arguments": {
                        "0": {"type": objc._C_INT},
                    },
                }
            }
        },
    ),
    (
        "getOldDoubleFunc",
        b"^?",
        "",
        {
            "retval": {
                "callable": {
                    "deprecated": 1005,
                    "retval": {"type": objc._C_INT},
                    "arguments": {
                        0: {"type": objc._C_INT},
                    },
                }
            }
        },
    ),
    (
        "getGetter",
        b"^?",
        "",
        {
            "retval": {
                "callable": {
                    "deprecated": 1005,
                    "retval": {"type": objc._C_VOID},
                    "arguments": {
                        0: {"type": objc._C_OUT + objc._C_PTR + objc._C_INT},
                        1: {"type": objc._C_OUT + objc._C_PTR + objc._C_INT},
                    },
                }
            }
        },
    ),
    (
        "get2ndGetter",
        b"^?",
        "",
        {
            "retval": {
                "callable": {
                    "deprecated": 1005,
                    "retval": {"type": objc._C_VOID},
                    "arguments": {
                        i: {"type": objc._C_OUT + objc._C_PTR + objc._C_INT}
                        for i in range(63)
                    },
                }
            }
        },
    ),
    ("oldDoubleFunc", b"ii", "", {"deprecated": 1005}),
    ("raiseFunc", b"v", "", {}),
    ("raiseFunc2", b"vn^i", "", {}),
    (
        "returnUnionArray",
        b"^" + union_SomeUnion,
        "",
        {"retval": {"c_array_of_variable_length": True}},
    ),
    (
        "returnPointerArray",
        b"^^{UnknownLabel=ii}22",
        "",
        {"retval": {"c_array_of_variable_length": True}},
    ),
    ("makeVoidPArrayOf_", b"^vi", "", {"retval": {"c_array_of_variable_length": True}}),
    #    (
    #        "return2ndPointerArray",
    #        b"^^{UnknownLabel=ii",
    #        "",
    #        {
    #            "retval": { "c_array_of_variable_length": True }
    #        }
    #    ),
]

objc.loadFunctionList(function_list, globals(), _FunctionTable, False)


class TestExists(TestCase):
    def testFunctionsExists(self):
        for item in _FunctionTable:
            self.assertIn(item[0], globals())


class TestArrayDefault(TestCase):
    # TODO: what is the default anyway?
    pass


class TestArraysOut(TestCase):
    def testFixedSize(self):
        v = fill4Tuple_(None)  # noqa: F821
        self.assertEqual(list(v), [0, -1, -8, -27])

        with self.assertRaisesRegex(ValueError, "argument 0 isn't allowed to be NULL"):
            fill4Tuple_(objc.NULL)  # noqa: F821

        n, v = nullfill4Tuple_(None)  # noqa: F821
        self.assertEqual(n, 1)
        self.assertEqual(list(v), [0, -1, -8, -27])

        n, v = nullfill4Tuple_(objc.NULL)  # noqa: F821
        self.assertEqual(n, 0)
        self.assertIs(v, objc.NULL)

    def testNullTerminated(self):
        # Output only arrays of null-terminated arrays cannot be
        # wrapped automaticly. How is the bridge supposed to know
        # how much memory it should allocate for the C-array?
        with self.assertRaisesRegex(
            TypeError, "NULL-terminated 'out' arguments are not supported"
        ):
            fillStringArray_(None)  # noqa: F821
        with self.assertRaisesRegex(ValueError, "argument 0 isn't allowed to be NULL"):
            fillStringArray_(objc.NULL)  # noqa: F821

        with self.assertRaisesRegex(TypeError, "Need 1 arguments, got 0"):
            nullfillStringArray_()  # noqa: F821
        with self.assertRaisesRegex(
            TypeError, "NULL-terminated 'out' arguments are not supported"
        ):
            nullfillStringArray_(None)  # noqa: F821
        n, v = nullfillStringArray_(objc.NULL)  # noqa: F821
        self.assertEqual(n, 0)
        self.assertIs(v, objc.NULL)

    def testWithCount(self):
        v = fillArray_count_(None, 3)  # noqa: F821
        self.assertEqual(list(v), [0, 1, 4])

        v = fillArray_count_(None, 3)  # noqa: F821
        self.assertEqual(list(v), [0, 1, 4])

        v = fillArray_count_(None, 5)  # noqa: F821
        self.assertEqual(list(v), [0, 1, 4, 9, 16])

        v = fillArray_count_(None, 0)  # noqa: F821
        self.assertEqual(list(v), [])

        with self.assertRaisesRegex(ValueError, "argument 0 isn't allowed to be NULL"):
            fillArray_count_(objc.NULL, 0)  # noqa: F821

        n, v = nullfillArray_count_(None, 3)  # noqa: F821
        self.assertEqual(n, 1)
        self.assertEqual(list(v), [0, 1, 4])
        n, v = nullfillArray_count_(None, 3)  # noqa: F821
        self.assertEqual(n, 1)
        self.assertEqual(list(v), [0, 1, 4])

        n, v = nullfillArray_count_(objc.NULL, 3)  # noqa: F821
        self.assertEqual(n, 0)
        self.assertIs(v, objc.NULL)

    def testWithCountInResult(self):
        self.maxDiff = None
        self.assertEqual(
            fillArray_uptoCount_.__metadata__(),  # noqa: F821
            {
                "full_signature": b"i^ii",
                "retval": {"type": b"i", "_template": True},
                "arguments": (
                    {
                        "type": b"o^i",
                        "c_array_length_in_arg": 1,
                        "c_array_length_in_result": True,
                        "null_accepted": False,
                    },
                    {"type": b"i", "_template": True},
                ),
            },
        )
        c, v = fillArray_uptoCount_(None, 20)  # noqa: F821
        self.assertEqual(c, 10)
        self.assertEqual(list(v), [i + 2 for i in range(10)])

        c, v = maybeFillArray_(None)  # noqa: F821
        self.assertEqual(c, 2)
        self.assertEqual(list(v), [10, 11])


class TestArraysInOut(TestCase):
    def testFixedSize(self):
        a = (1, 2, 3, 4)
        v = reverse4Tuple_(a)  # noqa: F821
        self.assertEqual(a, (1, 2, 3, 4))
        self.assertEqual(v, (4, 3, 2, 1))

        with self.assertRaisesRegex(ValueError, "expecting 4 values got 3"):
            reverse4Tuple_((1, 2, 3))  # noqa: F821
        with self.assertRaisesRegex(ValueError, "expecting 4 values got 5"):
            reverse4Tuple_((1, 2, 3, 4, 5))  # noqa: F821
        with self.assertRaisesRegex(ValueError, "argument 0 isn't allowed to be NULL"):
            reverse4Tuple_(objc.NULL)  # noqa: F821

        a = (1, 2, 3, 4)
        n, v = nullreverse4Tuple_(a)  # noqa: F821
        self.assertEqual(n, 1)
        self.assertEqual(a, (1, 2, 3, 4))
        self.assertEqual(v, (4, 3, 2, 1))

        n, v = nullreverse4Tuple_(objc.NULL)  # noqa: F821
        self.assertEqual(n, 0)
        self.assertIs(v, objc.NULL)

    def testNullTerminated(self):
        a = (b"a", b"b", b"c")
        v = reverseStrings_(a)  # noqa: F821
        self.assertEqual(a, (b"a", b"b", b"c"))
        self.assertEqual(v, (b"c", b"b", b"a"))

        with self.assertRaisesRegex(ValueError, "depythonifying 'charptr', got 'int'"):
            reverseStrings_((1, 2))  # noqa: F821
        with self.assertRaisesRegex(ValueError, "argument 0 isn't allowed to be NULL"):
            reverseStrings_(objc.NULL)  # noqa: F821

        a = (b"a", b"b", b"c")
        n, v = nullreverseStrings_(a)  # noqa: F821
        self.assertEqual(n, 1)
        self.assertEqual(a, (b"a", b"b", b"c"))
        self.assertEqual(v, (b"c", b"b", b"a"))

        n, v = nullreverseStrings_(objc.NULL)  # noqa: F821
        self.assertEqual(n, 0)
        self.assertIs(v, objc.NULL)

    def testWithCount(self):
        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        v = reverseArray_count_(a, 4)  # noqa: F821
        self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEqual(v, (4.0, 3.0, 2.0, 1.0))

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        v = reverseArray_count_(a, 5)  # noqa: F821
        self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEqual(v, (5.0, 4.0, 3.0, 2.0, 1.0))

        # Nice to have, but doesn't work without major
        # surgery:
        # a = (1.0, 2.0, 3.0, 4.0, 5.0)
        # v = reverseArray_count_(a, None)  # noqa: F821
        # self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        # self.assertEqual(v, (5.0, 4.0, 3.0, 2.0, 1.0))

        with self.assertRaisesRegex(
            ValueError, r"too few values \(2\) expecting at least 5"
        ):
            reverseArray_count_((1.0, 2.0), 5)  # noqa: F821
        with self.assertRaisesRegex(ValueError, "argument 0 isn't allowed to be NULL"):
            reverseArray_count_(objc.NULL, 0)  # noqa: F821

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        n, v = nullreverseArray_count_(a, 5)  # noqa: F821
        self.assertEqual(n, 1)
        self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEqual(v, (5.0, 4.0, 3.0, 2.0, 1.0))

        n, v = nullreverseArray_count_(objc.NULL, 0)  # noqa: F821
        self.assertEqual(n, 0)
        self.assertIs(v, objc.NULL)

    def testWithCountInResult(self):
        c, v = reverseArray_uptoCount_(range(10), 10)  # noqa: F821
        self.assertEqual(c, 5)
        self.assertEqual(len(v), 5)
        self.assertEqual(list(v), [9, 8, 7, 6, 5])

        c, v = maybeReverseArray_([1, 2, 3, 4])  # noqa: F821
        self.assertEqual(c, 2)
        self.assertEqual(len(v), 2)
        self.assertEqual(list(v), [4, 3])


class TestArraysIn(TestCase):
    def testFixedSize(self):
        v = make4Tuple_((1.0, 4.0, 8.0, 12.5))  # noqa: F821
        self.assertEqual(len(v), 4)
        self.assertEqual(list(v), [1.0, 4.0, 8.0, 12.5])

        v = make4Tuple_((1, 2, 3, 4))  # noqa: F821
        self.assertEqual(len(v), 4)
        self.assertEqual(list(v), [1.0, 2.0, 3.0, 4.0])

        with self.assertRaisesRegex(ValueError, "expecting 4 values got 3"):
            make4Tuple_((1, 2, 3))  # noqa: F821
        with self.assertRaisesRegex(ValueError, "expecting 4 values got 5"):
            make4Tuple_((1, 2, 3, 4, 5))  # noqa: F821
        with self.assertRaisesRegex(ValueError, "argument 0 isn't allowed to be NULL"):
            make4Tuple_(objc.NULL)  # noqa: F821

        v = null4Tuple_(objc.NULL)  # noqa: F821
        self.assertIs(v, None)

    def testNullTerminated(self):
        v = makeStringArray_((b"hello", b"world", b"there"))  # noqa: F821
        self.assertEqual(len(v), 3)
        self.assertEqual(list(v), ["hello", "world", "there"])
        self.assertIsInstance(v, objc.lookUpClass("NSArray"))
        self.assertIsInstance(v[0], str)

        NSObject = objc.lookUpClass("NSObject")
        p, q, r = NSObject.new(), NSObject.new(), NSObject.new()
        v = makeObjectArray_((p, q, r))  # noqa: F821
        self.assertEqual(len(v), 3)
        self.assertIs(v[0], p)
        self.assertIs(v[1], q)
        self.assertIs(v[2], r)

        v = makeStringArray_(())  # noqa: F821
        self.assertEqual(len(v), 0)

        with self.assertRaisesRegex(ValueError, "depythonifying 'charptr', got 'int'"):
            makeStringArray_([1, 2])  # noqa: F821
        with self.assertRaisesRegex(ValueError, "argument 0 isn't allowed to be NULL"):
            makeStringArray_(objc.NULL)  # noqa: F821

        v = nullStringArray_(objc.NULL)  # noqa: F821
        self.assertEqual(v, None)

    def testWithCount(self):
        v = makeIntArray_count_((1, 2, 3, 4), 3)  # noqa: F821
        self.assertEqual(len(v), 3)
        self.assertEqual(list(v), [1, 2, 3])

        # XXX: This one would be nice to have, but not entirely trivial
        # v = makeIntArray_count_((1,2,3,4), None)  # noqa: F821
        # self.assertEqual(len(v), 3)
        # self.assertEqual(list(v), [1,2,3,4])

        with self.assertRaisesRegex(
            ValueError, r"too few values \(3\) expecting at least 4"
        ):
            makeIntArray_count_([1, 2, 3], 4)  # noqa: F821
        with self.assertRaisesRegex(ValueError, "argument 0 isn't allowed to be NULL"):
            makeIntArray_count_(objc.NULL, 0)  # noqa: F821
        with self.assertRaisesRegex(ValueError, "argument 0 isn't allowed to be NULL"):
            makeIntArray_count_(objc.NULL, 1)  # noqa: F821

        v = nullIntArray_count_(objc.NULL, 0)  # noqa: F821
        self.assertEqual(v, None)

        with self.assertRaisesRegex(ValueError, "argument 0 isn't allowed to be NULL"):
            makeIntArray_count_(objc.NULL, 1)  # noqa: F821

        # Make sure this also works when the length is in a pass-by-reference argument
        v = makeIntArray_countPtr_((1, 2, 3, 4), 4)  # noqa: F821
        self.assertEqual(len(v), 4)
        self.assertEqual(list(v), [1, 2, 3, 4])


class TestArrayReturns(TestCase):
    # TODO:
    # - Add null-terminated arrays of various supported types:
    #   -> integers
    #   -> CF-types
    def testFixedSize(self):
        v = makeIntArrayOf5()  # noqa: F821
        self.assertEqual(len(v), 5)
        self.assertEqual(v[0], 0)
        self.assertEqual(v[1], 1)
        self.assertEqual(v[2], 4)
        self.assertEqual(v[3], 9)
        self.assertEqual(v[4], 16)

        v = nullIntArrayOf5()  # noqa: F821
        self.assertEqual(v, objc.NULL)

    def testSizeInArgument(self):
        v = makeIntArrayOf_(3)  # noqa: F821
        self.assertEqual(len(v), 3)
        self.assertEqual(v[0], 0)
        self.assertEqual(v[1], 1)
        self.assertEqual(v[2], 8)

        v = makeIntArrayOf_(10)  # noqa: F821
        self.assertEqual(len(v), 10)
        for i in range(10):
            self.assertEqual(v[i], i**3)

        v = nullIntArrayOf_(100)  # noqa: F821
        self.assertEqual(v, objc.NULL)

    def testNULLterminated(self):
        v = makeStringArray()  # noqa: F821
        self.assertEqual(len(v), 4)
        self.assertEqual(list(v), [b"hello", b"world", b"out", b"there"])

        v = nullStringArray()  # noqa: F821
        self.assertEqual(v, objc.NULL)


class TestByReference(TestCase):
    # Pass by reference arguments.
    # Note that these tests aren't exhaustive, we have test_methods and
    # test_methods2 for that :-)

    def testInput(self):
        r = sumX_andY_(1, 2)  # noqa: F821
        self.assertEqual(r, 1 + 2)

        r = sumX_andY_(2535, 5325)  # noqa: F821
        self.assertEqual(r, 2535 + 5325)

        with self.assertRaisesRegex(ValueError, "argument 1 isn't allowed to be NULL"):
            sumX_andY_(42, objc.NULL)  # noqa: F821

    def testOutput(self):
        div, rem = divBy5_remainder_(55, None)  # noqa: F821
        self.assertEqual(div, 11)
        self.assertEqual(rem, 0)

        div, rem = divBy5_remainder_(13, None)  # noqa: F821
        self.assertEqual(div, 2)
        self.assertEqual(rem, 3)

        with self.assertRaisesRegex(ValueError, "argument 1 isn't allowed to be NULL"):
            divBy5_remainder_(42, objc.NULL)  # noqa: F821

    def testInputOutput(self):
        x, y = swapX_andY_(42, 284)  # noqa: F821
        self.assertEqual(x, 284)
        self.assertEqual(y, 42)

        with self.assertRaisesRegex(ValueError, "argument 1 isn't allowed to be NULL"):
            swapX_andY_(42, objc.NULL)  # noqa: F821

    def testNullAccepted(self):
        # Note: the commented-out test-cases require a change in the pyobjc-core

        def makeNum(value):
            return int(value, 0)

        r, y, z = input_output_inputAndOutput_(1, None, 2)  # noqa: F821
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(None, map(makeNum, r)))), 3)
        self.assertEqual(y, 3)
        self.assertEqual(z, -1)

        # Argument 1 is NULL
        r, y, z = input_output_inputAndOutput_(objc.NULL, None, 2)  # noqa: F821
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(None, map(makeNum, r)))), 2)
        self.assertEqual(y, 40)
        self.assertEqual(z, -2)

        r, y, z = input_output_inputAndOutput_(objc.NULL, None, 2)  # noqa: F821
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(None, map(makeNum, r)))), 2)
        self.assertEqual(y, 40)
        self.assertEqual(z, -2)

        # Argument 2 is NULL
        r, y, z = input_output_inputAndOutput_(1, objc.NULL, 2)  # noqa: F821
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(None, map(makeNum, r)))), 2)
        self.assertEqual(y, objc.NULL)
        self.assertEqual(z, -1)

        # Argument 3 is NULL
        r, y, z = input_output_inputAndOutput_(1, None, objc.NULL)  # noqa: F821
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(None, map(makeNum, r)))), 2)
        self.assertEqual(y, 43)
        self.assertEqual(z, objc.NULL)

        r, y, z = input_output_inputAndOutput_(1, None, objc.NULL)  # noqa: F821
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(None, map(makeNum, r)))), 2)
        self.assertEqual(y, 43)
        self.assertEqual(z, objc.NULL)


class TestPrintfFormat(TestCase):
    def test_nsformat(self):
        v = makeArrayWithFormat_("%3d", 10)  # noqa: F821
        self.assertEqual(list(v), ["%3d", " 10"])

        v = makeArrayWithFormat_("hello %s", b"world")  # noqa: F821
        self.assertEqual(list(v), ["hello %s", "hello world"])

        v = makeArrayWithFormat_("\xf1")  # noqa: F821
        self.assertEqual(list(v), ["\xf1", "\xf1"])

    def test_cformat(self):
        v = makeArrayWithCFormat_(b"%3d", 10)  # noqa: F821
        self.assertEqual(list(v), ["%3d", " 10"])

        v = makeArrayWithCFormat_(b"hello %s", b"world")  # noqa: F821
        self.assertEqual(list(v), ["hello %s", "hello world"])
