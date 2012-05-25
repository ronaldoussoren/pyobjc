from PyObjCTools.TestSupport import *
import objc
import types
import sys

from PyObjCTest.testhelper import PyObjC_TestClass3

from Foundation import *


class TestNSDictionarySubclassing(TestCase):
    # These tests seem to be specific for MacOSX
    def testExceptionInInit(self):
        if objc.platform != 'MACOSX': return

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
        if objc.platform != 'MACOSX': return

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
        if objc.platform != 'MACOSX': return

        class DictTestExceptionClass3 (NSDictionary):
            def initWithObjects_forKeys_count_(self, o, k, c):
                return super(DictTestExceptionClass3, self).initWithObjects_forKeys_count_(o, k, c)

        try:
            d = DictTestExceptionClass3.dictionaryWithDictionary_({})
            self.fail()
        except ValueError:
            pass


class TestNSDictionaryInteraction(TestCase):
    def testMethods(self):
        for nm in dir(dict):
            if nm.startswith('__'):
                continue

            if isinstance(getattr(dict, nm), (types.BuiltinFunctionType, types.FunctionType)):
                # Skip class methods, that needs more work in the core
                continue

            self.assertTrue(hasattr(NSMutableDictionary, nm), "NSMutableDictionary has no method '%s'"%(nm,))

    def testRepeatedAllocInit(self):
        for i in range(1,1000):
            d = NSDictionary.alloc().init()

    def testBasicInteraction(self):
        d = NSMutableDictionary.dictionary()
        d[b'a'.decode('ascii')] = b"foo".decode('ascii')
        d[b'b'.decode('ascii')] = b"bar".decode('ascii')

        self.assertEqual(d[b'a'.decode('ascii')], b"foo".decode('ascii'), "Failed to retrieve the same thing that was put into the dict.")
        try:
            d[b'c'.decode('ascii')]
            self.fail("Should have raised...")
        except KeyError:
            pass

    def testPythonIteraction(self):
        d = NSMutableDictionary.dictionary()
        d[b'a'.decode('ascii')] = b"foo".decode('ascii')
        d[b'b'.decode('ascii')] = b"bar".decode('ascii')

        k = list(d.keys())
        k.sort()
        self.assertTrue(k == [b'a'.decode('ascii'), b'b'.decode('ascii')])

        k = list(d.values())
        k.sort()
        self.assertTrue(k == [b'bar'.decode('ascii'), b'foo'.decode('ascii')])

        k = list(d.items())
        k.sort()
        self.assertTrue(k == [(b'a'.decode('ascii'), b'foo'.decode('ascii')), (b'b'.decode('ascii'), b'bar'.decode('ascii')) ])


    def testIn(self):
        d = NSMutableDictionary.dictionary()
        d[b'a'.decode('ascii')] = b"foo".decode('ascii')
        d[b'b'.decode('ascii')] = b"bar".decode('ascii')
        d[1] = b"baz".decode('ascii')
        d[0] = b"bob".decode('ascii')
        # d[-1] = None -- this fails because the bridge doesn't proxy py(None) to objc(NSNull)... not sure if it should

        self.assertTrue( b'a'.decode('ascii') in d )
        self.assertTrue( 1 in d )
        # self.assertTrue( -1 in d )
        # self.assertTrue( d[-1] is None )
        self.assertTrue( b'q'.decode('ascii') not in d )

        for k in d.allKeys():
            self.assertEqual( d.objectForKey_( k ), d[k] )

        for k in d:
            self.assertEqual( d.objectForKey_( k ), d[k] )

        del d[b'a'.decode('ascii')]
        self.assertTrue( b'a'.decode('ascii') not in d )

    def test_varargConstruction(self):
        u = NSDictionary.dictionaryWithObjects_forKeys_([1,2,3,4], [b'one'.decode('ascii'), b'two'.decode('ascii'), b'three'.decode('ascii'), b'four'.decode('ascii')])
        v = NSDictionary.alloc().initWithObjects_forKeys_([1,2,3,4], [b'one'.decode('ascii'), b'two'.decode('ascii'), b'three'.decode('ascii'), b'four'.decode('ascii')])
        w = NSDictionary.dictionaryWithObjects_forKeys_count_([1,2,3,4,5], [b'one'.decode('ascii'), b'two'.decode('ascii'), b'three'.decode('ascii'), b'four'.decode('ascii'), b'five'.decode('ascii')], 4)
        x = NSDictionary.alloc().initWithObjects_forKeys_count_([1,2,3,4,5], [b'one'.decode('ascii'), b'two'.decode('ascii'), b'three'.decode('ascii'), b'four'.decode('ascii'), b'five'.decode('ascii')], 4)
        y = NSDictionary.dictionaryWithObjectsAndKeys_(1, b'one'.decode('ascii'), 2, b'two'.decode('ascii'), 3, b'three'.decode('ascii'), 4, b'four'.decode('ascii'), None)
        z = NSDictionary.alloc().initWithObjectsAndKeys_(1, b'one'.decode('ascii'), 2, b'two'.decode('ascii'), 3, b'three'.decode('ascii'), 4, b'four'.decode('ascii'), None)

        self.assertEqual(len(u), 4)
        self.assertEqual(len(v), 4)
        self.assertEqual(len(w), 4)
        self.assertEqual(len(x), 4)
        self.assertEqual(len(y), 4)
        self.assertEqual(len(z), 4)

        self.assertEqual(u[b'one'.decode('ascii')], 1)
        self.assertEqual(v[b'two'.decode('ascii')], 2)
        self.assertEqual(w[b'three'.decode('ascii')], 3)
        self.assertEqual(x[b'one'.decode('ascii')], 1)
        self.assertEqual(y[b'two'.decode('ascii')], 2)
        self.assertEqual(z[b'four'.decode('ascii')], 4)

    def test_varargConstruction2(self):
        u = NSMutableDictionary.dictionaryWithObjects_forKeys_([1,2,3,4], [b'one'.decode('ascii'), b'two'.decode('ascii'), b'three'.decode('ascii'), b'four'.decode('ascii')])
        v = NSMutableDictionary.alloc().initWithObjects_forKeys_([1,2,3,4], [b'one'.decode('ascii'), b'two'.decode('ascii'), b'three'.decode('ascii'), b'four'.decode('ascii')])
        w = NSMutableDictionary.dictionaryWithObjects_forKeys_count_([1,2,3,4,5], [b'one'.decode('ascii'), b'two'.decode('ascii'), b'three'.decode('ascii'), b'four'.decode('ascii'), b'five'.decode('ascii')], 4)
        x = NSMutableDictionary.alloc().initWithObjects_forKeys_count_([1,2,3,4,5], [b'one'.decode('ascii'), b'two'.decode('ascii'), b'three'.decode('ascii'), b'four'.decode('ascii'), b'five'.decode('ascii')], 4)

        #self.assertRaises(TypeError, NSMutableDictionary.dictionaryWithObjectsAndKeys_, 1, 'one', 2, 'two', None)
        y = NSMutableDictionary.dictionaryWithObjectsAndKeys_(1, b'one'.decode('ascii'), 2, b'two'.decode('ascii'), 3, b'three'.decode('ascii'), 4, b'four'.decode('ascii'), None)
        z = NSMutableDictionary.alloc().initWithObjectsAndKeys_(1, b'one'.decode('ascii'), 2, b'two'.decode('ascii'), 3, b'three'.decode('ascii'), 4, b'four'.decode('ascii'), None)

        self.assertEqual(len(u), 4)
        self.assertEqual(len(v), 4)
        self.assertEqual(len(w), 4)
        self.assertEqual(len(x), 4)
        #self.assertEqual(len(y), 4)
        #self.assertEqual(len(z), 4)

        self.assertEqual(u[b'one'.decode('ascii')], 1)
        self.assertEqual(v[b'two'.decode('ascii')], 2)
        self.assertEqual(w[b'three'.decode('ascii')], 3)
        self.assertEqual(x[b'one'.decode('ascii')], 1)
        #self.assertEqual(y[b'two'.decode('ascii')], 2)
        #self.assertEqual(z[b'four'.decode('ascii')], 4)


