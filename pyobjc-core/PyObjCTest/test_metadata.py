"""
Tests for the new-style metadata format interface.

Note: Tests for calling from ObjC into python are in test_metadata_py.py

TODO:
- Add tests for calling functions instead of methods
- The python->C interface (that is the contents of the metadata object) is
  likely to change when the bridge is feature-complete.
- Probably need special-casing for arrays (numarray and array.array)!
"""
import array
import sys

import objc
from PyObjCTest.metadata import OC_MetaDataTest
from PyObjCTools.TestSupport import TestCase

make_array = array.array


def setupMetaData():
    # Note to self: what we think of as the first argument of a method is
    # actually the third one, the objc runtime implicitly passed 'self' and
    # the selector as well. Therefore we need to start counting at 2 instead
    # of 0.
    #
    # Note2: the code below would normally be done using a metadata file
    # instead of hardcoding.
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest", b"boolClassMethod", {"retval": {"type": objc._C_NSBOOL}}
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"unknownLengthArray",
        {"retval": {"c_array_of_variable_length": True}},
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"unknownLengthMutable",
        {"retval": {"c_array_of_variable_length": True}},
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"makeVariableLengthArray:halfCount:",
        {
            "arguments": {
                2 + 0: {"c_array_of_variable_length": True, "type_modifier": objc._C_IN}
            }
        },
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest", b"varargsMethodWithObjects:", {"variadic": True}
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest", b"ignoreMethod", {"suggestion": "please ignore me"}
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"makeArrayWithFormat:",
        {"variadic": True, "arguments": {2 + 0: {"printf_format": True}}},
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"makeArrayWithCFormat:",
        {"variadic": True, "arguments": {2 + 0: {"printf_format": True}}},
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"makeArrayWithArguments:",
        {"variadic": True, "c_array_delimited_by_null": True},
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"make4Tuple:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_IN,
                    "c_array_of_fixed_length": 4,
                    "null_accepted": False,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"null4Tuple:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_IN,
                    "c_array_of_fixed_length": 4,
                    "null_accepted": True,
                }
            }
        },
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"makeObjectArray:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_IN,
                    "c_array_delimited_by_null": True,
                    "null_accepted": False,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"makeStringArray:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_IN,
                    "c_array_delimited_by_null": True,
                    "null_accepted": False,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"nullStringArray:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_IN,
                    "c_array_delimited_by_null": True,
                    "null_accepted": True,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"makeIntArray:count:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_IN,
                    "c_array_length_in_arg": 2 + 1,
                    "null_accepted": False,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"makeIntArray:halfCount:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_IN,
                    "c_array_of_variable_length": True,
                    "null_accepted": False,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"makeIntArray:countPtr:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_IN,
                    "c_array_length_in_arg": 2 + 1,
                    "null_accepted": False,
                },
                2 + 1: {"type_modifier": objc._C_IN, "null_accepted": False},
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"nullIntArray:count:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_IN,
                    "c_array_length_in_arg": 2 + 1,
                    "null_accepted": True,
                }
            }
        },
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"fillArray:uptoCount:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_OUT,
                    "c_array_length_in_arg": 2 + 1,
                    "c_array_length_in_result": True,
                    "null_accepted": False,
                }
            }
        },
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"fillArray:count:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_OUT,
                    "c_array_length_in_arg": 2 + 1,
                    "null_accepted": False,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"nullfillArray:count:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_OUT,
                    "c_array_length_in_arg": 2 + 1,
                    "null_accepted": True,
                }
            }
        },
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"maybeFillArray:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_OUT,
                    "c_array_of_fixed_length": 4,
                    "c_array_length_in_result": True,
                    "null_accepted": False,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"fill4Tuple:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_OUT,
                    "c_array_of_fixed_length": 4,
                    "null_accepted": False,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"nullfill4Tuple:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_OUT,
                    "c_array_of_fixed_length": 4,
                    "null_accepted": True,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"fillStringArray:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_OUT,
                    "c_array_delimited_by_null": True,
                    "null_accepted": False,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"nullfillStringArray:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_OUT,
                    "c_array_delimited_by_null": True,
                    "null_accepted": True,
                }
            }
        },
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"reverseArray:uptoCount:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_INOUT,
                    "c_array_length_in_arg": 2 + 1,
                    "c_array_length_in_result": True,
                    "null_accepted": False,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"reverseArray:count:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_INOUT,
                    "c_array_length_in_arg": 2 + 1,
                    "null_accepted": False,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"nullreverseArray:count:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_INOUT,
                    "c_array_length_in_arg": 2 + 1,
                    "null_accepted": True,
                }
            }
        },
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"reverseStrings:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_INOUT,
                    "c_array_delimited_by_null": True,
                    "null_accepted": False,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"nullreverseStrings:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_INOUT,
                    "c_array_delimited_by_null": True,
                    "null_accepted": True,
                }
            }
        },
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"maybeReverseArray:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_INOUT,
                    "c_array_of_fixed_length": 4,
                    "c_array_length_in_result": True,
                    "null_accepted": False,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"reverse4Tuple:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_INOUT,
                    "c_array_of_fixed_length": 4,
                    "null_accepted": False,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"nullreverse4Tuple:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_INOUT,
                    "c_array_of_fixed_length": 4,
                    "null_accepted": True,
                }
            }
        },
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"makeIntArrayOf5",
        {"retval": {"c_array_of_fixed_length": 5}},
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"makeStringArray",
        {"retval": {"c_array_delimited_by_null": True}},
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"makeIntArrayOf:",
        {"retval": {"c_array_length_in_arg": 2 + 0}},
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"nullIntArrayOf5",
        {"retval": {"c_array_of_fixed_length": 5}},
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"nullStringArray",
        {"retval": {"c_array_delimited_by_null": True}},
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"nullIntArrayOf:",
        {"retval": {"c_array_length_in_arg": 2 + 0}},
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"sumX:andY:",
        {
            "arguments": {
                2 + 0: {"type_modifier": objc._C_IN, "null_accepted": False},
                2 + 1: {"type_modifier": objc._C_IN, "null_accepted": False},
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"divBy5:remainder:",
        {"arguments": {2 + 1: {"type_modifier": objc._C_OUT, "null_accepted": False}}},
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"swapX:andY:",
        {
            "arguments": {
                2 + 0: {"type_modifier": objc._C_INOUT, "null_accepted": False},
                2 + 1: {"type_modifier": objc._C_INOUT, "null_accepted": False},
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"input:output:inputAndOutput:",
        {
            "arguments": {
                2 + 0: {"type_modifier": objc._C_IN, "null_accepted": True},
                2 + 1: {"type_modifier": objc._C_OUT, "null_accepted": True},
                2 + 2: {"type_modifier": objc._C_INOUT, "null_accepted": True},
            }
        },
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"makeDataForBytes:count:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_IN,
                    "c_array_length_in_arg": 2 + 1,
                    "null_accepted": False,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"makeDataForVoids:count:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_IN,
                    "c_array_length_in_arg": 2 + 1,
                    "null_accepted": False,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"addOneToBytes:count:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_INOUT,
                    "c_array_length_in_arg": 2 + 1,
                    "null_accepted": False,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"addOneToVoids:count:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_INOUT,
                    "c_array_length_in_arg": 2 + 1,
                    "null_accepted": False,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"fillBuffer:count:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_OUT,
                    "c_array_length_in_arg": 2 + 1,
                    "null_accepted": False,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"fillVoids:count:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_OUT,
                    "c_array_length_in_arg": 2 + 1,
                    "null_accepted": False,
                }
            }
        },
    )


