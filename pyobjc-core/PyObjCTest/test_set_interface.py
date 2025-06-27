"""
Tests if NSSet conforms to the interface of the python type set()

This is a port of the set tests from the Python stdlib for 3.2
"""

import collections.abc
import operator
import test.test_set
from test.test_set import PassThru, check_pass_thru

import objc
from PyObjCTools.TestSupport import TestCase, skipUnless

NSSet = objc.lookUpClass("NSSet")
NSMutableSet = objc.lookUpClass("NSMutableSet")


test.test_set.empty_set = NSMutableSet()


class TestPyObjCSet(TestCase):
    def test_reverse_operator(self):
        class MySet(collections.abc.Set):
            def __init__(self, init=()):
                self._value = list(init)

            def __iter__(self):
                return iter(self._value)

            def __contains__(self, value):
                return value in self._value

            def __len__(self):
                return len(self._value)

            def __or__(self, other):
                return NotImplemented

            def __and__(self, other):
                return NotImplemented

            def __xor__(self, other):
                return NotImplemented

            def __sub__(self, other):
                return NotImplemented

            def __add__(self, other):
                return NotImplemented

        s = NSSet([1, 2, 3])

        res = MySet([3, 4]) | s
        self.assertEqual(res, NSSet([1, 2, 3, 4]))
        self.assertIsInstance(res, NSSet)
        with self.assertRaisesRegex(
            TypeError, r"value\|NSSet where value is not a set"
        ):
            (3, 4) | s

        res = MySet([3, 4]) & s
        self.assertEqual(res, NSSet([3]))
        self.assertIsInstance(res, NSSet)
        with self.assertRaisesRegex(TypeError, r"value&NSSet where value is not a set"):
            (3, 4) & s

        res = MySet([3, 4]) - s
        self.assertEqual(res, NSSet([4]))
        self.assertIsInstance(res, NSSet)

        res = MySet([3, 4]) ^ s
        self.assertEqual(res, NSSet([1, 2, 4]))
        self.assertIsInstance(res, NSSet)

    def test_subset(self):
        s = {1, 2, 3}
        self.assertTrue(s.issubset([1, 2, 3, 4]))
        self.assertFalse(s.issubset([1, 2, 4, 5]))

        s = NSSet([1, 2, 3])
        self.assertTrue(s.issubset([1, 2, 3, 4]))
        self.assertFalse(s.issubset([1, 2, 4, 5]))

    def test_superset(self):
        s = {1, 2, 3}
        self.assertTrue(s.issuperset([1, 2]))
        self.assertFalse(s.issuperset([1, 5]))

        s = NSSet([1, 2, 3])
        self.assertTrue(s.issuperset([1, 2]))
        self.assertFalse(s.issuperset([1, 5]))

    def test_conversion(self):
        s = NSSet([1, 2, 3])
        self.assertCountEqual(list(s), [1, 2, 3])

        it = iter(s)
        self.assertCountEqual(list(it), [1, 2, 3])

        it = iter(s)
        next(it)
        v = list(it)
        self.assertEqual(len(v), 2)
        seen = set()
        for x in v:
            self.assertIn(x, s)
            self.assertNotIn(x, seen)
            seen.add(x)


