"""
Tests for the new-style metadata format interface.

Note: Tests for calling from ObjC into python are in test_metadata_py.py

TODO:
- Add tests for calling functions instead of methods
- The python->C interface (that is the contents of the metadata object) is
  likely to change when the bridge is feature-complete.
- Probably need special-casing for arrays (numarray and array.array)!
"""
from __future__ import unicode_literals
import objc
from PyObjCTools.TestSupport import *

from PyObjCTest.metadata import *
import PyObjCTest.test_metadata # to get the right metadata
import warnings

import sys
if sys.version_info[0] == 3:
    unicode = str


class TestArrayDefault (TestCase):
    # TODO: what is the default anyway?
    pass

class TestArraysOut (TestCase):
    def testFixedSize(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('fill4Tuple:')

        v = m(o, None)
        self.assertEqual(list(v), [0, -1, -8, -27])

        self.assertRaises(ValueError, m, o, objc.NULL)

        m = o.methodForSelector_('nullfill4Tuple:')
        n, v = m(o, None)
        self.assertEqual(n, 1)
        self.assertEqual(list(v), [0, -1, -8, -27])

        n, v = m(o, None)
        self.assertEqual(n, 1)
        self.assertEqual(list(v), [0, -1, -8, -27])

        n, v = m(o, objc.NULL)
        self.assertEqual(n, 0)
        self.assertIs(v, objc.NULL)

    def testNullTerminated(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('fillStringArray:')


        # Output only arrays of null-terminated arrays cannot be
        # wrapped automaticly. How is the bridge supposed to know
        # how much memory it should allocate for the C-array?
        self.assertRaises(TypeError, m, o, None)
        self.assertRaises(ValueError, m, o, objc.NULL)

        m = o.methodForSelector_('fillStringArray:')
        self.assertRaises(TypeError, m, o)
        self.assertRaises(TypeError, m, o, None)
        n, v = o.nullfillStringArray_(objc.NULL)
        self.assertEqual(n, 0)
        self.assertIs(v, objc.NULL)

    def testWithCount(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('fillArray:count:')

        v = m(o, None, 3)
        self.assertEqual(list(v),  [0,1,4])

        v = m(o, None, 3)
        self.assertEqual(list(v),  [0,1,4])

        v = m(o, None, 5)
        self.assertEqual(list(v),  [0,1,4,9,16])

        v = m(o, None, 0)
        self.assertEqual(list(v),  [])

        self.assertRaises(ValueError, m, o, objc.NULL, 0)

        m = o.methodForSelector_('nullfillArray:count:')
        n, v = m(o, None, 3)
        self.assertEqual(n, 1)
        self.assertEqual(list(v),  [0,1,4])
        n, v = m(o, None, 3)
        self.assertEqual(n, 1)
        self.assertEqual(list(v),  [0,1,4])


        n, v = m(o, objc.NULL, 3)
        self.assertEqual(n, 0)
        self.assertIs(v, objc.NULL)

    def testWithCountInResult(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('fillArray:uptoCount:')

        c, v = m(o, None, 20)
        self.assertEqual(c, 10)
        self.assertEqual(list(v),  [i+2 for i in range(10)])

        m = o.methodForSelector_('maybeFillArray:')
        c, v = m(o, None)
        self.assertEqual(c, 2)
        self.assertEqual(list(v),  [10, 11])



class TestArraysInOut (TestCase):
    def testFixedSize(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('reverse4Tuple:')

        a = (1,2,3,4)
        v = m(o, a)
        self.assertEqual(a, (1,2,3,4))
        self.assertEqual(v, (4,3,2,1))

        self.assertRaises(ValueError, m, o, (1,2,3))
        self.assertRaises(ValueError, m, o, (1,2,3,4,5))
        self.assertRaises(ValueError, m, o, objc.NULL)

        m = o.methodForSelector_('nullreverse4Tuple:')
        a = (1,2,3,4)
        n, v = m(o, a)
        self.assertEqual(n, 1)
        self.assertEqual(a, (1,2,3,4))
        self.assertEqual(v, (4,3,2,1))

        n, v = m(o, objc.NULL)
        self.assertEqual(n, 0)
        self.assertIs(v, objc.NULL)

    def testNullTerminated(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('reverseStrings:')

        a = (b'a', b'b', b'c')
        v = m(o, a)
        self.assertEqual(a, (b'a', b'b', b'c'))
        self.assertEqual(v, (b'c', b'b', b'a'))

        self.assertRaises(ValueError, m, o, (1,2))
        self.assertRaises(ValueError, m, o, objc.NULL)

        m = o.methodForSelector_('nullreverseStrings:')
        a = (b'a', b'b', b'c')
        n, v = m(o, a)
        self.assertEqual(n, 1)
        self.assertEqual(a, (b'a', b'b', b'c'))
        self.assertEqual(v, (b'c', b'b', b'a'))

        n, v = m(o, objc.NULL)
        self.assertEqual(n, 0)
        self.assertIs(v, objc.NULL)

    def testWithCount(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('reverseArray:count:')

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        v = m(o, a, 4)
        self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEqual(v, (4.0, 3.0, 2.0, 1.0))

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        v = m(o, a, 5)
        self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEqual(v, (5.0, 4.0, 3.0, 2.0, 1.0))

        # Nice to have, but doesn't work without major
        # surgery:
        #a = (1.0, 2.0, 3.0, 4.0, 5.0)
        #v = m(o, a, None)
        #self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        #self.assertEqual(v, (5.0, 4.0, 3.0, 2.0, 1.0))

        self.assertRaises(ValueError, m, o, (1.0, 2.0), 5)
        self.assertRaises(ValueError, m, o, objc.NULL, 0)

        m = o.methodForSelector_('nullreverseArray:count:')
        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        n, v = m(o, a, 5)
        self.assertEqual(n, 1)
        self.assertEqual(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEqual(v, (5.0, 4.0, 3.0, 2.0, 1.0))

        n, v = m(o, objc.NULL, 0)
        self.assertEqual(n, 0)
        self.assertIs(v, objc.NULL)

    def testWithCountInResult(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('reverseArray:uptoCount:')

        c, v = m(o, range(10), 10)
        self.assertEqual(c, 5)
        self.assertEqual(len(v), 5)
        self.assertEqual(list(v),  [9, 8, 7, 6, 5])

        m = o.methodForSelector_('maybeReverseArray:')
        c, v = m(o, [1,2,3,4])
        self.assertEqual(c, 2)
        self.assertEqual(len(v), 2)
        self.assertEqual(list(v),  [4, 3])

class TestArraysIn (TestCase):
    def testFixedSize(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('make4Tuple:')

        v = m(o, (1.0, 4.0, 8.0, 12.5))
        self.assertEqual(len(v), 4)
        self.assertEqual(list(v), [1.0, 4.0, 8.0, 12.5])

        v = m(o, (1, 2, 3, 4))
        self.assertEqual(len(v), 4)
        self.assertEqual(list(v), [1.0, 2.0, 3.0, 4.0])

        self.assertRaises(ValueError, m, o, (1, 2, 3))
        self.assertRaises(ValueError, m, o, (1, 2, 3, 4, 5))
        self.assertRaises(ValueError, m, o, objc.NULL)

        m = o.methodForSelector_('null4Tuple:')
        v = m(o, objc.NULL)
        self.assertIsNone(v)

    def testNullTerminated(self):
        o = OC_MetaDataTest.new()

        m = o.methodForSelector_('makeStringArray:')

        v = m(o, (b"hello", b"world", b"there"))
        self.assertEqual(len(v), 3)
        self.assertEqual(list(v), ["hello", "world", "there"])
        self.assertIsInstance(v, objc.lookUpClass("NSArray"))
        self.assertIsInstance(v[0], unicode)

        m = o.methodForSelector_('makeObjectArray:')

        NSObject = objc.lookUpClass('NSObject')
        p, q, r = NSObject.new(), NSObject.new(), NSObject.new()
        v = m(o, (p, q, r))
        self.assertEqual(len(v), 3)
        self.assertIs(v[0], p)
        self.assertIs(v[1], q)
        self.assertIs(v[2], r)

        m = o.methodForSelector_('makeStringArray:')

        v = m(o, ())
        self.assertEqual(len(v), 0)

        self.assertRaises(ValueError, m, o, [1,2])
        self.assertRaises(ValueError, m, o, objc.NULL)

        m = o.methodForSelector_('nullStringArray:')
        v = m(o, objc.NULL)
        self.assertEqual(v, None)

    def testWithCount(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('makeIntArray:count:')

        v = m(o, (1,2,3,4), 3)
        self.assertEqual(len(v), 3)
        self.assertEqual(list(v), [1,2,3])

        # XXX: This one would be nice to have, but not entirely trivial
        #v = m(o, (1,2,3,4), None)
        #self.assertEqual(len(v), 3)
        #self.assertEqual(list(v), [1,2,3,4])

        self.assertRaises(ValueError, m, o, [1,2,3], 4)
        self.assertRaises(ValueError, m, o, objc.NULL, 0)
        self.assertRaises(ValueError, m, o, objc.NULL, 1)

        self.assertRaises(ValueError, m, o, objc.NULL, 1)

        m = o.methodForSelector_('nullIntArray:count:')
        v = m(o, objc.NULL, 0)
        self.assertEqual(v, None)


        # Make sure this also works when the length is in a pass-by-reference argument
        m = o.methodForSelector_('makeIntArray:countPtr:')
        v = m(o, (1,2,3,4), 4)
        self.assertEqual(len(v), 4)
        self.assertEqual(list(v), [1,2,3,4])

class TestArrayReturns (TestCase):
    # TODO:
    # - Add null-terminated arrays of various supported types:
    #   -> integers
    #   -> CF-types
    def testFixedSize(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_(b'makeIntArrayOf5')

        v = m(o)
        self.assertEqual( len(v), 5 )
        self.assertEqual( v[0], 0 )
        self.assertEqual( v[1], 1 )
        self.assertEqual( v[2], 4 )
        self.assertEqual( v[3], 9 )
        self.assertEqual( v[4], 16 )

        m = o.methodForSelector_(b'nullIntArrayOf5')
        v = m(o)
        self.assertEqual(v, objc.NULL)

    def testSizeInArgument(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_(b'makeIntArrayOf:')

        v = m(o, 3)
        self.assertEqual(len(v), 3)
        self.assertEqual(v[0], 0)
        self.assertEqual(v[1], 1)
        self.assertEqual(v[2], 8)

        v = m(o, 10)
        self.assertEqual(len(v), 10)
        for i in range(10):
            self.assertEqual(v[i], i**3)

        m = o.methodForSelector_(b'nullIntArrayOf:')
        v = m(o, 100)
        self.assertEqual(v, objc.NULL)

    def testNULLterminated(self):
        o  = OC_MetaDataTest.new()
        m = o.methodForSelector_(b'makeStringArray')

        v = m(o)
        self.assertEqual(len(v), 4)
        self.assertEqual(list(v), [b"hello", b"world", b"out", b"there"])

        m = o.methodForSelector_(b'nullStringArray')
        v = m(o)
        self.assertEqual(v, objc.NULL)

class TestByReference (TestCase):
    # Pass by reference arguments.
    # Note that these tests aren't exhaustive, we have test_methods and
    # test_methods2 for that :-)

    def testInput(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('sumX:andY:')

        r = m(o, 1, 2)
        self.assertEqual(r, 1+2)

        r = m(o, 2535, 5325)
        self.assertEqual(r, 2535 + 5325)

        self.assertRaises(ValueError, m, o, 42, objc.NULL)

    def testOutput(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('divBy5:remainder:')

        div, rem = m(o, 55, None)
        self.assertEqual(div, 11)
        self.assertEqual(rem, 0)

        div, rem = m(o, 13, None)
        self.assertEqual(div, 2)
        self.assertEqual(rem, 3)

        # To be fixed:
        #self.assertRaises(ValueError, m, o, 42, objc.NULL)

    def testInputOutput(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('swapX:andY:')

        x, y = m(o, 42, 284)
        self.assertEqual(x, 284)
        self.assertEqual(y, 42)

        self.assertRaises(ValueError, m, o, 42, objc.NULL)

    def testNullAccepted(self):
        # Note: the commented-out test-cases require a change in the pyobjc-core
        o = OC_MetaDataTest.new();
        m = o.methodForSelector_('input:output:inputAndOutput:')

        def makeNum(value):
            return int(value, 0)

        # All arguments present
        r, y, z = m(o, 1, None, 2)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(None, map(makeNum, r)))), 3)
        self.assertEqual(y, 3)
        self.assertEqual(z, -1)

        r, y, z = m(o, 1, None, 2)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(None, map(makeNum, r)))), 3)
        self.assertEqual(y, 3)
        self.assertEqual(z, -1)

        # Argument 1 is NULL
        r, y, z = m(o, objc.NULL, None, 2)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(None, map(makeNum, r)))), 2)
        self.assertEqual(y, 40)
        self.assertEqual(z, -2)

        r, y, z = m(o, objc.NULL, None, 2)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(None, map(makeNum, r)))), 2)
        self.assertEqual(y, 40)
        self.assertEqual(z, -2)

        # Argument 2 is NULL
        r, y, z = m(o, 1, objc.NULL, 2)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(None, map(makeNum, r)))), 2)
        self.assertEqual(y, objc.NULL)
        self.assertEqual(z, -1)

        # Argument 3 is NULL
        r, y, z = m(o, 1, None, objc.NULL)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(None, map(makeNum, r)))), 2)
        self.assertEqual(y, 43)
        self.assertEqual(z, objc.NULL)

        r, y, z = m(o, 1, None, objc.NULL)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(list(filter(None, map(makeNum, r)))), 2)
        self.assertEqual(y, 43)
        self.assertEqual(z, objc.NULL)


if __name__ == "__main__":
    main()
