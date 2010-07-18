"""
Tests for the proxy of Python sets
"""
import sys
from PyObjCTools.TestSupport import *
from PyObjCTest.fnd import NSSet, NSMutableSet, NSPredicate, NSObject, NSNull
from PyObjCTest.pythonset import OC_TestSet
import objc

import os

onLeopard = int(os.uname()[2].split('.')[0]) >= 9

OC_PythonSet = objc.lookUpClass("OC_PythonSet")

class OC_SetPredicate (NSPredicate):
    # A simple test predicate class
    def initWithFunction_(self, pred):
        self = super(OC_SetPredicate, self).init()
        if self is None:
            return None

        self.pred = pred
        return self

    def evaluateWithObject_(self, object):
        return self.pred(object)

class OC_TestElem(NSObject):

    def __new__(self, k):
        return self.alloc().initWithK_(k)

    def initWithK_(self, k):
        super(OC_TestElem, self).init()
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
        self.assertIs(OC_TestSet.classOf_(self.setClass()), OC_PythonSet)

    def testMutableCopy(self):

        s = self.setClass(range(20))
        o = OC_TestSet.set_mutableCopyWithZone_(s, None)
        self.assertEquals(s, o)
        self.assertIsNot(s, o)
        self.assertIsInstance(o, set)

        s = self.setClass()
        o = OC_TestSet.set_mutableCopyWithZone_(s, None)
        self.assertEquals(s, o)
        self.assertIsNot(s, o)
        self.assertIsInstance(o, set)


    def testAllObject(self):
        s = self.setClass()
        self.assertEquals(OC_TestSet.allObjectsOfSet_(s), [])

        s = self.setClass([1,2,3])
        o = OC_TestSet.allObjectsOfSet_(s)
        o.sort()
        self.assertEquals(o, [1,2,3])

    def testCount(self):
        s = self.setClass()
        self.assertEquals(OC_TestSet.countOfSet_(s), 0)

        s = self.setClass([1,2,3])
        self.assertEquals(OC_TestSet.countOfSet_(s), 3)

    def testAnyObject(self):
        s = self.setClass()
        self.assertEquals(OC_TestSet.anyObjectOfSet_(s), None)

        s = self.setClass([1,2,3,4])
        self.assertIn(OC_TestSet.anyObjectOfSet_(s), s)

    def testContainsObject_(self):
        s = self.setClass([1,2,3])

        self.assertFalse(OC_TestSet.set_containsObject_(s, 4))
        self.assertTrue(OC_TestSet.set_containsObject_(s, 2))

    if onLeopard:
        def testFilteredSetUsingPredicate(self):
            s = self.setClass(range(10))
            p = OC_SetPredicate.alloc().initWithFunction_(lambda x: x % 2 == 0)

            o = OC_TestSet.set_filteredSetUsingPredicate_(s, p)
            self.assertEquals(o, self.setClass([0, 2, 4, 6, 8]))
            self.assertEquals(len(s), 10)

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
        l = []
        v = enum.nextObject()
        while v is not None:
            l.append(v)
            v = enum.nextObject()
        self.assertEquals(l, list(range(10)))

        s = self.setClass([1, 2, None, 3])
        enum = OC_TestSet.objectEnumeratorOfSet_(s)
        l = []
        v = enum.nextObject()
        while v is not None:
            l.append(v)
            v = enum.nextObject()


        self.assertEquals(dict.fromkeys(l), dict.fromkeys([1,2,NSNull.null(),3]))

    def testIsSubSet(self):
        s1 = self.setClass(range(10))
        s2 = self.setClass(range(5))

        self.assertTrue(OC_TestSet.set_isSubsetOfSet_(s2, s1))
        self.assertTrue(OC_TestSet.set_isSubsetOfSet_(s2, s2))
        self.assertFalse(OC_TestSet.set_isSubsetOfSet_(s1, s2))

    def testIntersects(self):
        s1 = self.setClass([1,2,3,4])
        s2 = self.setClass([3,4,5,6])
        s3 = self.setClass([5,6,7,8])

        self.assertTrue(OC_TestSet.set_intersectsSet_(s1, s2))
        self.assertTrue(OC_TestSet.set_intersectsSet_(s2, s3))
        self.assertFalse(OC_TestSet.set_intersectsSet_(s1, s3))

    def testDescription(self):
        s = self.setClass([OC_TestElem(1), 2])
        o = OC_TestSet.descriptionOfSet_(s)
        self.assertIsInstance(o, unicode)


