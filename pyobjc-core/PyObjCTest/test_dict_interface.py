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

import collections.abc

# Import some of the stdlib tests
from test import mapping_tests

import objc
from PyObjCTools.TestSupport import TestCase

NSDictionary = objc.lookUpClass("NSDictionary")
NSMutableDictionary = objc.lookUpClass("NSMutableDictionary")


class TestNSDictionaryInterface(TestCase):
    def dictClass(self):
        return NSDictionary

    def createDictionary(self, **kwds):
        return NSDictionary.dictionaryWithDictionary_(kwds)

    def testConstructor(self):
        value = self.dictClass()()
        self.assertEqual(value, {})

    def testBool(self):
        self.assertIs(not self.createDictionary(), True)
        self.assertTrue(self.createDictionary(foo="1"))
        self.assertIs(bool(self.createDictionary()), False)
        self.assertIs(bool(self.createDictionary(foo="1")), True)

    def testKeys(self):
        d = self.createDictionary()
        self.assertEqual(set(d.keys()), set())

        d = self.createDictionary(a=1, b=2)
        k = d.keys()

        self.assertIn("a", d)
        self.assertIn("b", d)
        self.assertIn("a", k)
        self.assertIn("b", k)

        self.assertNotIsInstance(k, list)

        s = d.keys() | {"c"}
        self.assertEqual(s, {"a", "b", "c"})

        s = {"c"} | d.keys()
        self.assertEqual(s, {"a", "b", "c"})

        s = d.keys() & {"b"}
        self.assertEqual(s, {"b"})

        s = {"b", "c"} & d.keys()
        self.assertEqual(s, {"b"})

        s = d.keys() - {"b"}
        self.assertEqual(s, {"a"})

        s = {"c", "b"} - d.keys()
        self.assertEqual(s, {"c"})

        s = d.keys() ^ {"b", "c"}
        self.assertEqual(s, {"a", "c"})

        s = {"c", "b"} ^ d.keys()
        self.assertEqual(s, {"a", "c"})

        self.assertEqual(
            repr(self.createDictionary(a=1).keys()), "<nsdict_keys(['a'])>"
        )

    def testValues(self):
        d = self.createDictionary()
        self.assertEqual(set(d.values()), set())

        d = self.createDictionary(a=1)

        self.assertEqual(set(d.values()), {1})
        with self.assertRaisesRegex(
            TypeError, r".*\(\) takes 1 positional argument but 2 were given"
        ):
            d.values(None)
        self.assertNotIsInstance(d.values(), list)

        self.assertEqual(
            repr(self.createDictionary(a=1).values()), "<nsdict_values([1])>"
        )

    def testItems(self):
        d = self.createDictionary()
        self.assertEqual(set(d.items()), set())

        d = self.createDictionary(a=1)
        self.assertEqual(set(d.items()), {("a", 1)})
        with self.assertRaisesRegex(
            TypeError, r".*\(\) takes 1 positional argument but 2 were given"
        ):
            d.items(None)
        self.assertEqual(
            repr(self.createDictionary(a=1).items()), "<nsdict_items([('a', 1)])>"
        )

    def testContains(self):
        d = self.createDictionary()
        self.assertNotIn("a", d)
        self.assertFalse("a" in d)
        self.assertTrue("a" not in d)

        d = self.createDictionary(a=1, b=2)
        self.assertIn("a", d)
        self.assertIn("b", d)
        self.assertNotIn("c", d)

        with self.assertRaisesRegex(
            TypeError, r".*\(\) missing 1 required positional argument: 'key'"
        ):
            d.__contains__()

    def testLen(self):
        d = self.createDictionary()
        self.assertEqual(len(d), 0)

        d = self.createDictionary(a=1, b=2)
        self.assertEqual(len(d), 2)

    def testGetItem(self):
        d = self.createDictionary(a=1, b=2)
        self.assertEqual(d["a"], 1)
        self.assertEqual(d["b"], 2)

        with self.assertRaisesRegex(
            TypeError, r".*\(\) missing 1 required positional argument: 'key'"
        ):
            d.__getitem__()

    def testFromKeys(self):
        d = self.dictClass().fromkeys("abc")
        self.assertEqual(d, {"a": None, "b": None, "c": None})

        d = self.createDictionary()
        self.assertIsNot(d.fromkeys("abc"), d)
        self.assertEqual(d.fromkeys("abc"), {"a": None, "b": None, "c": None})
        self.assertEqual(d.fromkeys((4, 5), 0), {4: 0, 5: 0})
        self.assertEqual(d.fromkeys([]), {})

        def g():
            yield 1

        self.assertEqual(d.fromkeys(g()), {1: None})
        with self.assertRaisesRegex(TypeError, "'int' object is not iterable"):
            {}.fromkeys(3)

        d = self.dictClass()(zip(range(6), range(6)))
        self.assertEqual(dict.fromkeys(d, 0), dict(zip(range(6), [0] * 6)))

    def _testCopy(self):
        self.fail("Decide what to do w.r.t. -copy and -mutableCopy")

    def testGet(self):
        d = self.createDictionary()
        self.assertIs(d.get("c"), None)
        self.assertEqual(d.get("c", 3), 3)

        d = self.createDictionary(a=1, b=2)
        self.assertIs(d.get("c"), None)
        self.assertEqual(d.get("c", 3), 3)
        self.assertEqual(d.get("a"), 1)
        self.assertEqual(d.get("a", 3), 1)
        with self.assertRaisesRegex(
            TypeError, r".*\(\) missing 1 required positional argument: 'key'"
        ):
            d.get()
        with self.assertRaisesRegex(
            TypeError, r".*\(\) takes from 2 to 3 positional arguments but 4 were given"
        ):
            d.get(None, None, None)

    def testEq(self):
        self.assertEqual(self.createDictionary(), self.createDictionary())
        self.assertEqual(self.createDictionary(a=1), self.createDictionary(a=1))

        class Exc(Exception):
            pass

        class BadCmp:
            def __eq__(self, other):
                raise Exc()

            def __hash__(self):
                return 1

        d1 = {BadCmp(): 1}
        d2 = {BadCmp(): 1}

        with self.assertRaises(Exc):
            d1 == d2  # noqa: B015

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

        self.assertTrue(smaller < larger)
        self.assertTrue(smaller <= larger)
        self.assertTrue(larger > smaller)
        self.assertTrue(larger >= smaller)

        self.assertFalse(smaller >= larger)
        self.assertFalse(smaller > larger)
        self.assertFalse(larger <= smaller)
        self.assertFalse(larger < smaller)

        self.assertFalse(smaller < larger3)
        self.assertFalse(smaller <= larger3)
        self.assertFalse(larger3 > smaller)
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
            d1.items() == d2.items()  # noqa: B015
        with self.assertRaises(RuntimeError):
            d1.items() != d2.items()  # noqa: B015
        with self.assertRaises(RuntimeError):
            d1.items() <= d2.items()  # noqa: B015
        with self.assertRaises(RuntimeError):
            d1.items() >= d2.items()  # noqa: B015

        d3 = self.dictClass().dictionaryWithDictionary_({1: C(), 2: C()})
        with self.assertRaises(RuntimeError):
            d2.items() < d3.items()  # noqa: B015
        with self.assertRaises(RuntimeError):
            d3.items() > d2.items()  # noqa: B015

        k1 = self.dictClass().dictionaryWithDictionary_({1: 1, 2: 2}).keys()
        k2 = self.dictClass().dictionaryWithDictionary_({1: 1, 2: 2, 3: 3}).keys()
        k3 = self.dictClass().dictionaryWithDictionary_({4: 4}).keys()

        self.assertEqual(k1 - k2, set())
        self.assertEqual(k1 - k3, {1, 2})
        self.assertEqual(k2 - k1, {3})
        self.assertEqual(k3 - k1, {4})
        self.assertEqual(k1 & k2, {1, 2})
        self.assertEqual(k1 & k3, set())
        self.assertEqual(k1 | k2, {1, 2, 3})
        self.assertEqual(k1 ^ k2, {3})
        self.assertEqual(k1 ^ k3, {1, 2, 4})

    def testDictviewSetOperationsOnItems(self):
        k1 = self.dictClass().dictionaryWithDictionary_({1: 1, 2: 2}).items()
        k2 = self.dictClass().dictionaryWithDictionary_({1: 1, 2: 2, 3: 3}).items()
        k3 = self.dictClass().dictionaryWithDictionary_({4: 4}).items()

        self.assertEqual(k1 - k2, set())
        self.assertEqual(k1 - k3, {(1, 1), (2, 2)})
        self.assertEqual(k2 - k1, {(3, 3)})
        self.assertEqual(k3 - k1, {(4, 4)})
        self.assertEqual(k1 & k2, {(1, 1), (2, 2)})
        self.assertEqual(k1 & k3, set())
        self.assertEqual(k1 | k2, {(1, 1), (2, 2), (3, 3)})
        self.assertEqual(k1 ^ k2, {(3, 3)})
        self.assertEqual(k1 ^ k3, {(1, 1), (2, 2), (4, 4)})

    def testDictviewMixedSetOperations(self):
        # Just a few for .keys()
        self.assertTrue(
            self.dictClass().dictionaryWithDictionary_({1: 1}).keys() == {1}
        )
        self.assertTrue(
            {1} == self.dictClass().dictionaryWithDictionary_({1: 1}).keys()
        )
        self.assertEqual(
            self.dictClass().dictionaryWithDictionary_({1: 1}).keys() | {2}, {1, 2}
        )
        self.assertEqual(
            {2} | self.dictClass().dictionaryWithDictionary_({1: 1}).keys(), {1, 2}
        )
        self.assertFalse(
            self.dictClass().dictionaryWithDictionary_({1: 1}).keys() == [1]
        )

        # And a few for .items()
        self.assertTrue(
            self.dictClass().dictionaryWithDictionary_({1: 1}).items() == {(1, 1)}
        )
        self.assertTrue(
            {(1, 1)} == self.dictClass().dictionaryWithDictionary_({1: 1}).items()
        )
        self.assertEqual(
            self.dictClass().dictionaryWithDictionary_({1: 1}).items() | {2},
            {(1, 1), 2},
        )
        self.assertEqual(
            {2} | self.dictClass().dictionaryWithDictionary_({1: 1}).items(),
            {(1, 1), 2},
        )
        self.assertFalse(
            self.dictClass().dictionaryWithDictionary_({1: 1}).items() == [(1, 1)]
        )


