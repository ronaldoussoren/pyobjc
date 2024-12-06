"""
Tests for the proxy of Python sets
"""

import objc
from PyObjCTest.fnd import NSNull, NSObject, NSPredicate
from PyObjCTest.pythonset import OC_TestSet
from PyObjCTools.TestSupport import TestCase, pyobjc_options
from PyObjCTest.test_object_proxy import NoObjectiveC

OC_PythonSet = objc.lookUpClass("OC_PythonSet")
OC_BuiltinPythonSet = objc.lookUpClass("OC_BuiltinPythonSet")


class OC_SetPredicate(NSPredicate):
    # A simple test predicate class
    def initWithFunction_(self, pred):
        self = objc.super(OC_SetPredicate, self).init()
        if self is None:
            return None

        self.pred = pred
        return self

    def evaluateWithObject_(self, value):
        return self.pred(value)


class OC_TestElem(NSObject):
    def __new__(self, k):
        return self.alloc().initWithK_(k)

    def initWithK_(self, k):
        objc.super(OC_TestElem, self).init()
        self.k = k
        return self

    def __eq__(self, other):
        return self.k == other.k

    def __hash__(self):
        return hash(self.k)


class BasicSetTests:
    # Tests for sets that don't try to mutate the set.
    # Shared between tests for set() and frozenset()
    setClass = None

    def testProxyClass(self):
        # Ensure that the right class is used to proxy sets
        self.assertIs(OC_TestSet.classOf_(self.setClass()), OC_BuiltinPythonSet)

    def testMutableCopy(self):
        s = self.setClass(range(20))
        o = OC_TestSet.set_mutableCopyWithZone_(s, None)
        self.assertEqual(s, o)
        self.assertIsNot(s, o)
        self.assertIsInstance(o, set)

        s = self.setClass()
        o = OC_TestSet.set_mutableCopyWithZone_(s, None)
        self.assertEqual(s, o)
        self.assertIsNot(s, o)
        self.assertIsInstance(o, set)

    def testAllObject(self):
        s = self.setClass()
        self.assertEqual(OC_TestSet.allObjectsOfSet_(s), [])

        s = self.setClass([1, 2, 3])
        o = OC_TestSet.allObjectsOfSet_(s)
        o.sort()
        self.assertEqual(o, [1, 2, 3])

    def testCount(self):
        s = self.setClass()
        self.assertEqual(OC_TestSet.countOfSet_(s), 0)

        s = self.setClass([1, 2, 3])
        self.assertEqual(OC_TestSet.countOfSet_(s), 3)

    def testAnyObject(self):
        s = self.setClass()
        self.assertEqual(OC_TestSet.anyObjectOfSet_(s), None)

        s = self.setClass([1, 2, 3, 4])
        self.assertIn(OC_TestSet.anyObjectOfSet_(s), s)

    def testContainsObject_(self):
        s = self.setClass([1, 2, 3])

        self.assertFalse(OC_TestSet.set_containsObject_(s, 4))
        self.assertTrue(OC_TestSet.set_containsObject_(s, 2))

        s = self.setClass([1, None])
        self.assertTrue(OC_TestSet.set_containsObject_(s, NSNull.null()))

    def testFilteredSetUsingPredicate(self):
        s = self.setClass(range(10))
        p = OC_SetPredicate.alloc().initWithFunction_(lambda x: x % 2 == 0)

        o = OC_TestSet.set_filteredSetUsingPredicate_(s, p)
        self.assertEqual(o, self.setClass([0, 2, 4, 6, 8]))
        self.assertEqual(len(s), 10)

    def testMakeObjectsPerform(self):
        o1 = OC_TestElem(1)
        o2 = OC_TestElem(2)
        o3 = OC_TestElem(3)
        s = self.setClass([o1, o2, o3])

        o = OC_TestSet.set_member_(s, OC_TestElem(4))
        self.assertIsNone(o)

        o = OC_TestSet.set_member_(s, OC_TestElem(2))
        self.assertIs(o, o2)

    def testObjectEnumerator(self):
        s = self.setClass(range(10))

        enum = OC_TestSet.objectEnumeratorOfSet_(s)
        lst = []
        v = enum.nextObject()
        while v is not None:
            lst.append(v)
            v = enum.nextObject()
        self.assertEqual(lst, list(range(10)))

        s = self.setClass([1, 2, None, 3])
        enum = OC_TestSet.objectEnumeratorOfSet_(s)
        lst = []
        v = enum.nextObject()
        while v is not None:
            lst.append(v)
            v = enum.nextObject()

        self.assertEqual(dict.fromkeys(lst), dict.fromkeys([1, 2, NSNull.null(), 3]))

    def testIsSubSet(self):
        s1 = self.setClass(range(10))
        s2 = self.setClass(range(5))

        self.assertTrue(OC_TestSet.set_isSubsetOfSet_(s2, s1))
        self.assertTrue(OC_TestSet.set_isSubsetOfSet_(s2, s2))
        self.assertFalse(OC_TestSet.set_isSubsetOfSet_(s1, s2))

    def testIntersects(self):
        s1 = self.setClass([1, 2, 3, 4])
        s2 = self.setClass([3, 4, 5, 6])
        s3 = self.setClass([5, 6, 7, 8])

        self.assertTrue(OC_TestSet.set_intersectsSet_(s1, s2))
        self.assertTrue(OC_TestSet.set_intersectsSet_(s2, s3))
        self.assertFalse(OC_TestSet.set_intersectsSet_(s1, s3))

    def testDescription(self):
        s = self.setClass([OC_TestElem(1), 2])
        o = OC_TestSet.descriptionOfSet_(s)
        self.assertIsInstance(o, str)


