import sys

import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

if sys.version_info[0] == 3:

    def cmp(a, b):
        if a < b:
            return -1
        elif b < a:
            return 1
        return 0


class TestNSArrayInteraction(TestCase):
    def testRepeatedAllocInit(self):
        for _ in range(1, 1000):
            _ = Foundation.NSArray.alloc().init()

    def testIndices(self):
        x = Foundation.NSArray.arrayWithArray_(["foo", "bar", "baz"])

        self.assertEqual(x.indexOfObject_("bar"), 1)

        self.assertRaises(IndexError, x.objectAtIndex_, 100)

    def testEnumeration(self):
        x = Foundation.NSArray.arrayWithArray_([1, 2, "foo", "bar", "", "baz"])
        y = []

        for o in x:
            y.append(o)

        self.assertEqual(len(x), len(y))

    def testContains(self):
        x = Foundation.NSArray.arrayWithArray_(["foo", "bar", "baz"])
        self.assertEqual(x.count(), 3)
        self.assertEqual(len(x), 3)

        self.assertTrue(x.containsObject_("foo"))
        self.assertTrue(not x.containsObject_("dumbledorf"))

        self.assertTrue("foo" in x)
        self.assertTrue("dumbledorf" not in x)

    def testIn(self):
        x = Foundation.NSMutableArray.array()
        for i in range(0, 100):
            x.addObject_(i)

        y = []
        for i in x:
            y.append(i)

        z = []
        for i in range(0, 100):
            z.append(i)

        self.assertEqual(x, y)
        self.assertEqual(x, z)
        self.assertEqual(y, z)

        for i in range(0, 100):
            self.assertTrue(i in x)

        self.assertTrue(101 not in x)
        self.assertTrue(None not in x)
        self.assertTrue("foo bar" not in x)

    def assertSlicesEqual(self, x, y, z):
        self.assertEqual(x, x[:])
        self.assertEqual(y, y[:])
        self.assertEqual(z, z[:])

        self.assertEqual(x[25:75], y[25:75])
        self.assertEqual(x[25:75], z[25:75])
        self.assertEqual(y[25:75], z[25:75])

        self.assertEqual(x[:15], y[:15])
        self.assertEqual(x[:15], z[:15])
        self.assertEqual(y[:15], z[:15])

        self.assertEqual(x[15:], y[15:])
        self.assertEqual(x[15:], z[15:])
        self.assertEqual(y[15:], z[15:])

        self.assertEqual(x[-15:], y[-15:])
        self.assertEqual(x[-15:], z[-15:])
        self.assertEqual(y[-15:], z[-15:])

        self.assertEqual(x[-15:30], y[-15:30])
        self.assertEqual(x[-15:30], z[-15:30])
        self.assertEqual(y[-15:30], z[-15:30])

        self.assertEqual(x[-15:-5], y[-15:-5])
        self.assertEqual(x[-15:-5], z[-15:-5])
        self.assertEqual(y[-15:-5], z[-15:-5])

    def testSlice(self):
        x = Foundation.NSMutableArray.array()
        for i in range(0, 100):
            x.addObject_(i)

        y = []
        for i in x:
            y.append(i)

        z = []
        for i in range(0, 100):
            z.append(i)

        self.assertSlicesEqual(x, y, z)

        k = range(300, 50)
        x[20:30] = k
        y[20:30] = k
        z[20:30] = k

        self.assertSlicesEqual(x, y, z)

        # Note that x[1] = x works in python, but not for a bridged Foundation.NS*Array*.
        # Not sure if there is anything we can do about that.
        x[1] = x[:]
        y[1] = y[:]
        z[1] = z[:]

        self.assertSlicesEqual(x, y, z)

        del x[-15:-5]
        del y[-15:-5]
        del z[-15:-5]

        self.assertSlicesEqual(x, y, z)

    def test_mixSliceNDice(self):
        # This test failes on Python 2.2, that is expected.
        x = list(range(0, 10))
        y = Foundation.NSMutableArray.arrayWithArray_(range(0, 10))

        y[2:4] = x[1:5]
        x[2:8] = y[3:7]
        y[2:4] = y[1:8]

    def test_subScripts(self):
        x = list(range(0, 10))
        y = Foundation.NSMutableArray.arrayWithArray_(x)

        self.assertEqual(x[0], y[0])
        self.assertEqual(x[2], y[2])

        self.assertEqual(x[-1], y[-1])
        self.assertEqual(x[-5], y[-5])

        self.assertRaises(IndexError, x.__getitem__, 100)
        self.assertRaises(IndexError, x.__getitem__, -100)

    def test_varargConstruction(self):
        w = Foundation.NSArray.arrayWithObjects_(1, 2, 3, 4)
        x = Foundation.NSArray.alloc().initWithObjects_(1, 2, 3, 4)

        y = Foundation.NSArray.arrayWithObjects_count_([1, 2, 3, 4, 5, 6], 4)
        z = Foundation.NSArray.alloc().initWithObjects_count_([1, 2, 3, 4, 5, 6], 4)

        self.assertEqual(len(w), 4)
        self.assertEqual(len(x), 4)
        self.assertEqual(len(y), 4)
        self.assertEqual(len(z), 4)

        self.assertEqual(w[0], 1)
        self.assertEqual(x[1], 2)
        self.assertEqual(y[2], 3)
        self.assertEqual(z[3], 4)

    def test_varargConstruction2(self):
        w = Foundation.NSMutableArray.arrayWithObjects_(1, 2, 3, 4, None)
        x = Foundation.NSMutableArray.alloc().initWithObjects_(1, 2, 3, 4, None)
        y = Foundation.NSMutableArray.arrayWithObjects_count_([1, 2, 3, 4, 5, 6], 4)
        z = Foundation.NSMutableArray.alloc().initWithObjects_count_(
            [1, 2, 3, 4, 5, 6], 4
        )

        self.assertEqual(len(w), 4)
        self.assertEqual(len(x), 4)
        self.assertEqual(len(y), 4)
        self.assertEqual(len(z), 4)

        self.assertEqual(w[0], 1)
        self.assertEqual(x[1], 2)
        self.assertEqual(y[2], 3)
        self.assertEqual(z[3], 4)


