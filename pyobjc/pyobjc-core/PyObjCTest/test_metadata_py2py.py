"""
Tests for the new-style metadata format interface.

Note: Tests for calling from python into ObjC are in test_metadata.py

TODO:
-> OutputOptional version for TestByReference
-> Testcode might need changes, C code definitely needs changes

- Add more testcases: python methods that return the wrong value
- The python->C interface (that is the contents of the metadata object) is
  likely to change when the bridge is feature-complete.
- Probably need special-casing for arrays (numarray and array.array)!
"""
import objc
from PyObjCTools.TestSupport import *

from PyObjCTest.metadata import *

# To ensure we have the right metadata
import PyObjCTest.test_metadata
from PyObjCTest.test_metadata_py import Py_MetaDataTest_AllArgs

if 0:
    from PyObjCTest.test_metadata_py2 import Py_MetaDataTest_OutputOptional

class TestArraysOut_AllArgs (TestCase):
    def testFixedSize(self):
        o = Py_MetaDataTest_AllArgs.new()

        v = o.fill4Tuple_()
        self.assertEquals(list(v), list(range(9, 13)))

        v = o.fill4Tuple_(None)
        self.assertEquals(list(v), list(range(9, 13)))

        self.assertRaises(ValueError, OC_MetaDataTest.fill4Tuple_on_, objc.NULL, o)

        n, v = o.nullfill4Tuple_()
        self.assertEquals(n, 1)
        self.assertEquals(list(v), list(range(1, 5)))

        n, v = o.nullfill4Tuple_(None)
        self.assertEquals(n, 1)
        self.assertEquals(list(v), list(range(1, 5)))

        n, v = o.nullfill4Tuple_(objc.NULL)
        self.assertEquals(n, 2)
        #self.assertIs(v, objc.NULL )
        
    def testNullTerminated(self):
        o = Py_MetaDataTest_AllArgs.new()

        # Output only arrays of null-terminated arrays cannot be
        # wrapped automaticly. How is the bridge supposed to know
        # how much memory it should allocate for the C-array?

        #self.assertRaises(TypeError, o.fillStringArray_)
        #self.assertRaises(TypeError, o.fillStringArray_, None)
        #self.assertRaises(ValueError, o.fillStringArray_, objc.NULL)

        #self.assertRaises(TypeError, o.nullfillStringArray_)
        #self.assertRaises(TypeError, o.nullfillStringArray_, None)
        n, v = o.nullfillStringArray_(objc.NULL)
        self.assertEquals(n, 9)
        self.assertIs(v, objc.NULL)

    def testWithCount(self):
        o = Py_MetaDataTest_AllArgs.new()

        v = o.fillArray_count_(3)
        self.assertEquals(list(v),  [10, 11, 12])

        v = o.fillArray_count_(None, 3)
        self.assertEquals(list(v),  [10, 11, 12])

        v = o.fillArray_count_(5)
        self.assertEquals(list(v),  [10, 11, 12, 13, 14])

        v = o.fillArray_count_(0)
        self.assertEquals(list(v),  [])

        #self.assertRaises(ValueError, o.fillArray_count_, objc.NULL, 0)
        
        n, v = o.nullfillArray_count_(3)
        self.assertEquals(n, 2)
        self.assertEquals(list(v),  [30,31,32])
        n, v = o.nullfillArray_count_(None, 3)
        self.assertEquals(n, 2)
        self.assertEquals(list(v),  [30,31,32])

        n, v = o.nullfillArray_count_(objc.NULL, 3)
        self.assertEquals(n, 1)
        #self.assertIs(v, objc.NULL )

    def testWithCountInResult(self):
        o = Py_MetaDataTest_AllArgs.new()

        c, v = o.fillArray_uptoCount_(20)
        self.assertEquals(c, 10)
        self.assertEquals(list(v),  [i+10 for i in range(10)])

        c, v = o.maybeFillArray_()
        self.assertEquals(c, 2)
        self.assertEquals(list(v),  [0, 1])

