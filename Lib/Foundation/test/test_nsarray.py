import unittest
import objc

from Foundation import *

class TestNSArrayInteraction(unittest.TestCase):
    def testRepeatedAllocInit(self):
        for i in range(1,1000):
            a = NSArray.alloc().init()

    def testIndices(self):
        x = NSArray.arrayWithArray_( ["foo", "bar", "baz"] )

        self.assertEquals( x.indexOfObject_("bar"), 1 )

        self.assertRaises( IndexError, x.objectAtIndex_, 100)

    def testEnumeration(self):
        x = NSArray.arrayWithArray_([1, 2, "foo", "bar", "", "baz"])
        y = []

        for o in x:
            y.append(o)

        self.assertEquals(len(x), len(y))

    def testContains(self):
        x = NSArray.arrayWithArray_( ["foo", "bar", "baz"] )
        self.assertEquals( x.count(), 3 )
        self.assertEquals( len(x), 3 )

        self.assert_( x.containsObject_("foo") )
        self.assert_( not x.containsObject_("dumbledorf") )

        self.assert_( "foo" in x )
        self.assert_( not "dumbledorf" in x )

    def testIn(self):
        x = NSMutableArray.array()
        for i in range(0, 100):
            x.addObject_(i)

        y = []
        for i in x:
            y.append( i )

        z = []
        for i in range(0, 100):
            z.append( i )

        self.assertEquals(x, y)
        self.assertEquals(x, z)
        self.assertEquals(y, z)

        for i in range(0, 100):
            self.assert_( i in x )

        self.assert_( 101 not in x )
        self.assert_( None not in x )
        self.assert_( "foo bar" not in x )

    def assertSlicesEqual(self,  x, y, z):
        self.assertEquals( x, x[:] )
        self.assertEquals( y, y[:] )
        self.assertEquals( z, z[:] )
    
        self.assertEquals( x[25:75], y[25:75] )
        self.assertEquals( x[25:75], z[25:75] )
        self.assertEquals( y[25:75], z[25:75] )

        self.assertEquals( x[:15], y[:15] )
        self.assertEquals( x[:15], z[:15] )
        self.assertEquals( y[:15], z[:15] )

        self.assertEquals( x[15:], y[15:] )
        self.assertEquals( x[15:], z[15:] )
        self.assertEquals( y[15:], z[15:] )

        self.assertEquals( x[-15:], y[-15:] )
        self.assertEquals( x[-15:], z[-15:] )
        self.assertEquals( y[-15:], z[-15:] )

        self.assertEquals( x[-15:30], y[-15:30] )
        self.assertEquals( x[-15:30], z[-15:30] )
        self.assertEquals( y[-15:30], z[-15:30] )

        self.assertEquals( x[-15:-5], y[-15:-5] )
        self.assertEquals( x[-15:-5], z[-15:-5] )
        self.assertEquals( y[-15:-5], z[-15:-5] )

    def testSlice(self):
        x = NSMutableArray.array()
        for i in range(0, 100):
            x.addObject_(i)

        y = []
        for i in x:
            y.append( i )

        z = []
        for i in range(0, 100):
            z.append( i )

        self.assertSlicesEqual(x, y, z)

        k = range(300, 50)
        x[20:30] = k
        y[20:30] = k
        z[20:30] = k

        self.assertSlicesEqual(x, y, z)

        # Note that x[1] = x works in python, but not for a bridged NS*Array*.
        # Not sure if there is anything we can do about that.
        x[1] = x[:]
        y[1] = y[:]
        z[1] = z[:]

        self.assertSlicesEqual(x, y, z)

        del x[-15:-5]
        del y[-15:-5]
        del z[-15:-5]

        self.assertSlicesEqual(x, y, z)

    def test_mixSliceNDice(self):
        # This test failes on Python 2.2, that is expected.
        x = range(0, 10)
        y = NSMutableArray.arrayWithArray_( range(0, 10) )

        y[2:4] = x[1:5]
        x[2:8] = y[3:7]
        y[2:4] = y[1:8]

    def test_subScripts(self):
        x = range(0, 10)
        y = NSMutableArray.arrayWithArray_(x)

        self.assertEquals( x[0], y[0] )
        self.assertEquals( x[2], y[2] )

        self.assertEquals( x[-1], y[-1] )
        self.assertEquals( x[-5], y[-5] )

        self.assertRaises( IndexError, x.__getitem__, 100)
        self.assertRaises( IndexError, x.__getitem__, -100)

    def test_varargConstruction(self):
        w = NSArray.arrayWithObjects_(1,2,3,4, None)
        x = NSArray.alloc().initWithObjects_(1,2,3,4, None)
        y = NSArray.arrayWithObjects_count_([1,2,3,4,5,6], 4)
        z = NSArray.alloc().initWithObjects_count_([1,2,3,4,5,6], 4)

        self.assert_(len(w) == 4)
        self.assert_(len(x) == 4)
        self.assert_(len(y) == 4)
        self.assert_(len(z) == 4)

        self.assert_(w[0] == 1)
        self.assert_(x[1] == 2)
        self.assert_(y[2] == 3)
        self.assert_(z[3] == 4)

    def test_varargConstruction2(self):
        w = NSMutableArray.arrayWithObjects_(1,2,3,4, None)
        x = NSMutableArray.alloc().initWithObjects_(1,2,3,4, None)
        y = NSMutableArray.arrayWithObjects_count_([1,2,3,4,5,6], 4)
        z = NSMutableArray.alloc().initWithObjects_count_([1,2,3,4,5,6], 4)

        self.assert_(len(w) == 4)
        self.assert_(len(x) == 4)
        self.assert_(len(y) == 4)
        self.assert_(len(z) == 4)

        self.assert_(w[0] == 1)
        self.assert_(x[1] == 2)
        self.assert_(y[2] == 3)
        self.assert_(z[3] == 4)

