"""
Tests for using special type codes in struct definitions

TODO:
* _C_UNICHAR, _C_CHAR_AS_INT, _C_CHAR_AS_TEXT
"""
import weakref
from PyObjCTools.TestSupport import *
from PyObjCTest.fnd import NSObject

from PyObjCTest.specialtypecodes import *


EmbeddedBoolStruct = objc.createStructType(
        "EmbeddedBoolStruct", 
        "{_EmbeddedBool=" + objc._C_INT + objc._C_NSBOOL + "}", 
        [
            "count",
            "isValid"
        ])

EmbeddedBoolArrayStruct = objc.createStructType(
        "EmbeddedBoolArrayStruct", 
        "{_EmbeddedBoolArray=" + objc._C_INT + "[4" + objc._C_NSBOOL + "]}", 
        [
            "count",
            "valid"
        ])



class TestRecode (TestCase):
    # Use recode to test to/from Objective-C. 
    #
    # This has limited because in 'real life' we'd encode/decode based on a
    # typestring from the Objective-C runtime and those don't include our
    # special type codes.
    #
    # This does make sure that the basic encoding machinery works.
    def testBoolStruct(self):
        v = (55, True)
        w = objc.repythonify(v, EmbeddedBoolStruct.__typestr__)
        self.assert_(isinstance(w, EmbeddedBoolStruct))
        self.assertEquals(w.count, 55)
        self.assert_(w.isValid is True)

    def testBoolArrayStruct(self):
        v = (42, [0, 1, 1, 0])
        w = objc.repythonify(v, EmbeddedBoolArrayStruct.__typestr__)
        self.assert_(isinstance(w, EmbeddedBoolArrayStruct))
        self.assertEquals(w.count, 42)
        self.assert_(w.valid[0] is False)
        self.assert_(w.valid[1] is True)
        self.assert_(w.valid[2] is True)
        self.assert_(w.valid[3] is False)


class TestObjectiveC (TestCase):
    # Use an Objective-C class to test to/from Objective-C. 
    #
    def testBoolStruct(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = (55, True)
        w = o.identicalEmbeddedBoolStruct_(v)
        self.assert_(isinstance(w, EmbeddedBoolStruct))
        self.assertEquals(w.count, 55)
        self.assert_(w.isValid is True)

    def testBoolArrayStruct(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = (42, [0, 1, 1, 0])
        w = o.identicalEmbeddedBoolArrayStruct_(v)
        self.assert_(isinstance(w, EmbeddedBoolArrayStruct))
        self.assertEquals(w.count, 42)
        self.assert_(w.valid[0] is False)
        self.assert_(w.valid[1] is True)
        self.assert_(w.valid[2] is True)
        self.assert_(w.valid[3] is False)

if __name__ == "__main__":
    main()
