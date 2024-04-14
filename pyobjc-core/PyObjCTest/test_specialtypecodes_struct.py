"""
Tests for using special type codes in struct definitions

TODO:
* _C_UNICHAR, _C_CHAR_AS_INT, _C_CHAR_AS_TEXT
"""

from PyObjCTest.specialtypecodes import OC_TestSpecialTypeCode
from PyObjCTools.TestSupport import TestCase
import objc

EmbeddedBoolStruct = objc.createStructType(
    "EmbeddedBoolStruct",
    b"{_EmbeddedBool=" + objc._C_INT + objc._C_NSBOOL + b"}",
    ["count", "isValid"],
)

EmbeddedBoolArrayStruct = objc.createStructType(
    "EmbeddedBoolArrayStruct",
    b"{_EmbeddedBoolArray=" + objc._C_INT + b"[4" + objc._C_NSBOOL + b"]}",
    ["count", "valid"],
)


class TestRecode(TestCase):
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
        self.assertIsInstance(w, EmbeddedBoolStruct)
        self.assertEqual(w.count, 55)
        self.assertIs(w.isValid, True)

    def testBoolArrayStruct(self):
        v = (42, [0, 1, 1, 0])
        w = objc.repythonify(v, EmbeddedBoolArrayStruct.__typestr__)
        self.assertIsInstance(w, EmbeddedBoolArrayStruct)
        self.assertEqual(w.count, 42)
        self.assertIs(w.valid[0], False)
        self.assertIs(w.valid[1], True)
        self.assertIs(w.valid[2], True)
        self.assertIs(w.valid[3], False)


class TestObjectiveC(TestCase):
    # Use an Objective-C class to test to/from Objective-C.
    #
    def testBoolStruct(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = (55, True)
        w = o.identicalEmbeddedBoolStruct_(v)
        self.assertIsInstance(w, EmbeddedBoolStruct)
        self.assertEqual(w.count, 55)
        self.assertIs(w.isValid, True)

    def testBoolArrayStruct(self):
        o = OC_TestSpecialTypeCode.alloc().init()

        v = (42, [0, 1, 1, 0])
        w = o.identicalEmbeddedBoolArrayStruct_(v)
        self.assertIsInstance(w, EmbeddedBoolArrayStruct)
        self.assertEqual(w.count, 42)
        self.assertIs(w.valid[0], False)
        self.assertIs(w.valid[1], True)
        self.assertIs(w.valid[2], True)
        self.assertIs(w.valid[3], False)