class TestNSMutableDictionaryInterface(TestNSDictionaryInterface):
    def dictClass(self):
        return NSMutableDictionary

    def createDictionary(self, **kwds):
        return NSMutableDictionary.dictionaryWithDictionary_(kwds)

    def testKeysMutable(self):
        d = self.createDictionary()
        self.assertEqual(set(d.keys()), set())

        d = self.createDictionary(a=1, b=2)
        k = d.keys()

        self.assertIn("a", d)
        self.assertIn("b", d)
        self.assertIn("a", k)
        self.assertIn("b", k)

        self.assertNotIsInstance(k, list)

        self.assertNotIn("c", d)
        self.assertNotIn("c", k)

        d["c"] = 3
        self.assertIn("c", d)
        self.assertIn("c", k)

    def testValuesMutable(self):
        d = self.createDictionary()
        self.assertEqual(set(d.values()), set())

        d = self.createDictionary(a=1)
        v = d.values()

        self.assertEqual(set(v), {1})

        d["b"] = 2
        self.assertEqual(set(v), {1, 2})

    def testItemsMutable(self):
        d = self.createDictionary()
        self.assertEqual(set(d.items()), set())

        d = self.createDictionary(a=1)
        i = d.items()

        self.assertEqual(set(i), {("a", 1)})

        d["b"] = 2

        self.assertEqual(set(i), {("a", 1), ("b", 2)})

    def testGetItem(self):
        d = self.createDictionary(a=1, b=2)
        self.assertEqual(d["a"], 1)
        self.assertEqual(d["b"], 2)

        d["c"] = 3
        d["a"] = 4
        self.assertEqual(d["c"], 3)
        self.assertEqual(d["a"], 4)
        del d["b"]
        self.assertEqual(d, {"a": 4, "c": 3})

        with self.assertRaisesRegex(
            TypeError, r".*\(\) missing 1 required positional argument: 'key'"
        ):
            d.__getitem__()

        class Exc(Exception):
            pass

        class BadEq:
            def __eq__(self, other):
                raise Exc()

            def __hash__(self):
                return hash(23)

        d = self.createDictionary()
        d[BadEq()] = 42
        with self.assertRaisesRegex(KeyError, "23"):
            d.__getitem__(23)

        class BadHash:
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
        # with self.assertRaises(Exc):
        #    d[x]

    def testClear(self):
        d = self.createDictionary(a=1, b=2, c=3)
        d.clear()

        self.assertEqual(d, {})

        with self.assertRaisesRegex(
            TypeError, r".*\(\) takes 1 positional argument but 2 were given"
        ):
            d.clear(None)

    def testUpdate(self):
        d = self.createDictionary()
        d.update({1: 100})
        d.update({2: 20})
        d.update({1: 1, 2: 2, 3: 3})
        self.assertEqual(d, {1: 1, 2: 2, 3: 3})

        d.update()
        self.assertEqual(d, {1: 1, 2: 2, 3: 3})

        with self.assertRaisesRegex(
            (TypeError, AttributeError), "'NoneType' object is not iterable"
        ):
            d.update(None)

        class SimpleUserDict:
            def __init__(self):
                self.d = {1: 1, 2: 2, 3: 3}

            def keys(self):
                return self.d.keys()

            def __getitem__(self, i):
                return self.d[i]

        d = self.createDictionary()
        d.update(SimpleUserDict())
        self.assertEqual(d, {1: 1, 2: 2, 3: 3})

        class Exc(Exception):
            pass

        d.clear()

        class FailingUserDict:
            def keys(self):
                raise Exc()

        with self.assertRaises(Exc):
            d.update(FailingUserDict())

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
                            return "a"
                        raise Exc

                return BogonIter()

            def __getitem__(self, key):
                return key

        with self.assertRaises(Exc):
            d.update(FailingUserDict())

        class FailingUserDict:
            def keys(self):
                class BogonIter:
                    def __init__(self):
                        self.i = ord("a")

                    def __iter__(self):
                        return self

                    def __next__(self):
                        if self.i <= ord("z"):
                            rtn = chr(self.i)
                            self.i += 1
                            return rtn
                        raise StopIteration

                return BogonIter()

            def __getitem__(self, key):
                raise Exc

        with self.assertRaises(Exc):
            d.update(FailingUserDict())

        class badseq:
            def __iter__(self):
                return self

            def __next__(self):
                raise Exc()

        with self.assertRaises(Exc):
            {}.update(badseq())
            with self.assertRaisesRegex(ValueError, "foo"):
                {}.update([(1, 2, 3)])

    def setDefault(self):
        d = self.createDictionary()
        self.assertIs(d.setdefault("key0"), None)
        d.setdefault("key0", [])
        self.assertIs(d.setdefault("key0"), None)
        d.setdefault("key", []).append(3)
        self.assertEqual(d["key"][0], 3)
        d.setdefault("key", []).append(4)
        self.assertEqual(len(d["key"]), 2)
        with self.assertRaisesRegex(TypeError, "foo"):
            d.setdefault()

        class Exc(Exception):
            pass

        class BadHash:
            fail = False

            def __hash__(self):
                if self.fail:
                    raise Exc()
                else:
                    return 42

        x = BadHash()
        d[x] = 42
        x.fail = True
        with self.assertRaises(Exc):
            d.setdefault(x, [])

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
                for _ in range(size):
                    ka, va = ta = a.popitem()
                    self.assertEqual(va, int(ka))
                    kb, vb = tb = b.popitem()
                    self.assertEqual(vb, int(kb))
                    self.assertFalse(copymode < 0 and ta != tb)
                self.assertFalse(a)
                self.assertFalse(b)

        d = self.createDictionary()
        with self.assertRaisesRegex(
            KeyError, "'popitem on an empty [A-Z0-9_]*NSDictionary[A-Z0-9_]*"
        ):
            d.popitem()

    def testPop(self):
        d = self.createDictionary()
        k, v = "abc", "def"
        d[k] = v
        with self.assertRaisesRegex(KeyError, "^'ghi'$"):
            d.pop("ghi")

        self.assertEqual(d.pop(k), v)
        self.assertEqual(len(d), 0)

        with self.assertRaisesRegex(KeyError, k):
            d.pop(k)

        self.assertEqual(d.pop(k, v), v)
        d[k] = v
        self.assertEqual(d.pop(k, 1), v)

        with self.assertRaisesRegex(
            TypeError, r".*\(\) missing 1 required positional argument: 'key'"
        ):
            d.pop()

        class Exc(Exception):
            pass

        class BadHash:
            fail = False

            def __hash__(self):
                if self.fail:
                    raise Exc()
                else:
                    return 42

        # XXX
        # x = BadHash()
        # d[x] = 42
        # x.fail = True
        # with self.assertRaises(Exc): d.pop( x)


