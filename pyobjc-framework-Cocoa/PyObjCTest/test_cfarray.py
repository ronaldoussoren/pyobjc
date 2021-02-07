import CoreFoundation
from Foundation import NSArray, NSMutableArray
from PyObjCTools.TestSupport import TestCase


def cmp(a, b):
    if a < b:
        return -1
    elif b < a:
        return 1
    return 0


class TestCFArray(TestCase):
    def testCFArrayIsNSArray(self):
        self.assertTrue(issubclass(CoreFoundation.CFArrayRef, NSArray))
        self.assertTrue(issubclass(CoreFoundation.CFMutableArrayRef, NSMutableArray))

    def testCFArrayCreate(self):
        array = CoreFoundation.CFArrayCreate(
            None, [1, 2, 3, 4], 4, CoreFoundation.kCFTypeArrayCallBacks
        )
        self.assertEqual(array, [1, 2, 3, 4])
        self.assertIsInstance(array, NSArray)

        array = CoreFoundation.CFArrayCreateMutable(
            None, 0, CoreFoundation.kCFTypeArrayCallBacks
        )
        CoreFoundation.CFArrayAppendValue(array, 42)
        CoreFoundation.CFArrayAppendValue(array, 43)
        CoreFoundation.CFArrayAppendValue(array, 44)
        self.assertEqual(array, [42, 43, 44])
        self.assertIsInstance(array, CoreFoundation.CFMutableArrayRef)

    def testCFArrayApplyFunction(self):
        array = CoreFoundation.CFArrayCreate(
            None, [1, 2, 3, 4], 4, CoreFoundation.kCFTypeArrayCallBacks
        )

        self.assertArgIsFunction(CoreFoundation.CFArrayApplyFunction, 2, b"v@@", False)
        self.assertArgHasType(CoreFoundation.CFArrayApplyFunction, 3, b"@")

        items = []
        infos = []

        def applier(item, info):
            items.append(item * item)
            infos.append(info)

        CoreFoundation.CFArrayApplyFunction(array, (0, 4), applier, 42)
        self.assertEqual(items, [1, 4, 9, 16])
        self.assertEqual(infos, [42, 42, 42, 42])

        items = []
        infos = []
        CoreFoundation.CFArrayApplyFunction(array, (1, 2), applier, 42)
        self.assertEqual(items, [4, 9])
        self.assertEqual(infos, [42, 42])

    def testBSearchValues(self):
        # This method causes a hard crash, reason unclear.
        array = CoreFoundation.CFArrayCreate(
            None, range(20), 20, CoreFoundation.kCFTypeArrayCallBacks
        )

        self.assertArgHasType(CoreFoundation.CFArrayBSearchValues, 2, b"@")
        self.assertArgIsFunction(CoreFoundation.CFArrayBSearchValues, 3, b"l@@@", False)
        self.assertArgHasType(CoreFoundation.CFArrayBSearchValues, 4, b"@")

        def compare(l, r, context):
            return cmp(l, r)

        r = CoreFoundation.CFArrayBSearchValues(array, (0, 20), 10, compare, None)
        self.assertEqual(r, 10)

        r = CoreFoundation.CFArrayBSearchValues(array, (0, 20), 9.5, compare, None)
        self.assertEqual(r, 10)

        r = CoreFoundation.CFArrayBSearchValues(array, (0, 20), 99, compare, None)
        self.assertTrue(r >= 20)

        r = CoreFoundation.CFArrayBSearchValues(array, (0, 20), -1, compare, None)
        self.assertEqual(r, 0)

    def testSortValues(self):
        array = CoreFoundation.NSMutableArray.arrayWithArray_([4, 2, 1, 3, 0, 5])

        self.assertArgIsFunction(CoreFoundation.CFArraySortValues, 2, b"l@@@", False)
        self.assertArgHasType(CoreFoundation.CFArraySortValues, 3, b"@")

        def compare(l, r, context):
            return cmp(l, r)

        CoreFoundation.CFArraySortValues(array, (0, 6), compare, None)

        self.assertEqual(array, [0, 1, 2, 3, 4, 5])

    def testTypeID(self):
        v = CoreFoundation.CFArrayGetTypeID()
        self.assertIsInstance(v, int)

    def testCopy(self):
        array = CoreFoundation.CFArrayCreate(
            None, [1, 2, 3, 4], 4, CoreFoundation.kCFTypeArrayCallBacks
        )
        self.assertEqual(array, [1, 2, 3, 4])
        self.assertIsInstance(array, NSArray)

        cpy = CoreFoundation.CFArrayCreateCopy(None, array)
        self.assertEqual(cpy, [1, 2, 3, 4])
        self.assertIsInstance(cpy, NSArray)

        cpy = CoreFoundation.CFArrayCreateMutableCopy(None, 0, array)
        self.assertEqual(cpy, [1, 2, 3, 4])
        self.assertIsInstance(cpy, CoreFoundation.CFMutableArrayRef)
        self.assertIsNot(cpy, array)

    def testCounts(self):
        array = CoreFoundation.CFArrayCreate(
            None, [1, 2, 3, 4, 4, 2], 6, CoreFoundation.kCFTypeArrayCallBacks
        )
        self.assertEqual(array, [1, 2, 3, 4, 4, 2])
        self.assertIsInstance(array, NSArray)

        self.assertEqual(CoreFoundation.CFArrayGetCount(array), 6)
        self.assertEqual(CoreFoundation.CFArrayGetCountOfValue(array, (0, 6), 4), 2)
        self.assertEqual(CoreFoundation.CFArrayGetCountOfValue(array, (0, 6), 2), 2)
        self.assertEqual(CoreFoundation.CFArrayGetCountOfValue(array, (0, 6), 3), 1)

    def testContains(self):
        array = CoreFoundation.CFArrayCreate(
            None, ["a", 2, 3, 4, 4, 2], 6, CoreFoundation.kCFTypeArrayCallBacks
        )
        self.assertEqual(array, ["a", 2, 3, 4, 4, 2])
        self.assertIsInstance(array, NSArray)

        self.assertFalse(CoreFoundation.CFArrayContainsValue(array, (0, 6), "hello"))
        self.assertTrue(CoreFoundation.CFArrayContainsValue(array, (0, 6), 4))
        self.assertFalse(CoreFoundation.CFArrayContainsValue(array, (0, 2), 4))

        self.assertEqual(
            CoreFoundation.CFArrayGetFirstIndexOfValue(array, (0, 6), 3), 2
        )
        self.assertEqual(
            CoreFoundation.CFArrayGetFirstIndexOfValue(array, (0, 6), 2), 1
        )
        self.assertEqual(
            CoreFoundation.CFArrayGetFirstIndexOfValue(array, (0, 6), "hello"),
            CoreFoundation.kCFNotFound,
        )
        self.assertEqual(CoreFoundation.CFArrayGetLastIndexOfValue(array, (0, 6), 3), 2)
        self.assertEqual(CoreFoundation.CFArrayGetLastIndexOfValue(array, (0, 6), 2), 5)
        self.assertEqual(
            CoreFoundation.CFArrayGetLastIndexOfValue(array, (0, 6), "hello"),
            CoreFoundation.kCFNotFound,
        )
        self.assertArgHasType(CoreFoundation.CFArrayGetFirstIndexOfValue, 2, b"@")
        self.assertArgHasType(CoreFoundation.CFArrayGetLastIndexOfValue, 2, b"@")

    def testGetting(self):
        array = CoreFoundation.CFArrayCreate(
            None, ["a", 2, 3, 4, 4, 2], 6, CoreFoundation.kCFTypeArrayCallBacks
        )
        self.assertEqual(array, ["a", 2, 3, 4, 4, 2])
        self.assertIsInstance(array, NSArray)

        self.assertEqual(CoreFoundation.CFArrayGetValueAtIndex(array, 0), "a")
        self.assertEqual(CoreFoundation.CFArrayGetValueAtIndex(array, 1), 2)
        self.assertArgHasType(CoreFoundation.CFArrayGetValues, 2, b"o^@")
        self.assertArgSizeInArg(CoreFoundation.CFArrayGetValues, 2, 1)

        vals = CoreFoundation.CFArrayGetValues(array, (0, 3), None)
        self.assertIsInstance(vals, tuple)
        self.assertEqual(vals, ("a", 2, 3))

    def testUpdating(self):
        array = CoreFoundation.CFArrayCreate(
            None, ["a", 2, 3, 4, 4, 2], 6, CoreFoundation.kCFTypeArrayCallBacks
        )
        self.assertEqual(array, ["a", 2, 3, 4, 4, 2])
        self.assertIsInstance(array, CoreFoundation.NSArray)
        array = CoreFoundation.CFArrayCreateMutableCopy(None, 0, array)

        self.assertArgHasType(CoreFoundation.CFArrayAppendValue, 1, b"@")
        self.assertArgHasType(CoreFoundation.CFArrayInsertValueAtIndex, 2, b"@")
        self.assertArgHasType(CoreFoundation.CFArraySetValueAtIndex, 2, b"@")

        CoreFoundation.CFArrayAppendValue(array, "foo")
        self.assertEqual(array, ["a", 2, 3, 4, 4, 2, "foo"])

        CoreFoundation.CFArrayInsertValueAtIndex(array, 1, 4)
        self.assertEqual(array, ["a", 4, 2, 3, 4, 4, 2, "foo"])

        CoreFoundation.CFArrayRemoveValueAtIndex(array, 2)
        self.assertEqual(array, ["a", 4, 3, 4, 4, 2, "foo"])

        CoreFoundation.CFArraySetValueAtIndex(array, 2, "two")
        self.assertEqual(array, ["a", 4, "two", 4, 4, 2, "foo"])

        CoreFoundation.CFArrayExchangeValuesAtIndices(array, 1, 2)
        self.assertEqual(array, ["a", "two", 4, 4, 4, 2, "foo"])

        self.assertArgHasType(CoreFoundation.CFArrayReplaceValues, 2, b"n^@")
        self.assertArgSizeInArg(CoreFoundation.CFArrayReplaceValues, 2, 3)
        CoreFoundation.CFArrayReplaceValues(
            array, (2, 3), ("a", "b", "c", "d", "e", "f"), 6
        )
        self.assertEqual(array, ["a", "two", "a", "b", "c", "d", "e", "f", 2, "foo"])

        array2 = CoreFoundation.CFArrayCreate(
            None, ["hello", "earth"], 2, CoreFoundation.kCFTypeArrayCallBacks
        )
        CoreFoundation.CFArrayAppendArray(array, array2, (0, 2))
        self.assertEqual(
            array,
            ["a", "two", "a", "b", "c", "d", "e", "f", 2, "foo", "hello", "earth"],
        )

        CoreFoundation.CFArrayRemoveAllValues(array)
        self.assertEqual(array, [])
