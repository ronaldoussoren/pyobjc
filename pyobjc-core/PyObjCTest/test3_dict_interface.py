"""
Tests to ensure that NSDictionary and NSMutableDictionary conform
to the python dict interface

These tests are basicly a port of the Python 3.2 tests for dictionaries
and dictionary views.

TODO:
- Port all tests
- Do the same for python 2.x
- Do the same for sets (NSSet) and lists (NSArray)
"""
from PyObjCTools.TestSupport import *
import objc

# Import some of the stdlib tests
from test import mapping_tests

NSDictionary = objc.lookUpClass('NSDictionary')
NSMutableDictionary = objc.lookUpClass('NSMutableDictionary')

class TestNSDictionaryInterface (TestCase):
    def dictClass(self):
        return NSDictionary

    def createDictionary(self, **kwds):
        return NSDictionary.dictionaryWithDictionary_(kwds)

    def testConstructor(self):
        value = self.dictClass()()
        self.assertEqual(value, {})

    def testBool(self):
        self.assertIs(not self.createDictionary(), True)
        self.assertTrue(self.createDictionary(foo='1'))
        self.assertIs(bool(self.createDictionary()), False)
        self.assertIs(bool(self.createDictionary(foo='1')), True)

    def testKeys(self):
        d = self.createDictionary()
        self.assertEqual(set(d.keys()), set())

        d = self.createDictionary(a=1, b=2)
        k = d.keys()

        self.assertIn('a', d)
        self.assertIn('b', d)
        self.assertIn('a', k)
        self.assertIn('b', k)

        self.assertIsNotInstance(k, list)

        self.assertEqual(repr(self.createDictionary(a=1).keys()),
                "<nsdict_keys(['a'])>")

    def testValues(self):
        d = self.createDictionary()
        self.assertEqual(set(d.values()), set())

        d = self.createDictionary(a=1)

        self.assertEqual(set(d.values()), {1})
        self.assertRaises(TypeError, d.values, None)
        self.assertIsNotInstance(d.values(), list)

        self.assertEqual(repr(self.createDictionary(a=1).values()),
                "<nsdict_values([1])>")

    def testItems(self):
        d = self.createDictionary()
        self.assertEqual(set(d.items()), set())

        d = self.createDictionary(a=1)
        self.assertEqual(set(d.items()), {('a', 1)})
        self.assertRaises(TypeError, d.items, None)
        self.assertEqual(repr(self.createDictionary(a=1).items()),
                "<nsdict_items([('a', 1)])>")

    def testContains(self):
        d = self.createDictionary()
        self.assertNotIn('a', d)
        self.assertFalse('a' in d)
        self.assertTrue('a' not in d)

        d = self.createDictionary(a=1, b=2)
        self.assertIn('a', d)
        self.assertIn('b', d)
        self.assertNotIn('c', d)

        self.assertRaises(TypeError, d.__contains__)

    def testLen(self):
        d = self.createDictionary()
        self.assertEqual(len(d), 0)

        d = self.createDictionary(a=1, b=2)
        self.assertEqual(len(d), 2)

    def testGetItem(self):
        d = self.createDictionary(a=1, b=2)
        self.assertEqual(d['a'], 1)
        self.assertEqual(d['b'], 2)

        self.assertRaises(TypeError, d.__getitem__)

    def testFromKeys(self):
        d = self.dictClass().fromkeys('abc')
        self.assertEqual(d, {'a':None, 'b':None, 'c':None})

        d = self.createDictionary()
        self.assertIsNot(d.fromkeys('abc'), d)
        self.assertEqual(d.fromkeys('abc'), {'a':None, 'b':None, 'c':None})
        self.assertEqual(d.fromkeys((4,5),0), {4:0, 5:0})
        self.assertEqual(d.fromkeys([]), {})

        def g():
            yield 1

        self.assertEqual(d.fromkeys(g()), {1:None})
        self.assertRaises(TypeError, {}.fromkeys, 3)

        d = self.dictClass()(zip(range(6), range(6)))
        self.assertEqual(dict.fromkeys(d, 0), dict(zip(range(6), [0]*6)))

    def _testCopy(self):
        self.fail("Decide what to do w.r.t. -copy and -mutableCopy")

    def testGet(self):
        d = self.createDictionary()
        self.assertIs(d.get('c'), None)
        self.assertEqual(d.get('c', 3), 3)


        d = self.createDictionary(a=1, b=2)
        self.assertIs(d.get('c'), None)
        self.assertEqual(d.get('c', 3), 3)
        self.assertEqual(d.get('a'), 1)
        self.assertEqual(d.get('a', 3), 1)
        self.assertRaises(TypeError, d.get)
        self.assertRaises(TypeError, d.get, None, None, None)


    def testEq(self):
        self.assertEqual(self.createDictionary(), self.createDictionary())
        self.assertEqual(self.createDictionary(a=1), self.createDictionary(a=1))

        class Exc(Exception): pass

        class BadCmp(object):
            def __eq__(self, other):
                raise Exc()
            def __hash__(self):
                return 1

        d1 = {BadCmp(): 1}
        d2 = {BadCmp(): 1}

        with self.assertRaises(Exc):
            d1 == d2


    def testKeysContained(self):
        self.helper_keys_contained(lambda x: x.keys())
        self.helper_keys_contained(lambda x: x.items())

    def helper_keys_contained(self, fn):
        # Test rich comparisons against dict key views, which should behave the
        # same as sets.

        empty = fn(self.createDictionary())
        empty2 = fn(self.createDictionary())
        smaller = fn(self.createDictionary(a=1, b=2))
        larger = fn(self.createDictionary(a=1, b=2, c=3))
        larger2 = fn(self.createDictionary(a=1, b=2, c=3))
        larger3 = fn(self.createDictionary(d=1, b=2, c=3))

        self.assertTrue(smaller <  larger)
        self.assertTrue(smaller <= larger)
        self.assertTrue(larger >  smaller)
        self.assertTrue(larger >= smaller)

        self.assertFalse(smaller >= larger)
        self.assertFalse(smaller >  larger)
        self.assertFalse(larger  <= smaller)
        self.assertFalse(larger  <  smaller)

        self.assertFalse(smaller <  larger3)
        self.assertFalse(smaller <= larger3)
        self.assertFalse(larger3 >  smaller)
        self.assertFalse(larger3 >= smaller)

        # Inequality strictness
        self.assertTrue(larger2 >= larger)
        self.assertTrue(larger2 <= larger)
        self.assertFalse(larger2 > larger)
        self.assertFalse(larger2 < larger)

        self.assertTrue(larger == larger2)
        self.assertTrue(smaller != larger)

        # There is an optimization on the zero-element case.
        self.assertTrue(empty == empty2)
        self.assertFalse(empty != empty2)
        self.assertFalse(empty == smaller)
        self.assertTrue(empty != smaller)

        # With the same size, an elementwise compare happens
        self.assertTrue(larger != larger3)
        self.assertFalse(larger == larger3)

    def testErrorsInViewContainmentCheck(self):
        class C:
            def __eq__(self, other):
                raise RuntimeError()

        d1 = self.dictClass().dictionaryWithDictionary_({1: C()})
        d2 = self.dictClass().dictionaryWithDictionary_({1: C()})

        with self.assertRaises(RuntimeError):
            d1.items() == d2.items()
        with self.assertRaises(RuntimeError):
            d1.items() != d2.items()
        with self.assertRaises(RuntimeError):
            d1.items() <= d2.items()
        with self.assertRaises(RuntimeError):
            d1.items() >= d2.items()

        d3 = self.dictClass().dictionaryWithDictionary_({1: C(), 2: C()})
        with self.assertRaises(RuntimeError):
            d2.items() < d3.items()
        with self.assertRaises(RuntimeError):
            d3.items() > d2.items()

        k1 = self.dictClass().dictionaryWithDictionary_({1:1, 2:2}).keys()
        k2 = self.dictClass().dictionaryWithDictionary_({1:1, 2:2, 3:3}).keys()
        k3 = self.dictClass().dictionaryWithDictionary_({4:4}).keys()

        self.assertEqual(k1 - k2, set())
        self.assertEqual(k1 - k3, {1,2})
        self.assertEqual(k2 - k1, {3})
        self.assertEqual(k3 - k1, {4})
        self.assertEqual(k1 & k2, {1,2})
        self.assertEqual(k1 & k3, set())
        self.assertEqual(k1 | k2, {1,2,3})
        self.assertEqual(k1 ^ k2, {3})
        self.assertEqual(k1 ^ k3, {1,2,4})

    def testDictviewSetOperationsOnItems(self):
        k1 = self.dictClass().dictionaryWithDictionary_({1:1, 2:2}).items()
        k2 = self.dictClass().dictionaryWithDictionary_({1:1, 2:2, 3:3}).items()
        k3 = self.dictClass().dictionaryWithDictionary_({4:4}).items()

        self.assertEqual(k1 - k2, set())
        self.assertEqual(k1 - k3, {(1,1), (2,2)})
        self.assertEqual(k2 - k1, {(3,3)})
        self.assertEqual(k3 - k1, {(4,4)})
        self.assertEqual(k1 & k2, {(1,1), (2,2)})
        self.assertEqual(k1 & k3, set())
        self.assertEqual(k1 | k2, {(1,1), (2,2), (3,3)})
        self.assertEqual(k1 ^ k2, {(3,3)})
        self.assertEqual(k1 ^ k3, {(1,1), (2,2), (4,4)})

    def testDictviewMixedSetOperations(self):
        # Just a few for .keys()
        self.assertTrue(self.dictClass().dictionaryWithDictionary_({1:1}).keys() == {1})
        self.assertTrue({1} == self.dictClass().dictionaryWithDictionary_({1:1}).keys())
        self.assertEqual(self.dictClass().dictionaryWithDictionary_({1:1}).keys() | {2}, {1, 2})
        self.assertEqual({2} | self.dictClass().dictionaryWithDictionary_({1:1}).keys(), {1, 2})
        # And a few for .items()
        self.assertTrue(self.dictClass().dictionaryWithDictionary_({1:1}).items() == {(1,1)})
        self.assertTrue({(1,1)} == self.dictClass().dictionaryWithDictionary_({1:1}).items())
        self.assertEqual(self.dictClass().dictionaryWithDictionary_({1:1}).items() | {2}, {(1,1), 2})
        self.assertEqual({2} | self.dictClass().dictionaryWithDictionary_({1:1}).items(), {(1,1), 2})


