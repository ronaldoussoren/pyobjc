"""
Tests for the new-style metadata format interface.

Note: Tests for calling from python into ObjC are in test_metadata.py

TODO:
- Add more testcases: python methods that return the wrong value
- The python->C interface (that is the contents of the metadata object) is
  likely to change when the bridge is feature-complete.
- Probably need special-casing for arrays (numarray and array.array)!
"""
import objc
from PyObjCTools.TestSupport import *
import warnings

from PyObjCTest.metadata import *

# To ensure we have the right metadata
import PyObjCTest.test_metadata

def setupMetaData():
    # Note to self: what we think of as the first argument of a method is 
    # actually the third one, the objc runtime implicitly passed 'self' and
    # the selector as well. Therefore we need to start counting at 2 instead
    # of 0.
    #
    # Note2: the code below would normally be done using a metadata file 
    # instead of hardcoding.

    objc.registerMetaDataForSelector("OC_MetaDataTest", "make4Tuple:on:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_of_fixed_length=4, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector("OC_MetaDataTest", "null4Tuple:on:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_of_fixed_length=4, null_accepted=True),
                }
            )
        )

    objc.registerMetaDataForSelector("OC_MetaDataTest", "makeObjectArray:on:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_delimited_by_null=True, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector("OC_MetaDataTest", "makeStringArray:on:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_delimited_by_null=True, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector("OC_MetaDataTest", "nullStringArray:on:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_delimited_by_null=True, null_accepted=True),
                }
            )
        )
    objc.registerMetaDataForSelector("OC_MetaDataTest", "makeIntArray:count:on:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_length_in_arg=2+1, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector("OC_MetaDataTest", "makeIntArray:countPtr:on:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_length_in_arg=2+1, null_accepted=False),
                  2+1:  dict(type_modifier=objc._C_IN, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector("OC_MetaDataTest", "nullIntArray:count:on:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_length_in_arg=2+1, null_accepted=True),
                }
            )
        )

    objc.registerMetaDataForSelector("OC_MetaDataTest", "fillArray:uptoCount:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_OUT, c_array_length_in_arg=2+1, c_array_length_in_result=True, null_accepted=False),
                }
            )
        )

    objc.registerMetaDataForSelector("OC_MetaDataTest", "fillArray:count:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_OUT, c_array_length_in_arg=2+1, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector("OC_MetaDataTest", "nullfillArray:count:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_OUT, c_array_length_in_arg=2+1, null_accepted=True),
                }
            )
        )

    objc.registerMetaDataForSelector("OC_MetaDataTest", "maybeFillArray:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_OUT, c_array_of_fixed_length=4, c_array_length_in_result=True, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector("OC_MetaDataTest", "fill4Tuple:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_OUT, c_array_of_fixed_length=4, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector("OC_MetaDataTest", "nullfill4Tuple:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_OUT, c_array_of_fixed_length=4, null_accepted=True),
                }
            )
        )
    objc.registerMetaDataForSelector("OC_MetaDataTest", "fillStringArray:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_OUT, c_array_delimited_by_null=True, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector("OC_MetaDataTest", "nullfillStringArray:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_OUT, c_array_delimited_by_null=True, null_accepted=True),
                }
            )
        )

    objc.registerMetaDataForSelector("OC_MetaDataTest", "reverseArray:uptoCount:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, c_array_length_in_arg=2+1, c_array_length_in_result=True, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector("OC_MetaDataTest", "reverseArray:count:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, c_array_length_in_arg=2+1, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector("OC_MetaDataTest", "nullreverseArray:count:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, c_array_length_in_arg=2+1, null_accepted=True),
                }
            )
        )

    objc.registerMetaDataForSelector("OC_MetaDataTest", "reverseStrings:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, c_array_delimited_by_null=True, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector("OC_MetaDataTest", "nullreverseStrings:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, c_array_delimited_by_null=True, null_accepted=True),
                }
            )
        )

    objc.registerMetaDataForSelector("OC_MetaDataTest", "maybeReverseArray:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, c_array_of_fixed_length=4, c_array_length_in_result=True, null_accepted=True),
                }
            )
        )
    objc.registerMetaDataForSelector("OC_MetaDataTest", "reverse4Tuple:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, c_array_of_fixed_length=4, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector("OC_MetaDataTest", "nullreverse4Tuple:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, c_array_of_fixed_length=4, null_accepted=True),
                }
            )
        )




    objc.registerMetaDataForSelector("OC_MetaDataTest", "makeIntArrayOf5On:",
            dict(
                retval=dict(c_array_of_fixed_length=5)
            ),
        )

    objc.registerMetaDataForSelector("OC_MetaDataTest", "makeStringArrayOn:",
            dict(
                retval=dict(c_array_delimited_by_null=True),
            ),
        )

    objc.registerMetaDataForSelector("OC_MetaDataTest", "makeIntArrayOf:on:",
            dict(
                retval=dict(c_array_length_in_arg=2+0)
            ),
        )

    objc.registerMetaDataForSelector("OC_MetaDataTest", "nullIntArrayOf5On:",
            dict(
                retval=dict(c_array_of_fixed_length=5)
            ),
        )

    objc.registerMetaDataForSelector("OC_MetaDataTest", "nullStringArrayOn:",
            dict(
                retval=dict(c_array_delimited_by_null=True),
            ),
        )

    objc.registerMetaDataForSelector("OC_MetaDataTest", "nullIntArrayOf:on:",
            dict(
                retval=dict(c_array_length_in_arg=2+0)
            ),
        )


    objc.registerMetaDataForSelector("OC_MetaDataTest", "sumX:andY:on:", 
            dict(arguments={
                    2+0: dict(type_modifier=objc._C_IN, null_accepted=False),
                    2+1: dict(type_modifier=objc._C_IN, null_accepted=False),
                }))
    objc.registerMetaDataForSelector("OC_MetaDataTest", "divBy5:remainder:on:", 
            dict(arguments={
                    2+1: dict(type_modifier=objc._C_OUT, null_accepted=False),
                }))
    objc.registerMetaDataForSelector("OC_MetaDataTest", "swapX:andY:on:", 
            dict(arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, null_accepted=False),
                    2+1: dict(type_modifier=objc._C_INOUT, null_accepted=False),
                }))
    objc.registerMetaDataForSelector("OC_MetaDataTest", "input:output:inputAndOutput:on:",
            dict(arguments={
                    2+0: dict(type_modifier=objc._C_IN, null_accepted=True),
                    2+1: dict(type_modifier=objc._C_OUT, null_accepted=True),
                    2+2: dict(type_modifier=objc._C_INOUT, null_accepted=True),
            }))