class TestImmutableSet(TestCase, BasicSetTests):
    setClass = frozenset

    def testCopy(self):
        s = self.setClass()
        o = OC_TestSet.set_copyWithZone_(s, None)
        self.assertEqual(s, o)

        s = self.setClass(range(20))
        o = OC_TestSet.set_copyWithZone_(s, None)
        self.assertEqual(s, o)

    def testNotMutable(self):
        # Ensure that a frozenset cannot be mutated
        o = self.setClass([1, 2, 3])
        with self.assertRaisesRegex(TypeError, "Cannot mutate a frozenset"):
            OC_TestSet.set_addObject_(o, 4)

        with self.assertRaisesRegex(TypeError, "Cannot mutate a frozenset"):
            OC_TestSet.set_removeObject_(o, 2)

        with self.assertRaisesRegex(TypeError, "Cannot mutate a frozenset"):
            OC_TestSet.set_addObjectsFromArray_(o, [4, 5, 6])

        with self.assertRaisesRegex(TypeError, "Cannot mutate a frozenset"):
            OC_TestSet.set_filterUsingPredicate_(
                o,
                NSPredicate.predicateWithValue_(True),
            )

        with self.assertRaisesRegex(TypeError, "Cannot mutate a frozenset"):
            OC_TestSet.set_intersectSet_(o, self.setClass([2, 3, 4]))

        with self.assertRaisesRegex(TypeError, "Cannot mutate a frozenset"):
            OC_TestSet.set_minusSet_(o, self.setClass([2, 3, 4]))

        with self.assertRaisesRegex(TypeError, "Cannot mutate a frozenset"):
            OC_TestSet.set_setSet_(o, self.setClass([2, 3, 4]))

        with self.assertRaisesRegex(TypeError, "Cannot mutate a frozenset"):
            OC_TestSet.set_minusSet_(o, self.setClass([2, 3, 4]))

        with self.assertRaisesRegex(TypeError, "Cannot mutate a frozenset"):
            OC_TestSet.removeAllObjecsFromSet_(o)


class TestMutableSet(TestCase, BasicSetTests):
    setClass = set

    def testCopy(self):
        s = self.setClass()
        o = OC_TestSet.set_copyWithZone_(s, None)
        self.assertEqual(s, o)
        self.assertIsNot(s, o)

        s = self.setClass(range(20))
        o = OC_TestSet.set_copyWithZone_(s, None)
        self.assertEqual(s, o)
        self.assertIsNot(s, o)

    def testUnionSet(self):
        s1 = self.setClass([1, 2, 3])
        s2 = self.setClass([3, 4, 5])

        OC_TestSet.set_unionSet_(s1, s2)
        self.assertEqual(s1, self.setClass([1, 2, 3, 4, 5]))

    def testSetSet(self):
        s1 = self.setClass([1, 2, 3])
        s2 = self.setClass([3, 4, 5])

        OC_TestSet.set_setSet_(s1, s2)
        self.assertEqual(s1, self.setClass([3, 4, 5]))

    def testMinusSet(self):
        s1 = self.setClass([1, 2, 3])
        s2 = self.setClass([3, 4, 5])

        OC_TestSet.set_minusSet_(s1, s2)
        self.assertEqual(s1, self.setClass([1, 2]))

    def testIntersectSet(self):
        s1 = self.setClass([1, 2, 3])
        s2 = self.setClass([3, 4, 5])

        OC_TestSet.set_intersectSet_(s1, s2)
        self.assertEqual(s1, self.setClass([3]))

    def testFilterSet(self):
        s = self.setClass(range(10))
        p = OC_SetPredicate.alloc().initWithFunction_(lambda x: x % 2 == 0)

        OC_TestSet.set_filterUsingPredicate_(s, p)
        self.assertEqual(s, self.setClass([0, 2, 4, 6, 8]))

    def testAddObject(self):
        s = self.setClass([1, 2, 3])

        OC_TestSet.set_addObject_(s, 1)
        self.assertEqual(s, self.setClass([1, 2, 3]))

        OC_TestSet.set_addObject_(s, 9)
        self.assertEqual(s, self.setClass([1, 2, 3, 9]))

    def testAddObjectsFromArray(self):
        s = self.setClass([1, 2, 3])

        OC_TestSet.set_addObjectsFromArray_(s, [1, 2])
        self.assertEqual(s, self.setClass([1, 2, 3]))

        OC_TestSet.set_addObjectsFromArray_(s, [9, 5, 4])
        self.assertEqual(s, self.setClass([1, 2, 3, 9, 5, 4]))

    def testRemoveObject(self):
        s = self.setClass([1, 2, 3])

        OC_TestSet.set_removeObject_(s, 1)
        self.assertEqual(s, self.setClass([2, 3]))

        OC_TestSet.set_removeObject_(s, 9)
        self.assertEqual(s, self.setClass([2, 3]))

    def testRemoveAllObjects(self):
        s = self.setClass([1, 2, 3])

        OC_TestSet.removeAllObjecsFromSet_(s)
        self.assertEqual(s, self.setClass())


