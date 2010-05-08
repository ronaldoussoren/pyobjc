"""
Tests if NSSet conforms to the interface of the python type set()

This is a port of the set tests from the Python stdlib for 3.2
"""
from PyObjCTools.TestSupport import *

import objc
NSSet = objc.lookUpClass('NSSet')
NSMutableSet = objc.lookUpClass('NSMutableSet')

import test.test_set
from test.test_set import PassThru, check_pass_thru



class TestMutableSet (test.test_set.TestJointOps, TestCase):
    thetype = NSMutableSet
    basetype = NSMutableSet

    def test_cyclical_repr(self): pass
    def test_pickling(self): pass
    def test_do_not_rehash_dict_keys(self): pass
    def test_badcmp(self): pass
    def test_subclass_with_custom_hash(self): pass

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
        #self.assertEqual(type(u), self.thetype)
        self.assertIsInstance(u, self.thetype)
        self.assertRaises(PassThru, self.s.union, check_pass_thru())
        self.assertRaises(TypeError, self.s.union, [[]])
        for C in set, frozenset, dict.fromkeys, str, unicode, list, tuple:
            self.assertEqual(self.thetype('abcba').union(C('cdc')), set('abcd'))
            self.assertEqual(self.thetype('abcba').union(C('efgfe')), set('abcefg'))
            self.assertEqual(self.thetype('abcba').union(C('ccb')), set('abc'))
            self.assertEqual(self.thetype('abcba').union(C('ef')), set('abcef'))
            self.assertEqual(self.thetype('abcba').union(C('ef'), C('fg')), set('abcefg'))
        
        # Issue #6573
        x = self.thetype()
        self.assertEqual(x.union(set([1]), x, set([2])), self.thetype([1, 2]))

    def test_symmetric_difference(self):
        i = self.s.symmetric_difference(self.otherword)
        for c in self.letters:
            self.assertEqual(c in i, (c in self.d) ^ (c in self.otherword))
        self.assertEqual(self.s, self.thetype(self.word))
        #self.assertEqual(type(i), self.thetype)
        self.assertIsInstance(i, self.thetype)
        self.assertRaises(PassThru, self.s.symmetric_difference, check_pass_thru())
        self.assertRaises(TypeError, self.s.symmetric_difference, [[]])
        for C in set, frozenset, dict.fromkeys, str, unicode, list, tuple:
            self.assertEqual(self.thetype('abcba').symmetric_difference(C('cdc')), set('abd'))
            self.assertEqual(self.thetype('abcba').symmetric_difference(C('efgfe')), set('abcefg'))
            self.assertEqual(self.thetype('abcba').symmetric_difference(C('ccb')), set('a'))
            self.assertEqual(self.thetype('abcba').symmetric_difference(C('ef')), set('abcef'))

    def test_difference(self):
         i = self.s.difference(self.otherword)
         for c in self.letters:
             self.assertEqual(c in i, c in self.d and c not in self.otherword)
         self.assertEqual(self.s, self.thetype(self.word))
         #self.assertEqual(type(i), self.thetype)
         self.assertIsInstance(i, self.thetype)
         self.assertRaises(PassThru, self.s.difference, check_pass_thru())
         self.assertRaises(TypeError, self.s.difference, [[]])        
         for C in set, frozenset, dict.fromkeys, str, unicode, list, tuple:
             self.assertEqual(self.thetype('abcba').difference(C('cdc')), set('ab'))
             self.assertEqual(self.thetype('abcba').difference(C('efgfe')), set('abc'))
             self.assertEqual(self.thetype('abcba').difference(C('ccb')), set('a'))
             self.assertEqual(self.thetype('abcba').difference(C('ef')), set('abc'))
             self.assertEqual(self.thetype('abcba').difference(), set('abc'))
             self.assertEqual(self.thetype('abcba').difference(C('a'), C('b')), set('c'))

    def test_intersection(self):
        i = self.s.intersection(self.otherword)
        for c in self.letters:
            self.assertEqual(c in i, c in self.d and c in self.otherword)
        self.assertEqual(self.s, self.thetype(self.word))
        #self.assertEqual(type(i), self.thetype)        
        self.assertIsInstance(i, self.thetype)        
        self.assertRaises(PassThru, self.s.intersection, check_pass_thru())
        for C in set, frozenset, dict.fromkeys, str, unicode, list, tuple:
            self.assertEqual(self.thetype('abcba').intersection(C('cdc')), set('cc'))
            self.assertEqual(self.thetype('abcba').intersection(C('efgfe')), set(''))
            self.assertEqual(self.thetype('abcba').intersection(C('ccb')), set('bc'))
            self.assertEqual(self.thetype('abcba').intersection(C('ef')), set(''))
            self.assertEqual(self.thetype('abcba').intersection(C('cbcf'), C('bag')), set('b'))
        s = self.thetype('abcba')
        z = s.intersection()
        if self.thetype == frozenset():
            self.assertEqual(id(s), id(z))
        else:
            self.assertNotEqual(id(s), id(z))



class TestSet (TestMutableSet):
    thetype = NSSet
    basetype = NSSet




if __name__ == "__main__":
    main()