setupMetaData()

class Py_MetaDataTest_AllArgs (OC_MetaDataTest):
    # Return value arrays:
    def makeIntArrayOf5(self):
        return [100, 200, 300, 400, 500]

    def makeStringArray(self):
        return [ "jaap", "pieter", "hans" ]

    def makeIntArrayOf_(self, count):
        return [ i + 20 for i in range(count) ]

    def nullIntArrayOf5(self):
        return objc.NULL

    def nullStringArray(self):
        return objc.NULL

    def nullIntArrayOf_(self, count):
        return objc.NULL

    # In arrays: 
    def makeIntArray_count_(self, data, count): return [data, count]
    def makeIntArray_countPtr_(self, data, count): return [data, count]
    def nullIntArray_count_(self, data, count): return [data, count]
    def makeStringArray_(self, data): return [data]
    def makeObjectArray_(self, data): return [data]
    def nullStringArray_(self, data): return [data]
    def make4Tuple_(self, data): return [data]
    def null4Tuple_(self, data): return [data]

    # Out arrays:
    def fillArray_count_(self, data, count):
        if data is None:
            return range(10, count+10)
        else:
            return range(20, count+20)

    def nullfillArray_count_(self, data, count):
        if data is objc.NULL:
            return 1, None

        elif data is None:
            return 2, range(30, count+30)

        else:
            return 3, range(40, count+40)

    def fill4Tuple_(self, data):
        if data is None:
            return range(9, 13)
        else:
            return range(14, 18)

    def nullfill4Tuple_(self, data):
        if data is None:
            return 1, range(1, 5)
        elif data is objc.NULL:
            return 2, range(6, 10)
        else:
            return 3, range(100, 104)

    def fillArray_uptoCount_(self, data, count):
        if data is None:
            return count/2, range(10, 10 + (count/2))
        else:
            return count/2, range(15, 15 + (count/2))

    def maybeFillArray_(self, data):
        if data is None:
            return 2, range(2)
        else:
            return 2, range(2, 4)

    def fillStringArray_(self, data):
        raise RuntimeError("Should not reach this")

    def nullfillStringArray_(self, data):
        if data is objc.NULL:
            return 9, objc.NULL

        raise RuntimeError("Should not reach this")

    # In/out arrays:
    def reverseArray_count_(self, data, count):
        if count == len(data):
            x = 1
        else:
            x = 2

        data = list(data)
        for i in range(len(data)):
            data[i] += x

        return data

    def nullreverseArray_count_(self, data, count):
        if data is objc.NULL:
            return 2, objc.NULL
        
        else:
            data = list(data)
            for i in range(len(data)):
                data[i] += 42
            return 9, data

    def reverseStrings_(self, data):
        data = list(data)
        for i in range(len(data)):
            data[i] = data[i][::-1]
        return data

    def nullreverseStrings_(self, data):
        if data is objc.NULL:
            return 9, objc.NULL

        else:
            data = list(data)
            for i in range(len(data)):
                data[i] = data[i][::-1]
            return 10, data

    def reverse4Tuple_(self, data):
        data = list(data)
        for i in range(len(data)):
            data[i] += 42
        return data

    def nullreverse4Tuple_(self, data):
        if data is objc.NULL:
            return -1, objc.NULL

        else:
            data = list(data)
            for i in range(len(data)):
                data[i] += 42
            return 1, data

    def reverseArray_uptoCount_(self, data, count):
        data = list(data)
        for i in range(len(data)/2):
            data[i] = data[i] * 10

        return count/2, data

    def maybeReverseArray_(self, data):
        return 2, (data[0] + 44, data[1] + 49)

    # pass-by-reference 
    def sumX_andY_(self, x, y):
        return x ** 2 + y ** 2

    def divBy5_remainder_(self, v, r):
        if r is None:
            return v / 7, v % 7
        else:
            return v / 9, v % 9

    def swapX_andY_(self, x, y):
        return y * 2, x * 2

    def input_output_inputAndOutput_(self, x, y, z):
        if x is not objc.NULL and y is not objc.NULL and z is not objc.NULL:
            return [x, y, z], 9, 10

        elif x is objc.NULL:
            return [x, y, z], 11, 12

        elif y is objc.NULL:
            return [x, y, z], 13, 14

        elif z is objc.NULL:
            return [x, y, z], 15, 16