class DictSetTest(TestCase):
    dictclass = NSDictionary

    def testDictKeys(self):
        d = self.dictclass.dictionaryWithDictionary_({1: 10, "a": "ABC"})

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

        e = self.dictclass.dictionaryWithDictionary_({1: 11, "a": "def"})
        self.assertEqual(d.keys(), e.keys())

    def testDictItems(self):
        d = self.dictclass.dictionaryWithDictionary_({1: 10, "a": "ABC"})
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


class DictSetTest(DictSetTest):
    dictclass = NSMutableDictionary

    def testDictKeysMutable(self):
        d = self.dictclass.dictionaryWithDictionary_({1: 10, "a": "ABC"})
        e = self.dictclass.dictionaryWithDictionary_({1: 11, "a": "def"})
        self.assertEqual(d.keys(), e.keys())

        del e["a"]
        self.assertNotEqual(d.keys(), e.keys())

    def testDictItemsMutable(self):
        d = self.dictclass.dictionaryWithDictionary_({1: 10, "a": "ABC"})

        e = d.copy()
        self.assertEqual(d.items(), e.items())
        d["a"] = "def"
        self.assertNotEqual(d.items(), e.items())

    def testDictMixedKeysItems(self):
        d = self.dictclass.dictionaryWithDictionary_({(1, 1): 11, (2, 2): 22})
        e = self.dictclass.dictionaryWithDictionary_({1: 1, 2: 2})
        self.assertEqual(d.keys(), e.items())
        self.assertNotEqual(d.items(), e.keys())

    def testDictValues(self):
        d = self.dictclass.dictionaryWithDictionary_({1: 10, "a": "ABC"})
        values = d.values()
        self.assertEqual(set(values), {10, "ABC"})
        self.assertEqual(len(values), 2)


