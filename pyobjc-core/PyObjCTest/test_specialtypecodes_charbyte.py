"""
Test handling of the private typecodes:  _C_CHAR_AS_BYTE

This typecode doesn't actually exists in the ObjC runtime but 
are private to PyObjC. We use these to simplify the bridge code
while at the same time getting a higher fidelity bridge.

- Add tests for calling methods from ObjC
"""
import weakref, objc, sys
from PyObjCTools.TestSupport import *
from PyObjCTest.fnd import NSObject

from PyObjCTest.specialtypecodes import *
import array

def setupMetaData():
    objc.registerMetaDataForSelector(b"OC_TestSpecialTypeCode", b"byteValue",
        dict(
            retval=dict(type=objc._C_CHAR_AS_TEXT),
        ))

    objc.registerMetaDataForSelector(b"OC_TestSpecialTypeCode", b"byteArray",
        dict(
            retval=dict(type=objc._C_PTR+objc._C_CHAR_AS_TEXT, c_array_of_fixed_length=4),
        ))

    objc.registerMetaDataForSelector(b"OC_TestSpecialTypeCode", b"byteString",
        dict(
            retval=dict(type=objc._C_PTR + objc._C_CHAR_AS_TEXT, c_array_delimited_by_null=True),
        ))

    objc.registerMetaDataForSelector(b"OC_TestSpecialTypeCode", b"byteStringArg:",
        dict(
            arguments={
                2: dict(type=objc._C_PTR + objc._C_CHAR_AS_TEXT, c_array_delimited_by_null=True, type_modifier=objc._C_IN),
            }
        ))

    objc.registerMetaDataForSelector(b"OC_TestSpecialTypeCode", b"byteArg:andbyteArg:",
        dict(
            arguments={
                2: dict(type=objc._C_CHAR_AS_TEXT),
                3: dict(type=objc._C_CHAR_AS_TEXT),
            }
        ))
    objc.registerMetaDataForSelector(b"OC_TestSpecialTypeCode", b"byteArrayOf4In:",
        dict(
            arguments={
                2: dict(type=objc._C_PTR+objc._C_CHAR_AS_TEXT, type_modifier=objc._C_IN, c_array_of_fixed_length=4),
            }
        ))
    objc.registerMetaDataForSelector(b"OC_TestSpecialTypeCode", b"byteArrayOf4Out:",
        dict(
            arguments={
                2: dict(type=objc._C_PTR+objc._C_CHAR_AS_TEXT, type_modifier=objc._C_OUT, c_array_of_fixed_length=4),
            }
        ))
    objc.registerMetaDataForSelector(b"OC_TestSpecialTypeCode", b"byteArrayOf4InOut:",
        dict(
            arguments={
                2: dict(type=objc._C_PTR+objc._C_CHAR_AS_TEXT, type_modifier=objc._C_INOUT, c_array_of_fixed_length=4),
            }
        ))
    objc.registerMetaDataForSelector(b"OC_TestSpecialTypeCode", b"byteArrayOfCount:In:",
        dict(
            arguments={
                3: dict(type=objc._C_PTR+objc._C_CHAR_AS_TEXT, type_modifier=objc._C_IN, c_array_of_lenght_in_arg=2),
            }
        ))
    objc.registerMetaDataForSelector(b"OC_TestSpecialTypeCode", b"byteArrayOfCount:Out:",
        dict(
            arguments={
                3: dict(type=objc._C_PTR+objc._C_CHAR_AS_TEXT, type_modifier=objc._C_OUT, c_array_of_lenght_in_arg=2),
            }
        ))
    objc.registerMetaDataForSelector(b"OC_TestSpecialTypeCode", b"byteArrayOfCount:InOut:",
        dict(
            arguments={
                3: dict(type=objc._C_PTR+objc._C_CHAR_AS_TEXT, type_modifier=objc._C_INOUT, c_array_of_lenght_in_arg=2),
            }
        ))


setupMetaData()

class TestTypeCode_byte (TestCase):
    def testReturnValue(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        self.assertEquals(o.byteValue(), b'a')
        self.assertEquals(o.byteValue(), b'\x37')
        self.assertEquals(o.byteValue(), b'z')

    def testReturnValueArray(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.byteArray()
        self.assertEquals(len(v), 4)
        self.assertIsInstance(v, bytes)

        if sys.version_info[0] == 2:
            self.assertEquals(v[0], b'\x64')
            self.assertEquals(v[1], b'\xc8')
            self.assertEquals(v[2], b'\x96')
            self.assertEquals(v[3], b'\x63')
        else:
            self.assertEquals(v[0], 0x64)
            self.assertEquals(v[1], 0xc8)
            self.assertEquals(v[2], 0x96)
            self.assertEquals(v[3], 0x63)

    def testReturnValueString(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.byteString()
        self.assertIsInstance(v, bytes)
        self.assertEquals(v, b"hello world");

    def testSimpleArg(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.byteArg_andbyteArg_(b'\x44', b'\x99')
        self.assertEquals(v, (unichr(0x44), unichr(0x99)))

        v = o.byteArg_andbyteArg_(b'a', b'b')
        self.assertEquals(v, ('a', 'b'))

        self.assertRaises(ValueError, o.byteArg_andbyteArg_, 200, 100)

    def testStringArgument(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.byteStringArg_(b"hello world")
        self.assertEquals(v, "hello world")
        self.assertIsInstance(v, unicode)

        v = o.byteStringArg_([b'a', b'b'])
        self.assertIsInstance(v, unicode)
        self.assertEquals(v, "ab")

        self.assertRaises(ValueError,  o.byteStringArg_, [99, 100, 100, 0])

    def testFixedArrayIn(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.byteArrayOf4In_(b"work")
        self.assertEquals(v, "work")

        v = o.byteArrayOf4In_([b'a', b'b', b'c', b'd'])
        self.assertEquals(v, 'abcd')

        a = array.array('B', [200, 150, 80, 20])
        v = o.byteArrayOf4In_(a)
        self.assertEquals(v, u''.join([
            unichr(200), unichr(150), unichr(80), unichr(20)]))

    def testFixedArrayOut(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.byteArrayOf4Out_(None)
        self.assertEquals(v, b"boat")

        o = OC_TestSpecialTypeCode.alloc().init()
        a = array.array('b', [0] * 4) 
        v = o.byteArrayOf4Out_(a)
        self.assertIs(v, a)
        self.assertEquals(v[0], ord('b'))
        self.assertEquals(v[1], ord('o'))
        self.assertEquals(v[2], ord('a'))
        self.assertEquals(v[3], ord('t'))

    def testFixedArrayInOut_(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v, w = o.byteArrayOf4InOut_(b"foot")
        self.assertEquals(v, "foot")
        self.assertEquals(w, b"hand")

if __name__ == "__main__":
    main()
