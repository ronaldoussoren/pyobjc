"""
Tests for the new-style metadata format interface.

These tests only test ``out`` arguments where the out
argument isn't present in the python prototype.

TODO:
- Add more testcases: python methods that return the wrong value
- The python->C interface (that is the contents of the metadata object) is
  likely to change when the bridge is feature-complete.
- Probably need special-casing for arrays (numarray and array.array)!
"""
import objc
import objc.test

from objc.test.metadata import *

# To ensure we have the right metadata
import objc.test.test_metadata
import objc.test.test_metadata_py

import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

try:
    class Py_MetaDataTest_OutputOptional (OC_MetaDataTest):
        # Out arrays:
        def fillArray_count_(self, count):
            return range(10, count+10)

        def nullfillArray_count_(self, count):
            return 2, range(30, count+30)

        def fill4Tuple_(self):
            return range(9, 13)

        def nullfill4Tuple_(self, data):
            return 1, range(1, 5)

        def fillArray_uptoCount_(self, count):
            return count/2, range(10, 10 + (count/2))

        def maybeFillArray_(self):
            return 2, range(2)

        def fillStringArray_(self):
            raise RuntimeError("Should not reach this")

        def nullfillStringArray_(self):
            raise RuntimeError("Should not reach this")

finally:
    del warnings.filters[0]

class TestArraysOut (objc.test.TestCase):
    def testFixedSize(self):
        o = Py_MetaDataTest_OutputOptional.new()

        warnings.filterwarnings('ignore', category=DeprecationWarning)
        try:
            v = OC_MetaDataTest.fill4Tuple_on_(o)
            self.assertEquals(list(v), list(range(9, 13)))
        finally:
            del warnings.filters[0]

        v = OC_MetaDataTest.fill4Tuple_on_(None, o)
        self.assertEquals(list(v), list(range(9, 13)))

        self.assertRaises(ValueError, OC_MetaDataTest.fill4Tuple_on_, objc.NULL, o)

        warnings.filterwarnings('ignore', category=DeprecationWarning)
        try:
            n, v = OC_MetaDataTest.nullfill4Tuple_on_(o)
            self.assertEquals(n, 1)
            self.assertEquals(list(v), list(range(1, 5)))
        finally:
            del warnings.filters[0]

        n, v = OC_MetaDataTest.nullfill4Tuple_on_(None, o)
        self.assertEquals(n, 1)
        self.assertEquals(list(v), list(range(1, 5)))

        n, v = OC_MetaDataTest.nullfill4Tuple_on_(objc.NULL, o)
        self.assertEquals(n, 1)
        self.assert_( v is objc.NULL )
        
    def testNullTerminated(self):
        o = Py_MetaDataTest_OutputOptional.new()

        # Output only arrays of null-terminated arrays cannot be
        # wrapped automaticly. How is the bridge supposed to know
        # how much memory it should allocate for the C-array?
        warnings.filterwarnings('ignore', category=DeprecationWarning)
        try:
            self.assertRaises(TypeError, OC_MetaDataTest.fillStringArray_on_, o)
        finally:
            del warnings.filters[0]
        self.assertRaises(TypeError, OC_MetaDataTest.fillStringArray_on_, None, o)
        self.assertRaises(ValueError, OC_MetaDataTest.fillStringArray_on_, objc.NULL, o)

        self.assertRaises(TypeError, OC_MetaDataTest.nullfillStringArray_on_, o)
        self.assertRaises(TypeError, OC_MetaDataTest.nullfillStringArray_on_, None, o)

    def testWithCount(self):
        o = Py_MetaDataTest_OutputOptional.new()

        warnings.filterwarnings('ignore', category=DeprecationWarning)
        try:
            v = OC_MetaDataTest.fillArray_count_on_(3, o)
            self.assertEquals(list(v),  [10, 11, 12])
        finally:
            del warnings.filters[0]

        v = OC_MetaDataTest.fillArray_count_on_(None, 3, o)
        self.assertEquals(list(v),  [10, 11, 12])

        warnings.filterwarnings('ignore', category=DeprecationWarning)
        try:
            v = OC_MetaDataTest.fillArray_count_on_(5, o)
            self.assertEquals(list(v),  [10, 11, 12, 13, 14])

            v = OC_MetaDataTest.fillArray_count_on_(0, o)
            self.assertEquals(list(v),  [])
        finally:
            del warnings.filters[0]

        self.assertRaises(ValueError, OC_MetaDataTest.fillArray_count_on_, objc.NULL, 0, o)
        
        warnings.filterwarnings('ignore', category=DeprecationWarning)
        try:
            n, v = OC_MetaDataTest.nullfillArray_count_on_(3, o)
            self.assertEquals(n, 2)
            self.assertEquals(list(v),  [30,31,32])
        finally:
            del warnings.filters[0]

        n, v = OC_MetaDataTest.nullfillArray_count_on_(None, 3, o)
        self.assertEquals(n, 2)
        self.assertEquals(list(v),  [30,31,32])

        n, v = OC_MetaDataTest.nullfillArray_count_on_(objc.NULL, 3, o)
        self.assertEquals(n, 2)
        self.assert_( v is objc.NULL )

    def testWithCountInResult(self):
        o = Py_MetaDataTest_OutputOptional.new()

        warnings.filterwarnings('ignore', category=DeprecationWarning)
        try:
            c, v = OC_MetaDataTest.fillArray_uptoCount_on_(20, o)
            self.assertEquals(c, 10)
            self.assertEquals(list(v),  [i+10 for i in range(10)])

            c, v = OC_MetaDataTest.maybeFillArray_on_(o)
            self.assertEquals(c, 2)
            self.assertEquals(list(v),  [0, 1])
        finally:
            del warnings.filters[0]


if __name__ == "__main__":
    objc.test.main()
