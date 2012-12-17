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

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"make4Tuple:on:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_of_fixed_length=4, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"null4Tuple:on:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_of_fixed_length=4, null_accepted=True),
                }
            )
        )

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"makeObjectArray:on:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_delimited_by_null=True, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"makeStringArray:on:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_delimited_by_null=True, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"nullStringArray:on:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_delimited_by_null=True, null_accepted=True),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"makeIntArray:count:on:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_length_in_arg=2+1, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"makeIntArray:countPtr:on:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_length_in_arg=2+1, null_accepted=False),
                  2+1:  dict(type_modifier=objc._C_IN, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"nullIntArray:count:on:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_length_in_arg=2+1, null_accepted=True),
                }
            )
        )

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"fillArray:uptoCount:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_OUT, c_array_length_in_arg=2+1, c_array_length_in_result=True, null_accepted=False),
                }
            )
        )

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"fillArray:count:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_OUT, c_array_length_in_arg=2+1, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"nullfillArray:count:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_OUT, c_array_length_in_arg=2+1, null_accepted=True),
                }
            )
        )

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"maybeFillArray:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_OUT, c_array_of_fixed_length=4, c_array_length_in_result=True, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"fill4Tuple:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_OUT, c_array_of_fixed_length=4, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"nullfill4Tuple:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_OUT, c_array_of_fixed_length=4, null_accepted=True),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"fillStringArray:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_OUT, c_array_delimited_by_null=True, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"nullfillStringArray:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_OUT, c_array_delimited_by_null=True, null_accepted=True),
                }
            )
        )

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"reverseArray:uptoCount:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, c_array_length_in_arg=2+1, c_array_length_in_result=True, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"reverseArray:count:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, c_array_length_in_arg=2+1, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"nullreverseArray:count:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, c_array_length_in_arg=2+1, null_accepted=True),
                }
            )
        )

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"reverseStrings:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, c_array_delimited_by_null=True, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"nullreverseStrings:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, c_array_delimited_by_null=True, null_accepted=True),
                }
            )
        )

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"maybeReverseArray:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, c_array_of_fixed_length=4, c_array_length_in_result=True, null_accepted=True),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"reverse4Tuple:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, c_array_of_fixed_length=4, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"nullreverse4Tuple:on:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, c_array_of_fixed_length=4, null_accepted=True),
                }
            )
        )




    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"makeIntArrayOf5On:",
            dict(
                retval=dict(c_array_of_fixed_length=5)
            ),
        )

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"makeStringArrayOn:",
            dict(
                retval=dict(c_array_delimited_by_null=True),
            ),
        )

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"makeIntArrayOf:on:",
            dict(
                retval=dict(c_array_length_in_arg=2+0)
            ),
        )

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"nullIntArrayOf5On:",
            dict(
                retval=dict(c_array_of_fixed_length=5)
            ),
        )

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"nullStringArrayOn:",
            dict(
                retval=dict(c_array_delimited_by_null=True),
            ),
        )

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"nullIntArrayOf:on:",
            dict(
                retval=dict(c_array_length_in_arg=2+0)
            ),
        )


    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"sumX:andY:on:",
            dict(arguments={
                    2+0: dict(type_modifier=objc._C_IN, null_accepted=False),
                    2+1: dict(type_modifier=objc._C_IN, null_accepted=False),
                }))
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"divBy5:remainder:on:",
            dict(arguments={
                    2+1: dict(type_modifier=objc._C_OUT, null_accepted=False),
                }))
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"swapX:andY:on:",
            dict(arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, null_accepted=False),
                    2+1: dict(type_modifier=objc._C_INOUT, null_accepted=False),
                }))
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"input:output:inputAndOutput:on:",
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
        return [ b"jaap", b"pieter", b"hans" ]

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
    def makeStringArray_(self, data): return [[ x.decode('latin1') for x in data]]
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
            return int(count/2), range(10, 10 + int(count/2))
        else:
            return int(count/2), range(15, 15 + int(count/2))

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
        for i in range(int(len(data)/2)):
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
        self.assertEqual(list(v), list(range(9, 13)))

        v = OC_MetaDataTest.fill4Tuple_on_(None, o)
        self.assertEqual(list(v), list(range(9, 13)))

        self.assertRaises(ValueError, OC_MetaDataTest.fill4Tuple_on_, objc.NULL, o)

        n, v = OC_MetaDataTest.nullfill4Tuple_on_(None, o)
        self.assertEqual(n, 1)
        self.assertEqual(list(v), list(range(1, 5)))

        n, v = OC_MetaDataTest.nullfill4Tuple_on_(None, o)
        self.assertEqual(n, 1)
        self.assertEqual(list(v), list(range(1, 5)))

        n, v = OC_MetaDataTest.nullfill4Tuple_on_(objc.NULL, o)
        self.assertEqual(n, 2)
        self.assertIs(v, objc.NULL)

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
        self.assertEqual(n, 9)
        self.assertIs(v, objc.NULL)

    def testWithCount(self):
        o = Py_MetaDataTest_AllArgs.new()

        v = OC_MetaDataTest.fillArray_count_on_(None, 3, o)
        self.assertEqual(list(v),  [10, 11, 12])

        v = OC_MetaDataTest.fillArray_count_on_(None, 5, o)
        self.assertEqual(list(v),  [10, 11, 12, 13, 14])

        v = OC_MetaDataTest.fillArray_count_on_(None, 0, o)
        self.assertEqual(list(v),  [])

        self.assertRaises(ValueError, OC_MetaDataTest.fillArray_count_on_, objc.NULL, 0, o)

        n, v = OC_MetaDataTest.nullfillArray_count_on_(None, 3, o)
        self.assertEqual(n, 2)
        self.assertEqual(list(v),  [30,31,32])


        n, v = OC_MetaDataTest.nullfillArray_count_on_(objc.NULL, 3, o)
        self.assertEqual(n, 1)
        self.assertIs(v, objc.NULL)

    def testWithCountInResult(self):
        o = Py_MetaDataTest_AllArgs.new()

        c, v = OC_MetaDataTest.fillArray_uptoCount_on_(None, 20, o)
        self.assertEqual(c, 10)
        self.assertEqual(list(v),  [i+10 for i in range(10)])

        c, v = OC_MetaDataTest.maybeFillArray_on_(None, o)
        self.assertEqual(c, 2)
        self.assertEqual(list(v),  [0, 1])

