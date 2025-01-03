"""
Tests for the new-style metadata format interface.

Note: Tests for calling from python into ObjC are in test_metadata.py

TODO:
- Add more testcases: python methods that return the wrong value
- The python->C interface (that is the contents of the metadata object) is
  likely to change when the bridge is feature-complete.
- Probably need special-casing for arrays (numarray and array.array)!
"""

import warnings
import objc

# To ensure we have the right metadata
import PyObjCTest.test_metadata  # noqa: F401
from PyObjCTest.metadata import OC_MetaDataTest
from PyObjCTools.TestSupport import TestCase
from .fnd import NSArray, NSObject
from objc import super  # noqa: A004
from .test_metadata import NoObjCClass


def setupMetaData():
    # Note to self: what we think of as the first argument of a method is
    # actually the third one, the objc runtime implicitly passed 'self' and
    # the selector as well. Therefore we need to start counting at 2 instead
    # of 0.
    #
    # Note2: the code below would normally be done using a metadata file
    # instead of hardcoding.

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"retainedObjCObject",
        {
            "retval": {
                "already_retained": True,
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"retainedObjCObjectOn:",
        {
            "retval": {
                "already_retained": True,
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"retainedCFObject",
        {
            "retval": {
                "already_cfretained": True,
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"retainedCFObjectOn:",
        {
            "retval": {
                "already_cfretained": True,
            }
        },
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"charpArgPlain:",
        {
            "arguments": {
                2
                + 0: {
                    "type": objc._C_CHARPTR,
                }
            }
        },
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"charpArgNullTerminated:",
        {
            "arguments": {
                2
                + 0: {
                    "type": objc._C_CHARPTR,
                    "c_array_delimited_by_null": True,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"charpArg5Chars:",
        {
            "arguments": {
                2
                + 0: {
                    "type": objc._C_CHARPTR,
                    "c_array_of_fixed_length": 5,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"charpArgVariadic:",
        {
            "arguments": {
                2
                + 0: {
                    "type": objc._C_CHARPTR,
                    "c_array_of_variable_length": True,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"charpArgDeref:",
        {
            "arguments": {
                2
                + 0: {
                    "type": objc._C_CHARPTR,
                    "deref_result_pointer": True,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"charpArgCounted:count:",
        {
            "arguments": {
                2
                + 0: {
                    "type": objc._C_CHARPTR,
                    "c_array_length_in_arg": 3,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"charpArgCounted:floatcount:",
        {
            "arguments": {
                2
                + 0: {
                    "type": objc._C_CHARPTR,
                    "c_array_length_in_arg": 3,
                }
            }
        },
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"make4Tuple:on:",
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
        b"null4Tuple:on:",
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
        b"makeObjectArray:on:",
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
        b"makeStringArray:on:",
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
        b"nullStringArray:on:",
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
        b"makeIntArray:count:on:",
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
        b"makeIntArray:countPtr:on:",
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
        b"nullIntArray:count:on:",
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
        b"fillArray:uptoCount:on:",
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
        b"fillArray:count:on:",
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
        b"nullfillArray:count:on:",
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
        b"maybeFillArray:on:",
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
        b"fill4Tuple:on:",
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
        b"nullfill4Tuple:on:",
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
        b"fillStringArray:on:",
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
        b"nullfillStringArray:on:",
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
        b"reverseArray:uptoCount:on:",
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
        b"reverseArray:count:on:",
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
        b"nullreverseArray:count:on:",
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
        b"reverseStrings:on:",
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
        b"nullreverseStrings:on:",
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
        b"maybeReverseArray:on:",
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_INOUT,
                    "c_array_of_fixed_length": 4,
                    "c_array_length_in_result": True,
                    "null_accepted": True,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"reverse4Tuple:on:",
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
        b"nullreverse4Tuple:on:",
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
        b"returnPointerFixedLen",
        {"retval": {"c_array_of_fixed_length": 5}},
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"returnCharPFixedLen",
        {"retval": {"c_array_of_fixed_length": 5}},
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"returnPointerVariadic",
        {"retval": {"c_array_of_variable_length": True}},
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"returnPointerNullDelimited",
        {"retval": {"c_array_delimited_by_null": True}},
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"returnCharPNullDelimited",
        {"retval": {"c_array_delimited_by_null": True}},
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"returnPointerCounted:",
        {"retval": {"c_array_length_in_arg": 2}},
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"returnPointerFloatCounted:",
        {"retval": {"c_array_length_in_arg": 2}},
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"returnPointerCountedIn:",
        {
            "retval": {"c_array_length_in_arg": 2},
            "arguments": {2: {"type_modifier": "n"}},
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"returnPointerCountedOut:",
        {
            "retval": {"c_array_length_in_arg": 2},
            "arguments": {2: {"type_modifier": "o"}},
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"returnPointerCountedInOut:",
        {
            "retval": {"c_array_length_in_arg": 2},
            "arguments": {2: {"type_modifier": "N"}},
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"returnPointerDeref",
        {"retval": {"deref_result_pointer": True}},
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"returnPointerToFree",
        {"retval": {"c_array_of_fixed_length": 4, "free_result": True}},
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"returnPointerToFreeVariadic",
        {"retval": {"c_array_of_variable_length": True, "free_result": True}},
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"makeIntArrayOf5On:",
        {"retval": {"c_array_of_fixed_length": 5}},
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"makeStringArrayOn:",
        {"retval": {"c_array_delimited_by_null": True}},
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"makeIntArrayOf:on:",
        {"retval": {"c_array_length_in_arg": 2 + 0}},
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"returnPointerFixedLenOn:",
        {"retval": {"c_array_of_fixed_length": 5}},
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"returnCharPFixedLenOn:",
        {"retval": {"c_array_of_fixed_length": 5}},
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"returnPointerVariadicOn:",
        {"retval": {"c_array_of_variable_length": True}},
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"returnPointerNullDelimitedOn:",
        {"retval": {"c_array_delimited_by_null": True}},
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"returnPointerCounted:on:",
        {"retval": {"c_array_length_in_arg": 2}},
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"returnPointerFloatCounted:on:",
        {"retval": {"c_array_length_in_arg": 2}},
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"returnPointerCountedIn:on:",
        {
            "retval": {"c_array_length_in_arg": 2},
            "arguments": {2: {"type_modifier": "n"}},
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"returnPointerCountedOut:on:",
        {
            "retval": {"c_array_length_in_arg": 2},
            "arguments": {2: {"type_modifier": "o"}},
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"returnPointerCountedInOut:on:",
        {
            "retval": {"c_array_length_in_arg": 2},
            "arguments": {2: {"type_modifier": "N"}},
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"returnPointerDerefOn:",
        {"retval": {"deref_result_pointer": True}},
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"returnPointerToFreeOn:",
        {"retval": {"c_array_of_fixed_length": 4}},
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"returnPointerToFreeVariadicOn:",
        {"retval": {"c_array_of_variable_length": True}},
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"nullIntArrayOf5On:",
        {"retval": {"c_array_of_fixed_length": 5}},
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"nullStringArrayOn:",
        {"retval": {"c_array_delimited_by_null": True}},
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"nullIntArrayOf:on:",
        {"retval": {"c_array_length_in_arg": 2 + 0}},
    )

    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"sumX:andY:on:",
        {
            "arguments": {
                2 + 0: {"type_modifier": objc._C_IN, "null_accepted": False},
                2 + 1: {"type_modifier": objc._C_IN, "null_accepted": False},
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"divBy5:remainder:on:",
        {"arguments": {2 + 1: {"type_modifier": objc._C_OUT, "null_accepted": False}}},
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"swapX:andY:on:",
        {
            "arguments": {
                2 + 0: {"type_modifier": objc._C_INOUT, "null_accepted": False},
                2 + 1: {"type_modifier": objc._C_INOUT, "null_accepted": False},
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_MetaDataTest",
        b"input:output:inputAndOutput:on:",
        {
            "arguments": {
                2 + 0: {"type_modifier": objc._C_IN, "null_accepted": True},
                2 + 1: {"type_modifier": objc._C_OUT, "null_accepted": True},
                2 + 2: {"type_modifier": objc._C_INOUT, "null_accepted": True},
            }
        },
    )

    for pfx in (b"void", b"int"):
        for sfx in (b"CharPtr", b"Id"):
            objc.registerMetaDataForSelector(
                b"OC_MetaDataTest",
                b"%sOut%s:" % (pfx, sfx),
                {
                    "arguments": {
                        2: {"type_modifier": objc._C_OUT},
                    }
                },
            )
            objc.registerMetaDataForSelector(
                b"OC_MetaDataTest",
                b"%sOut%s:on:" % (pfx, sfx),
                {
                    "arguments": {
                        2: {"type_modifier": objc._C_OUT},
                    }
                },
            )

        objc.registerMetaDataForSelector(
            b"OC_MetaDataTest",
            b"%sOutChar:" % (pfx,),
            {
                "arguments": {
                    2: {"type_modifier": objc._C_OUT, "type": b"*"},
                }
            },
        )
        objc.registerMetaDataForSelector(
            b"OC_MetaDataTest",
            b"%sOutChar:on:" % (pfx,),
            {
                "arguments": {
                    2: {"type_modifier": objc._C_OUT, "type": b"*"},
                }
            },
        )

        objc.registerMetaDataForSelector(
            b"OC_MetaDataTest",
            b"%sOutIdRetained:" % (pfx,),
            {
                "arguments": {
                    2: {"type_modifier": objc._C_OUT, "already_retained": True},
                }
            },
        )
        objc.registerMetaDataForSelector(
            b"OC_MetaDataTest",
            b"%sOutIdRetained:on:" % (pfx,),
            {
                "arguments": {
                    2: {"type_modifier": objc._C_OUT, "already_retained": True},
                }
            },
        )
        objc.registerMetaDataForSelector(
            b"OC_MetaDataTest",
            b"%sOutIdCFRetained:" % (pfx,),
            {
                "arguments": {
                    2: {"type_modifier": objc._C_OUT, "already_cfretained": True},
                }
            },
        )
        objc.registerMetaDataForSelector(
            b"OC_MetaDataTest",
            b"%sOutIdCFRetained:on:" % (pfx,),
            {
                "arguments": {
                    2: {"type_modifier": objc._C_OUT, "already_cfretained": True},
                }
            },
        )

        objc.registerMetaDataForSelector(
            b"OC_MetaDataTest",
            b"%sOutInt:add:" % (pfx,),
            {
                "arguments": {
                    2: {"type_modifier": objc._C_OUT},
                }
            },
        )
        objc.registerMetaDataForSelector(
            b"OC_MetaDataTest",
            b"%sOutInt:add:on:" % (pfx,),
            {
                "arguments": {
                    2: {"type_modifier": objc._C_OUT},
                }
            },
        )


setupMetaData()


class Py_MetaDataTest_AllArgs_Invalid(OC_MetaDataTest):
    # Return value arrays:
    def makeIntArrayOf5(self):
        return [100, 200, 300]

    def makeStringArray(self):
        return 42

    def makeIntArrayOf_(self, count):
        return [i + 20 for i in range(count * 2)]


class Py_MetaDataTest_AllArgs(OC_MetaDataTest):
    # Return value arrays:
    def makeIntArrayOf5(self):
        return [100, 200, 300, 400, 500]

    def makeStringArray(self):
        return [b"jaap", b"pieter", b"hans"]

    def makeIntArrayOf_(self, count):
        return [i + 20 for i in range(count)]

    def nullIntArrayOf5(self):
        return objc.NULL

    def nullStringArray(self):
        return objc.NULL

    def nullIntArrayOf_(self, count):
        return objc.NULL

    # In arrays:
    def makeIntArray_count_(self, data, count):
        return [data, count]

    def makeIntArray_countPtr_(self, data, count):
        return [data, count]

    def nullIntArray_count_(self, data, count):
        return [data, count]

    def makeStringArray_(self, data):
        return [[x.decode("latin1") for x in data]]

    def makeObjectArray_(self, data):
        return [data]

    def nullStringArray_(self, data):
        return [data]

    def make4Tuple_(self, data):
        return [data]

    def null4Tuple_(self, data):
        return [data]

    # Out arrays:
    def fillArray_count_(self, data, count):
        if data is None:
            return range(10, count + 10)
        else:
            return range(20, count + 20)

    def nullfillArray_count_(self, data, count):
        if data is objc.NULL:
            return 1, None

        elif data is None:
            return 2, range(30, count + 30)

        else:
            return 3, range(40, count + 40)

    def fill4Tuple_(self, data):
        if data is None:
            return range(9, 13)
        else:
            return range(14, 18)

    def nullfill4Tuple_(self, data):
        if data is None:
            return 1, range(1, 5)
        elif data is objc.NULL:
            return 2, range(6, 10)
        else:
            return 3, range(100, 104)

    def fillArray_uptoCount_(self, data, count):
        if data is None:
            return int(count / 2), range(10, 10 + int(count / 2))
        else:
            return int(count / 2), range(15, 15 + int(count / 2))

    def maybeFillArray_(self, data):
        if data is None:
            return 2, range(2)
        else:
            return 2, range(2, 4)

    def fillStringArray_(self, data):
        raise RuntimeError("Should not reach this")

    def nullfillStringArray_(self, data):
        if data is objc.NULL:
            return 9, objc.NULL

        raise RuntimeError("Should not reach this")

    # In/out arrays:
    def reverseArray_count_(self, data, count):
        if count == len(data):
            x = 1
        else:
            x = 2

        data = list(data)
        for i in range(len(data)):
            data[i] += x

        return data

    def nullreverseArray_count_(self, data, count):
        if data is objc.NULL:
            return 2, objc.NULL

        else:
            data = list(data)
            for i in range(len(data)):
                data[i] += 42
            return 9, data

    def reverseStrings_(self, data):
        data = list(data)
        for i in range(len(data)):
            data[i] = data[i][::-1]
        return data

    def nullreverseStrings_(self, data):
        if data is objc.NULL:
            return 9, objc.NULL

        else:
            data = list(data)
            for i in range(len(data)):
                data[i] = data[i][::-1]
            return 10, data

    def reverse4Tuple_(self, data):
        data = list(data)
        for i in range(len(data)):
            data[i] += 42
        return data

    def nullreverse4Tuple_(self, data):
        if data is objc.NULL:
            return -1, objc.NULL

        else:
            data = list(data)
            for i in range(len(data)):
                data[i] += 42
            return 1, data

    def reverseArray_uptoCount_(self, data, count):
        data = list(data)
        for i in range(int(len(data) / 2)):
            data[i] = data[i] * 10

        return count / 2, data

    def maybeReverseArray_(self, data):
        return 2, (data[0] + 44, data[1] + 49)

    # pass-by-reference
    def sumX_andY_(self, x, y):
        return x**2 + y**2

    def divBy5_remainder_(self, v, r):
        if r is None:
            return v / 7, v % 7
        else:
            return v / 9, v % 9

    def swapX_andY_(self, x, y):
        return y * 2, x * 2

    def input_output_inputAndOutput_(self, x, y, z):
        if x is not objc.NULL and y is not objc.NULL and z is not objc.NULL:
            return [x, y, z], 9, 10

        elif x is objc.NULL:
            return [x, y, z], 11, 12

        elif y is objc.NULL:
            return [x, y, z], 13, 14

        elif z is objc.NULL:
            return [x, y, z], 15, 16


class TestArrayDefault(TestCase):
    # TODO: what is the default anyway?
    pass


class TestArraysOut(TestCase):
    def testFixedSize(self):
        o = Py_MetaDataTest_AllArgs.new()

        v = OC_MetaDataTest.fill4Tuple_on_(None, o)
        self.assertEqual(list(v), list(range(9, 13)))

        v = OC_MetaDataTest.fill4Tuple_on_(None, o)
        self.assertEqual(list(v), list(range(9, 13)))

        with self.assertRaisesRegex(ValueError, "argument 0 isn't allowed to be NULL"):
            OC_MetaDataTest.fill4Tuple_on_(objc.NULL, o)

        n, v = OC_MetaDataTest.nullfill4Tuple_on_(None, o)
        self.assertEqual(n, 1)
        self.assertEqual(list(v), list(range(1, 5)))

        n, v = OC_MetaDataTest.nullfill4Tuple_on_(None, o)
        self.assertEqual(n, 1)
        self.assertEqual(list(v), list(range(1, 5)))

        n, v = OC_MetaDataTest.nullfill4Tuple_on_(objc.NULL, o)
        self.assertEqual(n, 2)
        self.assertIs(v, objc.NULL)

    def testNullTerminated(self):
        o = Py_MetaDataTest_AllArgs.new()

        # Output only arrays of null-terminated arrays cannot be
        # wrapped automaticly. How is the bridge supposed to know
        # how much memory it should allocate for the C-array?
        with self.assertRaisesRegex(
            TypeError, "NULL-terminated 'out' arguments are not supported"
        ):
            OC_MetaDataTest.fillStringArray_on_(None, o)
        with self.assertRaisesRegex(ValueError, "argument 0 isn't allowed to be NULL"):
            OC_MetaDataTest.fillStringArray_on_(objc.NULL, o)

        with self.assertRaisesRegex(TypeError, "Need 2 arguments, got 1"):
            OC_MetaDataTest.nullfillStringArray_on_(o)
        with self.assertRaisesRegex(
            TypeError, "NULL-terminated 'out' arguments are not supported"
        ):
            OC_MetaDataTest.nullfillStringArray_on_(None, o)
        n, v = OC_MetaDataTest.nullfillStringArray_on_(objc.NULL, o)
        self.assertEqual(n, 9)
        self.assertIs(v, objc.NULL)

    def testWithCount(self):
        o = Py_MetaDataTest_AllArgs.new()

        v = OC_MetaDataTest.fillArray_count_on_(None, 3, o)
        self.assertEqual(list(v), [10, 11, 12])

        v = OC_MetaDataTest.fillArray_count_on_(None, 5, o)
        self.assertEqual(list(v), [10, 11, 12, 13, 14])

        v = OC_MetaDataTest.fillArray_count_on_(None, 0, o)
        self.assertEqual(list(v), [])

        with self.assertRaisesRegex(ValueError, "argument 0 isn't allowed to be NULL"):
            OC_MetaDataTest.fillArray_count_on_(objc.NULL, 0, o)

        n, v = OC_MetaDataTest.nullfillArray_count_on_(None, 3, o)
        self.assertEqual(n, 2)
        self.assertEqual(list(v), [30, 31, 32])

        n, v = OC_MetaDataTest.nullfillArray_count_on_(objc.NULL, 3, o)
        self.assertEqual(n, 1)
        self.assertIs(v, objc.NULL)

    def testWithCountInResult(self):
        o = Py_MetaDataTest_AllArgs.new()

        c, v = OC_MetaDataTest.fillArray_uptoCount_on_(None, 20, o)
        self.assertEqual(c, 10)
        self.assertEqual(list(v), [i + 10 for i in range(10)])

        c, v = OC_MetaDataTest.maybeFillArray_on_(None, o)
        self.assertEqual(c, 2)
        self.assertEqual(list(v), [0, 1])


class TestArraysInOut(TestCase):
    def testFixedSize(self):
        o = Py_MetaDataTest_AllArgs.new()

        a = (1, 2, 3, 4)
        v = OC_MetaDataTest.reverse4Tuple_on_(a, o)
        self.assertEqual(a, (1, 2, 3, 4))
        self.assertEqual(v, (43, 44, 45, 46))

        with self.assertRaisesRegex(ValueError, "expecting 4 values got 3"):
            OC_MetaDataTest.reverse4Tuple_on_((1, 2, 3), o)
        with self.assertRaisesRegex(ValueError, "expecting 4 values got 5"):
            OC_MetaDataTest.reverse4Tuple_on_((1, 2, 3, 4, 5), o)
        with self.assertRaisesRegex(ValueError, "argument 0 isn't allowed to be NULL"):
            OC_MetaDataTest.reverse4Tuple_on_(objc.NULL, o)

        a = (1, 2, 3, 4)
        n, v = OC_MetaDataTest.nullreverse4Tuple_on_(a, o)
        self.assertEqual(n, 1)
        self.assertEqual(a, (1, 2, 3, 4))
        self.assertEqual(v, (43, 44, 45, 46))

        n, v = OC_MetaDataTest.nullreverse4Tuple_on_(objc.NULL, o)
        self.assertEqual(n, -1)
        self.assertIs(v, objc.NULL)

    def testNullTerminated(self):
        o = Py_MetaDataTest_AllArgs.new()

        a = (b"aap", b"boot", b"cello")
        v = OC_MetaDataTest.reverseStrings_on_(a, o)
        self.assertEqual(a, (b"aap", b"boot", b"cello"))
        self.assertEqual(v, (b"paa", b"toob", b"ollec"))

        with self.assertRaisesRegex(ValueError, "depythonifying 'charptr', got 'int'"):
            OC_MetaDataTest.reverseStrings_on_((1, 2), o)
        with self.assertRaisesRegex(ValueError, "argument 0 isn't allowed to be NULL"):
            OC_MetaDataTest.reverseStrings_on_(objc.NULL, o)

        a = (b"aap", b"boot", b"cello")
        n, v = OC_MetaDataTest.nullreverseStrings_on_(a, o)
        self.assertEqual(n, 10)
        self.assertEqual(a, (b"aap", b"boot", b"cello"))
        self.assertEqual(v, (b"paa", b"toob", b"ollec"))

        n, v = OC_MetaDataTest.nullreverseStrings_on_(objc.NULL, o)
        self.assertEqual(n, 9)
        self.assertIs(v, objc.NULL)

    def testWithCount(self):
        o = Py_MetaDataTest_AllArgs.new()

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        v = OC_MetaDataTest.reverseArray_count_on_(a, 4, o)
        self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEqual(v, (2.0, 3.0, 4.0, 5.0))

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        v = OC_MetaDataTest.reverseArray_count_on_(a, 5, o)
        self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEqual(v, (2.0, 3.0, 4.0, 5.0, 6.0))

        # Nice to have, but doesn't work without major
        # surgery:
        # a = (1.0, 2.0, 3.0, 4.0, 5.0)
        # v = OC_MetaDataTest.reverseArray_count_on_(a, None, o)
        # self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        # self.assertEqual(v, (2.0, 3.0, 4.0, 5.0, 6.0))

        with self.assertRaisesRegex(
            ValueError, r"too few values \(2\) expecting at least 5"
        ):
            OC_MetaDataTest.reverseArray_count_on_((1.0, 2.0), 5, o)
        with self.assertRaisesRegex(ValueError, "argument 0 isn't allowed to be NULL"):
            OC_MetaDataTest.reverseArray_count_on_(objc.NULL, 0, o)

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        n, v = OC_MetaDataTest.nullreverseArray_count_on_(a, 5, o)
        self.assertEqual(n, 9)
        self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEqual(v, (43.0, 44.0, 45.0, 46.0, 47.0))

        n, v = OC_MetaDataTest.nullreverseArray_count_on_(objc.NULL, 0, o)
        self.assertEqual(n, 2)
        self.assertIs(v, objc.NULL)

    def testWithCountInResult(self):
        o = Py_MetaDataTest_AllArgs.new()

        c, v = OC_MetaDataTest.reverseArray_uptoCount_on_(range(10), 10, o)
        self.assertEqual(c, 5)
        self.assertEqual(len(v), 5)
        self.assertEqual(list(v), [0, 10, 20, 30, 40])

        c, v = OC_MetaDataTest.maybeReverseArray_on_([1, 2, 3, 4], o)
        self.assertEqual(c, 2)
        self.assertEqual(len(v), 2)
        self.assertEqual(list(v), [45, 51])


class TestArraysIn(TestCase):
    def testFixedSize(self):
        o = Py_MetaDataTest_AllArgs.new()

        (v,) = OC_MetaDataTest.make4Tuple_on_((1.0, 4.0, 8.0, 12.5), o)
        self.assertEqual(len(v), 4)
        self.assertEqual(list(v), [1.0, 4.0, 8.0, 12.5])

        (v,) = OC_MetaDataTest.make4Tuple_on_((1, 2, 3, 4), o)
        self.assertEqual(len(v), 4)
        self.assertEqual(list(v), [1.0, 2.0, 3.0, 4.0])

        with self.assertRaisesRegex(ValueError, "expecting 4 values got 3"):
            OC_MetaDataTest.make4Tuple_on_((1, 2, 3), o)
        with self.assertRaisesRegex(ValueError, "expecting 4 values got 5"):
            OC_MetaDataTest.make4Tuple_on_((1, 2, 3, 4, 5), o)
        with self.assertRaisesRegex(ValueError, "argument 0 isn't allowed to be NULL"):
            OC_MetaDataTest.make4Tuple_on_(objc.NULL, o)

        (v,) = OC_MetaDataTest.null4Tuple_on_(objc.NULL, o)
        self.assertIs(v, objc.NULL)

    def testNullTerminated(self):
        o = Py_MetaDataTest_AllArgs.new()

        (v,) = OC_MetaDataTest.makeStringArray_on_((b"hello", b"world", b"there"), o)
        self.assertEqual(len(v), 3)
        self.assertEqual(list(v), ["hello", "world", "there"])

        NSObject = objc.lookUpClass("NSObject")
        p, q = NSObject.new(), NSObject.new()
        (v,) = o.makeObjectArray_((p, q))
        self.assertEqual(len(v), 2)
        self.assertIs(v[0], p)
        self.assertIs(v[1], q)

        (v,) = OC_MetaDataTest.makeStringArray_on_((), o)
        self.assertEqual(len(v), 0)

        with self.assertRaisesRegex(ValueError, "depythonifying 'charptr', got 'int'"):
            OC_MetaDataTest.makeStringArray_on_([1, 2], o)
        with self.assertRaisesRegex(ValueError, "argument 0 isn't allowed to be NULL"):
            OC_MetaDataTest.makeStringArray_on_(objc.NULL, o)

        (v,) = OC_MetaDataTest.nullStringArray_on_(objc.NULL, o)
        self.assertEqual(v, objc.NULL)

    def testWithCount(self):
        o = Py_MetaDataTest_AllArgs.new()

        v, c = OC_MetaDataTest.makeIntArray_count_on_((1, 2, 3, 4), 3, o)
        self.assertEqual(c, 3)
        self.assertEqual(len(v), 3)
        self.assertEqual(list(v), [1, 2, 3])

        # XXX: This one would be nice to have, but not entirely trivial
        # v, c = OC_MetaDataTest.makeIntArray_count_on_((1,2,3,4), None, o)
        # self.assertEqual(c, 3)
        # self.assertEqual(len(v), 3)
        # self.assertEqual(list(v), [1,2,3,4])

        with self.assertRaisesRegex(
            ValueError, r"too few values \(3\) expecting at least 4"
        ):
            OC_MetaDataTest.makeIntArray_count_on_([1, 2, 3], 4, o)
        with self.assertRaisesRegex(ValueError, "argument 0 isn't allowed to be NULL"):
            OC_MetaDataTest.makeIntArray_count_on_(objc.NULL, 0, o)
        with self.assertRaisesRegex(ValueError, "argument 0 isn't allowed to be NULL"):
            OC_MetaDataTest.makeIntArray_count_on_(objc.NULL, 1, o)

        v, c = OC_MetaDataTest.nullIntArray_count_on_(objc.NULL, 0, o)
        self.assertEqual(c, 0)
        self.assertEqual(v, objc.NULL)

        with self.assertRaisesRegex(ValueError, "argument 0 isn't allowed to be NULL"):
            OC_MetaDataTest.makeIntArray_count_on_(objc.NULL, 1, o)

        # Make sure this also works when the length is in a pass-by-reference argument
        v, c = OC_MetaDataTest.makeIntArray_countPtr_on_((1, 2, 3, 4), 4, o)
        self.assertEqual(c, 4)
        self.assertEqual(len(v), 4)
        self.assertEqual(list(v), [1, 2, 3, 4])


class TestArrayReturns(TestCase):
    # TODO:
    # - Add null-terminated arrays of various supported types:
    #   -> integers
    #   -> CF-types
    def testFixedSize(self):
        o = Py_MetaDataTest_AllArgs.new()

        v = OC_MetaDataTest.makeIntArrayOf5On_(o)
        self.assertEqual(len(v), 5)
        self.assertEqual(list(v), [100, 200, 300, 400, 500])

        v = OC_MetaDataTest.nullIntArrayOf5On_(o)
        self.assertEqual(v, objc.NULL)

    def testSizeInArgument(self):
        o = Py_MetaDataTest_AllArgs.new()
        v = OC_MetaDataTest.makeIntArrayOf_on_(3, o)
        self.assertEqual(len(v), 3)
        self.assertEqual(list(v), [20, 21, 22])

        v = OC_MetaDataTest.makeIntArrayOf_on_(10, o)
        self.assertEqual(len(v), 10)
        self.assertEqual(list(v), list(range(20, 30)))

        v = OC_MetaDataTest.nullIntArrayOf_on_(100, o)
        self.assertEqual(v, objc.NULL)

    def testNULLterminated(self):
        o = Py_MetaDataTest_AllArgs.new()

        v = OC_MetaDataTest.makeStringArrayOn_(o)
        self.assertEqual(len(v), 3)
        self.assertEqual(list(v), [b"jaap", b"pieter", b"hans"])

        v = OC_MetaDataTest.nullStringArrayOn_(o)
        self.assertEqual(v, objc.NULL)

    def test_invalid_returns(self):
        o = Py_MetaDataTest_AllArgs_Invalid()

        with self.assertRaisesRegex(
            ValueError, "depythonifying array of 5 items, got one of 3"
        ):
            OC_MetaDataTest.makeIntArrayOf5On_(o)

        with self.assertRaisesRegex(TypeError, "Sequence required"):
            OC_MetaDataTest.makeStringArrayOn_(o)

        with self.assertRaisesRegex(
            ValueError, "depythonifying array of 4 items, got one of 8"
        ):
            OC_MetaDataTest.makeIntArrayOf_on_(4, o)


class TestByReference(TestCase):
    # Pass by reference arguments.
    # Note that these tests aren't exhaustive, we have test_methods and
    # test_methods2 for that :-)

    def testInput(self):
        o = Py_MetaDataTest_AllArgs.new()

        r = OC_MetaDataTest.sumX_andY_on_(1, 2, o)
        self.assertEqual(r, 1**2 + 2**2)

        r = OC_MetaDataTest.sumX_andY_on_(2535, 5325, o)
        self.assertEqual(r, 2535**2 + 5325**2)

        with self.assertRaisesRegex(ValueError, "argument 1 isn't allowed to be NULL"):
            OC_MetaDataTest.sumX_andY_on_(42, objc.NULL, o)

    def testOutput(self):
        o = Py_MetaDataTest_AllArgs.new()

        div, rem = OC_MetaDataTest.divBy5_remainder_on_(55, None, o)
        self.assertEqual(div, int(55 / 7))
        self.assertEqual(rem, int(55 % 7))

        div, rem = OC_MetaDataTest.divBy5_remainder_on_(13, None, o)
        self.assertEqual(div, int(13 / 7))
        self.assertEqual(rem, int(13 % 7))

        with self.assertRaisesRegex(ValueError, "argument 1 isn't allowed to be NULL"):
            OC_MetaDataTest.divBy5_remainder_on_(42, objc.NULL, o)

    def testInputOutput(self):
        o = Py_MetaDataTest_AllArgs.new()
        x, y = OC_MetaDataTest.swapX_andY_on_(42, 284, o)
        self.assertEqual(x, 284 * 2)
        self.assertEqual(y, 42 * 2)

        with self.assertRaisesRegex(ValueError, "argument 1 isn't allowed to be NULL"):
            OC_MetaDataTest.swapX_andY_on_(42, objc.NULL, o)

    def testNullAccepted(self):
        # Note: the commented-out test-cases require a change in the pyobjc-core
        o = Py_MetaDataTest_AllArgs.new()

        def makeNum(value):
            return int(value, 0)

        # All arguments present
        r, y, z = OC_MetaDataTest.input_output_inputAndOutput_on_(1, None, 2, o)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(lambda x: x is not objc.NULL, r))), 3)
        self.assertEqual(y, 9)
        self.assertEqual(z, 10)

        r, y, z = OC_MetaDataTest.input_output_inputAndOutput_on_(1, None, 2, o)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(lambda x: x is not objc.NULL, r))), 3)
        self.assertEqual(y, 9)
        self.assertEqual(z, 10)

        # Argument 1 is NULL
        r, y, z = OC_MetaDataTest.input_output_inputAndOutput_on_(objc.NULL, None, 2, o)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(lambda x: x is not objc.NULL, r))), 2)
        self.assertEqual(y, 11)
        self.assertEqual(z, 12)

        r, y, z = OC_MetaDataTest.input_output_inputAndOutput_on_(objc.NULL, None, 2, o)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(lambda x: x is not objc.NULL, r))), 2)
        self.assertEqual(y, 11)
        self.assertEqual(z, 12)

        # Argument 2 is NULL
        r, y, z = OC_MetaDataTest.input_output_inputAndOutput_on_(1, objc.NULL, 2, o)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(lambda x: x is not objc.NULL, r))), 2)
        self.assertEqual(y, objc.NULL)
        self.assertEqual(z, 14)

        # Argument 3 is NULL
        r, y, z = OC_MetaDataTest.input_output_inputAndOutput_on_(1, None, objc.NULL, o)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(lambda x: x is not objc.NULL, r))), 2)
        self.assertEqual(y, 15)
        self.assertEqual(z, objc.NULL)

        r, y, z = OC_MetaDataTest.input_output_inputAndOutput_on_(1, None, objc.NULL, o)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(lambda x: x is not objc.NULL, r))), 2)
        self.assertEqual(y, 15)
        self.assertEqual(z, objc.NULL)


class OC_MetaDataTestCharPArgs(OC_MetaDataTest):
    def charpArgPlain_(self, a):
        return [a]

    def charpArgNullTerminated_(self, a):
        return [a]

    def charpArg5Chars_(self, a):
        return [a]

    def charpArgVariadic_(self, a):
        return [a, a[:3]]

    def charpArgDeref_(self, a):
        return [a]

    def charpArgCounted_count_(self, a, b):
        return [a, b]

    def charpArgCounted_floatcount_(self, a, b):
        return [a, b]


class TestCharPArgumentsIn(TestCase):
    def test_plain(self):
        self.assertArgHasType(OC_MetaDataTestCharPArgs.charpArgPlain_, 0, b"*")

        o = OC_MetaDataTestCharPArgs()
        v = OC_MetaDataTest.charpArgPlain_on_(b"hello\0world", o)
        self.assertEqual(v, [b"hello"])

        v = OC_MetaDataTest.charpArgPlainOn_(o)
        self.assertEqual(v, [objc.NULL])

    def test_nullterminated(self):
        self.assertArgHasType(OC_MetaDataTestCharPArgs.charpArgNullTerminated_, 0, b"*")

        o = OC_MetaDataTestCharPArgs()
        v = OC_MetaDataTest.charpArgNullTerminated_on_(b"hello\0world", o)
        self.assertEqual(v, [b"hello"])

    def test_5chars(self):
        self.assertArgHasType(OC_MetaDataTestCharPArgs.charpArg5Chars_, 0, b"*")

        o = OC_MetaDataTestCharPArgs()
        v = OC_MetaDataTest.charpArg5Chars_on_(b"hoi\0wereld", o)
        self.assertEqual(v, [b"hoi\0w"])

    def test_variadic(self):
        self.assertArgHasType(OC_MetaDataTestCharPArgs.charpArgVariadic_, 0, b"*")

        o = OC_MetaDataTestCharPArgs()
        v = OC_MetaDataTest.charpArgVariadic_on_(b"hello\0world", o)
        self.assertIsInstance(v[0], objc.varlist)
        self.assertEqual(v[1], tuple(b"hel"))

    def test_deref(self):
        self.assertArgHasType(OC_MetaDataTestCharPArgs.charpArgDeref_, 0, b"*")

        o = OC_MetaDataTestCharPArgs()
        with self.assertRaisesRegex(
            objc.error, "using 'deref_result_pointer' for an argument"
        ):
            OC_MetaDataTest.charpArgDeref_on_(b"hello\0world", o)

    def test_counted(self):
        self.assertArgHasType(
            OC_MetaDataTestCharPArgs.charpArgCounted_count_, 1, objc._C_INT
        )
        self.assertArgHasType(OC_MetaDataTestCharPArgs.charpArgCounted_count_, 0, b"*")

        self.assertArgHasType(
            OC_MetaDataTestCharPArgs.charpArgCounted_floatcount_, 1, objc._C_FLT
        )
        self.assertArgHasType(
            OC_MetaDataTestCharPArgs.charpArgCounted_floatcount_, 0, b"*"
        )

        o = OC_MetaDataTestCharPArgs()
        v = OC_MetaDataTest.charpArgCounted_count_on_(b"hello\0world", 8, o)
        self.assertEqual(v, [b"hello\0wo", 8])

        with self.assertRaisesRegex(
            TypeError, "Don't know how to extract count from encoding: f"
        ):
            OC_MetaDataTest.charpArgCounted_floatcount_on_(b"hello\0world", 8, o)


class OC_MetaDataTestPointerResult(OC_MetaDataTest):
    def returnPointerPlain(self):
        return 43

    def returnPointerFixedLen(self):
        return [13, 15, 17, 19, 23]

    def returnCharPFixedLen(self):
        return b"abcde"

    def returnPointerVariadic(self):
        return list(range(20))

    def returnPointerNullDelimited(self):
        return [5, 4, 3, 2, 1, 0, -1]

    def returnCharPNullDelimited(self):
        return b"aap noot mies"

    def returnPointerCounted_(self, count):
        return [count] * count

    def returnPointerFloatCounted_(self, count):
        return [int(count)] * int(count)

    def returnPointerCountedIn_(self, count):
        return [count] * count

    def returnPointerCountedOut_(self, count):
        count = 7
        return [count] * count, count

    def returnPointerCountedInOut_(self, count):
        newcount = 6
        return [count] * newcount, newcount

    def returnPointerDeref(self):
        return 99

    def returnPointerToFree(self):
        return list(range(4))[::-1]

    def returnPointerToFreeVariadic(self):
        return list(range(8))[::-1]


class OC_MetaDataTestPointerResult2(OC_MetaDataTest):
    def returnPointerToFreeVariadic(self):
        return object()

    def returnCharPNullDelimited(self):
        return bytearray(b"over een muur")

    def returnCharPFixedLen(self):
        return bytearray(b"vwxyz")

    def returnPointerFixedLen(self):
        return object()


class OC_MetaDataTestPointerResult3(OC_MetaDataTest):
    def returnPointerFixedLen(self):
        return [13, 15, 17]


class TestPointerResultNative(TestCase):
    def test_plain(self):
        obj = OC_MetaDataTest()

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=objc.ObjCPointerWarning)
            v = obj.returnPointerPlain()
            self.assertIsInstance(v, objc.ObjCPointer)

    def test_fixed(self):
        obj = OC_MetaDataTest()

        v = obj.returnPointerFixedLen()
        self.assertEqual(v, (2, 3, 5, 7, 11))

    def test_variadic(self):
        obj = OC_MetaDataTest()

        v = obj.returnPointerVariadic()
        self.assertIsInstance(v, objc.varlist)
        self.assertEqual(v[0], 2)
        self.assertEqual(v[4], 32)

    def test_null_delimited(self):
        obj = OC_MetaDataTest()

        v = obj.returnPointerNullDelimited()
        self.assertEqual(v, (10, 9, 8, 7, 6, 5, 4, 3, 2, 1))

        v = obj.returnCharPNullDelimited()
        self.assertEqual(v, b"hello world")

    def test_counted_simple(self):
        obj = OC_MetaDataTest()

        v = obj.returnPointerCounted_(5)
        self.assertEqual(v, (0, -1, -4, -9, -16))

    def test_counted_in(self):
        obj = OC_MetaDataTest()

        v = obj.returnPointerCounted_(4)
        self.assertEqual(v, (0, -1, -4, -9))

    def test_counted_out(self):
        obj = OC_MetaDataTest()

        v, cnt = obj.returnPointerCountedOut_(None)
        self.assertEqual(cnt, 3)
        self.assertEqual(v, (0, -1, -4))

    def test_counted_inout(self):
        obj = OC_MetaDataTest()

        v, cnt = obj.returnPointerCountedInOut_(5)
        self.assertEqual(cnt, 3)
        self.assertEqual(v, (5, -1, -4))

    def test_counted_deref(self):
        obj = OC_MetaDataTest()

        v = obj.returnPointerDeref()
        self.assertEqual(v, 99)

    def test_fixed_free(self):
        obj = OC_MetaDataTest()

        v = obj.returnPointerToFree()
        self.assertEqual(v, (0, 1, 2, 3))

    def test_fixed_variadic(self):
        obj = OC_MetaDataTest()

        v = obj.returnPointerToFreeVariadic()
        # XXX: This should be an error, we cannot return a pointer
        #      to a buffer that should be freed!
        self.assertIsInstance(v, objc.varlist)


class TestPointerResultPython(TestCase):
    def test_plain(self):
        obj = OC_MetaDataTestPointerResult()

        with self.assertRaisesRegex(ValueError, "depythonifying 'pointer', got 'int'"):
            OC_MetaDataTest.returnPointerPlainOn_(obj)

    def test_fixed(self):
        obj = OC_MetaDataTestPointerResult()

        v = OC_MetaDataTest.returnPointerFixedLenOn_(obj)
        self.assertEqual(v, (13, 15, 17, 19, 23))

        v = OC_MetaDataTest.returnCharPFixedLenOn_(obj)
        self.assertEqual(v, b"abcde")

        obj = OC_MetaDataTestPointerResult2()
        with self.assertRaisesRegex(TypeError, "Sequence required"):
            OC_MetaDataTest.returnPointerFixedLenOn_(obj)

        v = OC_MetaDataTest.returnCharPFixedLenOn_(obj)
        self.assertEqual(v, b"vwxyz")

        obj = OC_MetaDataTestPointerResult3()
        with self.assertRaisesRegex(
            ValueError, "depythonifying array of 5 items, got one of 3"
        ):
            OC_MetaDataTest.returnPointerFixedLenOn_(obj)

    def test_variadic(self):
        obj = OC_MetaDataTestPointerResult()

        v = OC_MetaDataTest.returnPointerVariadicOn_(obj)
        self.assertIsInstance(v, objc.varlist)
        self.assertEqual(v[0], 0)
        self.assertEqual(v[4], 4)

    def test_null_delimited(self):
        obj = OC_MetaDataTestPointerResult()

        v = OC_MetaDataTest.returnPointerNullDelimitedOn_(obj)
        self.assertEqual(v, (5, 4, 3, 2, 1))

        v = OC_MetaDataTest.returnCharPNullDelimitedOn_(obj)
        self.assertEqual(v, b"aap noot mies")

        obj = OC_MetaDataTestPointerResult2()
        v = OC_MetaDataTest.returnCharPNullDelimitedOn_(obj)
        self.assertEqual(v, b"over een muur")

    def test_counted_simple(self):
        obj = OC_MetaDataTestPointerResult()

        v = OC_MetaDataTest.returnPointerCounted_on_(5, obj)
        self.assertEqual(v, (5,) * 5)

        with self.assertRaisesRegex(
            TypeError, "Don't know how to extract count from encoding: f"
        ):
            OC_MetaDataTest.returnPointerFloatCounted_on_(5.5, obj)

    def test_counted_in(self):
        obj = OC_MetaDataTestPointerResult()

        v = OC_MetaDataTest.returnPointerCountedIn_on_(4, obj)
        self.assertEqual(v, (4,) * 4)

    def test_counted_out(self):
        obj = OC_MetaDataTestPointerResult()

        v, cnt = OC_MetaDataTest.returnPointerCountedOut_on_(None, obj)
        self.assertEqual(cnt, 7)
        self.assertEqual(v, (7,) * 7)

    def test_counted_inout(self):
        obj = OC_MetaDataTestPointerResult()

        v, cnt = OC_MetaDataTest.returnPointerCountedInOut_on_(5, obj)
        self.assertEqual(cnt, 6)
        self.assertEqual(v, (5,) * 6)

    def test_counted_deref(self):
        obj = OC_MetaDataTestPointerResult()

        with self.assertRaisesRegex(
            objc.error,
            "using 'deref_result_pointer' for python callable is not supported",
        ):
            OC_MetaDataTest.returnPointerDerefOn_(obj)

    def test_fixed_free(self):
        obj = OC_MetaDataTestPointerResult()

        v = OC_MetaDataTest.returnPointerToFreeOn_(obj)
        self.assertEqual(v, (3, 2, 1, 0))

    def test_fixed_variadic(self):
        obj = OC_MetaDataTestPointerResult()

        v = OC_MetaDataTest.returnPointerToFreeVariadicOn_(obj)
        # XXX: This should be an error, we cannot return a pointer
        #      to a buffer that should be freed!
        self.assertIsInstance(v, objc.varlist)

        obj = OC_MetaDataTestPointerResult2()
        with self.assertRaisesRegex(TypeError, "Sequence required"):
            v = OC_MetaDataTest.returnPointerToFreeVariadicOn_(obj)


dealloc_list = []


class OC_MetaDataTestRetainedHelper(NSObject):
    def initWithValue_(self, value):
        self = super().init()
        if self is None:
            return None

        self.value = value
        return self

    def dealloc(self):
        dealloc_list.append(self.value)
        return super().dealloc()


class OC_MetaDataTestRetained(OC_MetaDataTest):
    def retainedObjCObject(self):
        return OC_MetaDataTestRetainedHelper(value=1)

    def retainedCFObject(self):
        return OC_MetaDataTestRetainedHelper(value=2)


class TestRetainedResults(TestCase):
    def test_native(self):
        obj = OC_MetaDataTest.alloc().init()
        v = obj.retainedObjCObject()
        self.assertIsInstance(v, NSArray)

        v = obj.retainedCFObject()
        self.assertIsInstance(v, NSArray)

    def test_python(self):
        with objc.autorelease_pool():
            obj = OC_MetaDataTestRetained.alloc().init()
            v = OC_MetaDataTest.retainedObjCObjectOn_(obj)
            self.assertIsInstance(v, OC_MetaDataTestRetainedHelper)
            self.assertEqual(v.value, 1)

            v = OC_MetaDataTest.retainedCFObjectOn_(obj)
            self.assertIsInstance(v, OC_MetaDataTestRetainedHelper)
            self.assertEqual(v.value, 2)

        del v

        self.assertEqual(len(dealloc_list), 2)


class OC_MetaDataTestOutputVariants(OC_MetaDataTest):
    def voidOutChar_(self, value):
        if value is not objc.NULL:
            return 88
        else:
            return None

    def intOutChar_(self, value):
        if value is not objc.NULL:
            return 4, 99
        else:
            return 2, None

    def voidOutCharPtr_(self, value):
        if value is not objc.NULL:
            return b"XYZ"
        else:
            return None

    def intOutCharPtr_(self, value):
        if value is not objc.NULL:
            return 4, b"XYZ"
        else:
            return 2, None

    def voidOutId_(self, value):
        if value is not objc.NULL:
            return set()
        else:
            return None

    def intOutId_(self, value):
        if value is not objc.NULL:
            return 2, set()
        else:
            return 4, None

    def voidOutIdRetained_(self, value):
        if value is not objc.NULL:
            return {}
        else:
            return None

    def intOutIdRetained_(self, value):
        if value is not objc.NULL:
            return 2, {}
        else:
            return 4, None

    def voidOutIdCFRetained_(self, value):
        if value is not objc.NULL:
            return []
        else:
            return None

    def intOutIdCFRetained_(self, value):
        if value is not objc.NULL:
            return 2, []
        else:
            return 4, None

    def voidOutInt_add_(self, a, b):
        if a is not objc.NULL:
            return -b
        else:
            return None

    def intOutInt_add_(self, a, b):
        if a is not objc.NULL:
            return b, -b
        else:
            return -b, None


class OC_MetaDataTestOutputVariants2(OC_MetaDataTest):
    def intOutIdRetained_(self, value):
        if value is not objc.NULL:
            return 2, NoObjCClass()
        else:
            return 4, None

    def intOutId_(self, value):
        return (value,)

    def intOutCharPtr_(self, value):
        return 42


class TestOutputVariants(TestCase):
    def test_native(self):
        obj = OC_MetaDataTest()

        self.assertArgHasType(obj.voidOutChar_, 0, b"o*")
        self.assertArgHasType(obj.intOutChar_, 0, b"o*")
        self.assertArgHasType(obj.voidOutCharPtr_, 0, b"o^*")
        self.assertArgHasType(obj.intOutCharPtr_, 0, b"o^*")
        self.assertArgHasType(obj.voidOutId_, 0, b"o^@")
        self.assertArgHasType(obj.intOutId_, 0, b"o^@")
        self.assertArgHasType(obj.voidOutIdRetained_, 0, b"o^@")
        self.assertArgHasType(obj.intOutIdRetained_, 0, b"o^@")
        self.assertArgHasType(obj.voidOutIdCFRetained_, 0, b"o^@")
        self.assertArgHasType(obj.intOutIdCFRetained_, 0, b"o^@")
        self.assertArgHasType(obj.voidOutInt_add_, 0, b"o^i")
        self.assertArgHasType(obj.intOutInt_add_, 0, b"o^i")

        v = obj.voidOutChar_(None)
        self.assertEqual(v, 44)

        v = obj.intOutChar_(None)
        self.assertEqual(v, (1, 45))

        v = obj.intOutChar_(objc.NULL)
        self.assertEqual(v, (0, objc.NULL))

        v = obj.voidOutCharPtr_(None)
        self.assertEqual(v, b"hello")

        v = obj.intOutCharPtr_(None)
        self.assertEqual(v, (1, b"hello"))

        v = obj.intOutCharPtr_(objc.NULL)
        self.assertEqual(v, (0, objc.NULL))

        v = obj.voidOutId_(None)
        self.assertEqual(v, "hello world")

        v = obj.intOutId_(None)
        self.assertEqual(v, (1, "hello world"))

        v = obj.intOutId_(objc.NULL)
        self.assertEqual(v, (0, objc.NULL))

        v = obj.voidOutIdRetained_(None)
        self.assertIsInstance(v, NSArray)

        v = obj.intOutIdRetained_(None)
        self.assertEqual(v, (1, []))
        self.assertIsInstance(v[1], NSArray)

        v = obj.intOutIdRetained_(objc.NULL)
        self.assertEqual(v, (0, objc.NULL))

        v = obj.voidOutIdCFRetained_(None)
        self.assertIsInstance(v, NSArray)

        v = obj.intOutIdCFRetained_(None)
        self.assertEqual(v, (1, []))
        self.assertIsInstance(v[1], NSArray)

        v = obj.intOutIdCFRetained_(objc.NULL)
        self.assertEqual(v, (0, objc.NULL))

        v = obj.voidOutInt_add_(None, 42)
        self.assertEqual(v, 84)

        v = obj.intOutInt_add_(None, 42)
        self.assertEqual(v, (1, 84))

        v = obj.intOutInt_add_(objc.NULL, 42)
        self.assertEqual(v, (0, objc.NULL))

    def test_python(self):
        obj = OC_MetaDataTestOutputVariants()

        with self.subTest("metadata"):
            self.assertArgHasType(obj.voidOutCharPtr_, 0, b"o^*")
            self.assertArgHasType(obj.intOutCharPtr_, 0, b"o^*")
            self.assertArgHasType(obj.voidOutId_, 0, b"o^@")
            self.assertArgHasType(obj.intOutId_, 0, b"o^@")
            self.assertArgHasType(obj.voidOutIdRetained_, 0, b"o^@")
            self.assertArgHasType(obj.intOutIdRetained_, 0, b"o^@")
            self.assertArgHasType(obj.voidOutIdCFRetained_, 0, b"o^@")
            self.assertArgHasType(obj.intOutIdCFRetained_, 0, b"o^@")
            self.assertArgHasType(obj.voidOutInt_add_, 0, b"o^i")
            self.assertArgHasType(obj.voidOutInt_add_, 1, b"i")
            self.assertArgHasType(obj.intOutInt_add_, 0, b"o^i")
            self.assertArgHasType(obj.intOutInt_add_, 1, b"i")

        with self.subTest("voidOutChar(None)"):
            v = OC_MetaDataTest.voidOutChar_on_(None, obj)
            self.assertEqual(v, 88)

        with self.subTest("voidOutChar(NULL)"):
            v = OC_MetaDataTest.voidOutChar_on_(objc.NULL, obj)
            self.assertEqual(v, objc.NULL)

        with self.subTest("intOutChar(None)"):
            v = OC_MetaDataTest.intOutChar_on_(None, obj)
            self.assertEqual(v, (4, 99))

        with self.subTest("intOutChar(NULL)"):
            v = OC_MetaDataTest.intOutChar_on_(objc.NULL, obj)
            self.assertEqual(v, (2, objc.NULL))

        with self.subTest("voidOutCharPtr(None)"):
            v = OC_MetaDataTest.voidOutCharPtr_on_(None, obj)
            self.assertEqual(v, b"XYZ")

        with self.subTest("voidOutCharPtr(NULL)"):
            v = OC_MetaDataTest.voidOutCharPtr_on_(objc.NULL, obj)
            self.assertEqual(v, objc.NULL)

        with self.subTest("intOutCharPtr(None)"):
            v = OC_MetaDataTest.intOutCharPtr_on_(None, obj)
            self.assertEqual(v, (4, b"XYZ"))

        with self.subTest("intOutCharPtr(None) - invalid"):
            with self.assertRaisesRegex(
                TypeError, "intOutCharPtr:: Need tuple of 2 arguments as result"
            ):
                OC_MetaDataTest.intOutCharPtr_on_(
                    None, OC_MetaDataTestOutputVariants2()
                )

        with self.subTest("intOutCharPtr(NULL)"):
            v = OC_MetaDataTest.intOutCharPtr_on_(objc.NULL, obj)
            self.assertEqual(v, (2, objc.NULL))

        with self.subTest("voidOutId(None)"):
            v = OC_MetaDataTest.voidOutId_on_(None, obj)
            self.assertEqual(v, set())

        with self.subTest("voidOutId(NULL)"):
            v = OC_MetaDataTest.voidOutId_on_(objc.NULL, obj)
            self.assertEqual(v, objc.NULL)

        with self.subTest("intOutId(None)"):
            v = OC_MetaDataTest.intOutId_on_(None, obj)
            self.assertEqual(v, (2, set()))

        with self.subTest("intOutId(None) - bad"):
            with self.assertRaisesRegex(
                TypeError, "intOutId:: Need tuple of 2 arguments as result"
            ):
                OC_MetaDataTest.intOutId_on_(None, OC_MetaDataTestOutputVariants2())

        with self.subTest("intOutId(NULL)"):
            v = OC_MetaDataTest.intOutId_on_(objc.NULL, obj)
            self.assertEqual(v, (4, objc.NULL))

        with self.subTest("voidOutIdRetained(None)"):
            v = OC_MetaDataTest.voidOutIdRetained_on_(None, obj)
            self.assertEqual(v, {})

        with self.subTest("voidOutIdRetained(NULL)"):
            v = OC_MetaDataTest.voidOutIdRetained_on_(objc.NULL, obj)
            self.assertEqual(v, objc.NULL)

        with self.subTest("intOutIdRetained(None)"):
            v = OC_MetaDataTest.intOutIdRetained_on_(None, obj)
            self.assertEqual(v, (2, {}))

        with self.subTest("intOutIdRetained(NULL)"):
            v = OC_MetaDataTest.intOutIdRetained_on_(objc.NULL, obj)
            self.assertEqual(v, (4, objc.NULL))

        with self.subTest("intOutIdRetained(None) - cannot depythonify"):
            with self.assertRaisesRegex(TypeError, "Cannot proxy"):
                OC_MetaDataTest.intOutIdRetained_on_(
                    None, OC_MetaDataTestOutputVariants2()
                )

        with self.subTest("voidOutIdCFRetained(None)"):
            v = OC_MetaDataTest.voidOutIdCFRetained_on_(None, obj)
            self.assertEqual(v, [])

        with self.subTest("voidOutIdCFRetained(NULL)"):
            v = OC_MetaDataTest.voidOutIdCFRetained_on_(objc.NULL, obj)
            self.assertEqual(v, objc.NULL)

        with self.subTest("intOutIdCFRetained(None)"):
            v = OC_MetaDataTest.intOutIdCFRetained_on_(None, obj)
            self.assertEqual(v, (2, []))

        with self.subTest("intOutIdCFRetained(NULL)"):
            v = OC_MetaDataTest.intOutIdCFRetained_on_(objc.NULL, obj)
            self.assertEqual(v, (4, objc.NULL))

        with self.subTest("voidOutInt_add_(None)"):
            v = OC_MetaDataTest.voidOutInt_add_on_(None, 42, obj)
            self.assertEqual(v, -42)

        with self.subTest("voidOutInt_add_(NULL)"):
            v = OC_MetaDataTest.voidOutInt_add_on_(objc.NULL, 42, obj)
            self.assertEqual(v, objc.NULL)

        with self.subTest("intOutInt_add_(None)"):
            v = OC_MetaDataTest.intOutInt_add_on_(None, 90, obj)
            self.assertEqual(v, (90, -90))

        with self.subTest("intOutInt_add_(NULL)"):
            v = OC_MetaDataTest.intOutInt_add_on_(objc.NULL, 90, obj)
            self.assertEqual(v, (-90, objc.NULL))
