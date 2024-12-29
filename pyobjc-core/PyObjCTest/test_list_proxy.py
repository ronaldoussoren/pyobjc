"""
Minimal tests for sequence proxies

NOTE: this file is very, very incomplete and just tests copying at the moment.
"""

import objc
import collections.abc
import collections
from PyObjCTest.pythonset import OC_TestSet
from PyObjCTest.arrayint import OC_ArrayInt
from PyObjCTools.TestSupport import TestCase, pyobjc_options
from .objectint import OC_NoPythonRepresentation

# XXX: OC_TestSet usage should be moved to a different helper class.

OC_PythonArray = objc.lookUpClass("OC_PythonArray")
OC_BuiltinPythonArray = objc.lookUpClass("OC_BuiltinPythonArray")
NSException = objc.lookUpClass("NSException")
NSArray = objc.lookUpClass("NSArray")
NSNull = objc.lookUpClass("NSNull")


class Fake:
    # XXX: Move to utility module
    @property
    def __pyobjc_object__(self):
        raise TypeError("Cannot proxy")


class BasicSequenceTests:
    # Tests for sets that don't try to mutate the set.
    # Shared between tests for set() and frozenset()
    seqClass = None

    def testProxyClass(self):
        # Ensure that the right class is used to proxy tests
        self.assertIs(OC_TestSet.classOf_(self.seqClass()), OC_BuiltinPythonArray)

    def testMutableCopy(self):
        s = self.seqClass(range(20))
        o = OC_TestSet.set_mutableCopyWithZone_(s, None)
        self.assertEqual(list(s), o)
        self.assertIsNot(s, o)
        self.assertIsInstance(o, list)

        s = self.seqClass()
        o = OC_TestSet.set_mutableCopyWithZone_(s, None)
        self.assertEqual(list(s), o)
        self.assertIsNot(s, o)
        self.assertIsInstance(o, list)

    def test_gettingitems(self):
        seq = self.seqClass(range(5))

        self.assertEqual(OC_ArrayInt.getNthElement_offset_(seq, 0), 0)
        self.assertEqual(OC_ArrayInt.getNthElement_offset_(seq, 3), 3)

        v = OC_ArrayInt.getNthElement_offset_(seq, 9)
        self.assertIsInstance(v, NSException)
        self.assertRegex(str(v), "IndexError.*:.* out of range")

        v = OC_ArrayInt.getNthElement_offset_(seq, 2**63)
        self.assertIsInstance(v, NSException)
        self.assertRegex(str(v), "IndexError.*: out of range")

        seq = self.seqClass([0, None, 2])
        self.assertEqual(OC_ArrayInt.getNthElement_offset_(seq, 0), 0)
        self.assertEqual(OC_ArrayInt.getNthElement_offset_(seq, 1), NSNull.null())
        self.assertEqual(OC_ArrayInt.getNthElement_offset_(seq, 2), 2)

        seq = self.seqClass([Fake()])
        self.assertIsInstance(seq[0], Fake)
        v = OC_ArrayInt.getNthElement_offset_(seq, 0)
        self.assertIsInstance(v, NSException)
        self.assertRegex(str(v), "Cannot proxy")

    def test_getting_range(self):
        seq = self.seqClass(range(10))

        self.assertEqual(OC_ArrayInt.getSub_range_(seq, (0, 2)), [0, 1])
        self.assertEqual(OC_ArrayInt.getSub_range_(seq, (2, 3)), [2, 3, 4])

        with self.assertRaisesRegex(
            IndexError, r"range {22, 2} extends beyond bounds \[0 .. 9\]"
        ):
            OC_ArrayInt.getSub_range_(seq, (22, 2))

        with self.assertRaisesRegex(
            IndexError, r"range {2, 22} extends beyond bounds \[0 .. 9\]"
        ):
            OC_ArrayInt.getSub_range_(seq, (2, 22))

        seq = self.seqClass([Fake(), Fake(), Fake()])
        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            OC_ArrayInt.getSub_range_(seq, (0, 1))


