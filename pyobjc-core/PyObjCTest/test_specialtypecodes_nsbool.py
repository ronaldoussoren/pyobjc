"""
Test handling of the private typecodes: 
    _C_NSBOOL, _C_CHAR_AS_INT, _C_CHAR_AS_TEXT and _C_UNICHAR

These typecodes don't actually exists in the ObjC runtime but 
are private to PyObjC. We use these to simplify the bridge code
while at the same time getting a higher fidelity bridge.

TODO:
- Add support for UniChar
- Add support for char-as-int
- Add support for char-as-text

  (all these need the 0 terminated support as well)

- Add tests for calling methods from ObjC
- Add tests with these types in struct definitions
- Review test cases to make sure the tests are complete enough
"""
import weakref
from PyObjCTools.TestSupport import *
from PyObjCTest.fnd import NSObject

from PyObjCTest.specialtypecodes import *
import array

def setupMetaData():
    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "BOOLValue",
        dict(
            retval=dict(type=objc._C_NSBOOL),
        ))

    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "BOOLArray",
        dict(
            retval=dict(type=objc._C_PTR+objc._C_NSBOOL, c_array_of_fixed_length=4),
        ))

    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "BOOLArg:andBOOLArg:",
        dict(
            arguments={
                2: dict(type=objc._C_NSBOOL),
                3: dict(type=objc._C_NSBOOL),
            }
        ))
    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "BOOLArrayOf4In:",
        dict(
            arguments={
                2: dict(type=objc._C_PTR+objc._C_NSBOOL, type_modifier=objc._C_IN, c_array_of_fixed_length=4),
            }
        ))
    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "BOOLArrayOf4Out:",
        dict(
            arguments={
                2: dict(type=objc._C_PTR+objc._C_NSBOOL, type_modifier=objc._C_OUT, c_array_of_fixed_length=4),
            }
        ))
    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "BOOLArrayOf4InOut:",
        dict(
            arguments={
                2: dict(type=objc._C_PTR+objc._C_NSBOOL, type_modifier=objc._C_INOUT, c_array_of_fixed_length=4),
            }
        ))
    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "BOOLArrayOfCount:In:",
        dict(
            arguments={
                3: dict(type=objc._C_PTR+objc._C_NSBOOL, type_modifier=objc._C_IN, c_array_of_lenght_in_arg=2),
            }
        ))
    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "BOOLArrayOfCount:Out:",
        dict(
            arguments={
                3: dict(type=objc._C_PTR+objc._C_NSBOOL, type_modifier=objc._C_OUT, c_array_of_lenght_in_arg=2),
            }
        ))
    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "BOOLArrayOfCount:InOut:",
        dict(
            arguments={
                3: dict(type=objc._C_PTR+objc._C_NSBOOL, type_modifier=objc._C_INOUT, c_array_of_lenght_in_arg=2),
            }
        ))


setupMetaData()

class TestTypeCode_BOOL (TestCase):
    def testReturnValue(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        self.assert_(o.BOOLValue() is True)
        self.assert_(o.BOOLValue() is False)

    def testReturnValueArray(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.BOOLArray()
        self.assertEquals(len(v), 4)
        self.assert_(v[0] is True)
        self.assert_(v[1] is False)
        self.assert_(v[2] is True)
        self.assert_(v[3] is False)

    def testSimpleArg(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.BOOLArg_andBOOLArg_(True, False)
        self.assertEquals(v, (1, 0))

        v = o.BOOLArg_andBOOLArg_(False, True)
        self.assertEquals(v, (0, 1))

    def testFixedArrayIn(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.BOOLArrayOf4In_([True, False, True, False])
        self.assertEquals(v, (1, 0, 1, 0))

        v = o.BOOLArrayOf4In_([False, True, False, True])
        self.assertEquals(v, (0, 1, 0, 1))

        a = array.array('b', [1, 0, 1, 0])
        v = o.BOOLArrayOf4In_(a)
        self.assertEquals(v, (1, 0, 1, 0))

        # It should not be possible to use a string as an array of booleans
        self.assertRaises(ValueError, o.BOOLArrayOf4In_, "\x00\x01\x00\x01")

    def testFixedArrayOut(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.BOOLArrayOf4Out_(None)
        self.assertEquals(v, (True, False, True, False))

        v = o.BOOLArrayOf4Out_(None)
        self.assertEquals(v, (False, True, False, True))

        v = o.BOOLArrayOf4Out_(None)
        self.assertEquals(v, (True, True, True, True))

        v = o.BOOLArrayOf4Out_(None)
        self.assertEquals(v, (False, False, False, False))

        o = OC_TestSpecialTypeCode.alloc().init()
        a = array.array('b', [0] * 4) 
        v = o.BOOLArrayOf4Out_(a)
        self.assert_(v is a)
        self.assertEquals(v[0], 1)
        self.assertEquals(v[1], 0)
        self.assertEquals(v[2], 1)
        self.assertEquals(v[3], 0)

    def testFixedArrayInOut_(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v, w = o.BOOLArrayOf4InOut_([True, False, True, False])
        self.assertEquals(v, (True, False, True, False))
        self.assertEquals(w, (True, True, True, True))

        v, w = o.BOOLArrayOf4InOut_([False, True, False, True])
        self.assertEquals(v, (False, True, False, True))
        self.assertEquals(w, (False, False, False, False))

        # It should not be possible to use a string as an array of booleans
        self.assertRaises(ValueError, o.BOOLArrayOf4InOut_, "\x00\x01\x00\x01")

if __name__ == "__main__":
    main()