class TestNSMutableDictionaryInterface (TestNSDictionaryInterface):
    def dictClass(self):
        return NSMutableDictionary

    def createDictionary(self, **kwds):
        return NSMutableDictionary.dictionaryWithDictionary_(kwds)

    def testKeysMutable(self):
        d = self.createDictionary()
        self.assertEqual(set(d.keys()), set())

        d = self.createDictionary(a=1, b=2)
        k = d.keys()


        self.assertIn('a', d)
        self.assertIn('b', d)
        self.assertIn('a', k)
        self.assertIn('b', k)

        self.assertIsNotInstance(k, list)

        self.assertNotIn('c', d)
        self.assertNotIn('c', k)

        d['c'] = 3
        self.assertIn('c', d)
        self.assertIn('c', k)

    def testValuesMutable(self):
        d = self.createDictionary()
        self.assertEqual(set(d.values()), set())

        d = self.createDictionary(a=1)
        v = d.values()

        self.assertEqual(set(v), {1})

        d['b'] = 2
        self.assertEqual(set(v), {1, 2})

    def testItemsMutable(self):
        d = self.createDictionary()
        self.assertEqual(set(d.items()), set())

        d = self.createDictionary(a=1)
        i = d.items()

        self.assertEqual(set(i), {('a', 1)})

        d['b'] = 2

        self.assertEqual(set(i), {('a', 1), ('b', 2)})

    def testGetItem(self):
        d = self.createDictionary(a=1, b=2)
        self.assertEqual(d['a'], 1)
        self.assertEqual(d['b'], 2)

        d['c'] = 3
        d['a'] = 4
        self.assertEqual(d['c'], 3)
        self.assertEqual(d['a'], 4)
        del d['b']
        self.assertEqual(d, {'a': 4, 'c': 3})

        self.assertRaises(TypeError, d.__getitem__)

        class Exc (Exception): pass

        class BadEq(object):
            def __eq__(self, other):
                raise Exc()
            def __hash__(self):
                return hash(23)

        d = self.createDictionary()
        d[BadEq()] = 42
        self.assertRaises(KeyError, d.__getitem__, 23)

        class BadHash(object):
            fail = False
            def __hash__(self):
                if self.fail:
                    raise Exc()
                else:
                    return 42

        d = self.createDictionary()
        x = BadHash()
        d[x] = 42
        x.fail = True

        # FIXME
        #self.assertRaises(Exc, d.__getitem__, x)

    def testClear(self):
        d = self.createDictionary(a=1, b=2, c=3)
        d.clear()

        self.assertEqual(d, {})

        self.assertRaises(TypeError, d.clear, None)

    def testUpdate(self):
        d = self.createDictionary()
        d.update({1:100})
        d.update({2:20})
        d.update({1:1, 2:2, 3:3})
        self.assertEqual(d, {1:1, 2:2, 3:3})

        d.update()
        self.assertEqual(d, {1:1, 2:2, 3:3})

        self.assertRaises((TypeError, AttributeError), d.update, None)

        class SimpleUserDict:
            def __init__(self):
                self.d = {1:1, 2:2, 3:3}
            def keys(self):
                return self.d.keys()
            def __getitem__(self, i):
                return self.d[i]

        d = self.createDictionary()
        d.update(SimpleUserDict())
        self.assertEqual(d, {1:1, 2:2, 3:3})

        class Exc(Exception): pass

        d.clear()

        class FailingUserDict:
            def keys(self):
                raise Exc()

        self.assertRaises(Exc, d.update, FailingUserDict())


        class FailingUserDict:
            def keys(self):
                class BogonIter:
                    def __init__(self):
                        self.i = 1
                    def __iter__(self):
                        return self
                    def __next__(self):
                        if self.i:
                            self.i = 0
                            return 'a'
                        raise Exc
                return BogonIter()
            def __getitem__(self, key):
                return key

        self.assertRaises(Exc, d.update, FailingUserDict())


        class FailingUserDict:
            def keys(self):
                class BogonIter:
                    def __init__(self):
                        self.i = ord('a')
                    def __iter__(self):
                        return self
                    def __next__(self):
                        if self.i <= ord('z'):
                            rtn = chr(self.i)
                            self.i += 1
                            return rtn
                        raise StopIteration
                return BogonIter()
            def __getitem__(self, key):
                raise Exc
        self.assertRaises(Exc, d.update, FailingUserDict())

        class badseq(object):
            def __iter__(self):
                return self
            def __next__(self):
                raise Exc()

        self.assertRaises(Exc, {}.update, badseq())
        self.assertRaises(ValueError, {}.update, [(1, 2, 3)])


    def setDefault(self):
        d = self.createDictionary()
        self.assertIs(d.setdefault('key0'), None)
        d.setdefault('key0', [])
        self.assertIs(d.setdefault('key0'), None)
        d.setdefault('key', []).append(3)
        self.assertEqual(d['key'][0], 3)
        d.setdefault('key', []).append(4)
        self.assertEqual(len(d['key']), 2)
        self.assertRaises(TypeError, d.setdefault)

        class Exc (Exception): pass

        class BadHash(object):
            fail = False
            def __hash__(self):
                if self.fail:
                    raise Exc()
                else:
                    return 42

        x = BadHash()
        d[x] = 42
        x.fail = True
        self.assertRaises(Exc, d.setdefault, x, [])

    def testPopitem(self):
        for copymode in -1, +1:
            # -1: b has same structure as a
            # +1: b is a.copy()
            for log2size in range(12):
                size = 2**log2size
                a = self.createDictionary()
                b = self.createDictionary()
                for i in range(size):
                    a[repr(i)] = i
                    if copymode < 0:
                        b[repr(i)] = i
                if copymode > 0:
                    b = a.mutableCopy()
                for i in range(size):
                    ka, va = ta = a.popitem()
                    self.assertEqual(va, int(ka))
                    kb, vb = tb = b.popitem()
                    self.assertEqual(vb, int(kb))
                    self.assertFalse(copymode < 0 and ta != tb)
                self.assertFalse(a)
                self.assertFalse(b)

        d = self.createDictionary()
        self.assertRaises(KeyError, d.popitem)


    def testPop(self):
        d = self.createDictionary()
        k, v = 'abc', 'def'
        d[k] = v
        self.assertRaises(KeyError, d.pop, 'ghi')

        self.assertEqual(d.pop(k), v)
        self.assertEqual(len(d), 0)

        self.assertRaises(KeyError, d.pop, k)

        self.assertEqual(d.pop(k, v), v)
        d[k] = v
        self.assertEqual(d.pop(k, 1), v)

        self.assertRaises(TypeError, d.pop)

        class Exc(Exception): pass

        class BadHash(object):
            fail = False
            def __hash__(self):
                if self.fail:
                    raise Exc()
                else:
                    return 42

        #x = BadHash()
        #d[x] = 42
        #x.fail = True
        #self.assertRaises(Exc, d.pop, x)

