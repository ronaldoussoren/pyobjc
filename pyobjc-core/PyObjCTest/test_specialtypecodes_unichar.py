"""
Test handling of the private typecodes:  _C_UNICHAR

This typecode doesn't actually exists in the ObjC runtime but
are private to PyObjC. We use these to simplify the bridge code
while at the same time getting a higher fidelity bridge.

- Add tests for calling methods from ObjC
"""
from __future__ import unicode_literals
import weakref
from PyObjCTools.TestSupport import *
from PyObjCTest.fnd import NSObject

from PyObjCTest.specialtypecodes import *
import array

import sys
if sys.version_info[0] == 3:
    unichr = chr
    unicode = str

def setupMetaData():
    objc.registerMetaDataForSelector(b"OC_TestSpecialTypeCode", b"UniCharValue",
        dict(
            retval=dict(type=objc._C_UNICHAR),
        ))

    objc.registerMetaDataForSelector(b"OC_TestSpecialTypeCode", b"UniCharArray",
        dict(
            retval=dict(type=objc._C_PTR+objc._C_UNICHAR, c_array_of_fixed_length=4),
        ))

    objc.registerMetaDataForSelector(b"OC_TestSpecialTypeCode", b"UniCharString",
        dict(
            retval=dict(type=objc._C_PTR + objc._C_UNICHAR, c_array_delimited_by_null=True),
        ))

    objc.registerMetaDataForSelector(b"OC_TestSpecialTypeCode", b"UniCharStringArg:",
        dict(
            arguments={
                2: dict(type=objc._C_PTR + objc._C_UNICHAR, c_array_delimited_by_null=True, type_modifier=objc._C_IN),
            }
        ))

    objc.registerMetaDataForSelector(b"OC_TestSpecialTypeCode", b"UniCharArg:andUniCharArg:",
        dict(
            arguments={
                2: dict(type=objc._C_UNICHAR),
                3: dict(type=objc._C_UNICHAR),
            }
        ))
    objc.registerMetaDataForSelector(b"OC_TestSpecialTypeCode", b"UniCharArrayOf4In:",
        dict(
            arguments={
                2: dict(type=objc._C_PTR+objc._C_UNICHAR, type_modifier=objc._C_IN, c_array_of_fixed_length=4),
            }
        ))
    objc.registerMetaDataForSelector(b"OC_TestSpecialTypeCode", b"UniCharArrayOf4Out:",
        dict(
            arguments={
                2: dict(type=objc._C_PTR+objc._C_UNICHAR, type_modifier=objc._C_OUT, c_array_of_fixed_length=4),
            }
        ))
    objc.registerMetaDataForSelector(b"OC_TestSpecialTypeCode", b"UniCharArrayOf4InOut:",
        dict(
            arguments={
                2: dict(type=objc._C_PTR+objc._C_UNICHAR, type_modifier=objc._C_INOUT, c_array_of_fixed_length=4),
            }
        ))
    objc.registerMetaDataForSelector(b"OC_TestSpecialTypeCode", b"UniCharArrayOfCount:In:",
        dict(
            arguments={
                3: dict(type=objc._C_PTR+objc._C_UNICHAR, type_modifier=objc._C_IN, c_array_of_lenght_in_arg=2),
            }
        ))
    objc.registerMetaDataForSelector(b"OC_TestSpecialTypeCode", b"UniCharArrayOfCount:Out:",
        dict(
            arguments={
                3: dict(type=objc._C_PTR+objc._C_UNICHAR, type_modifier=objc._C_OUT, c_array_of_lenght_in_arg=2),
            }
        ))
    objc.registerMetaDataForSelector(b"OC_TestSpecialTypeCode", b"UniCharArrayOfCount:InOut:",
        dict(
            arguments={
                3: dict(type=objc._C_PTR+objc._C_UNICHAR, type_modifier=objc._C_INOUT, c_array_of_lenght_in_arg=2),
            }
        ))


setupMetaData()

class TestTypeCode_UniChar (TestCase):
    def testReturnValue(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        self.assertEqual(o.UniCharValue(), 'a')
        self.assertEqual(o.UniCharValue(), unichr(55))
        self.assertEqual(o.UniCharValue(), unichr(9243))

    def testReturnValueArray(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.UniCharArray()
        self.assertEqual(len(v), 4)
        self.assertEqual(v[0], unichr(100))
        self.assertEqual(v[1], unichr(400))
        self.assertEqual(v[2], unichr(955))
        self.assertEqual(v[3], unichr(40000))

    def testReturnValueString(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.UniCharString()
        self.assertIsInstance(v, unicode)
        self.assertEqual(v, "help");

    def testSimpleArg(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.UniCharArg_andUniCharArg_(unichr(44), unichr(450))
        self.assertEqual(v, (unichr(44), unichr(450)))

        v = o.UniCharArg_andUniCharArg_('a', 'b')
        self.assertEqual(v, ('a', 'b'))

        v = o.UniCharArg_andUniCharArg_('a', 'b')
        self.assertEqual(v, ('a', 'b'))

        self.assertRaises(ValueError, o.UniCharArg_andUniCharArg_, 400, 401)

    def testStringArgument(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.UniCharStringArg_("hello world")
        self.assertEqual(v, "hello world")
        self.assertIsInstance(v, unicode)

        v = o.UniCharStringArg_("hello world")
        self.assertEqual(v, "hello world")
        self.assertIsInstance(v, unicode)

        v = o.UniCharStringArg_(['a', 'b'])
        self.assertEqual(v, "ab")
        self.assertIsInstance(v, unicode)

        self.assertRaises(ValueError,  o.UniCharStringArg_, [99, 100, 100, 0])

    def testFixedArrayIn(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.UniCharArrayOf4In_("work")
        self.assertEqual(v, "work")

        v = o.UniCharArrayOf4In_(['a', 'b', 'c', 'd'])
        self.assertEqual(v, 'abcd')

        if sys.version_info[0] == 2:
            a = array.array(b'h', [200, 300, 400, 500])
        else:
            a = array.array('h', [200, 300, 400, 500])
        v = o.UniCharArrayOf4In_(a)
        self.assertEqual(v, ''.join([
            unichr(200), unichr(300), unichr(400), unichr(500)]))

    def testFixedArrayOut(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.UniCharArrayOf4Out_(None)
        self.assertEqual(v, "boat")

        o = OC_TestSpecialTypeCode.alloc().init()
        if sys.version_info[0] == 2:
            a = array.array(b'h', [0] * 4)
        else:
            a = array.array('h', [0] * 4)
        v = o.UniCharArrayOf4Out_(a)
        self.assertIs(v, a)
        self.assertEqual(v[0], ord('b'))
        self.assertEqual(v[1], ord('o'))
        self.assertEqual(v[2], ord('a'))
        self.assertEqual(v[3], ord('t'))

    def testFixedArrayInOut_(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v, w = o.UniCharArrayOf4InOut_("foot")
        self.assertEqual(v, "foot")
        self.assertEqual(w, "hand")

if __name__ == "__main__":
    main()
