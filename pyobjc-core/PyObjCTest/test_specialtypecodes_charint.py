"""
Test handling of the private typecodes:  _C_CHAR_AS_INT

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
        b"int8Value",
        {"retval": {"type": objc._C_CHAR_AS_INT}},
    )

    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"int8Array",
        {
            "retval": {
                "type": objc._C_PTR + objc._C_CHAR_AS_INT,
                "c_array_of_fixed_length": 4,
            }
        },
    )

    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"int8String",
        {
            "retval": {
                "type": objc._C_PTR + objc._C_CHAR_AS_INT,
                "c_array_delimited_by_null": True,
            }
        },
    )

    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"int8StringArg:",
        {
            "arguments": {
                2: {
                    "type": objc._C_PTR + objc._C_CHAR_AS_INT,
                    "c_array_delimited_by_null": True,
                    "type_modifier": objc._C_IN,
                }
            }
        },
    )

    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"int8Arg:andint8Arg:",
        {
            "arguments": {
                2: {"type": objc._C_CHAR_AS_INT},
                3: {"type": objc._C_CHAR_AS_INT},
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"int8ArrayOf4In:",
        {
            "arguments": {
                2: {
                    "type": objc._C_PTR + objc._C_CHAR_AS_INT,
                    "type_modifier": objc._C_IN,
                    "c_array_of_fixed_length": 4,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"int8ArrayOf4Out:",
        {
            "arguments": {
                2: {
                    "type": objc._C_PTR + objc._C_CHAR_AS_INT,
                    "type_modifier": objc._C_OUT,
                    "c_array_of_fixed_length": 4,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"int8ArrayOf4InOut:",
        {
            "arguments": {
                2: {
                    "type": objc._C_PTR + objc._C_CHAR_AS_INT,
                    "type_modifier": objc._C_INOUT,
                    "c_array_of_fixed_length": 4,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"int8ArrayOfCount:In:",
        {
            "arguments": {
                3: {
                    "type": objc._C_PTR + objc._C_CHAR_AS_INT,
                    "type_modifier": objc._C_IN,
                    "c_array_of_lenght_in_arg": 2,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"int8ArrayOfCount:Out:",
        {
            "arguments": {
                3: {
                    "type": objc._C_PTR + objc._C_CHAR_AS_INT,
                    "type_modifier": objc._C_OUT,
                    "c_array_of_lenght_in_arg": 2,
                }
            }
        },
    )
    objc.registerMetaDataForSelector(
        b"OC_TestSpecialTypeCode",
        b"int8ArrayOfCount:InOut:",
        {
            "arguments": {
                3: {
                    "type": objc._C_PTR + objc._C_CHAR_AS_INT,
                    "type_modifier": objc._C_INOUT,
                    "c_array_of_lenght_in_arg": 2,
                }
            }
        },
    )


setupMetaData()


class TestTypeCode_int8(TestCase):
    def testReturnValue(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        self.assertEqual(o.int8Value(), 1)
        self.assertEqual(o.int8Value(), 2)
        self.assertEqual(o.int8Value(), 3)
        self.assertEqual(o.int8Value(), 4)

    def testReturnValueArray(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.int8Array()
        self.assertEqual(len(v), 4)
        self.assertEqual(v[0], 100)
        self.assertEqual(v[1], -56)
        self.assertEqual(v[2], -106)
        self.assertEqual(v[3], 99)

    def testReturnValueString(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.int8String()
        self.assertIsInstance(v, (list, tuple))
        self.assertEqual(len(v), 5)
        self.assertEqual(v[0], ord("h"))
        self.assertEqual(v[1], ord("e"))
        self.assertEqual(v[2], ord("l"))
        self.assertEqual(v[3], ord("l"))
        self.assertEqual(v[4], ord("o"))

    def testSimpleArg(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.int8Arg_andint8Arg_(44, 127)
        self.assertEqual(v, (44, 127))

        v = o.int8Arg_andint8Arg_(ord("a"), ord("b"))
        self.assertEqual(v, (ord("a"), ord("b")))

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'char', got 'str' of 1"
        ):
            o.int8Arg_andint8Arg_("a", "b")
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'char', got 'bytes' of 1"
        ):
            o.int8Arg_andint8Arg_(b"a", b"b")

    def testStringArgument(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.int8StringArg_([1, 2, 3, 4])
        self.assertEqual(v, [1, 2, 3, 4])

        # XXX: This is not ideal, but changing this is not backward compatible.
        v = o.int8StringArg_(b"hello")
        self.assertEqual(v, [ord("h"), ord("e"), ord("l"), ord("l"), ord("o")])

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'char', got 'str' of 1"
        ):
            o.int8StringArg_("abc")

        # The message is fairly confusing because the generic code dealing with
        # C arrays unpacks the list argument and converts item by item.
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'char', got 'str' of 1"
        ):
            o.int8StringArg_(["a", "b"])
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'char', got 'bytes' of 1"
        ):
            o.int8StringArg_([b"a", b"b"])

    def testFixedArrayIn(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.int8ArrayOf4In_([1, 2, 3, 4])
        self.assertEqual(v, [1, 2, 3, 4])

        a = array.array("B", [200, 150, 80, 20])
        v = o.int8ArrayOf4In_(a)
        self.assertEqual(v, (-56, -106, 80, 20))

    def testFixedArrayOut(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.int8ArrayOf4Out_(None)
        self.assertEqual(v, (ord("b"), ord("o"), ord("a"), ord("t")))

        o = OC_TestSpecialTypeCode.alloc().init()
        a = array.array("b", [0] * 4)
        v = o.int8ArrayOf4Out_(a)
        self.assertIs(v, a)
        self.assertEqual(v[0], ord("b"))
        self.assertEqual(v[1], ord("o"))
        self.assertEqual(v[2], ord("a"))
        self.assertEqual(v[3], ord("t"))

    def testFixedArrayInOut_(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v, w = o.int8ArrayOf4InOut_([1, 2, 3, 4])
        self.assertEqual(v, [1, 2, 3, 4])
        self.assertEqual(w, (ord("h"), ord("a"), ord("n"), ord("d")))