setupMetaData()


class TestArrayDefault(TestCase):
    # TODO: what is the default anyway?
    pass


class TestArraysOut(TestCase):
    def testFixedSize(self):
        o = OC_MetaDataTest.new()

        v = o.fill4Tuple_(None)
        self.assertEqual(list(v), [0, -1, -8, -27])

        self.assertRaises(ValueError, o.fill4Tuple_, objc.NULL)

        n, v = o.nullfill4Tuple_(None)
        self.assertEqual(n, 1)
        self.assertEqual(list(v), [0, -1, -8, -27])

        n, v = o.nullfill4Tuple_(objc.NULL)
        self.assertEqual(n, 0)
        self.assertIs(v, objc.NULL)

        a = make_array("i", [0] * 4)
        v = o.fill4Tuple_(a)
        self.assertIs(a, v)
        self.assertEqual(list(a), [0, -1, -8, -27])

        a = make_array("i", [0] * 5)
        self.assertRaises(ValueError, o.fill4Tuple_, a)
        a = make_array("i", [0] * 3)
        self.assertRaises(ValueError, o.fill4Tuple_, a)

    def testNullTerminated(self):
        o = OC_MetaDataTest.new()

        # Output only arrays of null-terminated arrays cannot be
        # wrapped automaticly. How is the bridge supposed to know
        # how much memory it should allocate for the C-array?
        self.assertRaises(TypeError, o.fillStringArray_, None)
        self.assertRaises(ValueError, o.fillStringArray_, objc.NULL)

        self.assertRaises(TypeError, o.nullfillStringArray_)
        self.assertRaises(TypeError, o.nullfillStringArray_, None)
        n, v = o.nullfillStringArray_(objc.NULL)
        self.assertEqual(n, 0)
        self.assertIs(v, objc.NULL)

    def testWithCount(self):
        o = OC_MetaDataTest.new()

        v = o.fillArray_count_(None, 3)
        self.assertEqual(list(v), [0, 1, 4])

        v = o.fillArray_count_(None, 3)
        self.assertEqual(list(v), [0, 1, 4])

        v = o.fillArray_count_(None, 5)
        self.assertEqual(list(v), [0, 1, 4, 9, 16])

        v = o.fillArray_count_(None, 0)
        self.assertEqual(list(v), [])

        self.assertRaises(ValueError, o.fillArray_count_, objc.NULL, 0)

        n, v = o.nullfillArray_count_(None, 4)
        self.assertEqual(n, 1)
        self.assertEqual(list(v), [0, 1, 4, 9])
        n, v = o.nullfillArray_count_(None, 3)
        self.assertEqual(n, 1)
        self.assertEqual(list(v), [0, 1, 4])

        n, v = o.nullfillArray_count_(objc.NULL, 3)
        self.assertEqual(n, 0)
        self.assertIs(v, objc.NULL)

        a = make_array("i", [0] * 10)
        v = o.fillArray_count_(a, 10)
        self.assertIs(a, v)
        self.assertEqual(list(a), [0, 1, 4, 9, 16, 25, 36, 49, 64, 81])

    def testWithCountInResult(self):
        o = OC_MetaDataTest.new()

        c, v = o.fillArray_uptoCount_(None, 20)
        self.assertEqual(c, 10)
        self.assertEqual(list(v), [i + 2 for i in range(10)])

        c, v = o.maybeFillArray_(None)
        self.assertEqual(c, 2)
        self.assertEqual(list(v), [10, 11])


