import operator
import sys

# Import some of the stdlib tests
from test import list_tests, seq_tests

import objc
from PyObjCTools.TestSupport import skipUnless, expectedFailure

NSArray = objc.lookUpClass("NSArray")
NSMutableArray = objc.lookUpClass("NSMutableArray")


class ArrayTests(seq_tests.CommonTest):
    type2test = NSArray

    def test_from_iterator(self):
        a = NSArray(i for i in range(5))
        self.assertEqual(a, NSArray([0, 1, 2, 3, 4]))

    def test_pyobjc_copy(self):
        a = NSArray()
        b = a.copy()
        self.assertEqual(a, b)
        self.assertIsInstance(b, NSArray)

        a = NSArray([0])
        b = a.copy()
        self.assertEqual(a, b)
        self.assertIsInstance(b, NSArray)

        a = NSArray([0, 2])
        b = a.copy()
        self.assertEqual(a, b)
        self.assertIsInstance(b, NSArray)

    @skipUnless(0, "Not relevant for NSArray")
    def test_pickle(self):
        pass

    def test_constructors(self):
        self.assertEqual(NSArray(), ())
        t0_3 = (0, 1, 2, 3)
        t0_3_bis = NSArray(t0_3)
        self.assertEqual(t0_3, t0_3_bis)

        self.assertEqual(NSArray("hello"), NSArray(["h", "e", "l", "l", "o"]))

    def test_truth(self):
        super().test_truth()
        self.assertTrue(not NSArray())
        self.assertTrue(NSArray([1, 2]))

    def test_len(self):
        super().test_len()

    def test_count(self):
        # Disable test_count because NSArray.count
        # does not conform the right interface
        pass

    def test_index(self):
        # This duplicates the tests in seq_tests, but
        # disables the 'count' test because NSArray.count
        # is not the regular python one.

        u = self.type2test()
        with self.assertRaisesRegex(ValueError, ".*not in list"):
            u.index(1)
        with self.assertRaisesRegex(ValueError, ".*not in list"):
            u.index(1, 1)

        u = self.type2test([0, 1])
        self.assertEqual(u.index(0), 0)
        self.assertEqual(u.index(1), 1)
        with self.assertRaises(ValueError):
            u.index(2)

        u = self.type2test([-2, -1, 0, 0, 1, 2])
        # self.assertEqual(u.count(0), 2)
        self.assertEqual(u.index(0), 2)
        self.assertEqual(u.index(0, 2), 2)
        self.assertEqual(u.index(-2, -10), 0)
        self.assertEqual(u.index(0, 3), 3)
        self.assertEqual(u.index(0, 3, 4), 3)
        with self.assertRaisesRegex(ValueError, ".*not in list"):
            u.index(2, 0, -10)

        with self.assertRaises(TypeError):
            u.index()

    def test_addmul(self):
        # Same as the one in our superclass, but disables subclassing tests
        u1 = self.type2test([0])
        u2 = self.type2test([0, 1])
        self.assertEqual(u1, u1 + self.type2test())
        self.assertEqual(u1, self.type2test() + u1)
        self.assertEqual(u1 + self.type2test([1]), u2)
        self.assertEqual(self.type2test([-1]) + u1, self.type2test([-1, 0]))
        self.assertEqual(self.type2test(), u2 * 0)
        self.assertEqual(self.type2test(), 0 * u2)
        self.assertEqual(self.type2test(), u2 * 0)
        self.assertEqual(self.type2test(), 0 * u2)
        self.assertEqual(u2, u2 * 1)
        self.assertEqual(u2, 1 * u2)
        self.assertEqual(u2, u2 * 1)
        self.assertEqual(u2, 1 * u2)
        self.assertEqual(u2 + u2, u2 * 2)
        self.assertEqual(u2 + u2, 2 * u2)
        self.assertEqual(u2 + u2, u2 * 2)
        self.assertEqual(u2 + u2, 2 * u2)
        self.assertEqual(u2 + u2 + u2, u2 * 3)
        self.assertEqual(u2 + u2 + u2, 3 * u2)

    # Disable a couple of tests that are not relevant for us.

    def test_bigrepeat(self):
        pass

    def test_getitemoverwriteiter(self):
        pass

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

    @skipUnless(0, "test irrelevant for NSArray")
    def test_free_after_iterating(self):
        pass