class TestSet(test.test_set.TestJointOps, TestCase):
    thetype = NSSet
    basetype = NSSet

    @skipUnless(0, "test irrelevant for NSMutableSet")
    def test_cyclical_print(self):
        pass

    @skipUnless(0, "test irrelevant for NSMutableSet")
    def test_cyclical_repr(self):
        pass

    @skipUnless(0, "test irrelevant for NSMutableSet")
    def test_pickling(self):
        pass

    @skipUnless(0, "test irrelevant for NSMutableSet")
    def test_do_not_rehash_dict_keys(self):
        pass

    @skipUnless(0, "test irrelevant for NSMutableSet")
    def test_badcmp(self):
        pass

    @skipUnless(0, "test irrelevant for NSMutableSet")
    def test_subclass_with_custom_hash(self):
        pass

    @skipUnless(0, "test irrelevant for NSMutableSet")
    def test_iterator_pickling(self):
        pass

    @skipUnless(0, "test irrelevant for NSMutableSet")
    def test_free_after_iterating(self):
        pass

    def test_deepcopy(self):
        # XXX: is it possible to get this to work?
        pass

    def test_union(self):
        # Same test as inherrited in python 2.7, but without
        # type equality tests
        u = self.s.union(self.otherword)
        for c in self.letters:
            self.assertEqual(c in u, c in self.d or c in self.otherword)

        self.assertEqual(self.s, self.thetype(self.word))
        # self.assertEqual(type(u), self.thetype)
        self.assertIsInstance(u, self.thetype)
        with self.assertRaisesRegex(PassThru, "^$"):
            self.s.union(check_pass_thru())
        with self.assertRaisesRegex(TypeError, "unhashable type: 'list'"):
            self.s.union([[]])
        for C in set, frozenset, dict.fromkeys, str, list, tuple:
            self.assertEqual(self.thetype("abcba").union(C("cdc")), set("abcd"))
            self.assertEqual(self.thetype("abcba").union(C("efgfe")), set("abcefg"))
            self.assertEqual(self.thetype("abcba").union(C("ccb")), set("abc"))
            self.assertEqual(self.thetype("abcba").union(C("ef")), set("abcef"))
            self.assertEqual(
                self.thetype("abcba").union(C("ef"), C("fg")), set("abcefg")
            )

        # Issue #6573
        x = self.thetype()
        self.assertEqual(x.union({1}, x, {2}), self.thetype([1, 2]))

    def test_symmetric_difference(self):
        i = self.s.symmetric_difference(self.otherword)
        for c in self.letters:
            self.assertEqual(c in i, (c in self.d) ^ (c in self.otherword))
        self.assertEqual(self.s, self.thetype(self.word))
        # self.assertEqual(type(i), self.thetype)
        self.assertIsInstance(i, self.thetype)
        with self.assertRaisesRegex(PassThru, "^$"):
            self.s.symmetric_difference(check_pass_thru())
        with self.assertRaisesRegex(TypeError, "unhashable type: 'list'"):
            self.s.symmetric_difference([[]])
        for C in set, frozenset, dict.fromkeys, str, list, tuple:
            self.assertEqual(
                self.thetype("abcba").symmetric_difference(C("cdc")), set("abd")
            )
            self.assertEqual(
                self.thetype("abcba").symmetric_difference(C("efgfe")), set("abcefg")
            )
            self.assertEqual(
                self.thetype("abcba").symmetric_difference(C("ccb")), set("a")
            )
            self.assertEqual(
                self.thetype("abcba").symmetric_difference(C("ef")), set("abcef")
            )

    def test_difference(self):
        i = self.s.difference(self.otherword)
        for c in self.letters:
            self.assertEqual(c in i, c in self.d and c not in self.otherword)
        self.assertEqual(self.s, self.thetype(self.word))
        # self.assertEqual(type(i), self.thetype)
        self.assertIsInstance(i, self.thetype)
        with self.assertRaisesRegex(PassThru, "^$"):
            self.s.difference(check_pass_thru())
        with self.assertRaisesRegex(TypeError, "unhashable type: 'list'"):
            self.s.difference([[]])
        for C in set, frozenset, dict.fromkeys, str, list, tuple:
            self.assertEqual(self.thetype("abcba").difference(C("cdc")), set("ab"))
            self.assertEqual(self.thetype("abcba").difference(C("efgfe")), set("abc"))
            self.assertEqual(self.thetype("abcba").difference(C("ccb")), set("a"))
            self.assertEqual(self.thetype("abcba").difference(C("ef")), set("abc"))
            self.assertEqual(self.thetype("abcba").difference(), set("abc"))
            self.assertEqual(self.thetype("abcba").difference(C("a"), C("b")), set("c"))

    def test_intersection(self):
        i = self.s.intersection(self.otherword)
        for c in self.letters:
            self.assertEqual(c in i, c in self.d and c in self.otherword)
        self.assertEqual(self.s, self.thetype(self.word))
        # self.assertEqual(type(i), self.thetype)
        self.assertIsInstance(i, self.thetype)
        with self.assertRaisesRegex(PassThru, "^$"):
            self.s.intersection(check_pass_thru())
        for C in set, frozenset, dict.fromkeys, str, list, tuple:
            self.assertEqual(self.thetype("abcba").intersection(C("cdc")), set("cc"))
            self.assertEqual(self.thetype("abcba").intersection(C("efgfe")), set(""))
            self.assertEqual(self.thetype("abcba").intersection(C("ccb")), set("bc"))
            self.assertEqual(self.thetype("abcba").intersection(C("ef")), set(""))
            self.assertEqual(
                self.thetype("abcba").intersection(C("cbcf"), C("bag")), set("b")
            )
        s = self.thetype("abcba")
        z = s.intersection()
        if self.thetype == frozenset():
            self.assertEqual(id(s), id(z))
        else:
            self.assertNotEqual(id(s), id(z))

    def test_creation_from_sets(self):
        s1 = {1, 2, 3}
        s2 = frozenset({3, 4, 5})

        s = self.thetype(s1)
        self.assertIsInstance(s, self.thetype)
        self.assertEqual(s, s1)

        s = self.thetype(s2)
        self.assertIsInstance(s, self.thetype)
        self.assertEqual(s, s2)

        n = self.thetype(s)
        self.assertIsInstance(n, self.thetype)
        self.assertEqual(n, s)

    def test_copy(self):
        dup = self.s.copy()
        self.assertEqual(id(self.s), id(dup))

    def test_as_list(self):
        lst = list(self.s)
        self.assertIsInstance(lst, list)
        self.assertEqual(len(lst), len(self.s))
        for item in lst:
            self.assertIn(item, self.s)


