"""
Tests for the new-style metadata format interface.

These tests are for global function
"""
import objc
from PyObjCTools.TestSupport import *
import warnings

from PyObjCTest.metadatafunction import *

_FunctionTable = [
    (u"makeArrayWithFormat_", b'@@', '',
            dict(
                variadic=True,
                arguments={
                    0: dict(printf_format=True),
                }
            )),

    (u"makeArrayWithCFormat_", b'@*', '',
            dict(
                variadic=True,
                arguments={
                    0: dict(printf_format=True),
                }
            )),

    (u"make4Tuple_", b'@^d', '',
            dict(
                arguments={
                  0:  dict(type_modifier=objc._C_IN, c_array_of_fixed_length=4, null_accepted=False),
                }
            )),

    (u"null4Tuple_", b'@^d', '',
            dict(
                arguments={
                  0:  dict(type_modifier=objc._C_IN, c_array_of_fixed_length=4, null_accepted=True),
                }
            )),

    (u"makeObjectArray_", b'@^@', '',
            dict(
                arguments={
                  0:  dict(type_modifier=objc._C_IN, c_array_delimited_by_null=True, null_accepted=False),
                }
            )),

    (u"makeStringArray_", b'@^*', '',
            dict(
                arguments={
                  0:  dict(type_modifier=objc._C_IN, c_array_delimited_by_null=True, null_accepted=False),
                }
            )),

    (u"nullStringArray_", b'@^*', '',
            dict(
                arguments={
                  0:  dict(type_modifier=objc._C_IN, c_array_delimited_by_null=True, null_accepted=True),
                }
            )),

    (u"makeIntArray_count_", b'@^iI', '',
            dict(
                arguments={
                  0:  dict(type_modifier=objc._C_IN, c_array_length_in_arg=1, null_accepted=False),
                }
            )),

    (u"makeIntArray_countPtr_", b'@^i^I', '',
            dict(
                arguments={
                  0:  dict(type_modifier=objc._C_IN, c_array_length_in_arg=1, null_accepted=False),
                  1:  dict(type_modifier=objc._C_IN),
                }
            )),

    (u"nullIntArray_count_", b'@^iI', '',
            dict(
                arguments={
                  0:  dict(type_modifier=objc._C_IN, c_array_length_in_arg=1, null_accepted=True),
                }
            )),

    (u"fillArray_uptoCount_", b'i^ii', '',
            dict(
                arguments={
                    0: dict(type_modifier=objc._C_OUT, c_array_length_in_arg=1, c_array_length_in_result=True, null_accepted=False),
                }
            )),

    (u"fillArray_count_", b'v^ii', '',
            dict(
                arguments={
                    0: dict(type_modifier=objc._C_OUT, c_array_length_in_arg=1, null_accepted=False),
                }
            )),

    (u"nullfillArray_count_", b'i^ii', '',
            dict(
                arguments={
                    0: dict(type_modifier=objc._C_OUT, c_array_length_in_arg=1, null_accepted=True),
                }
            )),

    (u"maybeFillArray_", b'i^i', '',
            dict(
                arguments={
                    0: dict(type_modifier=objc._C_OUT, c_array_of_fixed_length=4, c_array_length_in_result=True, null_accepted=False),
                }
            )),

    (u"fill4Tuple_", b'v^i', '',
            dict(
                arguments={
                    0: dict(type_modifier=objc._C_OUT, c_array_of_fixed_length=4, null_accepted=False),
                }
            )),

    (u"nullfill4Tuple_", b'i^i', '',
            dict(
                arguments={
                    0: dict(type_modifier=objc._C_OUT, c_array_of_fixed_length=4, null_accepted=True),
                }
            )),

    (u"fillStringArray_", b'i^*', '',
            dict(
                arguments={
                    0: dict(type_modifier=objc._C_OUT, c_array_delimited_by_null=True, null_accepted=False),
                }
            )),

    (u"nullfillStringArray_", b'i^*', '',
            dict(
                arguments={
                    0: dict(type_modifier=objc._C_OUT, c_array_delimited_by_null=True, null_accepted=True),
                }
            )),

    (u"reverseArray_uptoCount_", b'i^fi', '',
            dict(
                arguments={
                    0: dict(type_modifier=objc._C_INOUT, c_array_length_in_arg=1, c_array_length_in_result=True, null_accepted=False),
                }
            )),

    (u"reverseArray_count_", b'v^fi', '',
            dict(
                arguments={
                    0: dict(type_modifier=objc._C_INOUT, c_array_length_in_arg=1, null_accepted=False),
                }
            )),

    (u"nullreverseArray_count_", b'i^fi', '',
            dict(
                arguments={
                    0: dict(type_modifier=objc._C_INOUT, c_array_length_in_arg=1, null_accepted=True),
                }
            )),

    (u"reverseStrings_", b'v^*', '',
            dict(
                arguments={
                    0: dict(type_modifier=objc._C_INOUT, c_array_delimited_by_null=True, null_accepted=False),
                }
            )),

    (u"nullreverseStrings_", b'i^*', '',
            dict(
                arguments={
                    0: dict(type_modifier=objc._C_INOUT, c_array_delimited_by_null=True, null_accepted=True),
                }
            )),

    (u"maybeReverseArray_", b'i^s', '',
            dict(
                arguments={
                    0: dict(type_modifier=objc._C_INOUT, c_array_of_fixed_length=4, c_array_length_in_result=True, null_accepted=False),
                }
            )),

    (u"reverse4Tuple_", b'v^s', '',
            dict(
                arguments={
                    0: dict(type_modifier=objc._C_INOUT, c_array_of_fixed_length=4, null_accepted=False),
                }
            )),

    (u"nullreverse4Tuple_", b'i^s', '',
            dict(
                arguments={
                    0: dict(type_modifier=objc._C_INOUT, c_array_of_fixed_length=4, null_accepted=True),
                }
            )),

    (u"makeIntArrayOf5", b'^i', '',
            dict(
                retval=dict(c_array_of_fixed_length=5)
            )),

    (u"makeStringArray", b'^*', '',
            dict(
                retval=dict(c_array_delimited_by_null=True),
            )),

    (u"makeIntArrayOf_", b'^ii', '',
            dict(
                retval=dict(c_array_length_in_arg=0)
            )),

    (u"nullIntArrayOf5", b'^i', '',
            dict(
                retval=dict(c_array_of_fixed_length=5)
            )),

    (u"nullStringArray", b'^*', '',
            dict(
                retval=dict(c_array_delimited_by_null=True),
            )),

    (u"nullIntArrayOf_", b'^ii',  '',
            dict(
                retval=dict(c_array_length_in_arg=0)
            )),


    (u"sumX_andY_",  b'i^i^i', '',
            dict(arguments={
                    0: dict(type_modifier=objc._C_IN, null_accepted=False),
                    1: dict(type_modifier=objc._C_IN, null_accepted=False),
                })),

    (u"divBy5_remainder_",  b'ii^i', '',
            dict(arguments={
                    1: dict(type_modifier=objc._C_OUT, null_accepted=False),
                })),

    (u"swapX_andY_", b'v^d^d', '',
            dict(arguments={
                    0: dict(type_modifier=objc._C_INOUT, null_accepted=False),
                    1: dict(type_modifier=objc._C_INOUT, null_accepted=False),
                })),

    (u"input_output_inputAndOutput_", b'@^i^i^i', '',
            dict(arguments={
                    0: dict(type_modifier=objc._C_IN, null_accepted=True),
                    1: dict(type_modifier=objc._C_OUT, null_accepted=True),
                    2: dict(type_modifier=objc._C_INOUT, null_accepted=True),
            })),
]

