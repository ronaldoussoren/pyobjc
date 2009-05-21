"""
Test handling of the private typecodes:  _C_CHAR_AS_BYTE

This typecode doesn't actually exists in the ObjC runtime but 
are private to PyObjC. We use these to simplify the bridge code
while at the same time getting a higher fidelity bridge.

- Add tests for calling methods from ObjC
"""
import weakref, objc
from PyObjCTools.TestSupport import *
from PyObjCTest.fnd import NSObject

from PyObjCTest.specialtypecodes import *
import array

def setupMetaData():
    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "byteValue",
        dict(
            retval=dict(type=objc._C_CHAR_AS_TEXT),
        ))

    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "byteArray",
        dict(
            retval=dict(type=objc._C_PTR+objc._C_CHAR_AS_TEXT, c_array_of_fixed_length=4),
        ))

    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "byteString",
        dict(
            retval=dict(type=objc._C_PTR + objc._C_CHAR_AS_TEXT, c_array_delimited_by_null=True),
        ))

    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "byteStringArg:",
        dict(
            arguments={
                2: dict(type=objc._C_PTR + objc._C_CHAR_AS_TEXT, c_array_delimited_by_null=True, type_modifier=objc._C_IN),
            }
        ))

    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "byteArg:andbyteArg:",
        dict(
            arguments={
                2: dict(type=objc._C_CHAR_AS_TEXT),
                3: dict(type=objc._C_CHAR_AS_TEXT),
            }
        ))
    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "byteArrayOf4In:",
        dict(
            arguments={
                2: dict(type=objc._C_PTR+objc._C_CHAR_AS_TEXT, type_modifier=objc._C_IN, c_array_of_fixed_length=4),
            }
        ))
    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "byteArrayOf4Out:",
        dict(
            arguments={
                2: dict(type=objc._C_PTR+objc._C_CHAR_AS_TEXT, type_modifier=objc._C_OUT, c_array_of_fixed_length=4),
            }
        ))
    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "byteArrayOf4InOut:",
        dict(
            arguments={
                2: dict(type=objc._C_PTR+objc._C_CHAR_AS_TEXT, type_modifier=objc._C_INOUT, c_array_of_fixed_length=4),
            }
        ))
    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "byteArrayOfCount:In:",
        dict(
            arguments={
                3: dict(type=objc._C_PTR+objc._C_CHAR_AS_TEXT, type_modifier=objc._C_IN, c_array_of_lenght_in_arg=2),
            }
        ))
    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "byteArrayOfCount:Out:",
        dict(
            arguments={
                3: dict(type=objc._C_PTR+objc._C_CHAR_AS_TEXT, type_modifier=objc._C_OUT, c_array_of_lenght_in_arg=2),
            }
        ))
    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "byteArrayOfCount:InOut:",
        dict(
            arguments={
                3: dict(type=objc._C_PTR+objc._C_CHAR_AS_TEXT, type_modifier=objc._C_INOUT, c_array_of_lenght_in_arg=2),
            }
        ))


setupMetaData()

class TestTypeCode_byte (TestCase):
    def testReturnValue(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        self.assertEquals(o.byteValue(), 'a')
        self.assertEquals(o.byteValue(), chr(55))
        self.assertEquals(o.byteValue(), 'z')

    def testReturnValueArray(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.byteArray()
        self.assertEquals(len(v), 4)
        self.assertEquals(v[0], chr(100))
        self.assertEquals(v[1], chr(200))
        self.assertEquals(v[2], chr(150))
        self.assertEquals(v[3], chr(99))

    def testReturnValueString(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.byteString()
        self.assert_(isinstance(v, str))
        self.assertEquals(v, "hello world");

    def testSimpleArg(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.byteArg_andbyteArg_(chr(44), chr(129))
        self.assertEquals(v, (unichr(44), unichr(129)))

        v = o.byteArg_andbyteArg_('a', 'b')
        self.assertEquals(v, ('a', 'b'))

        self.assertRaises(ValueError, o.byteArg_andbyteArg_, 200, 100)

    def testStringArgument(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.byteStringArg_("hello world")
        self.assertEquals(v, "hello world")
        self.assert_(isinstance(v, unicode))

        v = o.byteStringArg_(['a', 'b'])
        self.assertEquals(v, "ab")
        self.assert_(isinstance(v, unicode))

        self.assertRaises(ValueError,  o.byteStringArg_, [99, 100, 100, 0])

    def testFixedArrayIn(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.byteArrayOf4In_("work")
        self.assertEquals(v, "work")

        v = o.byteArrayOf4In_(['a', 'b', 'c', 'd'])
        self.assertEquals(v, 'abcd')

        a = array.array('B', [200, 150, 80, 20])
        v = o.byteArrayOf4In_(a)
        self.assertEquals(v, u''.join([
            unichr(200), unichr(150), unichr(80), unichr(20)]))

    def testFixedArrayOut(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.byteArrayOf4Out_(None)
        self.assertEquals(v, "boat")

        o = OC_TestSpecialTypeCode.alloc().init()
        a = array.array('b', [0] * 4) 
        v = o.byteArrayOf4Out_(a)
        self.assert_(v is a)
        self.assertEquals(v[0], ord('b'))
        self.assertEquals(v[1], ord('o'))
        self.assertEquals(v[2], ord('a'))
        self.assertEquals(v[3], ord('t'))

    def testFixedArrayInOut_(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v, w = o.byteArrayOf4InOut_("foot")
        self.assertEquals(v, "foot")
        self.assertEquals(w, "hand")

if __name__ == "__main__":
    main()