class TestMutableSet(TestSet, test.test_set.TestSet):
    thetype = NSMutableSet
    basetype = NSMutableSet

    def test_copy(self):
        # dup = self.s.copy()
        dup = self.s.mutableCopy()
        self.assertEqual(self.s, dup)
        self.assertNotEqual(id(self.s), id(dup))
        # self.assertEqual(type(dup), self.basetype)
        self.assertIsInstance(dup, self.basetype)

    # Tests from 'TestSet'
    @skipUnless(0, "test irrelevant for NSMutableSet")
    def test_init(self):
        pass

    @skipUnless(0, "test irrelevant for NSMutableSet")
    def test_hash(self):
        pass

    @skipUnless(0, "test irrelevant for NSMutableSet")
    def test_weakref(self):
        pass

    @skipUnless(0, "test irrelevant for NSMutableSet")
    def test_iterator_pickling(self):
        pass

    @skipUnless(0, "test irrelevant for NSMutableSet")
    def test_free_after_iterating(self):
        pass


class TestBasicOpsEmpty(test.test_set.TestBasicOps):
    def setUp(self):
        self.case = "empty set"
        self.values = []
        self.set = NSMutableSet(self.values)
        self.dup = NSMutableSet(self.values)
        self.length = 0
        self.repr = "{(\n)}"

    def test_pickling(self):
        pass


class TestBasicOpsSingleton(test.test_set.TestBasicOps):
    def setUp(self):
        self.case = "unit set (number)"
        self.values = [3]
        self.set = NSMutableSet(self.values)
        self.dup = NSMutableSet(self.values)
        self.length = 1
        self.repr = "{(\n    3\n)}"
        test.test_set.set = NSMutableSet

    def tearDown(self):
        del test.test_set.set

    def test_pickling(self):
        pass


class TestBasicOpsTuple(test.test_set.TestBasicOps):
    def setUp(self):
        self.case = "unit set (tuple)"
        self.values = [(0, "zero")]
        self.set = NSMutableSet(self.values)
        self.dup = NSMutableSet(self.values)
        self.length = 1
        self.repr = "{(\n        (\n        0,\n        zero\n    )\n)}"
        test.test_set.set = NSMutableSet

    def tearDown(self):
        del test.test_set.set

    def test_pickling(self):
        pass


class TestBasicOpsTriple(test.test_set.TestBasicOps):
    def setUp(self):
        self.case = "triple set"
        self.values = [0, "zero", operator.add]
        self.set = NSMutableSet(self.values)
        self.dup = NSMutableSet(self.values)
        self.length = 3
        self.repr = None

        test.test_set.set = NSMutableSet

    def tearDown(self):
        del test.test_set.set

    def test_pickling(self):
        pass


