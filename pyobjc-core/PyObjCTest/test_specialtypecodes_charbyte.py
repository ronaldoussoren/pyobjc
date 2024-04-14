"""
Test handling of the private typecodes:  _C_CHAR_AS_BYTE

This typecode doesn't actually exists in the ObjC runtime but
are private to PyObjC. We use these to simplify the bridge code
while at the same time getting a higher fidelity bridge.

- Add tests for calling methods from ObjC
"""

import array

from PyObjCTest.specialtypecodes import OC_TestSpecialTypeCode
from PyObjCTools.TestSupport import TestCase
import objc


def setupMetaData():
    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"byteValue",
        {"retval": {"type": objc._C_CHAR_AS_TEXT}},
    )

    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"byteArray",
        {
            "retval": {
                "type": objc._C_PTR + objc._C_CHAR_AS_TEXT,
                "c_array_of_fixed_length": 4,
            }
        },
    )

    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"byteString",
        {
            "retval": {
                "type": objc._C_PTR + objc._C_CHAR_AS_TEXT,
                "c_array_delimited_by_null": True,
            }
        },
    )

    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"byteStringArg:",
        {
            "arguments": {
                2: {
                    "type": objc._C_PTR + objc._C_CHAR_AS_TEXT,
                    "c_array_delimited_by_null": True,
                    "type_modifier": objc._C_IN,
                }
            }
        },
    )

    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"byteArg:andbyteArg:",
        {
            "arguments": {
                2: {"type": objc._C_CHAR_AS_TEXT},
                3: {"type": objc._C_CHAR_AS_TEXT},
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"byteArrayOf4In:",
        {
            "arguments": {
                2: {
                    "type": objc._C_PTR + objc._C_CHAR_AS_TEXT,
                    "type_modifier": objc._C_IN,
                    "c_array_of_fixed_length": 4,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"byteArrayOf4Out:",
        {
            "arguments": {
                2: {
                    "type": objc._C_PTR + objc._C_CHAR_AS_TEXT,
                    "type_modifier": objc._C_OUT,
                    "c_array_of_fixed_length": 4,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"byteArrayOf4InOut:",
        {
            "arguments": {
                2: {
                    "type": objc._C_PTR + objc._C_CHAR_AS_TEXT,
                    "type_modifier": objc._C_INOUT,
                    "c_array_of_fixed_length": 4,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"byteArrayOfCount:In:",
        {
            "arguments": {
                3: {
                    "type": objc._C_PTR + objc._C_CHAR_AS_TEXT,
                    "type_modifier": objc._C_IN,
                    "c_array_of_lenght_in_arg": 2,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"byteArrayOfCount:Out:",
        {
            "arguments": {
                3: {
                    "type": objc._C_PTR + objc._C_CHAR_AS_TEXT,
                    "type_modifier": objc._C_OUT,
                    "c_array_of_lenght_in_arg": 2,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"byteArrayOfCount:InOut:",
        {
            "arguments": {
                3: {
                    "type": objc._C_PTR + objc._C_CHAR_AS_TEXT,
                    "type_modifier": objc._C_INOUT,
                    "c_array_of_lenght_in_arg": 2,
                }
            }
        },
    )


setupMetaData()


class TestTypeCode_byte(TestCase):
    def testReturnValue(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        self.assertEqual(o.byteValue(), b"a")
        self.assertEqual(o.byteValue(), b"\x37")
        self.assertEqual(o.byteValue(), b"z")

    def testReturnValueArray(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.byteArray()
        self.assertEqual(len(v), 4)
        self.assertIsInstance(v, bytes)

        self.assertEqual(v[0], 0x64)
        self.assertEqual(v[1], 0xC8)
        self.assertEqual(v[2], 0x96)
        self.assertEqual(v[3], 0x63)

    def testReturnValueString(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.byteString()
        self.assertIsInstance(v, bytes)
        self.assertEqual(v, b"hello world")

    def testSimpleArg(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.byteArg_andbyteArg_(b"\x44", b"\x99")
        self.assertEqual(v, (chr(0x44), chr(0x99)))

        v = o.byteArg_andbyteArg_(b"a", b"b")
        self.assertEqual(v, ("a", "b"))

        with self.assertRaisesRegex(
            ValueError, "Expecting byte string of length 1, got a 'int'"
        ):
            o.byteArg_andbyteArg_(200, 100)

    def testStringArgument(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.byteStringArg_(b"hello world")
        self.assertEqual(v, "hello world")
        self.assertIsInstance(v, str)

        v = o.byteStringArg_([b"a", b"b"])
        self.assertIsInstance(v, str)
        self.assertEqual(v, "ab")

        # The message is fairly confusing because this is handled by
        # the generic code for handling C array arguments, which iterates
        # for the list to convert item by item.
        with self.assertRaisesRegex(
            ValueError, "Expecting byte string of length 1, got a 'int'"
        ):
            o.byteStringArg_([99, 100, 100, 0])

    def testFixedArrayIn(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.byteArrayOf4In_(b"work")
        self.assertEqual(v, "work")

        v = o.byteArrayOf4In_([b"a", b"b", b"c", b"d"])
        self.assertEqual(v, "abcd")

        a = array.array("B", [200, 150, 80, 20])
        v = o.byteArrayOf4In_(a)
        self.assertEqual(v, "".join([chr(200), chr(150), chr(80), chr(20)]))

    def testFixedArrayOut(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.byteArrayOf4Out_(None)
        self.assertEqual(v, b"boat")

        o = OC_TestSpecialTypeCode.alloc().init()
        a = array.array("b", [0] * 4)
        v = o.byteArrayOf4Out_(a)
        self.assertIs(v, a)
        self.assertEqual(v[0], ord("b"))
        self.assertEqual(v[1], ord("o"))
        self.assertEqual(v[2], ord("a"))
        self.assertEqual(v[3], ord("t"))

    def testFixedArrayInOut_(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v, w = o.byteArrayOf4InOut_(b"foot")
        self.assertEqual(v, "foot")
        self.assertEqual(w, b"hand")
