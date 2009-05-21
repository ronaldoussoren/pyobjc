"""
Minimal tests for sequence proxies

NOTE: this file is very, very incomplete and just tests copying at the moment.
"""
import sys
from PyObjCTools.TestSupport import *
from PyObjCTest.fnd import NSArray, NSMutableArray, NSPredicate, NSObject, NSNull
from PyObjCTest.pythonset import OC_TestSet
import objc

OC_PythonArray = objc.lookUpClass("OC_PythonArray")

class BasicSequenceTests:
    # Tests for sets that don't try to mutate the set.
    # Shared between tests for set() and frozenset()
    seqClass = None

    def testProxyClass(self):
        # Ensure that the right class is used to proxy sets
        self.assert_(OC_TestSet.classOf_(self.seqClass()) is OC_PythonArray)

    def testMutableCopy(self):

        s = self.seqClass(range(20))
        o = OC_TestSet.set_mutableCopyWithZone_(s, None)
        self.assertEquals(list(s), o)
        self.assert_(s is not o)
        self.assert_(isinstance(o, list))

        s = self.seqClass()
        o = OC_TestSet.set_mutableCopyWithZone_(s, None)
        self.assertEquals(list(s), o)
        self.assert_(s is not o)
        self.assert_(isinstance(o, list))




class TestImmutableSequence (TestCase, BasicSequenceTests):
    seqClass = tuple

    def testCopy(self):
        s = self.seqClass()
        o = OC_TestSet.set_copyWithZone_(s, None)
        self.assertEquals(s, o)

        s = self.seqClass(range(20))
        o = OC_TestSet.set_copyWithZone_(s, None)
        self.assertEquals(s, o)

    def testNotMutable(self):
        # Ensure that a frozenset cannot be mutated
        o = self.seqClass([1,2,3])
        self.assertRaises((TypeError, AttributeError),
                OC_TestSet.set_addObject_, o, 4)


class TestMutableSequence (TestCase, BasicSequenceTests):
    seqClass = list

    def testCopy(self):
        s = self.seqClass()
        o = OC_TestSet.set_copyWithZone_(s, None)
        self.assertEquals(s, o)
        self.assert_(s is not o)

        s = self.seqClass(range(20))
        o = OC_TestSet.set_copyWithZone_(s, None)
        self.assertEquals(s, o)
        self.assert_(s is not o)




if __name__ == "__main__":
    main()