class MutableArrayTest(list_tests.CommonTest):
    type2test = NSMutableArray

    def test_insert_beyond_end(self):
        lst = [1]
        lst.insert(99, "a")
        self.assertEqual(lst, [1, "a"])

        lst = NSMutableArray([1])
        lst.insert(99, "a")
        self.assertEqual(lst, [1, "a"])

    def test_pop(self):
        list_tests.CommonTest.test_pop(self)

    @skipUnless(0, "test irrelevant for NSMutableArray")
    def test_repr_deep(self):
        pass

    @skipUnless(0, "test irrelevant for NSMutableArray")
    def test_exhausted_iterator(self):
        pass

    @skipUnless(0, "test irrelevant for NSMutableArray")
    def test_free_after_iterating(self):
        pass

    @skipUnless(0, "test irrelevant for NSMutableArray")
    def test_copy(self):
        pass

    @skipUnless(0, "Not relevant for NSArray")
    def test_pickle(self):
        pass

    def test_pyobjc_setitem(self):
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        a = NSMutableArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
        with self.assertRaises(TypeError):
            operator.setitem(a, "a", "b")
        with self.assertRaises(ValueError):
            operator.setitem(a, slice(1, 4, 0), ("c", "d"))
        a[1:4] = a
        lst[1:4] = lst
        self.assertEqual(a, NSMutableArray(lst))

        lst = [1, 2, 3, 4]
        a = NSMutableArray([1, 2, 3, 4])
        lst[-2:2] = "a"
        a[-2:2] = "a"
        self.assertEqual(a, NSMutableArray(lst))

        lst = [1, 2, 3, 4]
        a = NSMutableArray([1, 2, 3, 4])
        with self.assertRaises(ValueError):
            operator.setitem(a, slice(None, None, 2), a)
        with self.assertRaises(ValueError):
            operator.setitem(a, slice(None, None, 2), lst)

    def test_pyobjc_clear(self):
        a = NSMutableArray([1, 2, 3])
        self.assertEqual(len(a), 3)

        a.clear()
        self.assertEqual(len(a), 0)

    def test_pyobjc_radd(self):
        a = NSArray([1, 2])

        res = a + [3, 4]
        self.assertEqual(res, NSArray([1, 2, 3, 4]))
        self.assertIsInstance(res, NSArray)

        res = a + (3, 4)
        self.assertEqual(res, NSArray([1, 2, 3, 4]))
        self.assertIsInstance(res, NSArray)

        res = a + (x for x in (3, 4))
        self.assertEqual(res, NSArray([1, 2, 3, 4]))
        self.assertIsInstance(res, NSArray)

        res = [3, 4] + a
        self.assertEqual(res, NSArray([3, 4, 1, 2]))
        self.assertIsInstance(res, NSArray)

        res = (3, 4) + a
        self.assertEqual(res, NSArray([3, 4, 1, 2]))
        self.assertIsInstance(res, NSArray)

        res = (x for x in (3, 4)) + a
        self.assertEqual(res, NSArray([3, 4, 1, 2]))
        self.assertIsInstance(res, NSArray)

    def test_pyobjc_insert(self):
        u = self.type2test([1, 2, 3, 4])
        u.insert(-8, 0)

        v = self.type2test([0, 1, 2, 3, 4])
        self.assertEqual(u, v)

        u = self.type2test([1, 2, 3, 4])
        u.insert(-2, 0)
        v = self.type2test([1, 2, 0, 3, 4])
        self.assertEqual(u, v)

    @expectedFailure
    def test_pyobjc_pop(self):
        u = self.type2test([1, 2, 3, 4])
        with self.assertRaises(IndexError):
            u.pop(-8)

        u = self.type2test([1, 2, 3, 4])
        self.assertEqual(u.pop(-2), 3)

    def test_pyobjc_delitem(self):
        u = self.type2test([1, 2, 3, 4])
        del u[3:1]

        v = self.type2test([1, 2, 3, 4])
        self.assertEqual(u, v)

    def test_init(self):
        # Removed tests that are not relevant

        # Iterable arg is optional
        self.assertEqual(self.type2test([]), self.type2test())

        if 0:
            # Invalid assumption

            # Init clears previous values
            a = self.type2test([1, 2, 3])
            a.__init__()
            self.assertEqual(a, self.type2test([]))

            # Init overwrites previous values
            a = self.type2test([1, 2, 3])
            a.__init__([4, 5, 6])
            self.assertEqual(a, self.type2test([4, 5, 6]))

        # Mutables always return a new object
        a = self.type2test([1, 2, 3])
        b = self.type2test(a)
        self.assertNotEqual(id(a), id(b))
        self.assertEqual(a, b)

    def test_index(self):
        # As superclass, but without calls to u.count
        u = self.type2test([0, 1])
        self.assertEqual(u.index(0), 0)
        self.assertEqual(u.index(1), 1)
        with self.assertRaises(ValueError):
            u.index(2)

        u = self.type2test([-2, -1, 0, 0, 1, 2])
        # self.assertEqual(u.count(0), 2)
        self.assertEqual(u.index(0), 2)
        self.assertEqual(u.index(0, 2), 2)
        self.assertEqual(u.index(-2, -10), 0)
        self.assertEqual(u.index(0, 3), 3)
        self.assertEqual(u.index(0, 3, 4), 3)
        with self.assertRaises(ValueError):
            u.index(2, 0, -10)

        with self.assertRaises(TypeError):
            u.index()

        if 0:
            # Disabled due to dependency on the
            # order of arguments in the '==' expression
            # used to test if an item matches.
            class BadExc(Exception):
                pass

            class BadCmp:
                def __eq__(self, other):
                    if other == 2:
                        raise BadExc()
                    return False

            a = self.type2test([0, 1, 2, 3])
            with self.assertRaises(BadExc):
                a.index(BadCmp())

        a = self.type2test([-2, -1, 0, 0, 1, 2])
        self.assertEqual(a.index(0), 2)
        self.assertEqual(a.index(0, 2), 2)
        self.assertEqual(a.index(0, -4), 2)
        self.assertEqual(a.index(-2, -10), 0)
        self.assertEqual(a.index(0, 3), 3)
        self.assertEqual(a.index(0, -3), 3)
        self.assertEqual(a.index(0, 3, 4), 3)
        self.assertEqual(a.index(0, -3, -2), 3)
        self.assertEqual(a.index(0, -4 * sys.maxsize, 4 * sys.maxsize), 2)
        with self.assertRaises(ValueError):
            a.index(0, 4 * sys.maxsize, -4 * sys.maxsize)
        with self.assertRaises(ValueError):
            a.index(2, 0, -10)
        a.remove(0)
        with self.assertRaises(ValueError):
            a.index(2, 0, 4)
        self.assertEqual(a, self.type2test([-2, -1, 0, 1, 2]))

        if 0:
            # See above
            # Test modifying the list during index's iteration
            class EvilCmp:
                def __init__(self, victim):
                    self.victim = victim

                def __eq__(self, other):
                    del self.victim[:]
                    return False

            a = self.type2test()
            a[:] = [EvilCmp(a) for _ in range(100)]
            # This used to seg fault before patch #1005778
            with self.assertRaises(ValueError):
                a.index(None)

    def test_remove(self):
        # Same as the test inherited from the superclass,
        # but without the tests that  are dependent on
        # the way 'in' tests if an element matches.
        a = self.type2test([0, 0, 1])
        a.remove(1)
        self.assertEqual(a, [0, 0])
        a.remove(0)
        self.assertEqual(a, [0])
        a.remove(0)
        self.assertEqual(a, [])

        with self.assertRaises(ValueError):
            a.remove(0)

        with self.assertRaises(TypeError):
            a.remove()

        d = self.type2test("abcdefghcij")
        d.remove("c")
        self.assertEqual(d, self.type2test("abdefghcij"))
        d.remove("c")
        self.assertEqual(d, self.type2test("abdefghij"))
        with self.assertRaises(ValueError):
            d.remove("c")
        self.assertEqual(d, self.type2test("abdefghij"))

    # Disable a couple of tests that are not relevant for us.
    def test_bigrepeat(self):
        pass

    def test_repr(self):
        pass

    def test_contains_fake(self):
        pass

    def test_print(self):
        pass

    def test_contains_order(self):
        pass

    def test_getitemoverwriteiter(self):
        pass

    # Disable inplace operation tests ( += and *= ) because
    # we cannot support true inplace operations: most NSArray
    # and NSMutable array instances are actually instances of
    # NSCFArray and we cannot (and shouldn't detect whether or
    # not a value is mutable)
    def test_imul(self):
        pass

    def test_iadd(self):
        pass

    def test_count(self):
        # Disabled because NSArray.count has a different
        # interface than list.count
        pass

    def test_sort(self):
        base = [2, 1, 5, 4, 1, 3]

        lst = self.type2test(base)
        lst.sort()
        self.assertEqual(lst, self.type2test([1, 1, 2, 3, 4, 5]))

        lst = self.type2test(base)
        lst.sort(reverse=True)
        self.assertEqual(lst, self.type2test([5, 4, 3, 2, 1, 1]))

        base = [-2, 1, -5, 4, 3]
        lst = self.type2test(base)
        lst.sort(key=lambda x: abs(x))
        self.assertEqual(lst, self.type2test([1, -2, 3, 4, -5]))

        lst = self.type2test(base)
        lst.sort(key=lambda x: abs(x), reverse=True)
        self.assertEqual(lst, self.type2test([-5, 4, 3, -2, 1]))