class TestArraysInOut(TestCase):
    def testFixedSize(self):
        o = OC_MetaDataTest.new()

        a = (1, 2, 3, 4)
        v = o.reverse4Tuple_(a)
        self.assertEqual(a, (1, 2, 3, 4))
        self.assertEqual(v, (4, 3, 2, 1))

        self.assertRaises(ValueError, o.reverse4Tuple_, (1, 2, 3))
        self.assertRaises(ValueError, o.reverse4Tuple_, (1, 2, 3, 4, 5))
        self.assertRaises(ValueError, o.reverse4Tuple_, objc.NULL)

        a = (1, 2, 3, 4)
        n, v = o.nullreverse4Tuple_(a)
        self.assertEqual(n, 1)
        self.assertEqual(a, (1, 2, 3, 4))
        self.assertEqual(v, (4, 3, 2, 1))

        n, v = o.nullreverse4Tuple_(objc.NULL)
        self.assertEqual(n, 0)
        self.assertIs(v, objc.NULL)

        a = make_array("h", [1, 2, 3, 4])
        v = o.reverse4Tuple_(a)
        self.assertIs(v, a)
        self.assertEqual(list(a), [4, 3, 2, 1])

        a = make_array("h", [1, 2, 3, 4, 5])
        self.assertRaises(ValueError, o.reverse4Tuple_, a)
        a = make_array("h", [1, 2, 3])
        self.assertRaises(ValueError, o.reverse4Tuple_, a)

    def testNullTerminated(self):
        o = OC_MetaDataTest.new()

        a = (b"a", b"b", b"c")
        v = o.reverseStrings_(a)
        self.assertEqual(a, (b"a", b"b", b"c"))
        self.assertEqual(v, (b"c", b"b", b"a"))

        self.assertRaises(ValueError, o.reverseStrings_, (1, 2))
        self.assertRaises(ValueError, o.reverseStrings_, objc.NULL)

        a = (b"a", b"b", b"c")
        n, v = o.nullreverseStrings_(a)
        self.assertEqual(n, 1)
        self.assertEqual(a, (b"a", b"b", b"c"))
        self.assertEqual(v, (b"c", b"b", b"a"))

        n, v = o.nullreverseStrings_(objc.NULL)
        self.assertEqual(n, 0)
        self.assertIs(v, objc.NULL)

    def testWithCount(self):
        o = OC_MetaDataTest.new()

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        v = o.reverseArray_count_(a, 4)
        self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEqual(v, (4.0, 3.0, 2.0, 1.0))

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        v = o.reverseArray_count_(a, 5)
        self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEqual(v, (5.0, 4.0, 3.0, 2.0, 1.0))

        # Nice to have, but doesn't work without major
        # surgery:
        # a = (1.0, 2.0, 3.0, 4.0, 5.0)
        # v = o.reverseArray_count_(a, None)
        # self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        # self.assertEqual(v, (5.0, 4.0, 3.0, 2.0, 1.0))

        self.assertRaises(ValueError, o.reverseArray_count_, (1.0, 2.0), 5)
        self.assertRaises(ValueError, o.reverseArray_count_, objc.NULL, 0)

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        n, v = o.nullreverseArray_count_(a, 4)
        self.assertEqual(n, 1)
        self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEqual(v, (4.0, 3.0, 2.0, 1.0))

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        n, v = o.nullreverseArray_count_(a, 5)
        self.assertEqual(n, 1)
        self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEqual(v, (5.0, 4.0, 3.0, 2.0, 1.0))

        n, v = o.nullreverseArray_count_(objc.NULL, 0)
        self.assertEqual(n, 0)
        self.assertIs(v, objc.NULL)

        a = make_array("f", [5.0, 7.0, 9.0, 11.0, 13.0])
        v = o.reverseArray_count_(a, 5)
        self.assertIs(a, v)
        self.assertEqual(list(a), [13.0, 11.0, 9.0, 7.0, 5.0])

    def testWithCountInResult(self):
        o = OC_MetaDataTest.new()

        c, v = o.reverseArray_uptoCount_(range(10), 10)
        self.assertEqual(c, 5)
        self.assertEqual(len(v), 5)
        self.assertEqual(list(v), [9, 8, 7, 6, 5])

        c, v = o.maybeReverseArray_([1, 2, 3, 4])
        self.assertEqual(c, 2)
        self.assertEqual(len(v), 2)
        self.assertEqual(list(v), [4, 3])