class TestNSArraySpecialMethods(unittest.TestCase):
    """
    Test calling 'difficult' methods from Python
    """

    def test_initWithObjects_count_(self):
        a = NSArray.alloc().initWithObjects_count_(('a','b','c','d'), 3)
        self.assertEquals(a, ['a','b','c'])

        self.assertRaises(ValueError, NSArray.alloc().initWithObjects_count_, ('a','b'), 3)

    def test_arrayWithObjects_count_(self):
        a = NSArray.arrayWithObjects_count_(('a','b','c','d'), 3)
        self.assertEquals(a, ['a','b','c'])
        
        self.assertRaises(ValueError, NSArray.arrayWithObjects_count_, ('a','b'), 3)

    def test_arrayByAddingObjects_count_(self):
        a = NSArray.arrayWithArray_(('a', 'b', 'c'))
        self.assertEquals(a, ('a', 'b', 'c'))

        b = a.arrayByAddingObjects_count_(('d', 'e', 'f'), 3)
        self.assertEquals(a, ('a', 'b', 'c'))
        self.assertEquals(b, ('a', 'b', 'c', 'd', 'e', 'f'))

        self.assertRaises(ValueError, a.arrayByAddingObjects_count_, ('a','b'), 3)
    def test_sortedArrayUsingFunction_context_(self):
        a = NSArray.arrayWithArray_(('a', 'b', 'c'))
        self.assertEquals(a, ('a', 'b', 'c'))

        def cmpfunc(l, r, c):
            return -cmp(l,r)

        b = a.sortedArrayUsingFunction_context_(cmpfunc, 'hello')
        self.assertEquals(a, ('a', 'b', 'c'))
        self.assertEquals(b, ('c', 'b', 'a'))

    def test_sortedArrayUsingFunction_context_hint_(self):
        a = NSArray.arrayWithArray_(('a', 'b', 'c'))
        self.assertEquals(a, ('a', 'b', 'c'))

        def cmpfunc(l, r, c):
            return -cmp(l,r)

        b = a.sortedArrayUsingFunction_context_hint_(cmpfunc, 'hello', a.sortedArrayHint())
        self.assertEquals(a, ('a', 'b', 'c'))
        self.assertEquals(b, ('c', 'b', 'a'))




if __name__ == '__main__':
    unittest.main( )