class TestImmutableSet (TestCase, BasicSetTests):
    setClass = frozenset

    def testCopy(self):
        s = self.setClass()
        o = OC_TestSet.set_copyWithZone_(s, None)
        self.assertEquals(s, o)

        s = self.setClass(range(20))
        o = OC_TestSet.set_copyWithZone_(s, None)
        self.assertEquals(s, o)

    def testNotMutable(self):
        # Ensure that a frozenset cannot be mutated
        o = self.setClass([1,2,3])
        self.assertRaises((TypeError, AttributeError),
                OC_TestSet.set_addObject_, o, 4)

        self.assertRaises(TypeError,
                OC_TestSet.set_removeObject_, o, 2)

        self.assertRaises(TypeError,
                OC_TestSet.set_addObjectsFromArray_, o, [4, 5, 6])

        if onLeopard:
            self.assertRaises(TypeError,
                    OC_TestSet.set_filterUsingPredicate_, o, 
                    NSPredicate.predicateWithValue_(True))

        self.assertRaises(TypeError,
                OC_TestSet.set_intersectSet_, o, self.setClass([2,3,4]))

        self.assertRaises(TypeError,
                OC_TestSet.set_minusSet_, o, self.setClass([2,3,4]))

        self.assertRaises(TypeError,
                OC_TestSet.set_setSet_, o, self.setClass([2,3,4]))

        self.assertRaises(TypeError,
                OC_TestSet.set_minusSet_, o, self.setClass([2,3,4]))

        self.assertRaises(TypeError,
                OC_TestSet.removeAllObjecsFromSet_, o)


class TestMutableSet (TestCase, BasicSetTests):
    setClass = set

    def testCopy(self):
        s = self.setClass()
        o = OC_TestSet.set_copyWithZone_(s, None)
        self.assertEquals(s, o)
        self.assertIsNot(s, o)

        s = self.setClass(range(20))
        o = OC_TestSet.set_copyWithZone_(s, None)
        self.assertEquals(s, o)
        self.assertIsNot(s, o)

    def testUnionSet(self):
        s1 = self.setClass([1,2,3])
        s2 = self.setClass([3,4,5])

        OC_TestSet.set_unionSet_(s1, s2)
        self.assertEquals(s1, self.setClass([1,2,3,4,5]))

    def testSetSet(self):
        s1 = self.setClass([1,2,3])
        s2 = self.setClass([3,4,5])

        OC_TestSet.set_setSet_(s1, s2)
        self.assertEquals(s1, self.setClass([3,4,5]))

    def testMinusSet(self):
        s1 = self.setClass([1,2,3])
        s2 = self.setClass([3,4,5])

        OC_TestSet.set_minusSet_(s1, s2)
        self.assertEquals(s1, self.setClass([1, 2]))

    def testIntersectSet(self):
        s1 = self.setClass([1,2,3])
        s2 = self.setClass([3,4,5])

        OC_TestSet.set_intersectSet_(s1, s2)
        self.assertEquals(s1, self.setClass([3]))

    if onLeopard:
        def testFilterSet(self):
            s = self.setClass(range(10))
            p = OC_SetPredicate.alloc().initWithFunction_(lambda x: x % 2 == 0)

            OC_TestSet.set_filterUsingPredicate_(s, p)
            self.assertEquals(s, self.setClass([0, 2, 4, 6, 8]))

    def testAddObject(self):
        s = self.setClass([1,2,3])

        OC_TestSet.set_addObject_(s, 1)
        self.assertEquals(s, self.setClass([1,2,3]))

        OC_TestSet.set_addObject_(s, 9)
        self.assertEquals(s, self.setClass([1,2,3,9]))

    def testAddObjectsFromArray(self):
        s = self.setClass([1,2,3])

        OC_TestSet.set_addObjectsFromArray_(s, [1,2])
        self.assertEquals(s, self.setClass([1,2,3]))

        OC_TestSet.set_addObjectsFromArray_(s, [9,5,4])
        self.assertEquals(s, self.setClass([1,2,3,9,5,4]))

    def testRemoveObject(self):
        s = self.setClass([1,2,3])

        OC_TestSet.set_removeObject_(s, 1)
        self.assertEquals(s, self.setClass([2,3]))

        OC_TestSet.set_removeObject_(s, 9)
        self.assertEquals(s, self.setClass([2,3]))

    def testRemoveAllObjects(self):
        s = self.setClass([1,2,3])

        OC_TestSet.removeAllObjecsFromSet_(s)
        self.assertEquals(s, self.setClass())



if __name__ == "__main__":
    main()