objc._loadFunctionList(function_list, globals(),  _FunctionTable, False)

class TestExists (TestCase):
    def testFunctionsExists(self):
        for item in _FunctionTable:
            self.assertIn(item[0], globals())

class TestArrayDefault (TestCase):
    # TODO: what is the default anyway?
    pass

class TestArraysOut (TestCase):
    def testFixedSize(self):
        v = fill4Tuple_(None)
        self.assertEquals(list(v), [0, -1, -8, -27])

        self.assertRaises(ValueError, fill4Tuple_, objc.NULL)

        n, v = nullfill4Tuple_(None)
        self.assertEquals(n, 1)
        self.assertEquals(list(v), [0, -1, -8, -27])

        n, v = nullfill4Tuple_(objc.NULL)
        self.assertEquals(n, 0)
        self.assertIs(v, objc.NULL)
        
    def testNullTerminated(self):

        # Output only arrays of null-terminated arrays cannot be
        # wrapped automaticly. How is the bridge supposed to know
        # how much memory it should allocate for the C-array?
        self.assertRaises(TypeError, fillStringArray_, None)
        self.assertRaises(ValueError, fillStringArray_, objc.NULL)

        self.assertRaises(TypeError, nullfillStringArray_)
        self.assertRaises(TypeError, nullfillStringArray_, None)
        n, v = nullfillStringArray_(objc.NULL)
        self.assertEquals(n, 0)
        self.assertIs(v, objc.NULL)

    def testWithCount(self):

        v = fillArray_count_(None, 3)
        self.assertEquals(list(v),  [0,1,4])

        v = fillArray_count_(None, 3)
        self.assertEquals(list(v),  [0,1,4])

        v = fillArray_count_(None, 5)
        self.assertEquals(list(v),  [0,1,4,9,16])

        v = fillArray_count_(None, 0)
        self.assertEquals(list(v),  [])

        self.assertRaises(ValueError, fillArray_count_, objc.NULL, 0)
        
        n, v = nullfillArray_count_(None, 3)
        self.assertEquals(n, 1)
        self.assertEquals(list(v),  [0,1,4])
        n, v = nullfillArray_count_(None, 3)
        self.assertEquals(n, 1)
        self.assertEquals(list(v),  [0,1,4])

        n, v = nullfillArray_count_(objc.NULL, 3)
        self.assertEquals(n, 0)
        self.assertIs(v, objc.NULL )

    def testWithCountInResult(self):

        c, v = fillArray_uptoCount_(None, 20)
        self.assertEquals(c, 10)
        self.assertEquals(list(v),  [i+2 for i in range(10)])

        c, v = maybeFillArray_(None)
        self.assertEquals(c, 2)
        self.assertEquals(list(v),  [10, 11])