if 0:
    class TestArraysOut_OutputOptional (TestCase):
        def testFixedSize(self):
            o = Py_MetaDataTest_OutputOptional.new()

            v = o.fill4Tuple_()
            self.assertEquals(list(v), list(range(9, 13)))

            v = o.fill4Tuple_(None)
            self.assertEquals(list(v), list(range(9, 13)))

            self.assertRaises(ValueError, OC_MetaDataTest.fill4Tuple_on_, objc.NULL, o)

            n, v = o.nullfill4Tuple_()
            self.assertEquals(n, 1)
            self.assertEquals(list(v), list(range(1, 5)))

            n, v = o.nullfill4Tuple_(None)
            self.assertEquals(n, 1)
            self.assertEquals(list(v), list(range(1, 5)))

            n, v = o.nullfill4Tuple_(objc.NULL)
            #self.assertEquals(n, 2)
            #self.assertIs(v, objc.NULL)
            
        def testNullTerminated(self):
            o = Py_MetaDataTest_OutputOptional.new()

            # Output only arrays of null-terminated arrays cannot be
            # wrapped automaticly. How is the bridge supposed to know
            # how much memory it should allocate for the C-array?

            #self.assertRaises(TypeError, o.fillStringArray_)
            #self.assertRaises(TypeError, o.fillStringArray_, None)
            #self.assertRaises(ValueError, o.fillStringArray_, objc.NULL)

            #self.assertRaises(TypeError, o.nullfillStringArray_)
            #self.assertRaises(TypeError, o.nullfillStringArray_, None)
            #n, v = o.nullfillStringArray_(objc.NULL)
            #self.assertEquals(n, 9)
            #self.assertIs(v, objc.NULL)

        def testWithCount(self):
            o = Py_MetaDataTest_OutputOptional.new()

            v = o.fillArray_count_(3)
            self.assertEquals(list(v),  [10, 11, 12])

            v = o.fillArray_count_(None, 3)
            self.assertEquals(list(v),  [10, 11, 12])

            v = o.fillArray_count_(5)
            self.assertEquals(list(v),  [10, 11, 12, 13, 14])

            v = o.fillArray_count_(0)
            self.assertEquals(list(v),  [])

            #self.assertRaises(ValueError, o.fillArray_count_, objc.NULL, 0)
            
            n, v = o.nullfillArray_count_(3)
            self.assertEquals(n, 2)
            self.assertEquals(list(v),  [30,31,32])
            n, v = o.nullfillArray_count_(None, 3)
            self.assertEquals(n, 2)
            self.assertEquals(list(v),  [30,31,32])

            n, v = o.nullfillArray_count_(objc.NULL, 3)
            #self.assertEquals(n, 1)
            #self.assertIs(v, objc.NULL)

        def testWithCountInResult(self):
            o = Py_MetaDataTest_OutputOptional.new()

            c, v = o.fillArray_uptoCount_(20)
            self.assertEquals(c, 10)
            self.assertEquals(list(v),  [i+10 for i in range(10)])

            c, v = o.maybeFillArray_()
            self.assertEquals(c, 2)
            self.assertEquals(list(v),  [0, 1])