class GeneralMappingTestsNSMutableDictionary(mapping_tests.BasicTestMappingProtocol):
    type2test = NSMutableDictionary


class TestDictUpdates(TestCase):
    def do_test(self, dictType):
        d = dictType()
        d["a"] = 42
        with self.assertRaisesRegex(
            TypeError, "update expected at most 1 argument(s)?, got 2"
        ):
            d.update({}, {})

        d.update({"b": 9})
        self.assertEqual(dict(d), {"a": 42, "b": 9})

        d.update({"a": 2})
        self.assertEqual(dict(d), {"a": 2, "b": 9})

        d.update([("a", 1), ("c", 3)])
        self.assertEqual(dict(d), {"a": 1, "b": 9, "c": 3})

        d.update(d=4, a=9, e=3)
        self.assertEqual(dict(d), {"a": 9, "b": 9, "c": 3, "d": 4, "e": 3})

        d.update()
        self.assertEqual(dict(d), {"a": 9, "b": 9, "c": 3, "d": 4, "e": 3})

    def test_native(self):
        self.do_test(dict)

    def test_objc(self):
        self.do_test(NSMutableDictionary)


class TestABC(TestCase):
    def testDictABC(self):
        self.assertTrue(issubclass(NSDictionary, collections.abc.Mapping))
        self.assertTrue(issubclass(NSMutableDictionary, collections.abc.Mapping))
        self.assertTrue(issubclass(NSMutableDictionary, collections.abc.MutableMapping))

    def testViewABC(self):
        d = NSDictionary.dictionary()
        self.assertTrue(isinstance(d.keys(), collections.abc.KeysView))
        self.assertTrue(isinstance(d.values(), collections.abc.ValuesView))
        self.assertTrue(isinstance(d.items(), collections.abc.ItemsView))

        d = NSMutableDictionary.dictionary()
        self.assertTrue(isinstance(d.keys(), collections.abc.KeysView))
        self.assertTrue(isinstance(d.values(), collections.abc.ValuesView))
        self.assertTrue(isinstance(d.items(), collections.abc.ItemsView))