class TestArraysInOut (TestCase):
    def testFixedSize(self):

        a = (1,2,3,4)
        v = reverse4Tuple_(a)
        self.assertEquals(a, (1,2,3,4))
        self.assertEquals(v, (4,3,2,1))

        self.assertRaises(ValueError, reverse4Tuple_, (1,2,3))
        self.assertRaises(ValueError, reverse4Tuple_, (1,2,3,4,5))
        self.assertRaises(ValueError, reverse4Tuple_, objc.NULL)

        a = (1,2,3,4)
        n, v = nullreverse4Tuple_(a)
        self.assertEquals(n, 1)
        self.assertEquals(a, (1,2,3,4))
        self.assertEquals(v, (4,3,2,1))

        n, v = nullreverse4Tuple_(objc.NULL)
        self.assertEquals(n, 0)
        self.assertIs(v, objc.NULL)

    def testNullTerminated(self):

        a = (b'a', b'b', b'c')
        v = reverseStrings_(a)
        self.assertEquals(a, (b'a', b'b', b'c'))
        self.assertEquals(v, (b'c', b'b', b'a'))

        self.assertRaises(ValueError, reverseStrings_, (1,2))
        self.assertRaises(ValueError, reverseStrings_, objc.NULL)

        a = (b'a', b'b', b'c')
        n, v = nullreverseStrings_(a)
        self.assertEquals(n, 1)
        self.assertEquals(a, (b'a', b'b', b'c'))
        self.assertEquals(v, (b'c', b'b', b'a'))

        n, v = nullreverseStrings_(objc.NULL)
        self.assertEquals(n, 0)
        self.assertIs(v, objc.NULL)

    def testWithCount(self):

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        v = reverseArray_count_(a, 4)
        self.assertEquals(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEquals(v, (4.0, 3.0, 2.0, 1.0))

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        v = reverseArray_count_(a, 5)
        self.assertEquals(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEquals(v, (5.0, 4.0, 3.0, 2.0, 1.0))

        # Nice to have, but doesn't work without major
        # surgery:
        #a = (1.0, 2.0, 3.0, 4.0, 5.0)
        #v = reverseArray_count_(a, None)
        #self.assertEquals(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        #self.assertEquals(v, (5.0, 4.0, 3.0, 2.0, 1.0))

        self.assertRaises(ValueError, reverseArray_count_, (1.0, 2.0), 5)
        self.assertRaises(ValueError, reverseArray_count_, objc.NULL, 0)

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        n, v = nullreverseArray_count_(a, 5)
        self.assertEquals(n, 1)
        self.assertEquals(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEquals(v, (5.0, 4.0, 3.0, 2.0, 1.0))

        n, v = nullreverseArray_count_(objc.NULL, 0)
        self.assertEquals(n, 0)
        self.assertIs(v, objc.NULL)

    def testWithCountInResult(self):

        c, v = reverseArray_uptoCount_(range(10), 10)
        self.assertEquals(c, 5)
        self.assertEquals(len(v), 5)
        self.assertEquals(list(v),  [9, 8, 7, 6, 5])
        
        c, v = maybeReverseArray_([1,2,3,4])
        self.assertEquals(c, 2)
        self.assertEquals(len(v), 2)
        self.assertEquals(list(v),  [4, 3])

class TestArraysIn (TestCase):
    def testFixedSize(self):

        v = make4Tuple_((1.0, 4.0, 8.0, 12.5))
        self.assertEquals(len(v), 4)
        self.assertEquals(list(v), [1.0, 4.0, 8.0, 12.5])

        v = make4Tuple_((1, 2, 3, 4))
        self.assertEquals(len(v), 4)
        self.assertEquals(list(v), [1.0, 2.0, 3.0, 4.0])

        self.assertRaises(ValueError, make4Tuple_, (1, 2, 3))
        self.assertRaises(ValueError, make4Tuple_, (1, 2, 3, 4, 5))
        self.assertRaises(ValueError, make4Tuple_, objc.NULL)

        v = null4Tuple_(objc.NULL)
        self.assertIs(v, None)

    def testNullTerminated(self):

        v = makeStringArray_((b"hello", b"world", b"there"))
        self.assertEquals(len(v), 3)
        self.assertEquals(list(v), [u"hello", u"world", u"there"])
        self.assertIsInstance(v, objc.lookUpClass("NSArray"))
        self.assertIsInstance(v[0], unicode)

        NSObject = objc.lookUpClass('NSObject')
        p, q, r = NSObject.new(), NSObject.new(), NSObject.new()
        v = makeObjectArray_((p, q, r))
        self.assertEquals(len(v), 3)
        self.assertIs(v[0], p)
        self.assertIs(v[1], q)
        self.assertIs(v[2], r)

        v = makeStringArray_(())
        self.assertEquals(len(v), 0)

        self.assertRaises(ValueError, makeStringArray_, [1,2])
        self.assertRaises(ValueError, makeStringArray_, objc.NULL)

        v = nullStringArray_(objc.NULL)
        self.assertEquals(v, None)

    def testWithCount(self):

        v = makeIntArray_count_((1,2,3,4), 3)
        self.assertEquals(len(v), 3)
        self.assertEquals(list(v), [1,2,3])
        
        # XXX: This one would be nice to have, but not entirely trivial
        #v = makeIntArray_count_((1,2,3,4), None)
        #self.assertEquals(len(v), 3)
        #self.assertEquals(list(v), [1,2,3,4])

        self.assertRaises(ValueError, makeIntArray_count_, [1,2,3], 4)
        self.assertRaises(ValueError, makeIntArray_count_, objc.NULL, 0)
        self.assertRaises(ValueError, makeIntArray_count_, objc.NULL, 1)

        v = nullIntArray_count_(objc.NULL, 0)
        self.assertEquals(v, None)

        self.assertRaises(ValueError, makeIntArray_count_, objc.NULL, 1)

        # Make sure this also works when the length is in a pass-by-reference argument
        v = makeIntArray_countPtr_((1,2,3,4), 4)
        self.assertEquals(len(v), 4)
        self.assertEquals(list(v), [1,2,3,4])

class TestArrayReturns (TestCase):
    # TODO:
    # - Add null-terminated arrays of various supported types:
    #   -> integers
    #   -> CF-types
    def testFixedSize(self):

        v = makeIntArrayOf5()
        self.assertEquals( len(v), 5 )
        self.assertEquals( v[0], 0 )
        self.assertEquals( v[1], 1 )
        self.assertEquals( v[2], 4 )
        self.assertEquals( v[3], 9 )
        self.assertEquals( v[4], 16 )

        v = nullIntArrayOf5()
        self.assertEquals(v, objc.NULL)

    def testSizeInArgument(self):
        v = makeIntArrayOf_(3)
        self.assertEquals(len(v), 3)
        self.assertEquals(v[0], 0)
        self.assertEquals(v[1], 1)
        self.assertEquals(v[2], 8)

        v = makeIntArrayOf_(10)
        self.assertEquals(len(v), 10)
        for i in range(10):
            self.assertEquals(v[i], i**3)

        v = nullIntArrayOf_(100)
        self.assertEquals(v, objc.NULL)

    def testNULLterminated(self):

        v = makeStringArray()
        self.assertEquals(len(v), 4)
        self.assertEquals(list(v), [b"hello", b"world", b"out", b"there"])

        v = nullStringArray()
        self.assertEquals(v, objc.NULL)

class TestByReference (TestCase):
    # Pass by reference arguments. 
    # Note that these tests aren't exhaustive, we have test_methods and
    # test_methods2 for that :-)

    def testInput(self):
        
        r = sumX_andY_(1, 2)
        self.assertEquals(r, 1+2)

        r = sumX_andY_(2535, 5325)
        self.assertEquals(r, 2535 + 5325)

        self.assertRaises(ValueError, sumX_andY_, 42, objc.NULL)

    def testOutput(self):

        div, rem = divBy5_remainder_(55, None)
        self.assertEquals(div, 11)
        self.assertEquals(rem, 0)

        div, rem = divBy5_remainder_(13, None)
        self.assertEquals(div, 2)
        self.assertEquals(rem, 3)

        self.assertRaises(ValueError, divBy5_remainder_, 42, objc.NULL)

    def testInputOutput(self):
        x, y = swapX_andY_(42, 284)
        self.assertEquals(x, 284)
        self.assertEquals(y, 42)

        self.assertRaises(ValueError, swapX_andY_, 42, objc.NULL)

    def testNullAccepted(self):
        # Note: the commented-out test-cases require a change in the pyobjc-core

        def makeNum(value):
            return int(value, 0)

        r, y, z = input_output_inputAndOutput_(1, None, 2)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(None, map(makeNum, r))), 3)
        self.assertEquals(y, 3)
        self.assertEquals(z, -1)

        # Argument 1 is NULL
        r, y, z = input_output_inputAndOutput_(objc.NULL, None, 2)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(None, map(makeNum, r))), 2)
        self.assertEquals(y, 40)
        self.assertEquals(z, -2)

        r, y, z = input_output_inputAndOutput_(objc.NULL, None, 2)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(None, map(makeNum, r))), 2)
        self.assertEquals(y, 40)
        self.assertEquals(z, -2)

        # Argument 2 is NULL
        r, y, z = input_output_inputAndOutput_(1, objc.NULL, 2)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(None, map(makeNum, r))), 2)
        self.assertEquals(y, objc.NULL)
        self.assertEquals(z, -1)

        # Argument 3 is NULL
        r, y, z = input_output_inputAndOutput_(1, None, objc.NULL)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(None, map(makeNum, r))), 2)
        self.assertEquals(y, 43)
        self.assertEquals(z, objc.NULL)

        r, y, z = input_output_inputAndOutput_(1, None, objc.NULL)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(None, map(makeNum, r))), 2)
        self.assertEquals(y, 43)
        self.assertEquals(z, objc.NULL)

class TestPrintfFormat (TestCase):
    def test_nsformat(self):

        v = makeArrayWithFormat_("%3d", 10)
        self.assertEquals(list(v), [ "%3d", " 10"])

        v = makeArrayWithFormat_("hello %s", b"world")
        self.assertEquals(list(v), [ "hello %s", "hello world"])

    def test_cformat(self):

        v = makeArrayWithCFormat_(b"%3d", 10)
        self.assertEquals(list(v), [ "%3d", " 10"])

        v = makeArrayWithCFormat_(b"hello %s", b"world")
        self.assertEquals(list(v), [ "hello %s", "hello world"])

if __name__ == "__main__":
    main()
