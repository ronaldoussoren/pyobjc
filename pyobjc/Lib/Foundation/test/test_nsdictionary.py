import unittest
import objc
import types

from Foundation import *

class TestNSDictionaryInteraction(unittest.TestCase):
    def testMethods(self):
        for nm in dir(types.DictType):
            if nm.startswith('__'):
                continue

            if isinstance(getattr(types.DictType, nm), (types.BuiltinFunctionType, types.FunctionType)):
                # Skip class methods, that needs more work in the core
                continue

            self.assert_(hasattr(NSMutableDictionary, nm), "NSMutableDictionary has no method '%s'"%(nm,))

    def testRepeatedAllocInit(self):
        for i in range(1,1000):
            d = NSDictionary.alloc().init()

    def testBasicInteraction(self):
        d = NSMutableDictionary.dictionary()
        d['a'] = "foo"
        d['b'] = "bar"

        self.assertEqual(d['a'], "foo", "Failed to retrieve the same thing that was put into the dict.")
        try:
            d['c']
            self.fail("Should have raised...")
        except KeyError:
            pass

    def testPythonIteraction(self):
        d = NSMutableDictionary.dictionary()
        d['a'] = "foo"
        d['b'] = "bar"

        k = list(d.keys())
        k.sort()
        self.assert_(k == ['a', 'b'])

        k = list(d.values())
        k.sort()
        self.assert_(k == ['bar', 'foo'])

        k = list(d.items())
        k.sort()
        self.assert_(k == [('a', 'foo'), ('b', 'bar') ])


    def testIn(self):
        d = NSMutableDictionary.dictionary()
        d['a'] = "foo"
        d['b'] = "bar"
        d[1] = "baz"
        d[0] = "bob"
        # d[-1] = None -- this fails because the bridge doesn't proxy py(None) to objc(NSNull)... not sure if it should

        self.assert_( 'a' in d )
        self.assert_( 1 in d )
        # self.assert_( -1 in d )
        # self.assert_( d[-1] is None )
        self.assert_( 'q' not in d )

        for k in d.allKeys():
            self.assertEqual( d.objectForKey_( k ), d[k] )

        for k in d:
            self.assertEqual( d.objectForKey_( k ), d[k] )
            
        del d['a']
        self.assert_( 'a' not in d )
    
    def test_varargConstruction(self):
        u = NSDictionary.dictionaryWithObjects_forKeys_([1,2,3,4], ['one', 'two', 'three', 'four'])
        v = NSDictionary.alloc().initWithObjects_forKeys_([1,2,3,4], ['one', 'two', 'three', 'four'])
        w = NSDictionary.dictionaryWithObjects_forKeys_count_([1,2,3,4,5], ['one', 'two', 'three', 'four', 'five'], 4)
        x = NSDictionary.alloc().initWithObjects_forKeys_count_([1,2,3,4,5], ['one', 'two', 'three', 'four', 'five'], 4)
        y = NSDictionary.dictionaryWithObjectsAndKeys_(1, 'one', 2, 'two', 3, 'three', 4, 'four', None)
        z = NSDictionary.alloc().initWithObjectsAndKeys_(1, 'one', 2, 'two', 3, 'three', 4, 'four', None)

        self.assert_(len(u) == 4)
        self.assert_(len(v) == 4)
        self.assert_(len(w) == 4)
        self.assert_(len(x) == 4)
        self.assert_(len(y) == 4)
        self.assert_(len(z) == 4)

        self.assert_(u['one'] == 1)
        self.assert_(v['two'] == 2)
        self.assert_(w['three'] == 3)
        self.assert_(x['one'] == 1)
        self.assert_(y['two'] == 2)
        self.assert_(z['four'] == 4)

    def test_varargConstruction2(self):
        u = NSMutableDictionary.dictionaryWithObjects_forKeys_([1,2,3,4], ['one', 'two', 'three', 'four'])
        v = NSMutableDictionary.alloc().initWithObjects_forKeys_([1,2,3,4], ['one', 'two', 'three', 'four'])
        w = NSMutableDictionary.dictionaryWithObjects_forKeys_count_([1,2,3,4,5], ['one', 'two', 'three', 'four', 'five'], 4)
        x = NSMutableDictionary.alloc().initWithObjects_forKeys_count_([1,2,3,4,5], ['one', 'two', 'three', 'four', 'five'], 4)
        y = NSMutableDictionary.dictionaryWithObjectsAndKeys_(1, 'one', 2, 'two', 3, 'three', 4, 'four', None)
        z = NSMutableDictionary.alloc().initWithObjectsAndKeys_(1, 'one', 2, 'two', 3, 'three', 4, 'four', None)

        self.assert_(len(u) == 4)
        self.assert_(len(v) == 4)
        self.assert_(len(w) == 4)
        self.assert_(len(x) == 4)
        self.assert_(len(y) == 4)
        self.assert_(len(z) == 4)

        self.assert_(u['one'] == 1)
        self.assert_(v['two'] == 2)
        self.assert_(w['three'] == 3)
        self.assert_(x['one'] == 1)
        self.assert_(y['two'] == 2)
        self.assert_(z['four'] == 4)

if __name__ == '__main__':
    unittest.main( )
