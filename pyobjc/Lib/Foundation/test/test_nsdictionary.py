# TODO: Tests for calling 
#   initWithObjects:forKeys:count and dictionaryWithObjects:forKeys:count
import unittest
import objc
import types
import sys

from objc.test.testbndl import PyObjC_TestClass3

from Foundation import *


class TestNSDictionarySubclassing(unittest.TestCase):
    # These tests seem to be specific for MacOSX
    def testExceptionInInit(self):
        if sys.platform != 'darwin': return

        class DictTestExceptionClass (NSDictionary):
            pass

        # Don't use self.assertRaises here, we once had a bug that 
        # causes this to fail, while the assertRaises version would
        # (probably) have worked.
        import warnings
        warnings.filterwarnings('ignore', 
            category=objc.UninitializedDeallocWarning)

        try:
            try:
                d = DictTestExceptionClass.alloc().initWithDictionary_({})
                self.fail()
            except ValueError:
                pass
        finally:
            del warnings.filters[0]

    def testAnotherExceptionInInit(self):
        if sys.platform != 'darwin': return

        class DictTestExceptionClass2 (NSDictionary):
            def initWithObjects_forKeys_count_(self, o, k, c):
                return super(DictTestExceptionClass2, self).initWithObjects_forKeys_count_(o, k, c)

        import warnings
        warnings.filterwarnings('ignore', 
            category=objc.UninitializedDeallocWarning)

        try:
            try:
                d = DictTestExceptionClass2.alloc().initWithDictionary_({})
                self.fail()
            except ValueError:
                pass
        finally:
            del warnings.filters[0]


    def testExceptionInInitClsMeth(self):
        if sys.platform != 'darwin': return

        class DictTestExceptionClass3 (NSDictionary):
            def initWithObjects_forKeys_count_(self, o, k, c):
                return super(DictTestExceptionClass3, self).initWithObjects_forKeys_count_(o, k, c)

        try:
            d = DictTestExceptionClass3.dictionaryWithDictionary_({})
            self.fail()
        except ValueError:
            pass


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


class MyDictionaryBase (NSDictionary):
    def count(self):
        if hasattr(self, '_count'):
            return self._count
        return -1

    def keyEnumerator(self):
        return None

    def objectForKey(self, key):
        return None
   
class MyDictionary1 (MyDictionaryBase):
    def initWithObjects_forKeys_count_(self, objects, keys, count):
        self.count = count
        self.objects = objects
        self.keys = keys
        return self

class MyDictionary2 (MyDictionaryBase):
    def dictionaryWithObjects_forKeys_count_(self, objects, keys, count):
        if not self is MyDictionary2: raise AssertionError, self
        return (objects, keys, count)

class TestSubclassing (unittest.TestCase):
    def testInitWithObjects(self):
        o = PyObjC_TestClass3.makeDictFromClass_method_(MyDictionary1, 1)
        
        self.assert_(isinstance(o, MyDictionary1))
        self.assertEquals(o.count, 4)
        self.assertEquals(len(o.keys), 4)
        self.assertEquals(len(o.objects), 4)

    def testDictWithObjects(self):
        o = PyObjC_TestClass3.makeDictFromClass_method_(MyDictionary2, 0)
        
        self.assert_(isinstance(o, tuple))
        self.assertEquals(o[2], 4)
        self.assertEquals(len(o[1]), 4)
        self.assertEquals(len(o[0]), 4)

if __name__ == '__main__':
    unittest.main( )