class TestArraysInOut (TestCase):
    def testFixedSize(self):
        o = Py_MetaDataTest_AllArgs.new()

        a = (1,2,3,4)
        v = OC_MetaDataTest.reverse4Tuple_on_(a, o)
        self.assertEqual(a, (1,2,3,4))
        self.assertEqual(v, (43, 44, 45, 46))

        self.assertRaises(ValueError, OC_MetaDataTest.reverse4Tuple_on_, (1,2,3), o)
        self.assertRaises(ValueError, OC_MetaDataTest.reverse4Tuple_on_, (1,2,3,4,5), o)
        self.assertRaises(ValueError, OC_MetaDataTest.reverse4Tuple_on_, objc.NULL, o)

        a = (1,2,3,4)
        n, v = OC_MetaDataTest.nullreverse4Tuple_on_(a, o)
        self.assertEqual(n, 1)
        self.assertEqual(a, (1,2,3,4))
        self.assertEqual(v, (43, 44, 45, 46))

        n, v = OC_MetaDataTest.nullreverse4Tuple_on_(objc.NULL, o)
        self.assertEqual(n, -1)
        self.assertIs(v, objc.NULL)

    def testNullTerminated(self):
        o = Py_MetaDataTest_AllArgs.new()

        a = (b'aap', b'boot', b'cello')
        v = OC_MetaDataTest.reverseStrings_on_(a, o)
        self.assertEqual(a, (b'aap', b'boot', b'cello'))
        self.assertEqual(v, (b'paa', b'toob', b'ollec'))

        self.assertRaises(ValueError, OC_MetaDataTest.reverseStrings_on_, (1,2), o)
        self.assertRaises(ValueError, OC_MetaDataTest.reverseStrings_on_, objc.NULL, o)

        a = (b'aap', b'boot', b'cello')
        n, v = OC_MetaDataTest.nullreverseStrings_on_(a, o)
        self.assertEqual(n, 10)
        self.assertEqual(a, (b'aap', b'boot', b'cello'))
        self.assertEqual(v, (b'paa', b'toob', b'ollec'))

        n, v = OC_MetaDataTest.nullreverseStrings_on_(objc.NULL, o)
        self.assertEqual(n, 9)
        self.assertIs(v, objc.NULL)

    def testWithCount(self):
        o = Py_MetaDataTest_AllArgs.new()

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        v = OC_MetaDataTest.reverseArray_count_on_(a, 4, o)
        self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEqual(v, (2.0, 3.0, 4.0, 5.0))

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        v = OC_MetaDataTest.reverseArray_count_on_(a, 5, o)
        self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEqual(v, (2.0, 3.0, 4.0, 5.0, 6.0))

        # Nice to have, but doesn't work without major
        # surgery:
        #a = (1.0, 2.0, 3.0, 4.0, 5.0)
        #v = OC_MetaDataTest.reverseArray_count_on_(a, None, o)
        #self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        #self.assertEqual(v, (2.0, 3.0, 4.0, 5.0, 6.0))

        self.assertRaises(ValueError, OC_MetaDataTest.reverseArray_count_on_, (1.0, 2.0), 5, o)
        self.assertRaises(ValueError, OC_MetaDataTest.reverseArray_count_on_, objc.NULL, 0, o)

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        n, v = OC_MetaDataTest.nullreverseArray_count_on_(a, 5, o)
        self.assertEqual(n, 9)
        self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEqual(v, (43.0, 44.0, 45.0, 46.0, 47.0))

        n, v = OC_MetaDataTest.nullreverseArray_count_on_(objc.NULL, 0, o)
        self.assertEqual(n, 2)
        self.assertIs(v, objc.NULL)

    def testWithCountInResult(self):
        o = Py_MetaDataTest_AllArgs.new()

        c, v = OC_MetaDataTest.reverseArray_uptoCount_on_(range(10), 10, o)
        self.assertEqual(c, 5)
        self.assertEqual(len(v), 5)
        self.assertEqual(list(v),  [0, 10, 20, 30, 40])

        c, v = OC_MetaDataTest.maybeReverseArray_on_([1,2,3,4], o)
        self.assertEqual(c, 2)
        self.assertEqual(len(v), 2)
        self.assertEqual(list(v),  [45, 51])