class TestImmutableSequence(TestCase, BasicSequenceTests):
    seqClass = tuple

    def testCopy(self):
        s = self.seqClass()
        o = OC_TestSet.set_copyWithZone_(s, None)
        self.assertEqual(s, o)

        s = self.seqClass(range(20))
        o = OC_TestSet.set_copyWithZone_(s, None)
        self.assertEqual(s, o)

    def testNotMutable(self):
        # Ensure that a frozenset cannot be mutated
        o = self.seqClass([1, 2, 3])
        with self.assertRaisesRegex(
            (TypeError, AttributeError), "'.*' object has no attribute 'append'"
        ):
            OC_TestSet.set_addObject_(o, 4)


class TestMutableSequence(TestCase, BasicSequenceTests):
    seqClass = list

    def testCopy(self):
        s = self.seqClass()
        o = OC_TestSet.set_copyWithZone_(s, None)
        self.assertEqual(s, o)
        self.assertIsNot(s, o)

        s = self.seqClass(range(20))
        o = OC_TestSet.set_copyWithZone_(s, None)
        self.assertEqual(s, o)
        self.assertIsNot(s, o)

    def test_setting_items(self):
        s = self.seqClass(range(5))

        r = OC_ArrayInt.setNthElement_offset_replacement_(s, 0, "hello")
        self.assertIs(r, None)
        self.assertEqual(s[0], "hello")

        r = OC_ArrayInt.setNthElement_offset_replacement_(s, 1, NSNull.null())
        self.assertIs(r, None)
        self.assertEqual(s[1], None)

        v = OC_ArrayInt.setNthElement_offset_replacement_(s, 9, "world")
        self.assertIsInstance(v, NSException)
        self.assertRegex(str(v), "IndexError.*:.* out of range")

        v = OC_ArrayInt.setNthElement_offset_replacement_(s, 2**63, "world")
        self.assertIsInstance(v, NSException)
        self.assertRegex(str(v), "IndexError.*: out of range")

        r = OC_ArrayInt.setNthElement_offset_from_(s, 1, OC_NoPythonRepresentation)
        self.assertIsNot(r, None)
        self.assertIn("cannot have Python representation", str(r))

    def test_add_item(self):
        s = self.seqClass()

        r = OC_ArrayInt.addToArray_value_(s, "hello")
        self.assertIs(r, None)
        self.assertEqual(s[-1], "hello")

        r = OC_ArrayInt.addToArray_value_(s, NSNull.null())
        self.assertIs(r, None)
        self.assertEqual(s[-1], None)

        r = OC_ArrayInt.addToArray_from_(s, OC_NoPythonRepresentation)
        self.assertIsNot(r, None)
        self.assertIn("cannot have Python representation", str(r))

    def test_insert_item(self):
        s = self.seqClass(range(5))

        r = OC_ArrayInt.insertIntoArray_offset_value_(s, 1, "hello")
        self.assertIs(r, None)
        self.assertEqual(s, [0, "hello", 1, 2, 3, 4])

        r = OC_ArrayInt.insertIntoArray_offset_value_(s, 1, NSNull.null())
        self.assertIs(r, None)
        self.assertEqual(s, [0, None, "hello", 1, 2, 3, 4])

        r = OC_ArrayInt.insertIntoArray_offset_value_(s, 2**63, "world")
        self.assertIsInstance(r, NSException)
        self.assertEqual(str(r), "<class 'IndexError'>: No such index")

        # OC_PythonArray forwards to .insert, and that behaves
        # slightly different than the Objective-C API when the index is
        # beyond the end of the list: Python will append, Objective-C
        # raises.
        #
        # The current behaviour has been here from the start and will
        # not be changed.
        r = OC_ArrayInt.insertIntoArray_offset_value_(s, 500, "world")
        self.assertIs(r, None)
        self.assertEqual(s, [0, None, "hello", 1, 2, 3, 4, "world"])

        t = ()
        r = OC_ArrayInt.insertIntoArray_offset_value_(t, 0, "world")
        self.assertIsInstance(r, NSException)
        self.assertEqual(
            str(r), "<class 'AttributeError'>: 'tuple' object has no attribute 'insert'"
        )

        r = OC_ArrayInt.insertIntoArray_offset_from_(s, 0, OC_NoPythonRepresentation)
        self.assertIsNot(r, None)
        self.assertIn("cannot have Python representation", str(r))

    def test_remove_last(self):
        s = self.seqClass(range(1))

        r = OC_ArrayInt.removeLast_(s)
        self.assertIs(r, None)
        self.assertEqual(s, [])

        r = OC_ArrayInt.removeLast_(s)
        self.assertIsInstance(r, NSException)
        self.assertEqual(str(r), "<class 'ValueError'>: pop empty sequence")

        r = OC_ArrayInt.removeLast_((1,))
        self.assertIsInstance(r, NSException)
        self.assertEqual(
            str(r), "<class 'TypeError'>: 'tuple' object doesn't support item deletion"
        )

        class Seq(collections.UserList):
            def __len__(self):
                return -1

        r = OC_ArrayInt.removeLast_(Seq())
        self.assertIsInstance(r, NSException)
        self.assertIn("should return >= 0", str(r))

    def test_remove_at_index(self):
        s = self.seqClass(range(3))

        r = OC_ArrayInt.remove_offset_(s, 1)
        self.assertIs(r, None)
        self.assertEqual(s, [0, 2])

        r = OC_ArrayInt.remove_offset_(s, 4)
        self.assertIsInstance(r, NSException)
        self.assertEqual(
            str(r), "<class 'IndexError'>: list assignment index out of range"
        )

        r = OC_ArrayInt.remove_offset_(s, 2**63 + 5)
        self.assertEqual(str(r), "<class 'IndexError'>: No such index")

        r = OC_ArrayInt.remove_offset_((1,), 0)
        self.assertIsInstance(r, NSException)
        self.assertEqual(
            str(r), "<class 'TypeError'>: 'tuple' object doesn't support item deletion"
        )