class TestArraysIn(TestCase):
    def testFixedSize(self):
        o = OC_MetaDataTest.new()

        v = o.make4Tuple_((1.0, 4.0, 8.0, 12.5))
        self.assertEqual(len(v), 4)
        self.assertEqual(list(v), [1.0, 4.0, 8.0, 12.5])

        v = o.make4Tuple_((1, 2, 3, 4))
        self.assertEqual(len(v), 4)
        self.assertEqual(list(v), [1.0, 2.0, 3.0, 4.0])

        self.assertRaises(ValueError, o.make4Tuple_, (1, 2, 3))
        self.assertRaises(ValueError, o.make4Tuple_, (1, 2, 3, 4, 5))
        self.assertRaises(ValueError, o.make4Tuple_, objc.NULL)

        v = o.null4Tuple_(objc.NULL)
        self.assertIsNone(v)

        a = make_array("d", [2.5, 3.5, 4.5, 5.5])
        v = o.make4Tuple_(a)
        self.assertEqual(list(v), [2.5, 3.5, 4.5, 5.5])

    def testNullTerminated(self):
        o = OC_MetaDataTest.new()

        v = o.makeStringArray_((b"hello", b"world", b"there"))
        self.assertEqual(len(v), 3)
        self.assertEqual(list(v), ["hello", "world", "there"])
        self.assertIsInstance(v, objc.lookUpClass("NSArray"))
        self.assertIsInstance(v[0], str)

        NSObject = objc.lookUpClass("NSObject")
        p, q, r = NSObject.new(), NSObject.new(), NSObject.new()
        v = o.makeObjectArray_((p, q, r))
        self.assertEqual(len(v), 3)
        self.assertIs(v[0], p)
        self.assertIs(v[1], q)
        self.assertIs(v[2], r)

        v = o.makeStringArray_(())
        self.assertEqual(len(v), 0)

        self.assertRaises(ValueError, o.makeStringArray_, [1, 2])
        self.assertRaises(ValueError, o.makeStringArray_, objc.NULL)

        v = o.nullStringArray_(objc.NULL)
        self.assertEqual(v, None)

    def testWithCount(self):
        o = OC_MetaDataTest.new()

        v = o.makeIntArray_count_((1, 2, 3, 4), 3)
        self.assertEqual(len(v), 3)
        self.assertEqual(list(v), [1, 2, 3])

        # XXX: This one would be nice to have, but not entirely trivial
        # v = o.makeIntArray_count_((1,2,3,4), None)
        # self.assertEqual(len(v), 3)
        # self.assertEqual(list(v), [1,2,3,4])

        self.assertRaises(ValueError, o.makeIntArray_count_, [1, 2, 3], 4)
        self.assertRaises(ValueError, o.makeIntArray_count_, objc.NULL, 0)
        self.assertRaises(ValueError, o.makeIntArray_count_, objc.NULL, 1)

        v = o.nullIntArray_count_(objc.NULL, 0)
        self.assertEqual(v, None)

        self.assertRaises(ValueError, o.makeIntArray_count_, objc.NULL, 1)

        # Make sure this also works when the length is in a pass-by-reference argument
        v = o.makeIntArray_countPtr_((1, 2, 3, 4), 4)
        self.assertEqual(len(v), 4)
        self.assertEqual(list(v), [1, 2, 3, 4])

        a = make_array("i", range(20))
        v = o.makeIntArray_count_(a, 7)
        self.assertEqual(list(v), list(range(7)))

        self.assertRaises(ValueError, o.makeIntArray_count_, a, 21)


class TestArrayReturns(TestCase):
    # TODO:
    # - Add null-terminated arrays of various supported types:
    #   -> integers
    #   -> CF-types

    def testFixedSize(self):
        o = OC_MetaDataTest.new()

        v = o.makeIntArrayOf5()
        self.assertEqual(len(v), 5)
        self.assertEqual(v[0], 0)
        self.assertEqual(v[1], 1)
        self.assertEqual(v[2], 4)
        self.assertEqual(v[3], 9)
        self.assertEqual(v[4], 16)

        v = o.nullIntArrayOf5()
        self.assertEqual(v, objc.NULL)

    def testSizeInArgument(self):
        o = OC_MetaDataTest.new()
        v = o.makeIntArrayOf_(3)
        self.assertEqual(len(v), 3)
        self.assertEqual(v[0], 0)
        self.assertEqual(v[1], 1)
        self.assertEqual(v[2], 8)

        v = o.makeIntArrayOf_(10)
        self.assertEqual(len(v), 10)
        for i in range(10):
            self.assertEqual(v[i], i ** 3)

        v = o.nullIntArrayOf_(100)
        self.assertEqual(v, objc.NULL)

    def testNULLterminated(self):
        o = OC_MetaDataTest.new()

        v = o.makeStringArray()
        self.assertEqual(len(v), 4)
        self.assertEqual(list(v), [b"hello", b"world", b"out", b"there"])

        v = o.nullStringArray()
        self.assertEqual(v, objc.NULL)


