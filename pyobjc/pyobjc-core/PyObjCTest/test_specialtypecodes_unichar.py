"""
Test handling of the private typecodes:  _C_UNICHAR

This typecode doesn't actually exists in the ObjC runtime but 
are private to PyObjC. We use these to simplify the bridge code
while at the same time getting a higher fidelity bridge.

- Add tests for calling methods from ObjC
"""
import weakref
from PyObjCTools.TestSupport import *
from PyObjCTest.fnd import NSObject

from PyObjCTest.specialtypecodes import *
import array

def setupMetaData():
    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "UniCharValue",
        dict(
            retval=dict(type=objc._C_UNICHAR),
        ))

    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "UniCharArray",
        dict(
            retval=dict(type=objc._C_PTR+objc._C_UNICHAR, c_array_of_fixed_length=4),
        ))

    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "UniCharString",
        dict(
            retval=dict(type=objc._C_PTR + objc._C_UNICHAR, c_array_delimited_by_null=True),
        ))

    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "UniCharStringArg:",
        dict(
            arguments={
                2: dict(type=objc._C_PTR + objc._C_UNICHAR, c_array_delimited_by_null=True, type_modifier=objc._C_IN),
            }
        ))

    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "UniCharArg:andUniCharArg:",
        dict(
            arguments={
                2: dict(type=objc._C_UNICHAR),
                3: dict(type=objc._C_UNICHAR),
            }
        ))
    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "UniCharArrayOf4In:",
        dict(
            arguments={
                2: dict(type=objc._C_PTR+objc._C_UNICHAR, type_modifier=objc._C_IN, c_array_of_fixed_length=4),
            }
        ))
    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "UniCharArrayOf4Out:",
        dict(
            arguments={
                2: dict(type=objc._C_PTR+objc._C_UNICHAR, type_modifier=objc._C_OUT, c_array_of_fixed_length=4),
            }
        ))
    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "UniCharArrayOf4InOut:",
        dict(
            arguments={
                2: dict(type=objc._C_PTR+objc._C_UNICHAR, type_modifier=objc._C_INOUT, c_array_of_fixed_length=4),
            }
        ))
    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "UniCharArrayOfCount:In:",
        dict(
            arguments={
                3: dict(type=objc._C_PTR+objc._C_UNICHAR, type_modifier=objc._C_IN, c_array_of_lenght_in_arg=2),
            }
        ))
    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "UniCharArrayOfCount:Out:",
        dict(
            arguments={
                3: dict(type=objc._C_PTR+objc._C_UNICHAR, type_modifier=objc._C_OUT, c_array_of_lenght_in_arg=2),
            }
        ))
    objc.registerMetaDataForSelector("OC_TestSpecialTypeCode", "UniCharArrayOfCount:InOut:",
        dict(
            arguments={
                3: dict(type=objc._C_PTR+objc._C_UNICHAR, type_modifier=objc._C_INOUT, c_array_of_lenght_in_arg=2),
            }
        ))


setupMetaData()

class TestTypeCode_UniChar (TestCase):
    def testReturnValue(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        self.assertEquals(o.UniCharValue(), u'a')
        self.assertEquals(o.UniCharValue(), unichr(55))
        self.assertEquals(o.UniCharValue(), unichr(9243))

    def testReturnValueArray(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.UniCharArray()
        self.assertEquals(len(v), 4)
        self.assertEquals(v[0], unichr(100))
        self.assertEquals(v[1], unichr(400))
        self.assertEquals(v[2], unichr(955))
        self.assertEquals(v[3], unichr(40000))

    def testReturnValueString(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.UniCharString()
        self.assert_(isinstance(v, unicode))
        self.assertEquals(v, u"help");

    def testSimpleArg(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.UniCharArg_andUniCharArg_(unichr(44), unichr(450))
        self.assertEquals(v, (unichr(44), unichr(450)))

        v = o.UniCharArg_andUniCharArg_(u'a', u'b')
        self.assertEquals(v, (u'a', u'b'))

        v = o.UniCharArg_andUniCharArg_('a', 'b')
        self.assertEquals(v, (u'a', u'b'))

        self.assertRaises(ValueError, o.UniCharArg_andUniCharArg_, 400, 401)

    def testStringArgument(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.UniCharStringArg_(u"hello world")
        self.assertEquals(v, u"hello world")
        self.assert_(isinstance(v, unicode))

        v = o.UniCharStringArg_("hello world")
        self.assertEquals(v, u"hello world")
        self.assert_(isinstance(v, unicode))

        v = o.UniCharStringArg_([u'a', u'b'])
        self.assertEquals(v, u"ab")
        self.assert_(isinstance(v, unicode))

        self.assertRaises(ValueError,  o.UniCharStringArg_, [99, 100, 100, 0])

    def testFixedArrayIn(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.UniCharArrayOf4In_(u"work")
        self.assertEquals(v, u"work")

        v = o.UniCharArrayOf4In_([u'a', u'b', u'c', u'd'])
        self.assertEquals(v, u'abcd')

        a = array.array('h', [200, 300, 400, 500])
        v = o.UniCharArrayOf4In_(a)
        self.assertEquals(v, u''.join([
            unichr(200), unichr(300), unichr(400), unichr(500)]))

    def testFixedArrayOut(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = o.UniCharArrayOf4Out_(None)
        self.assertEquals(v, u"boat")

        o = OC_TestSpecialTypeCode.alloc().init()
        a = array.array('h', [0] * 4) 
        v = o.UniCharArrayOf4Out_(a)
        self.assert_(v is a)
        self.assertEquals(v[0], ord('b'))
        self.assertEquals(v[1], ord('o'))
        self.assertEquals(v[2], ord('a'))
        self.assertEquals(v[3], ord('t'))

    def testFixedArrayInOut_(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v, w = o.UniCharArrayOf4InOut_(u"foot")
        self.assertEquals(v, u"foot")
        self.assertEquals(w, u"hand")

if __name__ == "__main__":
    main()