class SequenceWithoutLen(collections.abc.Sequence):
    def __getitem__(self, idx):
        return idx**2

    def __len__(self):
        raise RuntimeError("no length")

    def __length_hint__(self):
        raise RuntimeError("no length")


class SequenceWithNegativeLen(collections.abc.Sequence):
    def __getitem__(self, idx):
        return idx**2

    def __len__(self):
        return -4


class TestSequencesWithErrors(TestCase):
    def test_len_raises(self):
        s = SequenceWithoutLen()

        self.assertIs(OC_TestSet.classOf_(s), OC_PythonArray)

        r = OC_ArrayInt.countOf_(s)
        self.assertIsInstance(r, NSException)
        self.assertEqual(str(r), "<class 'RuntimeError'>: no length")

    def test_negative_len(self):
        s = SequenceWithNegativeLen()

        self.assertIs(OC_TestSet.classOf_(s), OC_PythonArray)

        r = OC_ArrayInt.countOf_(s)
        self.assertIsInstance(r, NSException)
        self.assertEqual(str(r), "<class 'ValueError'>: __len__() should return >= 0")

    def test_copy_without_helper(self):
        with pyobjc_options(_copy=None):
            s = [1, 2, 3]
            with self.assertRaisesRegex(ValueError, "cannot copy Python object"):
                OC_TestSet.set_copyWithZone_(s, None)

    def test_copy_raises(self):
        def copy_func(value):
            raise RuntimeError("no copy")

        with pyobjc_options(_copy=copy_func):
            s = [1, 2, 3]

            with self.assertRaisesRegex(RuntimeError, "no copy"):
                OC_TestSet.set_copyWithZone_(s, None)

    def test_copy_cannot_be_proxied(self):
        def copy_func(value):
            return Fake()

        with pyobjc_options(_copy=copy_func):
            s = [1, 2, 3]

            with self.assertRaisesRegex(TypeError, "Cannot proxy"):
                OC_TestSet.set_copyWithZone_(s, None)

    def test_copy_fails(self):
        seq = SequenceWithoutLen()

        with self.assertRaisesRegex(RuntimeError, "no length"):
            OC_TestSet.set_mutableCopyWithZone_(seq, None)