class TestByReference(TestCase):
    # Pass by reference arguments.
    # Note that these tests aren't exhaustive, we have test_methods and
    # test_methods2 for that :-)

    def testInput(self):
        o = OC_MetaDataTest.new()

        r = o.sumX_andY_(1, 2)
        self.assertEqual(r, 1 + 2)

        r = o.sumX_andY_(2535, 5325)
        self.assertEqual(r, 2535 + 5325)

        self.assertRaises(ValueError, o.sumX_andY_, 42, objc.NULL)

    def testOutput(self):
        o = OC_MetaDataTest.new()

        div, rem = o.divBy5_remainder_(55, None)
        self.assertEqual(div, 11)
        self.assertEqual(rem, 0)

        div, rem = o.divBy5_remainder_(13, None)
        self.assertEqual(div, 2)
        self.assertEqual(rem, 3)

        self.assertRaises(ValueError, o.divBy5_remainder_, 42, objc.NULL)

    def testInputOutput(self):
        o = OC_MetaDataTest.new()
        x, y = o.swapX_andY_(42, 284)
        self.assertEqual(x, 284)
        self.assertEqual(y, 42)

        self.assertRaises(ValueError, o.swapX_andY_, 42, objc.NULL)

    def testNullAccepted(self):
        o = OC_MetaDataTest.new()

        def makeNum(value):
            return int(value, 0)

        # All arguments present
        r, y, z = o.input_output_inputAndOutput_(1, None, 2)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(None, map(makeNum, r)))), 3)
        self.assertEqual(y, 3)
        self.assertEqual(z, -1)

        r, y, z = o.input_output_inputAndOutput_(1, None, 2)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(None, map(makeNum, r)))), 3)
        self.assertEqual(y, 3)
        self.assertEqual(z, -1)

        # Argument 1 is NULL
        r, y, z = o.input_output_inputAndOutput_(objc.NULL, None, 2)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(None, map(makeNum, r)))), 2)
        self.assertEqual(y, 40)
        self.assertEqual(z, -2)

        r, y, z = o.input_output_inputAndOutput_(objc.NULL, None, 2)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(None, map(makeNum, r)))), 2)
        self.assertEqual(y, 40)
        self.assertEqual(z, -2)

        # Argument 2 is NULL
        r, y, z = o.input_output_inputAndOutput_(1, objc.NULL, 2)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(None, map(makeNum, r)))), 2)
        self.assertEqual(y, objc.NULL)
        self.assertEqual(z, -1)

        # Argument 3 is NULL
        r, y, z = o.input_output_inputAndOutput_(1, None, objc.NULL)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(None, map(makeNum, r)))), 2)
        self.assertEqual(y, 43)
        self.assertEqual(z, objc.NULL)

        r, y, z = o.input_output_inputAndOutput_(1, None, objc.NULL)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(None, map(makeNum, r)))), 2)
        self.assertEqual(y, 43)
        self.assertEqual(z, objc.NULL)