class TestBinaryOps(test.test_set.TestBinaryOps):
    def setUp(self):
        self.set = NSMutableSet((2, 4, 6))


class TestUpdateOps(test.test_set.TestUpdateOps):
    def setUp(self):
        self.set = NSMutableSet((2, 4, 6))


class TestMutate(test.test_set.TestMutate):
    def setUp(self):
        self.values = ["a", "b", "c"]
        self.set = NSMutableSet(self.values)

        test.test_set.set = NSMutableSet

    def tearDown(self):
        del test.test_set.set


class TestSubsetEqualEmpty(test.test_set.TestSubsetEqualEmpty):
    left = NSMutableSet()
    right = NSMutableSet()


class TestSubsetEqualNonEmpty(test.test_set.TestSubsetEqualNonEmpty):
    left = NSMutableSet([1, 2])
    right = NSMutableSet([1, 2])


class TestSubsetPartial(test.test_set.TestSubsetPartial):
    left = NSMutableSet([1])
    right = NSMutableSet([1, 2])


class TestOnlySetsNumeric(test.test_set.TestOnlySetsNumeric):
    def setUp(self):
        self.set = NSMutableSet((1, 2, 3))
        self.other = 19
        self.otherIsIterable = False


if hasattr(test.test_set, "TestOnlySetsOperator"):

    class TestOnlySetsOperator(test.test_set.TestOnlySetsOperator):
        def setUp(self):
            self.set = NSMutableSet((1, 2, 3))
            self.other = operator.add
            self.otherIsIterable = False


class TestOnlySetsTuple(test.test_set.TestOnlySetsTuple):
    def setUp(self):
        self.set = NSMutableSet((1, 2, 3))
        self.other = (2, 4, 6)
        self.otherIsIterable = True


class TestOnlySetsString(test.test_set.TestOnlySetsString):
    def setUp(self):
        def gen():
            yield from range(0, 10, 2)

        self.set = NSMutableSet((1, 2, 3))
        self.other = gen()
        self.otherIsIterable = True


class TestIdentities(test.test_set.TestIdentities):
    def setUp(self):
        self.a = NSMutableSet("abracadabra")
        self.b = NSMutableSet("alacazam")


class TestVariousIteratorArgs(test.test_set.TestVariousIteratorArgs):
    def setUp(self):
        test.test_set.set = NSMutableSet

    def tearDown(self):
        del test.test_set.set

    def test_inplace_methods(self):
        for data in (
            "123",
            "",
            range(1000),
            ("do", 1.2),
            range(2000, 2200, 5),
            "december",
        ):
            for methname in (
                "update",
                "intersection_update",
                "difference_update",
                "symmetric_difference_update",
            ):
                with self.subTest(methname):
                    for g in (
                        test.test_set.G,
                        test.test_set.I,
                        test.test_set.Ig,
                        test.test_set.S,
                        test.test_set.L,
                        test.test_set.R,
                    ):
                        # s = set('january')
                        s = NSMutableSet("january")
                        # t = s.copy()
                        t = s.mutableCopy()
                        getattr(s, methname)(list(g(data)))
                        getattr(t, methname)(g(data))
                        self.assertEqual(sorted(s, key=repr), sorted(t, key=repr))

                    with self.assertRaisesRegex(
                        TypeError, "'X' object is not iterable"
                    ):
                        getattr(set("january"), methname)(test.test_set.X(data))

                    with self.assertRaisesRegex(
                        TypeError, r"iter\(\) returned non-iterator of type 'N'"
                    ):
                        getattr(set("january"), methname)(test.test_set.N(data))

                    with self.assertRaisesRegex(
                        ZeroDivisionError, "division.* by zero"
                    ):
                        getattr(set("january"), methname)(test.test_set.E(data))


class TestGraphs(test.test_set.TestGraphs):
    def setUp(self):
        test.test_set.set = NSMutableSet

    def tearDown(self):
        del test.test_set.set
