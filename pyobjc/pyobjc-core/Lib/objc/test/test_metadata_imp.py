"""
Tests for the new-style metadata format interface.

Note: Tests for calling from ObjC into python are in test_metadata_py.py

TODO:
- Add tests for calling functions instead of methods
- The python->C interface (that is the contents of the metadata object) is
  likely to change when the bridge is feature-complete.
- Probably need special-casing for arrays (numarray and array.array)!
"""
import objc
import objc.test

from objc.test.metadata import *
import objc.test.test_metadata # to get the right metadata
import warnings


class TestArrayDefault (objc.test.TestCase):
    # TODO: what is the default anyway?
    pass

class TestArraysOut (objc.test.TestCase):
    def testFixedSize(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('fill4Tuple:')

        warnings.filterwarnings('ignore', category=DeprecationWarning)
        try:
            v = m(o)
            self.assertEquals(list(v), [0, -1, -8, -27])
        finally:
            del warnings.filters[0]

        v = m(o, None)
        self.assertEquals(list(v), [0, -1, -8, -27])

        self.assertRaises(ValueError, m, o, objc.NULL)

        warnings.filterwarnings('ignore', category=DeprecationWarning)
        try:

            m = o.methodForSelector_('nullfill4Tuple:')
            n, v = m(o)
            self.assertEquals(n, 1)
            self.assertEquals(list(v), [0, -1, -8, -27])
        finally:
            del warnings.filters[0]

        n, v = m(o, None)
        self.assertEquals(n, 1)
        self.assertEquals(list(v), [0, -1, -8, -27])

        n, v = m(o, objc.NULL)
        self.assertEquals(n, 0)
        self.assert_( v is objc.NULL )
        
    def testNullTerminated(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('fillStringArray:')


        # Output only arrays of null-terminated arrays cannot be
        # wrapped automaticly. How is the bridge supposed to know
        # how much memory it should allocate for the C-array?
        warnings.filterwarnings('ignore', category=DeprecationWarning)
        try:
            self.assertRaises(TypeError, m, o)
        finally:
            del warnings.filters[0]
        
        self.assertRaises(TypeError, m, o, None)
        self.assertRaises(ValueError, m, o, objc.NULL)

        m = o.methodForSelector_('fillStringArray:')
        self.assertRaises(TypeError, m, o)
        self.assertRaises(TypeError, m, o, None)
        n, v = o.nullfillStringArray_(objc.NULL)
        self.assertEquals(n, 0)
        self.assert_( v is objc.NULL)

    def testWithCount(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('fillArray:count:')

        warnings.filterwarnings('ignore', category=DeprecationWarning)
        try:
            v = m(o, 3)
            self.assertEquals(list(v),  [0,1,4])

            v = m(o, None, 3)
            self.assertEquals(list(v),  [0,1,4])

            v = m(o, 5)
            self.assertEquals(list(v),  [0,1,4,9,16])

            v = m(o, 0)
            self.assertEquals(list(v),  [])
        finally:
            del warnings.filters[0]

        self.assertRaises(ValueError, m, o, objc.NULL, 0)
        

        warnings.filterwarnings('ignore', category=DeprecationWarning)
        try:
            m = o.methodForSelector_('nullfillArray:count:')
            n, v = m(o, 3)
            self.assertEquals(n, 1)
            self.assertEquals(list(v),  [0,1,4])
            n, v = m(o, None, 3)
            self.assertEquals(n, 1)
            self.assertEquals(list(v),  [0,1,4])
        finally:
            del warnings.filters[0]


        n, v = m(o, objc.NULL, 3)
        self.assertEquals(n, 0)
        self.assert_( v is objc.NULL )

    def testWithCountInResult(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('fillArray:uptoCount:')


        warnings.filterwarnings('ignore', category=DeprecationWarning)
        try:
            c, v = m(o, 20)
            self.assertEquals(c, 10)
            self.assertEquals(list(v),  [i+2 for i in range(10)])

            m = o.methodForSelector_('maybeFillArray:')
            c, v = m(o)
            self.assertEquals(c, 2)
            self.assertEquals(list(v),  [10, 11])
        finally:
            del warnings.filters[0]



class TestArraysInOut (objc.test.TestCase):
    def testFixedSize(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('reverse4Tuple:')

        a = (1,2,3,4)
        v = m(o, a)
        self.assertEquals(a, (1,2,3,4))
        self.assertEquals(v, (4,3,2,1))

        self.assertRaises(ValueError, m, o, (1,2,3))
        self.assertRaises(ValueError, m, o, (1,2,3,4,5))
        self.assertRaises(ValueError, m, o, objc.NULL)

        m = o.methodForSelector_('nullreverse4Tuple:')
        a = (1,2,3,4)
        n, v = m(o, a)
        self.assertEquals(n, 1)
        self.assertEquals(a, (1,2,3,4))
        self.assertEquals(v, (4,3,2,1))

        n, v = m(o, objc.NULL)
        self.assertEquals(n, 0)
        self.assert_( v is objc.NULL )

    def testNullTerminated(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('reverseStrings:')

        a = ('a', 'b', 'c')
        v = m(o, a)
        self.assertEquals(a, ('a', 'b', 'c'))
        self.assertEquals(v, ('c', 'b', 'a'))

        self.assertRaises(ValueError, m, o, (1,2))
        self.assertRaises(ValueError, m, o, objc.NULL)

        m = o.methodForSelector_('nullreverseStrings:')
        a = ('a', 'b', 'c')
        n, v = m(o, a)
        self.assertEquals(n, 1)
        self.assertEquals(a, ('a', 'b', 'c'))
        self.assertEquals(v, ('c', 'b', 'a'))

        n, v = m(o, objc.NULL)
        self.assertEquals(n, 0)
        self.assert_( v is objc.NULL )

    def testWithCount(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('reverseArray:count:')

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        v = m(o, a, 4)
        self.assertEquals(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEquals(v, (4.0, 3.0, 2.0, 1.0))

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        v = m(o, a, 5)
        self.assertEquals(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEquals(v, (5.0, 4.0, 3.0, 2.0, 1.0))

        # Nice to have, but doesn't work without major
        # surgery:
        #a = (1.0, 2.0, 3.0, 4.0, 5.0)
        #v = m(o, a, None)
        #self.assertEquals(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        #self.assertEquals(v, (5.0, 4.0, 3.0, 2.0, 1.0))

        self.assertRaises(ValueError, m, o, (1.0, 2.0), 5)
        self.assertRaises(ValueError, m, o, objc.NULL, 0)

        m = o.methodForSelector_('nullreverseArray:count:')
        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        n, v = m(o, a, 5)
        self.assertEquals(n, 1)
        self.assertEquals(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEquals(v, (5.0, 4.0, 3.0, 2.0, 1.0))

        n, v = m(o, objc.NULL, 0)
        self.assertEquals(n, 0)
        self.assert_( v is objc.NULL )

    def testWithCountInResult(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('reverseArray:uptoCount:')

        c, v = m(o, range(10), 10)
        self.assertEquals(c, 5)
        self.assertEquals(len(v), 5)
        self.assertEquals(list(v),  [9, 8, 7, 6, 5])
        
        m = o.methodForSelector_('maybeReverseArray:')
        c, v = m(o, [1,2,3,4])
        self.assertEquals(c, 2)
        self.assertEquals(len(v), 2)
        self.assertEquals(list(v),  [4, 3])

class TestArraysIn (objc.test.TestCase):
    def testFixedSize(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('make4Tuple:')

        v = m(o, (1.0, 4.0, 8.0, 12.5))
        self.assertEquals(len(v), 4)
        self.assertEquals(list(v), [1.0, 4.0, 8.0, 12.5])

        v = m(o, (1, 2, 3, 4))
        self.assertEquals(len(v), 4)
        self.assertEquals(list(v), [1.0, 2.0, 3.0, 4.0])

        self.assertRaises(ValueError, m, o, (1, 2, 3))
        self.assertRaises(ValueError, m, o, (1, 2, 3, 4, 5))
        self.assertRaises(ValueError, m, o, objc.NULL)

        m = o.methodForSelector_('null4Tuple:')
        v = m(o, objc.NULL)
        self.assert_( v is None )

    def testNullTerminated(self):
        o = OC_MetaDataTest.new()

        m = o.methodForSelector_('makeStringArray:')

        v = m(o, ("hello", "world", "there"))
        self.assertEquals(len(v), 3)
        self.assertEquals(list(v), [u"hello", u"world", u"there"])
        self.assert_( isinstance(v, objc.lookUpClass("NSArray")) )
        self.assert_( isinstance(v[0], unicode) )

        m = o.methodForSelector_('makeObjectArray:')

        NSObject = objc.lookUpClass('NSObject')
        p, q, r = NSObject.new(), NSObject.new(), NSObject.new()
        v = m(o, (p, q, r))
        self.assertEquals(len(v), 3)
        self.assert_( v[0] is p )
        self.assert_( v[1] is q )
        self.assert_( v[2] is r )

        m = o.methodForSelector_('makeStringArray:')

        v = m(o, ())
        self.assertEquals(len(v), 0)

        self.assertRaises(ValueError, m, o, [1,2])
        self.assertRaises(ValueError, m, o, objc.NULL)

        m = o.methodForSelector_('nullStringArray:')
        v = m(o, objc.NULL)
        self.assertEquals(v, None)

    def testWithCount(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('makeIntArray:count:')

        v = m(o, (1,2,3,4), 3)
        self.assertEquals(len(v), 3)
        self.assertEquals(list(v), [1,2,3])
        
        # XXX: This one would be nice to have, but not entirely trivial
        #v = m(o, (1,2,3,4), None)
        #self.assertEquals(len(v), 3)
        #self.assertEquals(list(v), [1,2,3,4])

        self.assertRaises(ValueError, m, o, [1,2,3], 4)
        self.assertRaises(ValueError, m, o, objc.NULL, 0)
        self.assertRaises(ValueError, m, o, objc.NULL, 1)

        self.assertRaises(ValueError, m, o, objc.NULL, 1)

        m = o.methodForSelector_('nullIntArray:count:')
        v = m(o, objc.NULL, 0)
        self.assertEquals(v, None)


        # Make sure this also works when the length is in a pass-by-reference argument
        m = o.methodForSelector_('makeIntArray:countPtr:')
        v = m(o, (1,2,3,4), 4)
        self.assertEquals(len(v), 4)
        self.assertEquals(list(v), [1,2,3,4])

class TestArrayReturns (objc.test.TestCase):
    # TODO:
    # - Add null-terminated arrays of various supported types:
    #   -> integers
    #   -> CF-types
    def testFixedSize(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('makeIntArrayOf5')

        v = m(o)
        self.assertEquals( len(v), 5 )
        self.assertEquals( v[0], 0 )
        self.assertEquals( v[1], 1 )
        self.assertEquals( v[2], 4 )
        self.assertEquals( v[3], 9 )
        self.assertEquals( v[4], 16 )

        m = o.methodForSelector_('nullIntArrayOf5')
        v = m(o)
        self.assertEquals(v, objc.NULL)

    def testSizeInArgument(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('makeIntArrayOf:')

        v = m(o, 3)
        self.assertEquals(len(v), 3)
        self.assertEquals(v[0], 0)
        self.assertEquals(v[1], 1)
        self.assertEquals(v[2], 8)

        v = m(o, 10)
        self.assertEquals(len(v), 10)
        for i in range(10):
            self.assertEquals(v[i], i**3)

        m = o.methodForSelector_('nullIntArrayOf:')
        v = m(o, 100)
        self.assertEquals(v, objc.NULL)

    def testNULLterminated(self):
        o  = OC_MetaDataTest.new()
        m = o.methodForSelector_('makeStringArray')

        v = m(o)
        self.assertEquals(len(v), 4)
        self.assertEquals(list(v), ["hello", "world", "out", "there"])

        m = o.methodForSelector_('nullStringArray')
        v = m(o)
        self.assertEquals(v, objc.NULL)

class TestByReference (objc.test.TestCase):
    # Pass by reference arguments. 
    # Note that these tests aren't exhaustive, we have test_methods and
    # test_methods2 for that :-)

    def testInput(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('sumX:andY:')
        
        r = m(o, 1, 2)
        self.assertEquals(r, 1+2)

        r = m(o, 2535, 5325)
        self.assertEquals(r, 2535 + 5325)

        self.assertRaises(ValueError, m, o, 42, objc.NULL)

    def testOutput(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('divBy5:remainder:')

        warnings.filterwarnings('ignore', category=DeprecationWarning)
        try:
            div, rem = m(o, 55)
            self.assertEquals(div, 11)
            self.assertEquals(rem, 0)

            div, rem = m(o, 13)
            self.assertEquals(div, 2)
            self.assertEquals(rem, 3)
        finally:
            del warnings.filters[0]

        # To be fixed: 
        #self.assertRaises(ValueError, m, o, 42, objc.NULL)

    def testInputOutput(self):
        o = OC_MetaDataTest.new()
        m = o.methodForSelector_('swapX:andY:')

        x, y = m(o, 42, 284)
        self.assertEquals(x, 284)
        self.assertEquals(y, 42)

        self.assertRaises(ValueError, m, o, 42, objc.NULL)

    def testNullAccepted(self):
        # Note: the commented-out test-cases require a change in the pyobjc-core
        o = OC_MetaDataTest.new();
        m = o.methodForSelector_('input:output:inputAndOutput:')

        def makeNum(value):
            return int(value, 0)

        # All arguments present
        warnings.filterwarnings('ignore', category=DeprecationWarning)
        try:
            r, y, z = m(o, 1, 2)
            self.assertEquals(len(r), 3)
            self.assertEquals(len(filter(None, map(makeNum, r))), 3)
            self.assertEquals(y, 3)
            self.assertEquals(z, -1)
        finally:
            del warnings.filters[0]

        r, y, z = m(o, 1, None, 2)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(None, map(makeNum, r))), 3)
        self.assertEquals(y, 3)
        self.assertEquals(z, -1)

        # Argument 1 is NULL
        warnings.filterwarnings('ignore', category=DeprecationWarning)
        try:
            r, y, z = m(o, objc.NULL, 2)
            self.assertEquals(len(r), 3)
            self.assertEquals(len(filter(None, map(makeNum, r))), 2)
            self.assertEquals(y, 40)
            self.assertEquals(z, -2)
        finally:
            del warnings.filters[0]

        r, y, z = m(o, objc.NULL, None, 2)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(None, map(makeNum, r))), 2)
        self.assertEquals(y, 40)
        self.assertEquals(z, -2)

        # Argument 2 is NULL
        r, y, z = m(o, 1, objc.NULL, 2)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(None, map(makeNum, r))), 2)
        self.assertEquals(y, objc.NULL)
        self.assertEquals(z, -1)

        # Argument 3 is NULL
        warnings.filterwarnings('ignore', category=DeprecationWarning)
        try:
            r, y, z = m(o, 1, objc.NULL)
            self.assertEquals(len(r), 3)
            self.assertEquals(len(filter(None, map(makeNum, r))), 2)
            self.assertEquals(y, 43)
            self.assertEquals(z, objc.NULL)
        finally:
            del warnings.filters[0]

        r, y, z = m(o, 1, None, objc.NULL)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(None, map(makeNum, r))), 2)
        self.assertEquals(y, 43)
        self.assertEquals(z, objc.NULL)


if __name__ == "__main__":
    objc.test.main()