class TestPrintfFormat(TestCase):
    def test_nsformat(self):
        o = OC_MetaDataTest.new()

        v = o.makeArrayWithFormat_("%3d", 10)
        self.assertEqual(list(v), ["%3d", " 10"])

        v = o.makeArrayWithFormat_("%s", b"foo")
        self.assertEqual(list(v), ["%s", "foo"])

        v = o.makeArrayWithFormat_("hello %s", b"world")
        self.assertEqual(list(v), ["hello %s", "hello world"])

        v = o.makeArrayWithFormat_("hello %s", b"world")
        self.assertEqual(list(v), ["hello %s", "hello world"])

        self.assertRaises(ValueError, o.makeArrayWithFormat_, "%s")

    def test_cformat(self):
        o = OC_MetaDataTest.new()

        with self.subTest("%3d"):
            v = o.makeArrayWithCFormat_(b"%3d", 10)
            self.assertEqual(list(v), ["%3d", " 10"])

        with self.subTest("hello %s"):
            v = o.makeArrayWithCFormat_(b"hello %s", b"world")
            self.assertEqual(list(v), ["hello %s", "hello world"])

        with self.subTest("hello %s x %d"):
            v = o.makeArrayWithCFormat_(b"hello %s x %d", b"world", 42)
            self.assertEqual(list(v), ["hello %s x %d", "hello world x 42"])

        # As we implement a format string parser we'd better make sure that
        # that code is correct...

        # Generic table below doesn't work for these
        for fmt, args in [(b"%#+x", (99,)), (b"%+#x", (99,)), (b"% #x", (99,))]:
            with self.subTest((fmt, args)):
                v = o.makeArrayWithCFormat_(fmt, *args)
                self.assertEqual(list(v), [fmt.decode(), ((fmt % args)[1:]).decode()])

        # Insert thousands seperator, the one in the C locale is ''
        with self.subTest("%'d"):
            v = o.makeArrayWithCFormat_(b"%'d", 20000)
            self.assertEqual(list(v), ["%'d", "20000"])

        with self.subTest("%hhd"):
            v = o.makeArrayWithCFormat_(b"%hhd", 20)
            self.assertEqual(list(v), ["%hhd", "20"])

        with self.subTest("%lld, 20"):
            v = o.makeArrayWithCFormat_(b"%lld", 20)
            self.assertEqual(list(v), ["%lld", "20"])

        with self.subTest("%lld, -20"):
            v = o.makeArrayWithCFormat_(b"%lld", -20)
            self.assertEqual(list(v), ["%lld", "-20"])

        with self.subTest("%zd"):
            v = o.makeArrayWithCFormat_(b"%zd", 20)
            self.assertEqual(list(v), ["%zd", "20"])

        with self.subTest("%td"):
            v = o.makeArrayWithCFormat_(b"%td", 20)
            self.assertEqual(list(v), ["%td", "20"])

        with self.subTest("%qd, 20"):
            v = o.makeArrayWithCFormat_(b"%qd", 20)
            self.assertEqual(list(v), ["%qd", "20"])

        with self.subTest("%qd, -20"):
            v = o.makeArrayWithCFormat_(b"%qd", -20)
            self.assertEqual(list(v), ["%qd", "-20"])

        with self.subTest("%D"):
            v = o.makeArrayWithCFormat_(b"%D", -20)
            self.assertEqual(list(v), ["%D", "-20"])

        with self.subTest("%O"):
            v = o.makeArrayWithCFormat_(b"%O", 8)
            self.assertEqual(list(v), ["%O", "10"])

        with self.subTest("%U"):
            v = o.makeArrayWithCFormat_(b"%U", 8)
            self.assertEqual(list(v), ["%U", "8"])

        with self.subTest("%p"):
            obj = object()
            v = o.makeArrayWithCFormat_(b"%p", obj)
            self.assertEqual(list(v), ["%p", "%#x" % (id(obj),)])

        with self.subTest("%lc%lc"):
            v = o.makeArrayWithCFormat_(b"%lc%lc", "d", "e")
            self.assertEqual(list(v), ["%lc%lc", "de"])

        with self.subTest("%C"):
            v = o.makeArrayWithCFormat_(b"%C", "A")
            self.assertEqual(list(v), ["%C", "A"])

        with self.subTest("%C%C%c"):
            v = o.makeArrayWithCFormat_(b"%C%C%c", "A", 90, "b")
            self.assertEqual(list(v), ["%C%C%c", "A%cb" % (90,)])

        with self.subTest("%S"):
            v = o.makeArrayWithCFormat_(b"%S", "hello world")
            self.assertEqual(list(v), ["%S", "hello world"])
            v = o.makeArrayWithCFormat_(b"%S", "hello world")
            self.assertEqual(list(v), ["%S", "hello world"])

        with self.subTest("%ls"):
            v = o.makeArrayWithCFormat_(b"%ls", "hello world")
            self.assertEqual(list(v), ["%ls", "hello world"])
            v = o.makeArrayWithCFormat_(b"%ls", "hello world")
            self.assertEqual(list(v), ["%ls", "hello world"])

        TEST_TAB = [
            (b"% #d", (99,)),
            (b"%0#4x", (99,)),
            (b"%#+d", (99,)),
            (b"%+#d", (99,)),
            (b"%o", (20,)),
            (b"%10o", (9,)),
            (b"%d %.*o", (2, 5, 7)),
            (b"%*o", (5, 7)),
            (b"%.*o", (5, 7)),
            (b"%.*f", (3, 0.23424)),
            (b"%*.*f", (12, 3, 0.23424)),
            (b"%F", (-4.6,)),
            (b"%f", (2.7,)),
            (b"%e", (2.7,)),
            (b"%E", (-4.6,)),
            (b"%g", (2.7,)),
            (b"%G", (-4.6,)),
            (b"%.9f", (0.249,)),
            (b"%ld", (42,)),
            (b"%c", (42,)),
            (b"%hd", (42,)),
            (b"%lx", (42,)),
            (b"%%%d%%", (99,)),
            (b"%c", ("a",)),
            (b"%c%c", ("c", "d")),
            (b"%c%c", (90, "d")),
            (b"%f %f %f %f %f %f %f %f", (1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5))
            # We don't have long double support at all
            # ( '%Lg', (42.0,)),
        ]

        for fmt, args in TEST_TAB:
            with self.subTest((fmt, args)):
                v = o.makeArrayWithCFormat_(fmt, *args)
                self.assertEqual(list(v), [fmt.decode(), fmt.decode() % args])


class TestVariadic(TestCase):
    def testRaises(self):
        o = OC_MetaDataTest.new()

        self.assertRaises(TypeError, o.varargsMethodWithObjects_, 1)
        self.assertRaises(TypeError, o.varargsMethodWithObjects_, 1, 2, 3)