class TestPyObjCDict(TestCase):
    def test_comparison(self):
        with self.assertRaisesRegex(
            TypeError, "'<' not supported between instances of 'dict' and 'dict'"
        ):
            {} < {}  # noqa: B015
        with self.assertRaisesRegex(
            TypeError, "'<=' not supported between instances of 'dict' and 'dict'"
        ):
            {} <= {}  # noqa: B015
        with self.assertRaisesRegex(
            TypeError, "'>' not supported between instances of 'dict' and 'dict'"
        ):
            {} > {}  # noqa: B015
        with self.assertRaisesRegex(
            TypeError, "'>=' not supported between instances of 'dict' and 'dict'"
        ):
            {} >= {}  # noqa: B015

        with self.assertRaisesRegex(
            TypeError,
            "'<' not supported between instances of '[^']*NSDictionary[^']*' and 'dict'",
        ):
            NSDictionary() < {}  # noqa: B015
        with self.assertRaisesRegex(
            TypeError,
            "'<=' not supported between instances of '[^']*NSDictionary[^']*' and 'dict'",
        ):
            NSDictionary() <= {}  # noqa: B015
        with self.assertRaisesRegex(
            TypeError,
            "'>' not supported between instances of '[^']*NSDictionary[^']*' and 'dict'",
        ):
            NSDictionary() > {}  # noqa: B015
        with self.assertRaisesRegex(
            TypeError,
            "'>=' not supported between instances of '[^']*NSDictionary[^']*' and 'dict'",
        ):
            NSDictionary() >= {}  # noqa: B015
        with self.assertRaisesRegex(
            TypeError,
            "'<' not supported between instances of 'dict' and '[^']*NSDictionary[^']*'",
        ):
            {} < NSDictionary()  # noqa: B015
        with self.assertRaisesRegex(
            TypeError,
            "'<=' not supported between instances of 'dict' and '[^']*NSDictionary[^']*'",
        ):
            {} <= NSDictionary()  # noqa: B015
        with self.assertRaisesRegex(
            TypeError,
            "'>' not supported between instances of 'dict' and '[^']*NSDictionary[^']*'",
        ):
            {} > NSDictionary()  # noqa: B015
        with self.assertRaisesRegex(
            TypeError,
            "'>=' not supported between instances of 'dict' and '[^']*NSDictionary[^']*'",
        ):
            {} >= NSDictionary()  # noqa: B015

        self.assertFalse(NSMutableDictionary() == [])
        self.assertFalse(NSDictionary() == [])
        self.assertFalse(NSMutableDictionary() == 42)
        self.assertFalse(NSDictionary() == 42)
        self.assertFalse(NSMutableDictionary() == object())
        self.assertFalse(NSDictionary() == object())

    def test_creation(self):
        for dict_type in (NSDictionary, NSMutableDictionary):
            v = dict_type()
            self.assertIsInstance(v, dict_type)
            self.assertEqual(len(v), 0)

            v = dict_type({1: 2, 2: 3})
            self.assertIsInstance(v, dict_type)
            self.assertEqual(len(v), 2)
            self.assertEqual(v[1], 2)
            self.assertEqual(v[2], 3)

            v = dict_type([(1, -1), (2, 9)])
            self.assertIsInstance(v, dict_type)
            self.assertEqual(len(v), 2)
            self.assertEqual(v[1], -1)
            self.assertEqual(v[2], 9)

            v = dict_type(v for v in [(1, -1), (2, 9)])
            self.assertIsInstance(v, dict_type)
            self.assertEqual(len(v), 2)
            self.assertEqual(v[1], -1)
            self.assertEqual(v[2], 9)

            with self.assertRaisesRegex(
                TypeError, "dict expected at most 1 arguments, got 2"
            ):
                dict_type((1, 2), (3, 4))

            v = dict_type(a=3, b=4)
            self.assertEqual(len(v), 2)
            self.assertEqual(v["a"], 3)
            self.assertEqual(v["b"], 4)

            v = dict_type((v for v in [(1, -1), (2, 9)]), a="hello", b="world")
            self.assertIsInstance(v, dict_type)
            self.assertEqual(len(v), 4)
            self.assertEqual(v[1], -1)
            self.assertEqual(v[2], 9)
            self.assertEqual(v["a"], "hello")
            self.assertEqual(v["b"], "world")

    def test_values(self):
        py = {"a": 4, "b": 3}
        oc = NSDictionary(a=4, b=3)

        self.assertIn(4, py.values())
        self.assertIn(4, oc.values())
        self.assertNotIn(9, py.values())
        self.assertNotIn(9, oc.values())

    def test_view_set(self):
        oc = NSDictionary(a=1, b=2, c=3, d=4, e=5)

        v = oc.keys() | {"a", "f"}
        self.assertEqual(v, {"a", "b", "c", "d", "e", "f"})
        self.assertIsInstance(v, set)
        with self.assertRaisesRegex(
            TypeError, r"unsupported operand type\(s\) for |: 'nsdict_keys' and 'tuple'"
        ):
            oc.keys() | ("a", "f")
        with self.assertRaisesRegex(
            TypeError, r"unsupported operand type\(s\) for |: 'tuple' and 'nsdict_keys'"
        ):
            ("a", "f") | oc.keys()

        v = oc.keys() & {"a", "f"}
        self.assertEqual(v, {"a"})
        self.assertIsInstance(v, set)
        with self.assertRaisesRegex(
            TypeError, r"unsupported operand type\(s\) for &: 'nsdict_keys' and 'tuple'"
        ):
            oc.keys() & ("a", "f")
        with self.assertRaisesRegex(
            TypeError, r"unsupported operand type\(s\) for &: 'tuple' and 'nsdict_keys'"
        ):
            ("a", "f") & oc.keys()

        v = oc.keys() ^ {"a", "f"}
        self.assertEqual(v, {"b", "c", "d", "e", "f"})
        self.assertIsInstance(v, set)
        with self.assertRaisesRegex(
            TypeError,
            r"unsupported operand type\(s\) for \^: 'nsdict_keys' and 'tuple'",
        ):
            oc.keys() ^ ("a", "f")
        with self.assertRaisesRegex(
            TypeError,
            r"unsupported operand type\(s\) for \^: 'tuple' and 'nsdict_keys'",
        ):
            ("a", "f") ^ oc.keys()

        v = oc.keys() - {"a", "f"}
        self.assertEqual(v, {"b", "c", "d", "e"})
        self.assertIsInstance(v, set)
        with self.assertRaisesRegex(
            TypeError, r"unsupported operand type\(s\) for -: 'nsdict_keys' and 'tuple'"
        ):
            oc.keys() - ("a", "f")
        with self.assertRaisesRegex(
            TypeError, r"unsupported operand type\(s\) for -: 'tuple' and 'nsdict_keys'"
        ):
            ("a", "f") - oc.keys()

        with self.assertRaisesRegex(
            TypeError,
            r"'<' not supported between instances of 'nsdict_keys' and 'tuple'",
        ):
            oc.keys() < ("a", "f")  # noqa: B015
        with self.assertRaisesRegex(
            TypeError,
            r"'<=' not supported between instances of 'nsdict_keys' and 'tuple'",
        ):
            oc.keys() <= ("a", "f")  # noqa: B015
        with self.assertRaisesRegex(
            TypeError,
            r"'>' not supported between instances of 'nsdict_keys' and 'tuple'",
        ):
            oc.keys() > ("a", "f")  # noqa: B015
        with self.assertRaisesRegex(
            TypeError,
            r"'>=' not supported between instances of 'nsdict_keys' and 'tuple'",
        ):
            oc.keys() >= ("a", "f")  # noqa: B015
