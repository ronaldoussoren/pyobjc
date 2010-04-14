from PyObjCTools.TestSupport import *
from test import list_tests, seq_tests
import objc

# Import some of the stdlib tests
from test import mapping_tests

NSArray = objc.lookUpClass('NSArray')
NSMutableArray = objc.lookUpClass('NSMutableArray')

# FIXME: Need to create a dictionary to activate the __new__ method.
NSArray.array()

class ArrayTests (seq_tests.CommonTest):
    type2test = NSArray

    def test_constructors(self):

        self.assertEqual(NSArray(), ())
        t0_3 = (0, 1, 2, 3)
        t0_3_bis = NSArray(t0_3)
        self.assertEqual(t0_3, t0_3_bis)

        self.assertEqual(NSArray("hello"), NSArray(["h", "e", "l", "l", "o"]))

    def test_truth(self):
        super(ArrayTests, self).test_truth()
        self.assertTrue(not NSArray())
        self.assertTrue(NSArray([1, 2]))

    def test_len(self):
        super(ArrayTests, self).test_len()

    def test_count(self):
        # Disable test_count because NSArray.count
        # does not conform the right interface
        pass

    def test_index(self):
        # This duplicates the tests in seq_tests, but
        # disables the 'count' test because NSArray.count
        # is not the regular python one.

        u = self.type2test([0, 1])
        self.assertEqual(u.index(0), 0)
        self.assertEqual(u.index(1), 1)
        self.assertRaises(ValueError, u.index, 2)

        u = self.type2test([-2, -1, 0, 0, 1, 2])
        #self.assertEqual(u.count(0), 2)
        self.assertEqual(u.index(0), 2)
        self.assertEqual(u.index(0, 2), 2)
        self.assertEqual(u.index(-2, -10), 0)
        self.assertEqual(u.index(0, 3), 3)
        self.assertEqual(u.index(0, 3, 4), 3)
        self.assertRaises(ValueError, u.index, 2, 0, -10)

        self.assertRaises(TypeError, u.index)


    def test_addmul(self):
        # Same as the one in our superclass, but disables subclassing tests
        u1 = self.type2test([0])
        u2 = self.type2test([0, 1])
        self.assertEqual(u1, u1 + self.type2test())
        self.assertEqual(u1, self.type2test() + u1)
        self.assertEqual(u1 + self.type2test([1]), u2)
        self.assertEqual(self.type2test([-1]) + u1, self.type2test([-1, 0]))
        self.assertEqual(self.type2test(), u2*0)
        self.assertEqual(self.type2test(), 0*u2)
        self.assertEqual(self.type2test(), u2*0)
        self.assertEqual(self.type2test(), 0*u2)
        self.assertEqual(u2, u2*1)
        self.assertEqual(u2, 1*u2)
        self.assertEqual(u2, u2*1)
        self.assertEqual(u2, 1*u2)
        self.assertEqual(u2+u2, u2*2)
        self.assertEqual(u2+u2, 2*u2)
        self.assertEqual(u2+u2, u2*2)
        self.assertEqual(u2+u2, 2*u2)
        self.assertEqual(u2+u2+u2, u2*3)
        self.assertEqual(u2+u2+u2, 3*u2)


    # Disable a couple of tests that are not relevant for us.

    def test_bigrepeat(self): pass
    def test_getitemoverwriteiter(self): pass
    def test_contains_fake(self): 
        # Disabled because the test seems to make use of an
        # implementation detail of sequences, it assumes 
        # that "X in SEQ" is implemented as:
        #
        #   for value in SEQ:
        #       if X == value:   # (1)
        #           return True
        #   return False
        #
        # NSArray seems to have the test on (1) in a 
        # different order: 'if value == X', which causes
        # this test to fail.
        pass
    def test_contains_order(self): 
        # See test_contains_fake
        pass

class MutableArrayTest (list_tests.CommonTest):
    type2test = NSMutableArray

    # Disable a couple of tests that are not relevant for us.
    def test_bigrepeat(self): pass
    def test_repr(self): pass
    def test_contains_fake(self): pass
    def test_print(self): pass

    # Disable inplace operation tests ( += and *= ) because
    # we cannot support true inplace operations: most NSArray
    # and NSMutable array instances are actually instances of
    # NSCFArray and we cannot (and shouldn't detect whether or
    # not a value is mutable)
    def test_imul(self): pass
    def test_iadd(self): pass

if __name__ == "__main__":
    main()