class TestArraysIn (TestCase):
    def testFixedSize(self):
        o = Py_MetaDataTest_AllArgs.new()

        v,  = OC_MetaDataTest.make4Tuple_on_((1.0, 4.0, 8.0, 12.5), o)
        self.assertEqual(len(v), 4)
        self.assertEqual(list(v), [1.0, 4.0, 8.0, 12.5])

        v, = OC_MetaDataTest.make4Tuple_on_((1, 2, 3, 4), o)
        self.assertEqual(len(v), 4)
        self.assertEqual(list(v), [1.0, 2.0, 3.0, 4.0])

        self.assertRaises(ValueError, OC_MetaDataTest.make4Tuple_on_, (1, 2, 3), o)
        self.assertRaises(ValueError, OC_MetaDataTest.make4Tuple_on_, (1, 2, 3, 4, 5), o)
        self.assertRaises(ValueError, OC_MetaDataTest.make4Tuple_on_, objc.NULL, o)

        v, = OC_MetaDataTest.null4Tuple_on_(objc.NULL, o)
        self.assertIs(v, objc.NULL)

    def testNullTerminated(self):
        o = Py_MetaDataTest_AllArgs.new()

        v, = OC_MetaDataTest.makeStringArray_on_((b"hello", b"world", b"there"), o)
        self.assertEqual(len(v), 3)
        self.assertEqual(list(v), ["hello", "world", "there"])

        NSObject = objc.lookUpClass('NSObject')
        p, q = NSObject.new(), NSObject.new()
        v, = o.makeObjectArray_((p, q))
        self.assertEqual(len(v), 2)
        self.assertIs(v[0], p)
        self.assertIs(v[1], q)

        v, = OC_MetaDataTest.makeStringArray_on_((), o)
        self.assertEqual(len(v), 0)

        self.assertRaises(ValueError, OC_MetaDataTest.makeStringArray_on_, [1,2], o)
        self.assertRaises(ValueError, OC_MetaDataTest.makeStringArray_on_, objc.NULL, o)

        v, = OC_MetaDataTest.nullStringArray_on_(objc.NULL, o)
        self.assertEqual(v, objc.NULL)

    def testWithCount(self):
        o = Py_MetaDataTest_AllArgs.new()

        v, c = OC_MetaDataTest.makeIntArray_count_on_((1,2,3,4), 3, o)
        self.assertEqual(c, 3)
        self.assertEqual(len(v), 3)
        self.assertEqual(list(v), [1,2,3])

        # XXX: This one would be nice to have, but not entirely trivial
        #v, c = OC_MetaDataTest.makeIntArray_count_on_((1,2,3,4), None, o)
        #self.assertEqual(c, 3)
        #self.assertEqual(len(v), 3)
        #self.assertEqual(list(v), [1,2,3,4])

        self.assertRaises(ValueError, OC_MetaDataTest.makeIntArray_count_on_, [1,2,3], 4, o)
        self.assertRaises(ValueError, OC_MetaDataTest.makeIntArray_count_on_, objc.NULL, 0, o)
        self.assertRaises(ValueError, OC_MetaDataTest.makeIntArray_count_on_, objc.NULL, 1, o)

        v, c = OC_MetaDataTest.nullIntArray_count_on_(objc.NULL, 0, o)
        self.assertEqual(c, 0)
        self.assertEqual(v, objc.NULL)

        self.assertRaises(ValueError, OC_MetaDataTest.makeIntArray_count_on_, objc.NULL, 1, o)

        # Make sure this also works when the length is in a pass-by-reference argument
        v, c = OC_MetaDataTest.makeIntArray_countPtr_on_((1,2,3,4), 4, o)
        self.assertEqual(c, 4)
        self.assertEqual(len(v), 4)
        self.assertEqual(list(v), [1,2,3,4])