class TestIgnore(TestCase):
    def testRaises(self):
        o = OC_MetaDataTest.new()

        self.assertRaises(TypeError, o.ignoreMethod)

    def testClassmethods(self):
        self.assertResultIsBOOL(OC_MetaDataTest.boolClassMethod)


class TestMetaDataAccess(TestCase):
    def testNew(self):
        self.assertResultIsRetained(OC_MetaDataTest.new)

    def testSuggestions(self):
        meta = OC_MetaDataTest.varargsMethodWithObjects_.__metadata__()
        self.assertIsInstance(meta, dict)
        self.assertIn("suggestion", meta)
        self.assertEqual(
            meta["suggestion"], "Variadic functions/methods are not supported"
        )

        meta = OC_MetaDataTest.ignoreMethod.__metadata__()
        self.assertIsInstance(meta, dict)
        self.assertIn("suggestion", meta)
        self.assertEqual(meta["suggestion"], "please ignore me")

    def testPrintfFormat(self):
        meta = OC_MetaDataTest.makeArrayWithFormat_.__metadata__()
        self.assertEqual(meta.get("variadic", False), True)
        self.assertNotIn("printf_format", meta["arguments"][0])
        self.assertEqual(meta["arguments"][2]["printf_format"], True)

    def testVariadic(self):
        meta = OC_MetaDataTest.makeArrayWithFormat_.__metadata__()
        self.assertEqual(meta.get("variadic", False), True)

        meta = OC_MetaDataTest.ignoreMethod.__metadata__()
        self.assertEqual(meta.get("variadic", False), False)

    def testTypes(self):
        meta = OC_MetaDataTest.ignoreMethod.__metadata__()
        self.assertEqual(meta["retval"]["type"], objc._C_INT)
        self.assertEqual(meta["arguments"][0]["type"], objc._C_ID)
        self.assertEqual(meta["arguments"][1]["type"], objc._C_SEL)

        meta = OC_MetaDataTest.make4Tuple_.__metadata__()
        self.assertEqual(meta["retval"]["type"], objc._C_ID)
        self.assertEqual(meta["arguments"][0]["type"], objc._C_ID)
        self.assertEqual(meta["arguments"][1]["type"], objc._C_SEL)
        self.assertEqual(
            meta["arguments"][2]["type"], objc._C_IN + objc._C_PTR + objc._C_DBL
        )

    def testAllowNull(self):
        meta = OC_MetaDataTest.make4Tuple_.__metadata__()
        self.assertNotIn("null_accepted", meta["retval"])
        self.assertNotIn("null_accepted", meta["arguments"][0])

        meta = OC_MetaDataTest.make4Tuple_.__metadata__()
        self.assertEqual(meta["arguments"][2]["null_accepted"], False)

        meta = OC_MetaDataTest.null4Tuple_.__metadata__()
        self.assertEqual(meta["arguments"][2]["null_accepted"], True)

    def alreadyRetained(self):
        meta = OC_MetaDataTest.null4Tuple_.__metadata__()
        self.assertEqual(meta["already_retained"], False)

        meta = OC_MetaDataTest.alloc.__metadata__()
        self.assertEqual(meta["already_retained"], True)

    def testClassMethod(self):
        meta = OC_MetaDataTest.alloc.__metadata__()
        self.assertEqual(meta["classmethod"], True)

        meta = OC_MetaDataTest.pyobjc_instanceMethods.init.__metadata__()
        self.assertEqual(meta["classmethod"], False)


def buffer_as_bytes(v):
    if isinstance(v, bytes):
        return v
    return bytes(v)