class TestNSArraySpecialMethods(TestCase):
    # Test calling 'difficult' methods from Python

    def test_initWithObjects_count_(self):
        a = Foundation.NSArray.alloc().initWithObjects_count_(("a", "b", "c", "d"), 3)
        self.assertEqual(a, ["a", "b", "c"])

        import warnings

        warnings.filterwarnings("ignore", category=objc.UninitializedDeallocWarning)

        try:
            self.assertRaises(
                ValueError,
                Foundation.NSArray.alloc().initWithObjects_count_,
                ("a", "b"),
                3,
            )

        finally:
            del warnings.filters[0]

    def test_arrayWithObjects_count_(self):
        a = Foundation.NSArray.arrayWithObjects_count_(("a", "b", "c", "d"), 3)
        self.assertEqual(a, ["a", "b", "c"])

        self.assertRaises(
            ValueError, Foundation.NSArray.arrayWithObjects_count_, ("a", "b"), 3
        )

    def test_arrayByAddingObjects_count_(self):
        return

        a = Foundation.NSArray.arrayWithArray_(("a", "b", "c"))
        self.assertEqual(a, ("a", "b", "c"))

        b = a.arrayByAddingObjects_count_(("d", "e", "f"), 3)
        self.assertEqual(a, ("a", "b", "c"))
        self.assertEqual(b, ("a", "b", "c", "d", "e", "f"))

        self.assertRaises(ValueError, a.arrayByAddingObjects_count_, ("a", "b"), 3)

    def test_sortedArrayUsingFunction_context_(self):
        a = Foundation.NSArray.arrayWithArray_(("a", "b", "c"))
        self.assertEqual(a, ("a", "b", "c"))

        def cmpfunc(l, r, c):
            return -cmp(l, r)

        b = a.sortedArrayUsingFunction_context_(cmpfunc, "hello")
        self.assertEqual(a, ("a", "b", "c"))
        self.assertEqual(b, ("c", "b", "a"))

    def test_sortedArrayUsingFunction_context_hint_(self):
        a = Foundation.NSArray.arrayWithArray_(("a", "b", "c"))
        self.assertEqual(a, ("a", "b", "c"))

        def cmpfunc(l, r, c):
            return -cmp(l, r)

        b = a.sortedArrayUsingFunction_context_hint_(
            cmpfunc, "hello", a.sortedArrayHint()
        )
        self.assertEqual(a, ("a", "b", "c"))
        self.assertEqual(b, ("c", "b", "a"))