class TestArrayReturns (TestCase):
    # TODO:
    # - Add null-terminated arrays of various supported types:
    #   -> integers
    #   -> CF-types
    def testFixedSize(self):
        o = Py_MetaDataTest_AllArgs.new()

        v = OC_MetaDataTest.makeIntArrayOf5On_(o)
        self.assertEqual( len(v), 5 )
        self.assertEqual( list(v), [100, 200, 300, 400, 500] )

        v = OC_MetaDataTest.nullIntArrayOf5On_(o)
        self.assertEqual(v, objc.NULL)

    def testSizeInArgument(self):
        o = Py_MetaDataTest_AllArgs.new()
        v = OC_MetaDataTest.makeIntArrayOf_on_(3, o)
        self.assertEqual(len(v), 3)
        self.assertEqual(list(v), [20, 21, 22])

        v = OC_MetaDataTest.makeIntArrayOf_on_(10, o)
        self.assertEqual(len(v), 10)
        self.assertEqual(list(v), list(range(20, 30)))

        v = OC_MetaDataTest.nullIntArrayOf_on_(100, o)
        self.assertEqual(v, objc.NULL)

    def testNULLterminated(self):
        o  = Py_MetaDataTest_AllArgs.new()

        v = OC_MetaDataTest.makeStringArrayOn_(o)
        self.assertEqual(len(v), 3)
        self.assertEqual(list(v), [ b"jaap", b"pieter", b"hans" ])

        v = OC_MetaDataTest.nullStringArrayOn_(o)
        self.assertEqual(v, objc.NULL)