class TestArraysInOut_AllArgs (TestCase):
    def testFixedSize(self):
        o = Py_MetaDataTest_AllArgs.new()

        a = (1,2,3,4)
        v = o.reverse4Tuple_(a)
        self.assertEquals(a, (1,2,3,4))
        self.assertEquals(list(v), [43, 44, 45, 46])

        #self.assertRaises(ValueError, o.reverse4Tuple_, (1,2,3))
        #self.assertRaises(ValueError, o.reverse4Tuple_, (1,2,3,4,5))
        #self.assertRaises(ValueError, o.reverse4Tuple_, objc.NULL)

        a = (1,2,3,4)
        n, v = o.nullreverse4Tuple_(a)
        self.assertEquals(n, 1)
        self.assertEquals(a, (1,2,3,4))
        self.assertEquals(list(v), [43, 44, 45, 46])

        n, v = o.nullreverse4Tuple_(objc.NULL)
        self.assertEquals(n, -1)
        self.assertIs(v, objc.NULL)

    def testNullTerminated(self):
        o = Py_MetaDataTest_AllArgs.new()

        a = ('aap', 'boot', 'cello')
        v = o.reverseStrings_(a)
        self.assertEquals(a, ('aap', 'boot', 'cello'))
        self.assertEquals(list(v), ['paa', 'toob', 'ollec'])

        #self.assertRaises(ValueError, o.reverseStrings_, (1,2))
        #self.assertRaises(ValueError, o.reverseStrings_, objc.NULL)

        a = ('aap', 'boot', 'cello')
        n, v = o.nullreverseStrings_(a)
        self.assertEquals(n, 10)
        self.assertEquals(a, ('aap', 'boot', 'cello'))
        self.assertEquals(list(v), ['paa', 'toob', 'ollec'])

        n, v = o.nullreverseStrings_(objc.NULL)
        self.assertEquals(n, 9)
        self.assertIs(v, objc.NULL)

    def testWithCount(self):
        o = Py_MetaDataTest_AllArgs.new()

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        v = o.reverseArray_count_(a, 4)
        self.assertEquals(a, (1.0, 2.0, 3.0, 4.0, 5.0))

        # Python->python: same semantics as normal python calls, therefore
        # the result is 5 long, and there is 2 added to the result (that is
        # the method sees the actual argument array instead of a truncated one)
        self.assertEquals(list(v[:4]), [3.0, 4.0, 5.0, 6.0])

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        v = o.reverseArray_count_(a, 5)
        self.assertEquals(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEquals(list(v), [2.0, 3.0, 4.0, 5.0, 6.0])

        # Nice to have, but doesn't work without major
        # surgery:
        #a = (1.0, 2.0, 3.0, 4.0, 5.0)
        #v = o.reverseArray_count_(a, None)
        #self.assertEquals(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        #self.assertEquals(v, (2.0, 3.0, 4.0, 5.0, 6.0))

        #self.assertRaises(ValueError, o.reverseArray_count_, (1.0, 2.0), 5)
        #self.assertRaises(ValueError, o.reverseArray_count_, objc.NULL, 0)

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        n, v = o.nullreverseArray_count_(a, 5)
        self.assertEquals(n, 9)
        self.assertEquals(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEquals(list(v), [43.0, 44.0, 45.0, 46.0, 47.0])

        n, v = o.nullreverseArray_count_(objc.NULL, 0)
        self.assertEquals(n, 2)
        self.assertIs(v, objc.NULL)

    def testWithCountInResult(self):
        o = Py_MetaDataTest_AllArgs.new()
        
        # XXX: caling python->python has the usual python semantics, hence
        # the argument won't be truncated!
        c, v = o.reverseArray_uptoCount_(range(10), 10)
        self.assertEquals(c, 5)
        self.assertEquals(len(v), 10)
        self.assertEquals(list(v)[:int(c)],  [0, 10, 20, 30, 40])
        
        c, v = o.maybeReverseArray_([1,2,3,4])
        self.assertEquals(c, 2)
        self.assertEquals(len(v), 2)
        self.assertEquals(list(v),  [45, 51])

class TestArraysIn_AllArgs (TestCase):
    def testFixedSize(self):
        o = Py_MetaDataTest_AllArgs.new()

        v,  = o.make4Tuple_((1.0, 4.0, 8.0, 12.5))
        self.assertEquals(len(v), 4)
        self.assertEquals(list(v), [1.0, 4.0, 8.0, 12.5])

        v, = o.make4Tuple_((1, 2, 3, 4))
        self.assertEquals(len(v), 4)
        self.assertEquals(list(v), [1.0, 2.0, 3.0, 4.0])

        # XXX: Calling python->python has a the same semantics as a normal
        # python call.
        #self.assertRaises(ValueError, o.make4Tuple_, (1, 2, 3))
        #self.assertRaises(ValueError, o.make4Tuple_, (1, 2, 3, 4, 5))
        #self.assertRaises(ValueError, o.make4Tuple_, objc.NULL)

        v, = o.null4Tuple_(objc.NULL)
        self.assertIs(v, objc.NULL)

    def testNullTerminated(self):
        o = Py_MetaDataTest_AllArgs.new()

        v, = OC_MetaDataTest.makeStringArray_on_((b"hello", b"world", b"there"), o)
        self.assertEquals(len(v), 3)
        self.assertEquals(list(v), ["hello", "world", "there"])

        NSObject = objc.lookUpClass('NSObject')
        p, q = NSObject.new(), NSObject.new()
        v, = o.makeObjectArray_((p, q))
        self.assertEquals(len(v), 2)
        self.assertIs(v[0], p)
        self.assertIs(v[1], q)

        v, = OC_MetaDataTest.makeStringArray_on_((), o)
        self.assertEquals(len(v), 0)

        self.assertRaises(ValueError, OC_MetaDataTest.makeStringArray_on_, [1,2], o)
        self.assertRaises(ValueError, OC_MetaDataTest.makeStringArray_on_, objc.NULL, o)

        v, = OC_MetaDataTest.nullStringArray_on_(objc.NULL, o)
        self.assertEquals(v, objc.NULL)

    def testWithCount(self):
        o = Py_MetaDataTest_AllArgs.new()

        v, c = o.makeIntArray_count_((1,2,3,4), 3)
        self.assertEquals(c, 3)

        # Calling python -> python doesn't pass through C, hence the usual
        # python semantics are used which are slightly different from calling
        # into C or from C.
        self.assertEquals(len(v), 4)
        self.assertEquals(list(v)[:c], [1,2,3])
        
        # XXX: This one would be nice to have, but not entirely trivial
        #v, c = o.makeIntArray_count_((1,2,3,4), None)
        #self.assertEquals(c, 3)
        #self.assertEquals(len(v), 3)
        #self.assertEquals(list(v), [1,2,3,4])

        # See above
        #self.assertRaises(ValueError, o.makeIntArray_count_, [1,2,3], 4)
        #self.assertRaises(ValueError, o.makeIntArray_count_, objc.NULL, 0)
        #self.assertRaises(ValueError, o.makeIntArray_count_, objc.NULL, 1)

        v, c = o.nullIntArray_count_(objc.NULL, 0)
        self.assertEquals(c, 0)
        self.assertEquals(v, objc.NULL)

        # See above
        #self.assertRaises(ValueError, o.makeIntArray_count_, objc.NULL, 1)

        # Make sure this also works when the length is in a pass-by-reference argument
        v, c = o.makeIntArray_countPtr_((1,2,3,4), 4)
        self.assertEquals(c, 4)
        self.assertEquals(len(v), 4)
        self.assertEquals(list(v), [1,2,3,4])

class TestArrayReturns_AllArgs (TestCase):
    # TODO:
    # - Add null-terminated arrays of various supported types:
    #   -> integers
    #   -> CF-types
    def testFixedSize(self):
        o = Py_MetaDataTest_AllArgs.new()

        v = o.makeIntArrayOf5()
        self.assertEquals( len(v), 5 )
        self.assertEquals( list(v), [100, 200, 300, 400, 500] )

        v = o.nullIntArrayOf5()
        self.assertEquals(v, objc.NULL)

    def testSizeInArgument(self):
        o = Py_MetaDataTest_AllArgs.new()
        v = o.makeIntArrayOf_(3)
        self.assertEquals(len(v), 3)
        self.assertEquals(list(v), [20, 21, 22])

        v = o.makeIntArrayOf_(10)
        self.assertEquals(len(v), 10)
        self.assertEquals(list(v), list(range(20, 30)))

        v = o.nullIntArrayOf_(100)
        self.assertEquals(v, objc.NULL)

    def testNULLterminated(self):
        o  = Py_MetaDataTest_AllArgs.new()

        v = o.makeStringArray()
        self.assertEquals(len(v), 3)
        self.assertEquals(list(v), [ b"jaap", b"pieter", b"hans" ])

        v = o.nullStringArray()
        self.assertEquals(v, objc.NULL)

class TestByReference_AllArgs (TestCase):
    # Pass by reference arguments. 
    # Note that these tests aren't exhaustive, we have test_methods and
    # test_methods2 for that :-)

    def testInput(self):
        o = Py_MetaDataTest_AllArgs.new()
        
        r = o.sumX_andY_(1, 2)
        self.assertEquals(r, 1**2+2**2)

        r = o.sumX_andY_(2535, 5325)
        self.assertEquals(r, 2535**2 + 5325**2)

        #self.assertRaises(ValueError, o.sumX_andY_, 42, objc.NULL)

    def testOutput(self):
        o = Py_MetaDataTest_AllArgs.new()

        div, rem = o.divBy5_remainder_(55)
        self.assertEquals(div, 55 / 7)
        self.assertEquals(rem, 55 % 7)

        div, rem = o.divBy5_remainder_(13)
        self.assertEquals(div, 13 / 7)
        self.assertEquals(rem, 13 % 7)

        # XXX: To be fixed: 
        #self.assertRaises(ValueError, o.divBy5_remainder_, 42, objc.NULL)

    def testInputOutput(self):
        o = Py_MetaDataTest_AllArgs.new()
        x, y = o.swapX_andY_(42, 284)
        self.assertEquals(x, 284*2)
        self.assertEquals(y, 42*2)

        #self.assertRaises(ValueError, o.swapX_andY_, 42, objc.NULL)

    def testNullAccepted(self):
        # Note: the commented-out test-cases require a change in the pyobjc-core
        o = Py_MetaDataTest_AllArgs.new();

        def makeNum(value):
            return int(value, 0)

        # All arguments present
        r, y, z = o.input_output_inputAndOutput_(1, 2)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(lambda x: x is not objc.NULL, r)), 3)
        self.assertEquals(y, 9)
        self.assertEquals(z, 10)

        r, y, z = o.input_output_inputAndOutput_(1, None, 2)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(lambda x: x is not objc.NULL, r)), 3)
        self.assertEquals(y, 9)
        self.assertEquals(z, 10)

        # Argument 1 is NULL
        r, y, z = o.input_output_inputAndOutput_(objc.NULL, 2)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(lambda x: x is not objc.NULL, r)), 2)
        self.assertEquals(y, 11)
        self.assertEquals(z, 12)

        r, y, z = o.input_output_inputAndOutput_(objc.NULL, None, 2)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(lambda x: x is not objc.NULL, r)), 2)
        self.assertEquals(y, 11)
        self.assertEquals(z, 12)

        # Argument 2 is NULL
        r, y, z = o.input_output_inputAndOutput_(1, objc.NULL, 2)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(lambda x: x is not objc.NULL, r)), 2)
        self.assertEquals(y, 13) # objc.NULL ...
        self.assertEquals(z, 14)

        # Argument 3 is NULL
        r, y, z = o.input_output_inputAndOutput_(1, objc.NULL)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(lambda x: x is not objc.NULL, r)), 2)
        self.assertEquals(y, 15)
        self.assertEquals(z, 16) # objc.NULL ...

        r, y, z = o.input_output_inputAndOutput_(1, None, objc.NULL)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(lambda x: x is not objc.NULL, r)), 2)
        self.assertEquals(y, 15)
        self.assertEquals(z, 16) # , objc.NULL)

if __name__ == "__main__":
    main()