class MyDictionaryBase (NSDictionary):
    def count(self):
        if hasattr(self, '_count'):
            return self._count
        return -1

    def keyEnumerator(self):
        return None

    def objectForKey_(self, key):
        return None

class MyDictionary1 (MyDictionaryBase):
    def initWithObjects_forKeys_count_(self, objects, keys, count):
        self._count = count
        self._objects = objects
        self._keys = keys
        return self

class MyDictionary2 (MyDictionaryBase):
    def dictionaryWithObjects_forKeys_count_(self, objects, keys, count):
        if not self is MyDictionary2: raise AssertionError(self)
        return (objects, keys, count)

class TestSubclassing (TestCase):
    def testInitWithObjects(self):
        o = PyObjC_TestClass3.makeDictFromClass_method_(MyDictionary1, 1)

        self.assertIsInstance(o, MyDictionary1)
        self.assertEqual(o._count, 4)
        self.assertEqual(len(o._keys), 4)
        self.assertEqual(len(o._objects), 4)

    def testDictWithObjects(self):
        o = PyObjC_TestClass3.makeDictFromClass_method_(MyDictionary2, 0)

        self.assertIsInstance(o, tuple)
        self.assertEqual(o[2], 4)
        self.assertEqual(len(o[1]), 4)
        self.assertEqual(len(o[0]), 4)