class TestByReference (TestCase):
    # Pass by reference arguments.
    # Note that these tests aren't exhaustive, we have test_methods and
    # test_methods2 for that :-)

    def testInput(self):
        o = Py_MetaDataTest_AllArgs.new()

        r = OC_MetaDataTest.sumX_andY_on_(1, 2, o)
        self.assertEqual(r, 1**2+2**2)

        r = OC_MetaDataTest.sumX_andY_on_(2535, 5325, o)
        self.assertEqual(r, 2535**2 + 5325**2)

        self.assertRaises(ValueError, OC_MetaDataTest.sumX_andY_on_, 42, objc.NULL, o)

    def testOutput(self):
        o = Py_MetaDataTest_AllArgs.new()

        div, rem = OC_MetaDataTest.divBy5_remainder_on_(55, None, o)
        self.assertEqual(div, int(55 / 7))
        self.assertEqual(rem, int(55 % 7))

        div, rem = OC_MetaDataTest.divBy5_remainder_on_(13, None, o)
        self.assertEqual(div, int(13 / 7))
        self.assertEqual(rem, int(13 % 7))

        self.assertRaises(ValueError, OC_MetaDataTest.divBy5_remainder_on_, 42, objc.NULL, o)

    def testInputOutput(self):
        o = Py_MetaDataTest_AllArgs.new()
        x, y = OC_MetaDataTest.swapX_andY_on_(42, 284, o)
        self.assertEqual(x, 284*2)
        self.assertEqual(y, 42*2)

        self.assertRaises(ValueError, OC_MetaDataTest.swapX_andY_on_, 42, objc.NULL, o)

    def testNullAccepted(self):
        # Note: the commented-out test-cases require a change in the pyobjc-core
        o = Py_MetaDataTest_AllArgs.new();

        def makeNum(value):
            return int(value, 0)

        # All arguments present
        r, y, z = OC_MetaDataTest.input_output_inputAndOutput_on_(1, None, 2, o)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(lambda x: x is not objc.NULL, r))), 3)
        self.assertEqual(y, 9)
        self.assertEqual(z, 10)

        r, y, z = OC_MetaDataTest.input_output_inputAndOutput_on_(1, None, 2, o)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(lambda x: x is not objc.NULL, r))), 3)
        self.assertEqual(y, 9)
        self.assertEqual(z, 10)

        # Argument 1 is NULL
        r, y, z = OC_MetaDataTest.input_output_inputAndOutput_on_(objc.NULL, None, 2, o)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(lambda x: x is not objc.NULL, r))), 2)
        self.assertEqual(y, 11)
        self.assertEqual(z, 12)

        r, y, z = OC_MetaDataTest.input_output_inputAndOutput_on_(objc.NULL, None, 2, o)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(lambda x: x is not objc.NULL, r))), 2)
        self.assertEqual(y, 11)
        self.assertEqual(z, 12)

        # Argument 2 is NULL
        r, y, z = OC_MetaDataTest.input_output_inputAndOutput_on_(1, objc.NULL, 2, o)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(lambda x: x is not objc.NULL, r))), 2)
        self.assertEqual(y, objc.NULL)
        self.assertEqual(z, 14)

        # Argument 3 is NULL
        r, y, z = OC_MetaDataTest.input_output_inputAndOutput_on_(1, None, objc.NULL, o)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(lambda x: x is not objc.NULL, r))), 2)
        self.assertEqual(y, 15)
        self.assertEqual(z, objc.NULL)

        r, y, z = OC_MetaDataTest.input_output_inputAndOutput_on_(1, None, objc.NULL, o)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(lambda x: x is not objc.NULL, r))), 2)
        self.assertEqual(y, 15)
        self.assertEqual(z, objc.NULL)

if __name__ == "__main__":
    main()