class TestMisc(TestCase):
    def test_no_copy_helper(self):
        s = {1, 2, 3}
        with pyobjc_options(_copy=None):
            with self.assertRaisesRegex(ValueError, "cannot copy Python objects"):
                OC_TestSet.set_copyWithZone_(s, None)

    def test_copy_failure(self):
        class S(set):
            def __copy__(self):
                raise RuntimeError("don't copy me")

        s = S()

        with self.assertRaisesRegex(RuntimeError, "don't copy me"):
            OC_TestSet.set_copyWithZone_(s, None)

    def test_copy_not_in_objc(self):
        class S(set):
            def __copy__(self):
                return NoObjectiveC()

        s = S()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            OC_TestSet.set_copyWithZone_(s, None)

    def test_anyObject_not_iterable(self):
        class S(set):
            def __iter__(self):
                raise RuntimeError("no way")

        s = S({1, 2, 3})

        with self.assertRaisesRegex(RuntimeError, "no way"):
            OC_TestSet.anyObjectOfSet_(s)

        class S(set):
            def __iter__(self):
                raise RuntimeError("whoops")
                yield 42

        s = S({1})
        with self.assertRaisesRegex(RuntimeError, "whoops"):
            OC_TestSet.anyObjectOfSet_(s)

    def test_anyObject_not_objc(self):
        class S(set):
            def __iter__(self):
                yield NoObjectiveC()

        s = S({1, 2, 3})

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            OC_TestSet.anyObjectOfSet_(s)

    def test_contains_fails(self):
        class S(set):
            def __contains__(self, o):
                raise TypeError("no containment")

        s = S()

        with self.assertRaisesRegex(TypeError, "no containment"):
            OC_TestSet.set_containsObject_(s, 42)

    def test_len_fails(self):
        class S(set):
            def __len__(self):
                raise TypeError("no length")

        s = S()

        with self.assertRaisesRegex(TypeError, "no length"):
            OC_TestSet.countOfSet_(s)

    def test_objectEnumerator_not_iterable(self):
        class S(set):
            def __iter__(self):
                raise RuntimeError("no way")

        s = S({1, 2, 3})

        with self.assertRaisesRegex(RuntimeError, "no way"):
            OC_TestSet.objectEnumeratorOfSet_(s)

    def test_member_failures(self):
        class S(set):
            def __contains__(self, o):
                raise TypeError("no containment")

        s = S()

        with self.assertRaisesRegex(TypeError, "no containment"):
            OC_TestSet.set_member_(s, 1)

        class S(set):
            def __iter__(self):
                raise TypeError("no iter")

        s = S({1, 2})
        with self.assertRaisesRegex(TypeError, "no iter"):
            OC_TestSet.set_member_(s, 1)

        s = set({NoObjectiveC()})
        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            OC_TestSet.set_member_(s, "")

    def test_clear_fails(self):
        class S(set):
            def clear(self):
                raise TypeError("Cannot clear")

        s = S()

        with self.assertRaisesRegex(TypeError, "Cannot clear"):
            OC_TestSet.removeAllObjecsFromSet_(s)

    def test_discard_fails(self):
        class S(set):
            def discard(self, value):
                raise TypeError("Cannot discard")

        s = S({1, 2})

        with self.assertRaisesRegex(TypeError, "Cannot discard"):
            OC_TestSet.set_removeObject_(s, 2)

    def test_add_fails(self):
        class S(set):
            def add(self, value):
                raise TypeError("Cannot add")

        s = S({1, 2})

        with self.assertRaisesRegex(TypeError, "Cannot add"):
            OC_TestSet.set_addObject_(s, 2)