class TestVariadic (TestCase):
    def testDictionaryWithObjectsAndKeys(self):
        o = NSDictionary.dictionaryWithObjectsAndKeys_(
                42, 'a',
                43, 'b')
        self.assertEqual(o, {'a':42, 'b':43})
        self.assertIsInstance(o, NSDictionary)

        o = NSMutableDictionary.dictionaryWithObjectsAndKeys_(
                42, 'a',
                43, 'b')
        self.assertEqual(o, {'a':42, 'b':43})
        self.assertIsInstance(o, NSMutableDictionary)

    def testInitWithObjectsAndKeys(self):
        o = NSDictionary.alloc().initWithObjectsAndKeys_(
                42, 'a',
                43, 'b')
        self.assertEqual(o, {'a':42, 'b':43})
        self.assertIsInstance(o, NSDictionary)

        o = NSMutableDictionary.alloc().initWithObjectsAndKeys_(
                42, 'a',
                43, 'b')
        self.assertEqual(o, {'a':42, 'b':43})
        self.assertIsInstance(o, NSMutableDictionary)


class TestNSDictionary (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSDictionary.isEqualToDictionary_)
        self.assertResultIsBOOL(NSDictionary.writeToFile_atomically_)
        self.assertArgIsBOOL(NSDictionary.writeToFile_atomically_, 1)
        self.assertResultIsBOOL(NSDictionary.writeToURL_atomically_)
        self.assertArgIsBOOL(NSDictionary.writeToURL_atomically_, 1)

        self.assertArgIsSEL(NSDictionary.keysSortedByValueUsingSelector_, 0, b'i@:@')

        self.assertArgIsIn(NSDictionary.dictionaryWithObjects_forKeys_count_, 0)
        self.assertArgSizeInArg(NSDictionary.dictionaryWithObjects_forKeys_count_, 0, 2)
        self.assertArgIsIn(NSDictionary.dictionaryWithObjects_forKeys_count_, 1)
        self.assertArgSizeInArg(NSDictionary.dictionaryWithObjects_forKeys_count_, 1, 2)

        self.assertArgIsIn(NSDictionary.initWithObjects_forKeys_count_, 0)
        self.assertArgSizeInArg(NSDictionary.initWithObjects_forKeys_count_, 0, 2)
        self.assertArgIsIn(NSDictionary.initWithObjects_forKeys_count_, 1)
        self.assertArgSizeInArg(NSDictionary.initWithObjects_forKeys_count_, 1, 2)

        self.assertArgIsBOOL(NSDictionary.initWithDictionary_copyItems_, 1)

        self.assertIsNullTerminated(NSDictionary.initWithObjectsAndKeys_)
        self.assertIsNullTerminated(NSDictionary.dictionaryWithObjectsAndKeys_)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgIsBlock(NSDictionary.enumerateKeysAndObjectsUsingBlock_, 0, b'v@@o^'+objc._C_NSBOOL)
        self.assertArgIsBlock(NSDictionary.enumerateKeysAndObjectsWithOptions_usingBlock_, 1, b'v@@o^'+objc._C_NSBOOL)
        self.assertArgIsBlock(NSDictionary.keysSortedByValueUsingComparator_, 0, b'i@@')
        self.assertArgIsBlock(NSDictionary.keysSortedByValueWithOptions_usingComparator_, 1, objc._C_NSInteger + b'@@')

        self.assertArgIsBlock(NSDictionary.keysOfEntriesPassingTest_, 0, objc._C_NSBOOL + b'@@o^' + objc._C_NSBOOL)
        self.assertArgIsBlock(NSDictionary.keysOfEntriesWithOptions_passingTest_, 1, objc._C_NSBOOL + b'@@o^' + objc._C_NSBOOL)

if __name__ == '__main__':
    main( )