class TestBuffers(TestCase):
    # Some tests that check if buffer APIs get sane treatment

    def testInChars(self):
        o = OC_MetaDataTest.alloc().init()

        v = o.makeDataForBytes_count_(b"hello world", len(b"hello world"))
        self.assertIsInstance(v, objc.lookUpClass("NSData"))

        self.assertEqual(v.length(), len(b"hello world"))
        self.assertEqual(buffer_as_bytes(v), b"hello world")

        v = o.makeDataForBytes_count_(b"hello\0world", len(b"hello\0world"))
        self.assertIsInstance(v, objc.lookUpClass("NSData"))

        self.assertEqual(v.length(), len(b"hello\0world"))
        self.assertEqual(buffer_as_bytes(v), b"hello\0world")

        a = make_array("b", b"foobar monday")
        v = o.makeDataForBytes_count_(a, len(a))
        self.assertIsInstance(v, objc.lookUpClass("NSData"))

        self.assertEqual(v.length(), len(a))
        self.assertEqual(buffer_as_bytes(v), buffer_as_bytes(a))

    def testInVoids(self):
        o = OC_MetaDataTest.alloc().init()

        v = o.makeDataForBytes_count_(b"hello world", len(b"hello world"))
        self.assertIsInstance(v, objc.lookUpClass("NSData"))

        self.assertEqual(v.length(), len(b"hello world"))
        self.assertEqual(buffer_as_bytes(v), b"hello world")

        v = o.makeDataForBytes_count_(b"hello\0world", len(b"hello\0world"))
        self.assertIsInstance(v, objc.lookUpClass("NSData"))

        self.assertEqual(v.length(), len(b"hello\0world"))
        self.assertEqual(buffer_as_bytes(v), b"hello\0world")

        a = make_array("b", b"foobar monday")
        v = o.makeDataForBytes_count_(a, len(a))
        self.assertIsInstance(v, objc.lookUpClass("NSData"))

        self.assertEqual(v.length(), len(a))
        self.assertEqual(buffer_as_bytes(v), buffer_as_bytes(a))

    def testInOutChars(self):
        o = OC_MetaDataTest.alloc().init()

        input_value = b"hello " + b"world"
        v = o.addOneToBytes_count_(input_value, len(input_value))
        self.assertIsInstance(v, bytes)

        self.assertEqual(input_value, b"hello world")
        self.assertEqual(input_value[0:5], b"hello")
        self.assertEqual([x + 1 for x in input_value], list(v))

        input_value = make_array("b", b"hello\0world")
        v = o.addOneToBytes_count_(input_value, len(input_value))
        self.assertIs(v, input_value)
        self.assertNotEqual(input_value[0:5], b"hello")
        self.assertEqual([x + 1 for x in b"hello\0world"], list(v))

    def testInOutVoids(self):
        o = OC_MetaDataTest.alloc().init()

        input_value = b"hello " + b"world"
        v = o.addOneToVoids_count_(input_value, len(input_value))
        self.assertIsInstance(v, type(b""))

        self.assertEqual(input_value, b"hello world")
        self.assertEqual(input_value[0:5], b"hello")

        self.assertEqual([x + 2 for x in input_value], list(v))

        input_value = make_array("b", b"hello\0world")
        v = o.addOneToVoids_count_(input_value, len(input_value))
        self.assertIs(v, input_value)
        self.assertNotEqual(input_value[0:5], b"hello")
        self.assertEqual([x + 2 for x in b"hello\0world"], list(v))

    def testOutChars(self):
        o = OC_MetaDataTest.alloc().init()

        v = o.fillBuffer_count_(None, 44)
        self.assertEqual(v, b"\xfe" * 44)

        a = make_array("b", b"0" * 44)
        v = o.fillBuffer_count_(a, 44)
        self.assertEqual(buffer_as_bytes(v), b"\xfe" * 44)
        self.assertIs(v, a)

    def testOutVoids(self):
        o = OC_MetaDataTest.alloc().init()

        v = o.fillVoids_count_(None, 44)
        self.assertEqual(v, b"\xab" * 44)

        a = make_array("b", (0,) * 44)
        v = o.fillVoids_count_(a, 44)
        self.assertEqual(buffer_as_bytes(v), b"\xab" * 44)
        self.assertIs(v, a)


class TestVariableLengthValue(TestCase):
    def testResult(self):
        o = OC_MetaDataTest.alloc().init()

        v = o.unknownLengthArray()
        self.assertIsInstance(v, objc.varlist)
        self.assertEqual(v.__typestr__, objc._C_INT)

        self.assertEqual(v[0], 1)
        self.assertEqual(v[1], 3)
        self.assertEqual(v[5], 13)

        # self.fail((type(v), v))
        # self.fail((v[0:2], type(v[0:2])))
        self.assertEqual(v[0:2], (1, 3))

        self.assertEqual(v.as_tuple(5), (1, 3, 5, 7, 11))
        self.assertEqual(v.as_tuple(0), ())
        self.assertEqual(v.as_tuple(8), (1, 3, 5, 7, 11, 13, 17, 19))

        v = o.unknownLengthMutable()
        self.assertIsInstance(v, objc.varlist)

        v[1] = 42
        self.assertEqual(v[1], 42)
        v[0:10] = range(10)
        self.assertEqual(v[0], 0)
        self.assertEqual(v[5], 5)
        self.assertEqual(v[8], 8)

        data = v.as_buffer(4)
        self.assertEqual(data[0], 0)
        v[0] = 0x0F0F0F0F
        self.assertEqual(data[0], 0x0F)
        data[0] = 0

        if sys.byteorder == "little":
            self.assertEqual(v[0], 0x0F0F0F00)

        else:
            self.assertEqual(v[0], 0x000F0F0F)

    def testInput(self):
        o = OC_MetaDataTest.alloc().init()

        v = o.makeIntArray_halfCount_((1, 2, 3, 4, 5, 6), 2)
        self.assertEqual(list(v), [1, 2, 3, 4])

        # XXX: Hard crash when using o.makeVariableLengthArray_halfCount_???


class TestVariadicArray(TestCase):
    def testObjects(self):
        o = OC_MetaDataTest.alloc().init()

        v = o.makeArrayWithArguments_()
        self.assertEqual(v, [])

        v = o.makeArrayWithArguments_(1, 2, 3)
        self.assertEqual(v, [1, 2, 3])

        v = o.makeArrayWithArguments_(4, None, 5)
        self.assertEqual(v, [4])

        v = o.makeArrayWithArguments_(*range(40))
        self.assertEqual(v, list(range(40)))