class TestNSMutableArrayInteraction(TestCase):
    def testRemoveObjects(self):
        a = Foundation.NSMutableArray.arrayWithArray_(range(10))

        self.assertEqual(len(a), 10)
        self.assertEqual(a[0], 0)
        self.assertEqual(a[1], 1)
        self.assertEqual(a[2], 2)

        a.removeObjectsFromIndices_numIndices_([2, 4, 6, 8], 3)

        self.assertEqual(len(a), 7)
        self.assertEqual(a, (0, 1, 3, 5, 7, 8, 9))

    def testReplaceObjects(self):
        if objc.platform == "MACOSX" or hasattr(
            Foundation.NSMutableArray, "replaceObjectsInRange_withObjects_count_"
        ):

            a = Foundation.NSMutableArray.arrayWithArray_(range(4))
            self.assertEqual(a, (0, 1, 2, 3))

            a.replaceObjectsInRange_withObjects_count_((1, 2), ["a", "b", "c", "d"], 3)

            self.assertEqual(a, (0, "a", "b", "c", 3))

    def testSortInvalid(self):
        # Invalid calls to sortUsingFunction:context:
        def cmp(a, b):
            return -1

        a = Foundation.NSMutableArray.arrayWithArray_(range(4))
        self.assertEqual(a, (0, 1, 2, 3))

        t = objc.options.verbose
        # objc.options.verbose = True
        try:
            self.assertRaises(TypeError, a.sortUsingFunction_context_, dir)
            self.assertRaises(TypeError, a.sortUsingFunction_context_, dir, 1, 2)
            self.assertRaises(
                TypeError, a.sortUsingFunction_context_, lambda *args: cmp(*args), "a"
            )
        finally:
            objc.options.verbose = t

    def dont_testSort2(self):
        # sortUsingFunction:context:range: isn't documented an hence shouldn't be tested
        a = Foundation.NSMutableArray.arrayWithArray_(range(10))
        self.assertEqual(a, (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))

        if objc.platform == "MACOSX" or hasattr(a, "sortUsingFunction_context_range_"):

            def cmpfunc(l, r, c):
                return -cmp(l, r)

            a.sortUsingFunction_context_range_(cmpfunc, "a", (4, 4))

            self.assertEqual(a, (0, 1, 2, 3, 7, 6, 5, 4, 8, 9))

    def testSort1(self):
        a = Foundation.NSMutableArray.arrayWithArray_(range(4))
        self.assertEqual(a, (0, 1, 2, 3))

        def cmpfunc(l, r, c):
            return -cmp(l, r)

        a.sortUsingFunction_context_(cmpfunc, "a")

        self.assertEqual(a, (3, 2, 1, 0))

    def dont_testSort2_2(self):  # XXX
        a = Foundation.NSMutableArray.arrayWithArray_(range(10))
        self.assertEqual(a, (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))

        if objc.platform == "MACOSX" or hasattr(a, "sortUsingFunction_context_range_"):

            def cmpfunc(l, r, c):
                return -cmp(l, r)

            a.sortUsingFunction_context_range_(cmpfunc, "a", (4, 4))

            self.assertEqual(a, (0, 1, 2, 3, 7, 6, 5, 4, 8, 9))

    def testSort4(self):
        # check the sort method, list interface compatibility

        a = Foundation.NSMutableArray.arrayWithArray_(range(4))
        self.assertEqual(a, (0, 1, 2, 3))

        def cmpfunc(l, r):
            return -cmp(l, r)

        if sys.version_info[0] == 2:
            a.sort(cmp=cmpfunc)
            self.assertEqual(a, (3, 2, 1, 0))
        else:
            self.assertRaises(TypeError, a.sort, cmp=cmpfunc)

        a.sort()
        self.assertEqual(a, (0, 1, 2, 3))

        mapping = {0: "nul", 1: "een", 2: "twee", 3: "drie"}

        def keyfunc(l):
            return mapping[l]

        a.sort(key=keyfunc)
        self.assertEqual(a, (3, 1, 0, 2))

        a.sort(key=keyfunc, reverse=True)
        self.assertEqual(a, (2, 0, 1, 3))

        a.sort(reverse=True)
        self.assertEqual(a, (3, 2, 1, 0))

    def getObjectsRange(self):
        o = Foundation.NSArray.arrayWithArray_(range(4, 8))
        v = o.getObjects_range_((1, 2))
        self.assertEqual(v, (5, 6))

    def test_unsupportedMethods(self):
        #
        # Check that calling unsupported methods results in a TypeError
        #
        # NOTE: Some of these don't even exist on GNUstep
        o = Foundation.NSArray.arrayWithArray_(range(4))
        self.assertRaises(TypeError, o.getObjects_)

        #
        # if objc.platform == 'MACOSX' or hasattr(o, 'apply_context_'):
        #    self.assertRaises(TypeError, o.apply_context_, lambda x, y:None, 0)

    def testInsert(self):
        o = Foundation.NSMutableArray.arrayWithArray_(range(4))
        self.assertEqual(list(o), list(range(4)))

        self.assertEqual(o[0], 0)
        o.insert(0, "foo")
        self.assertEqual(o[0], "foo")
        self.assertEqual(o[1], 0)
        self.assertEqual(len(o), 5)

        # FIXME: test the entire interface of list.insert