class TestArrayDefault (TestCase):
    # TODO: what is the default anyway?
    pass

class TestArraysOut (TestCase):
    def testFixedSize(self):
        o = Py_MetaDataTest_AllArgs.new()

        v = OC_MetaDataTest.fill4Tuple_on_(None, o)
        self.assertEquals(list(v), list(range(9, 13)))

        v = OC_MetaDataTest.fill4Tuple_on_(None, o)
        self.assertEquals(list(v), list(range(9, 13)))

        self.assertRaises(ValueError, OC_MetaDataTest.fill4Tuple_on_, objc.NULL, o)

        n, v = OC_MetaDataTest.nullfill4Tuple_on_(None, o)
        self.assertEquals(n, 1)
        self.assertEquals(list(v), list(range(1, 5)))

        n, v = OC_MetaDataTest.nullfill4Tuple_on_(None, o)
        self.assertEquals(n, 1)
        self.assertEquals(list(v), list(range(1, 5)))

        n, v = OC_MetaDataTest.nullfill4Tuple_on_(objc.NULL, o)
        self.assertEquals(n, 2)
        self.assert_( v is objc.NULL )
        
    def testNullTerminated(self):
        o = Py_MetaDataTest_AllArgs.new()

        # Output only arrays of null-terminated arrays cannot be
        # wrapped automaticly. How is the bridge supposed to know
        # how much memory it should allocate for the C-array?
        self.assertRaises(TypeError, OC_MetaDataTest.fillStringArray_on_, None, o)
        self.assertRaises(ValueError, OC_MetaDataTest.fillStringArray_on_, objc.NULL, o)

        self.assertRaises(TypeError, OC_MetaDataTest.nullfillStringArray_on_, o)
        self.assertRaises(TypeError, OC_MetaDataTest.nullfillStringArray_on_, None, o)
        n, v = OC_MetaDataTest.nullfillStringArray_on_(objc.NULL, o)
        self.assertEquals(n, 9)
        self.assert_( v is objc.NULL)

    def testWithCount(self):
        o = Py_MetaDataTest_AllArgs.new()

        v = OC_MetaDataTest.fillArray_count_on_(None, 3, o)
        self.assertEquals(list(v),  [10, 11, 12])

        v = OC_MetaDataTest.fillArray_count_on_(None, 5, o)
        self.assertEquals(list(v),  [10, 11, 12, 13, 14])

        v = OC_MetaDataTest.fillArray_count_on_(None, 0, o)
        self.assertEquals(list(v),  [])

        self.assertRaises(ValueError, OC_MetaDataTest.fillArray_count_on_, objc.NULL, 0, o)
    
        n, v = OC_MetaDataTest.nullfillArray_count_on_(None, 3, o)
        self.assertEquals(n, 2)
        self.assertEquals(list(v),  [30,31,32])


        n, v = OC_MetaDataTest.nullfillArray_count_on_(objc.NULL, 3, o)
        self.assertEquals(n, 1)
        self.assert_( v is objc.NULL )

    def testWithCountInResult(self):
        o = Py_MetaDataTest_AllArgs.new()

        c, v = OC_MetaDataTest.fillArray_uptoCount_on_(None, 20, o)
        self.assertEquals(c, 10)
        self.assertEquals(list(v),  [i+10 for i in range(10)])

        c, v = OC_MetaDataTest.maybeFillArray_on_(None, o)
        self.assertEquals(c, 2)
        self.assertEquals(list(v),  [0, 1])

