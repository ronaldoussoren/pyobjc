"""
Test handling of the private typecodes:  _C_UNICHAR

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
        b"UniCharValue",
        {"retval": {"type": objc._C_UNICHAR}},
    )

    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"UniCharArray",
        {
            "retval": {
                "type": objc._C_PTR + objc._C_UNICHAR,
                "c_array_of_fixed_length": 4,
            }
        },
    )

    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"UniCharString",
        {
            "retval": {
                "type": objc._C_PTR + objc._C_UNICHAR,
                "c_array_delimited_by_null": True,
            }
        },
    )

    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"UniCharStringArg:",
        {
            "arguments": {
                2: {
                    "type": objc._C_PTR + objc._C_UNICHAR,
                    "c_array_delimited_by_null": True,
                    "type_modifier": objc._C_IN,
                }
            }
        },
    )

    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"UniCharArg:andUniCharArg:",
        {"arguments": {2: {"type": objc._C_UNICHAR}, 3: {"type": objc._C_UNICHAR}}},
    )
    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"UniCharArrayOf4In:",
        {
            "arguments": {
                2: {
                    "type": objc._C_PTR + objc._C_UNICHAR,
                    "type_modifier": objc._C_IN,
                    "c_array_of_fixed_length": 4,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"UniCharArrayOf4Out:",
        {
            "arguments": {
                2: {
                    "type": objc._C_PTR + objc._C_UNICHAR,
                    "type_modifier": objc._C_OUT,
                    "c_array_of_fixed_length": 4,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"UniCharArrayOf4InOut:",
        {
            "arguments": {
                2: {
                    "type": objc._C_PTR + objc._C_UNICHAR,
                    "type_modifier": objc._C_INOUT,
                    "c_array_of_fixed_length": 4,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"UniCharArrayOfCount:In:",
        {
            "arguments": {
                3: {
                    "type": objc._C_PTR + objc._C_UNICHAR,
                    "type_modifier": objc._C_IN,
                    "c_array_of_lenght_in_arg": 2,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"UniCharArrayOfCount:Out:",
        {
            "arguments": {
                3: {
                    "type": objc._C_PTR + objc._C_UNICHAR,
                    "type_modifier": objc._C_OUT,
                    "c_array_of_lenght_in_arg": 2,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"UniCharArrayOfCount:InOut:",
        {
            "arguments": {
                3: {
                    "type": objc._C_PTR + objc._C_UNICHAR,
                    "type_modifier": objc._C_INOUT,
                    "c_array_of_lenght_in_arg": 2,
                }
            }
        },
    )


setupMetaData()


class TestTypeCode_UniChar(TestCase):
    def testReturnValue(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        self.assertEqual(o.UniCharValue(), "a")
        self.assertEqual(o.UniCharValue(), chr(55))
        self.assertEqual(o.UniCharValue(), chr(9243))

    def testReturnValueArray(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.UniCharArray()
        self.assertEqual(len(v), 4)
        self.assertEqual(v[0], chr(100))
        self.assertEqual(v[1], chr(400))
        self.assertEqual(v[2], chr(955))
        self.assertEqual(v[3], chr(40000))

    def testReturnValueString(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.UniCharString()
        self.assertIsInstance(v, str)
        self.assertEqual(v, "help")

    def testSimpleArg(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.UniCharArg_andUniCharArg_(chr(44), chr(450))
        self.assertEqual(v, (chr(44), chr(450)))

        v = o.UniCharArg_andUniCharArg_("a", "b")
        self.assertEqual(v, ("a", "b"))

        v = o.UniCharArg_andUniCharArg_("a", "b")
        self.assertEqual(v, ("a", "b"))

        with self.assertRaisesRegex(
            ValueError, "Expecting unicode string of length 1, got a 'int'"
        ):
            o.UniCharArg_andUniCharArg_(400, 401)

    def testStringArgument(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.UniCharStringArg_("hello world")
        self.assertEqual(v, "hello world")
        self.assertIsInstance(v, str)

        v = o.UniCharStringArg_("hello world")
        self.assertEqual(v, "hello world")
        self.assertIsInstance(v, str)

        v = o.UniCharStringArg_(["a", "b"])
        self.assertEqual(v, "ab")
        self.assertIsInstance(v, str)

        with self.assertRaisesRegex(
            ValueError, "Expecting unicode string of length 1, got a 'int'"
        ):
            o.UniCharStringArg_([99, 100, 100, 0])

    def testFixedArrayIn(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.UniCharArrayOf4In_("work")
        self.assertEqual(v, "work")

        v = o.UniCharArrayOf4In_(["a", "b", "c", "d"])
        self.assertEqual(v, "abcd")

        a = array.array("h", [200, 300, 400, 500])
        v = o.UniCharArrayOf4In_(a)
        self.assertEqual(v, "".join([chr(200), chr(300), chr(400), chr(500)]))

    def testFixedArrayOut(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.UniCharArrayOf4Out_(None)
        self.assertEqual(v, "boat")

        o = OC_TestSpecialTypeCode.alloc().init()
        a = array.array("h", [0] * 4)
        v = o.UniCharArrayOf4Out_(a)
        self.assertIs(v, a)
        self.assertEqual(v[0], ord("b"))
        self.assertEqual(v[1], ord("o"))
        self.assertEqual(v[2], ord("a"))
        self.assertEqual(v[3], ord("t"))

    def testFixedArrayInOut_(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v, w = o.UniCharArrayOf4InOut_("foot")
        self.assertEqual(v, "foot")
        self.assertEqual(w, "hand")