class DictSetTest (TestCase):
    testclass = NSDictionary

    def testDictKeys(self):
        d = self.testclass.dictionaryWithDictionary_({1: 10, "a": "ABC"})

        keys = d.keys()

        self.assertEqual(len(keys), 2)
        self.assertEqual(set(keys), {1, "a"})
        self.assertEqual(keys, {1, "a"})
        self.assertNotEqual(keys, {1, "a", "b"})
        self.assertNotEqual(keys, {1, "b"})
        self.assertNotEqual(keys, {1})
        self.assertNotEqual(keys, 42)
        self.assertIn(1, keys)
        self.assertIn("a", keys)
        self.assertNotIn(10, keys)
        self.assertNotIn("Z", keys)
        self.assertEqual(d.keys(), d.keys())

        e = self.testclass.dictionaryWithDictionary_({1: 11, "a": "def"})
        self.assertEqual(d.keys(), e.keys())

    def testDictItems(self):
        d = self.testclass.dictionaryWithDictionary_({1: 10, "a": "ABC"})
        items = d.items()

        self.assertEqual(len(items), 2)
        self.assertEqual(set(items), {(1, 10), ("a", "ABC")})
        self.assertEqual(items, {(1, 10), ("a", "ABC")})
        self.assertNotEqual(items, {(1, 10), ("a", "ABC"), "junk"})
        self.assertNotEqual(items, {(1, 10), ("a", "def")})
        self.assertNotEqual(items, {(1, 10)})
        self.assertNotEqual(items, 42)
        self.assertIn((1, 10), items)
        self.assertIn(("a", "ABC"), items)
        self.assertNotIn((1, 11), items)
        self.assertNotIn(1, items)
        self.assertNotIn((), items)
        self.assertNotIn((1,), items)
        self.assertNotIn((1, 2, 3), items)
        self.assertEqual(d.items(), d.items())

        e = d.copy()
        self.assertEqual(d.items(), e.items())