class TestVariadic(TestCase):
    def testArrayWithObjects(self):
        a = Foundation.NSArray.arrayWithObjects_("foo", "bar", None)
        self.assertEqual(a, ("foo", "bar"))
        self.assertIsInstance(a, Foundation.NSArray)

        a = Foundation.NSMutableArray.arrayWithObjects_("foo", "bar", None)
        self.assertEqual(a, ["foo", "bar"])
        self.assertIsInstance(a, Foundation.NSMutableArray)

    def testInitWithObjecs(self):
        a = Foundation.NSArray.alloc().initWithObjects_("foo", "bar", None)
        self.assertEqual(a, ("foo", "bar"))
        self.assertIsInstance(a, Foundation.NSArray)

        a = Foundation.NSMutableArray.alloc().initWithObjects_("foo", "bar", None)
        self.assertEqual(a, ["foo", "bar"])
        self.assertIsInstance(a, Foundation.NSMutableArray)


class TestNSArray(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSArray.isEqualToArray_)
        self.assertResultIsBOOL(Foundation.NSArray.containsObject_)
        self.assertResultIsBOOL(Foundation.NSArray.writeToFile_atomically_)
        self.assertArgIsBOOL(Foundation.NSArray.writeToFile_atomically_, 1)
        self.assertResultIsBOOL(Foundation.NSArray.writeToURL_atomically_)
        self.assertArgIsBOOL(Foundation.NSArray.writeToURL_atomically_, 1)

        self.assertArgIsSEL(Foundation.NSArray.makeObjectsPerformSelector_, 0, b"v@:")
        self.assertArgIsSEL(
            Foundation.NSArray.makeObjectsPerformSelector_withObject_, 0, b"v@:@"
        )

        self.assertArgIsBOOL(Foundation.NSArray.initWithArray_copyItems_, 1)

        self.assertArgIsIn(Foundation.NSArray.arrayWithObjects_count_, 0)
        self.assertArgSizeInArg(Foundation.NSArray.arrayWithObjects_count_, 0, 1)
        self.assertArgIsIn(Foundation.NSArray.initWithObjects_count_, 0)
        self.assertArgSizeInArg(Foundation.NSArray.initWithObjects_count_, 0, 1)

        self.assertArgIsIn(
            Foundation.NSMutableArray.removeObjectsFromIndices_numIndices_, 0
        )
        self.assertArgSizeInArg(
            Foundation.NSMutableArray.removeObjectsFromIndices_numIndices_, 0, 1
        )

        self.assertArgIsFunction(
            Foundation.NSArray.sortedArrayUsingFunction_context_, 0, b"l@@@", False
        )
        self.assertArgHasType(
            Foundation.NSArray.sortedArrayUsingFunction_context_, 1, b"@"
        )
        self.assertArgIsFunction(
            Foundation.NSArray.sortedArrayUsingFunction_context_hint_, 0, b"l@@@", False
        )
        self.assertArgHasType(
            Foundation.NSArray.sortedArrayUsingFunction_context_hint_, 1, b"@"
        )
        self.assertArgIsSEL(Foundation.NSArray.sortedArrayUsingSelector_, 0, b"i@:@")

        self.assertArgIsFunction(
            Foundation.NSMutableArray.sortUsingFunction_context_, 0, b"l@@@", False
        )
        self.assertArgHasType(
            Foundation.NSMutableArray.sortUsingFunction_context_, 1, b"@"
        )

        self.assertArgIsSEL(Foundation.NSMutableArray.sortUsingSelector_, 0, b"i@:@")

        self.assertIsNullTerminated(Foundation.NSArray.arrayWithObjects_)
        self.assertIsNullTerminated(Foundation.NSArray.initWithObjects_)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgIsBlock(
            Foundation.NSArray.enumerateObjectsUsingBlock_,
            0,
            b"v@" + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            Foundation.NSArray.enumerateObjectsWithOptions_usingBlock_,
            1,
            b"v@" + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            Foundation.NSArray.enumerateObjectsAtIndexes_options_usingBlock_,
            2,
            b"v@" + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )

        self.assertArgIsBlock(
            Foundation.NSArray.indexOfObjectPassingTest_,
            0,
            objc._C_NSBOOL + b"@" + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            Foundation.NSArray.indexOfObjectWithOptions_passingTest_,
            1,
            objc._C_NSBOOL + b"@" + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            Foundation.NSArray.indexOfObjectAtIndexes_options_passingTest_,
            2,
            objc._C_NSBOOL + b"@" + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )

        self.assertArgIsBlock(
            Foundation.NSArray.indexesOfObjectsPassingTest_,
            0,
            objc._C_NSBOOL + b"@" + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            Foundation.NSArray.indexesOfObjectsWithOptions_passingTest_,
            1,
            objc._C_NSBOOL + b"@" + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            Foundation.NSArray.indexesOfObjectsAtIndexes_options_passingTest_,
            2,
            objc._C_NSBOOL + b"@" + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )

        self.assertArgIsBlock(Foundation.NSArray.sortedArrayUsingComparator_, 0, b"l@@")
        self.assertArgIsBlock(
            Foundation.NSArray.sortedArrayWithOptions_usingComparator_, 1, b"l@@"
        )
        self.assertArgIsBlock(
            Foundation.NSArray.indexOfObject_inSortedRange_options_usingComparator_,
            3,
            b"l@@",
        )
        self.assertArgHasType(
            Foundation.NSArray.indexOfObject_inSortedRange_options_usingComparator_,
            1,
            Foundation.NSRange.__typestr__,
        )

        self.assertArgIsBlock(
            Foundation.NSMutableArray.sortUsingComparator_, 0, objc._C_NSInteger + b"@@"
        )
        self.assertArgIsBlock(
            Foundation.NSMutableArray.sortWithOptions_usingComparator_,
            1,
            objc._C_NSInteger + b"@@",
        )

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(Foundation.NSArray.writeToURL_error_)
        self.assertArgIsOut(Foundation.NSArray.writeToURL_error_, 1)

        self.assertArgIsOut(Foundation.NSArray.initWithContentsOfURL_error_, 1)
        self.assertArgIsOut(Foundation.NSArray.arrayWithContentsOfURL_error_, 1)

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertArgIsBlock(
            Foundation.NSArray.differenceFromArray_withOptions_usingEquivalenceTest_,
            2,
            b"b@@",
        )

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(Foundation.NSBinarySearchingFirstEqual, 1 << 8)
        self.assertEqual(Foundation.NSBinarySearchingLastEqual, 1 << 9)
        self.assertEqual(Foundation.NSBinarySearchingInsertionIndex, 1 << 10)