class TestArraysInOut (TestCase):
    def testFixedSize(self):
        o = Py_MetaDataTest_AllArgs.new()

        a = (1,2,3,4)
        v = OC_MetaDataTest.reverse4Tuple_on_(a, o)
        self.assertEquals(a, (1,2,3,4))
        self.assertEquals(v, (43, 44, 45, 46))

        self.assertRaises(ValueError, OC_MetaDataTest.reverse4Tuple_on_, (1,2,3), o)
        self.assertRaises(ValueError, OC_MetaDataTest.reverse4Tuple_on_, (1,2,3,4,5), o)
        self.assertRaises(ValueError, OC_MetaDataTest.reverse4Tuple_on_, objc.NULL, o)

        a = (1,2,3,4)
        n, v = OC_MetaDataTest.nullreverse4Tuple_on_(a, o)
        self.assertEquals(n, 1)
        self.assertEquals(a, (1,2,3,4))
        self.assertEquals(v, (43, 44, 45, 46))

        n, v = OC_MetaDataTest.nullreverse4Tuple_on_(objc.NULL, o)
        self.assertEquals(n, -1)
        self.assert_( v is objc.NULL )

    def testNullTerminated(self):
        o = Py_MetaDataTest_AllArgs.new()

        a = ('aap', 'boot', 'cello')
        v = OC_MetaDataTest.reverseStrings_on_(a, o)
        self.assertEquals(a, ('aap', 'boot', 'cello'))
        self.assertEquals(v, ('paa', 'toob', 'ollec'))

        self.assertRaises(ValueError, OC_MetaDataTest.reverseStrings_on_, (1,2), o)
        self.assertRaises(ValueError, OC_MetaDataTest.reverseStrings_on_, objc.NULL, o)

        a = ('aap', 'boot', 'cello')
        n, v = OC_MetaDataTest.nullreverseStrings_on_(a, o)
        self.assertEquals(n, 10)
        self.assertEquals(a, ('aap', 'boot', 'cello'))
        self.assertEquals(v, ('paa', 'toob', 'ollec'))

        n, v = OC_MetaDataTest.nullreverseStrings_on_(objc.NULL, o)
        self.assertEquals(n, 9)
        self.assert_( v is objc.NULL )

    def testWithCount(self):
        o = Py_MetaDataTest_AllArgs.new()

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        v = OC_MetaDataTest.reverseArray_count_on_(a, 4, o)
        self.assertEquals(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEquals(v, (2.0, 3.0, 4.0, 5.0))

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        v = OC_MetaDataTest.reverseArray_count_on_(a, 5, o)
        self.assertEquals(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEquals(v, (2.0, 3.0, 4.0, 5.0, 6.0))

        # Nice to have, but doesn't work without major
        # surgery:
        #a = (1.0, 2.0, 3.0, 4.0, 5.0)
        #v = OC_MetaDataTest.reverseArray_count_on_(a, None, o)
        #self.assertEquals(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        #self.assertEquals(v, (2.0, 3.0, 4.0, 5.0, 6.0))

        self.assertRaises(ValueError, OC_MetaDataTest.reverseArray_count_on_, (1.0, 2.0), 5, o)
        self.assertRaises(ValueError, OC_MetaDataTest.reverseArray_count_on_, objc.NULL, 0, o)

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        n, v = OC_MetaDataTest.nullreverseArray_count_on_(a, 5, o)
        self.assertEquals(n, 9)
        self.assertEquals(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEquals(v, (43.0, 44.0, 45.0, 46.0, 47.0))

        n, v = OC_MetaDataTest.nullreverseArray_count_on_(objc.NULL, 0, o)
        self.assertEquals(n, 2)
        self.assert_( v is objc.NULL )

    def testWithCountInResult(self):
        o = Py_MetaDataTest_AllArgs.new()

        c, v = OC_MetaDataTest.reverseArray_uptoCount_on_(range(10), 10, o)
        self.assertEquals(c, 5)
        self.assertEquals(len(v), 5)
        self.assertEquals(list(v),  [0, 10, 20, 30, 40])
        
        c, v = OC_MetaDataTest.maybeReverseArray_on_([1,2,3,4], o)
        self.assertEquals(c, 2)
        self.assertEquals(len(v), 2)
        self.assertEquals(list(v),  [45, 51])

class TestArraysIn (TestCase):
    def testFixedSize(self):
        o = Py_MetaDataTest_AllArgs.new()

        v,  = OC_MetaDataTest.make4Tuple_on_((1.0, 4.0, 8.0, 12.5), o)
        self.assertEquals(len(v), 4)
        self.assertEquals(list(v), [1.0, 4.0, 8.0, 12.5])

        v, = OC_MetaDataTest.make4Tuple_on_((1, 2, 3, 4), o)
        self.assertEquals(len(v), 4)
        self.assertEquals(list(v), [1.0, 2.0, 3.0, 4.0])

        self.assertRaises(ValueError, OC_MetaDataTest.make4Tuple_on_, (1, 2, 3), o)
        self.assertRaises(ValueError, OC_MetaDataTest.make4Tuple_on_, (1, 2, 3, 4, 5), o)
        self.assertRaises(ValueError, OC_MetaDataTest.make4Tuple_on_, objc.NULL, o)

        v, = OC_MetaDataTest.null4Tuple_on_(objc.NULL, o)
        self.assert_(v is objc.NULL )

    def testNullTerminated(self):
        o = Py_MetaDataTest_AllArgs.new()

        v, = OC_MetaDataTest.makeStringArray_on_(("hello", "world", "there"), o)
        self.assertEquals(len(v), 3)
        self.assertEquals(list(v), ["hello", "world", "there"])

        NSObject = objc.lookUpClass('NSObject')
        p, q = NSObject.new(), NSObject.new()
        v, = o.makeObjectArray_((p, q))
        self.assertEquals(len(v), 2)
        self.assert_( v[0] is p )
        self.assert_( v[1] is q )

        v, = OC_MetaDataTest.makeStringArray_on_((), o)
        self.assertEquals(len(v), 0)

        self.assertRaises(ValueError, OC_MetaDataTest.makeStringArray_on_, [1,2], o)
        self.assertRaises(ValueError, OC_MetaDataTest.makeStringArray_on_, objc.NULL, o)

        v, = OC_MetaDataTest.nullStringArray_on_(objc.NULL, o)
        self.assertEquals(v, objc.NULL)

    def testWithCount(self):
        o = Py_MetaDataTest_AllArgs.new()

        v, c = OC_MetaDataTest.makeIntArray_count_on_((1,2,3,4), 3, o)
        self.assertEquals(c, 3)
        self.assertEquals(len(v), 3)
        self.assertEquals(list(v), [1,2,3])
        
        # XXX: This one would be nice to have, but not entirely trivial
        #v, c = OC_MetaDataTest.makeIntArray_count_on_((1,2,3,4), None, o)
        #self.assertEquals(c, 3)
        #self.assertEquals(len(v), 3)
        #self.assertEquals(list(v), [1,2,3,4])

        self.assertRaises(ValueError, OC_MetaDataTest.makeIntArray_count_on_, [1,2,3], 4, o)
        self.assertRaises(ValueError, OC_MetaDataTest.makeIntArray_count_on_, objc.NULL, 0, o)
        self.assertRaises(ValueError, OC_MetaDataTest.makeIntArray_count_on_, objc.NULL, 1, o)

        v, c = OC_MetaDataTest.nullIntArray_count_on_(objc.NULL, 0, o)
        self.assertEquals(c, 0)
        self.assertEquals(v, objc.NULL)

        self.assertRaises(ValueError, OC_MetaDataTest.makeIntArray_count_on_, objc.NULL, 1, o)

        # Make sure this also works when the length is in a pass-by-reference argument
        v, c = OC_MetaDataTest.makeIntArray_countPtr_on_((1,2,3,4), 4, o)
        self.assertEquals(c, 4)
        self.assertEquals(len(v), 4)
        self.assertEquals(list(v), [1,2,3,4])

class TestArrayReturns (TestCase):
    # TODO:
    # - Add null-terminated arrays of various supported types:
    #   -> integers
    #   -> CF-types
    def testFixedSize(self):
        o = Py_MetaDataTest_AllArgs.new()

        v = OC_MetaDataTest.makeIntArrayOf5On_(o)
        self.assertEquals( len(v), 5 )
        self.assertEquals( list(v), [100, 200, 300, 400, 500] )

        v = OC_MetaDataTest.nullIntArrayOf5On_(o)
        self.assertEquals(v, objc.NULL)

    def testSizeInArgument(self):
        o = Py_MetaDataTest_AllArgs.new()
        v = OC_MetaDataTest.makeIntArrayOf_on_(3, o)
        self.assertEquals(len(v), 3)
        self.assertEquals(list(v), [20, 21, 22])

        v = OC_MetaDataTest.makeIntArrayOf_on_(10, o)
        self.assertEquals(len(v), 10)
        self.assertEquals(list(v), list(range(20, 30)))

        v = OC_MetaDataTest.nullIntArrayOf_on_(100, o)
        self.assertEquals(v, objc.NULL)

    def testNULLterminated(self):
        o  = Py_MetaDataTest_AllArgs.new()

        v = OC_MetaDataTest.makeStringArrayOn_(o)
        self.assertEquals(len(v), 3)
        self.assertEquals(list(v), [ "jaap", "pieter", "hans" ])

        v = OC_MetaDataTest.nullStringArrayOn_(o)
        self.assertEquals(v, objc.NULL)

class TestByReference (TestCase):
    # Pass by reference arguments. 
    # Note that these tests aren't exhaustive, we have test_methods and
    # test_methods2 for that :-)

    def testInput(self):
        o = Py_MetaDataTest_AllArgs.new()
        
        r = OC_MetaDataTest.sumX_andY_on_(1, 2, o)
        self.assertEquals(r, 1**2+2**2)

        r = OC_MetaDataTest.sumX_andY_on_(2535, 5325, o)
        self.assertEquals(r, 2535**2 + 5325**2)

        self.assertRaises(ValueError, OC_MetaDataTest.sumX_andY_on_, 42, objc.NULL, o)

    def testOutput(self):
        o = Py_MetaDataTest_AllArgs.new()

        div, rem = OC_MetaDataTest.divBy5_remainder_on_(55, None, o)
        self.assertEquals(div, 55 / 7)
        self.assertEquals(rem, 55 % 7)

        div, rem = OC_MetaDataTest.divBy5_remainder_on_(13, None, o)
        self.assertEquals(div, 13 / 7)
        self.assertEquals(rem, 13 % 7)

        self.assertRaises(ValueError, OC_MetaDataTest.divBy5_remainder_on_, 42, objc.NULL, o)

    def testInputOutput(self):
        o = Py_MetaDataTest_AllArgs.new()
        x, y = OC_MetaDataTest.swapX_andY_on_(42, 284, o)
        self.assertEquals(x, 284*2)
        self.assertEquals(y, 42*2)

        self.assertRaises(ValueError, OC_MetaDataTest.swapX_andY_on_, 42, objc.NULL, o)

    def testNullAccepted(self):
        # Note: the commented-out test-cases require a change in the pyobjc-core
        o = Py_MetaDataTest_AllArgs.new();

        def makeNum(value):
            return int(value, 0)

        # All arguments present
        r, y, z = OC_MetaDataTest.input_output_inputAndOutput_on_(1, None, 2, o)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(lambda x: x is not objc.NULL, r)), 3)
        self.assertEquals(y, 9)
        self.assertEquals(z, 10)

        r, y, z = OC_MetaDataTest.input_output_inputAndOutput_on_(1, None, 2, o)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(lambda x: x is not objc.NULL, r)), 3)
        self.assertEquals(y, 9)
        self.assertEquals(z, 10)

        # Argument 1 is NULL
        r, y, z = OC_MetaDataTest.input_output_inputAndOutput_on_(objc.NULL, None, 2, o)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(lambda x: x is not objc.NULL, r)), 2)
        self.assertEquals(y, 11)
        self.assertEquals(z, 12)

        r, y, z = OC_MetaDataTest.input_output_inputAndOutput_on_(objc.NULL, None, 2, o)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(lambda x: x is not objc.NULL, r)), 2)
        self.assertEquals(y, 11)
        self.assertEquals(z, 12)

        # Argument 2 is NULL
        r, y, z = OC_MetaDataTest.input_output_inputAndOutput_on_(1, objc.NULL, 2, o)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(lambda x: x is not objc.NULL, r)), 2)
        self.assertEquals(y, objc.NULL)
        self.assertEquals(z, 14)

        # Argument 3 is NULL
        r, y, z = OC_MetaDataTest.input_output_inputAndOutput_on_(1, None, objc.NULL, o)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(lambda x: x is not objc.NULL, r)), 2)
        self.assertEquals(y, 15)
        self.assertEquals(z, objc.NULL)

        r, y, z = OC_MetaDataTest.input_output_inputAndOutput_on_(1, None, objc.NULL, o)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(lambda x: x is not objc.NULL, r)), 2)
        self.assertEquals(y, 15)
        self.assertEquals(z, objc.NULL)

if __name__ == "__main__":
    main()