class DictSetTest (DictSetTest):
    testclass = NSMutableDictionary

    def testDictKeysMutable(self):
        d = self.testclass.dictionaryWithDictionary_({1: 10, "a": "ABC"})
        e = self.testclass.dictionaryWithDictionary_({1: 11, "a": "def"})
        self.assertEqual(d.keys(), e.keys())

        del e["a"]
        self.assertNotEqual(d.keys(), e.keys())

    def testDictItemsMutable(self):
        d = self.testclass.dictionaryWithDictionary_({1: 10, "a": "ABC"})

        e = d.copy()
        self.assertEqual(d.items(), e.items())
        d["a"] = "def"
        self.assertNotEqual(d.items(), e.items())

    def testDictMixedKeysItems(self):
        d = self.testclass.dictionaryWithDictionary_(
                {(1, 1): 11, (2, 2): 22})
        e = self.testclass.dictionaryWithDictionary_(
                {1: 1, 2: 2})
        self.assertEqual(d.keys(), e.items())
        self.assertNotEqual(d.items(), e.keys())

    def testDictValues(self):
        d = self.testclass.dictionaryWithDictionary_(
                {1: 10, "a": "ABC"})
        values = d.values()
        self.assertEqual(set(values), {10, "ABC"})
        self.assertEqual(len(values), 2)





class GeneralMappingTestsNSMutableDictionary (
        mapping_tests.BasicTestMappingProtocol):
    type2test = NSMutableDictionary


import collections

class TestABC (TestCase):
    def testDictABC(self):
        self.assertTrue(issubclass(NSDictionary, collections.Mapping))
        self.assertTrue(issubclass(NSMutableDictionary, collections.Mapping))
        self.assertTrue(issubclass(NSMutableDictionary, collections.MutableMapping))

    def testViewABC(self):
        d = NSDictionary.dictionary()
        self.assertTrue(isinstance(d.keys(), collections.KeysView))
        self.assertTrue(isinstance(d.values(), collections.ValuesView))
        self.assertTrue(isinstance(d.items(), collections.ItemsView))

        d = NSMutableDictionary.dictionary()
        self.assertTrue(isinstance(d.keys(), collections.KeysView))
        self.assertTrue(isinstance(d.values(), collections.ValuesView))
        self.assertTrue(isinstance(d.items(), collections.ItemsView))

if __name__ == "__main__":
    main()
