import CoreFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestData(TestCase):
    def testTypes(self):
        try:
            NSCFData = objc.lookUpClass("__NSCFData")
        except objc.error:
            NSCFData = objc.lookUpClass("NSCFData")

        self.assertIs(CoreFoundation.CFDataRef, NSCFData)

    def testTypeID(self):
        v = CoreFoundation.CFDataGetTypeID()
        self.assertTrue(v, int)

    def testCreation(self):
        self.assertArgHasType(CoreFoundation.CFDataCreate, 1, b"n^v")
        self.assertArgSizeInArg(CoreFoundation.CFDataCreate, 1, 2)
        data = CoreFoundation.CFDataCreate(None, b"hello", 5)
        self.assertIsInstance(data, CoreFoundation.CFDataRef)
        bytes_data = b"hello world"
        self.assertArgHasType(CoreFoundation.CFDataCreateWithBytesNoCopy, 1, b"n^v")
        self.assertArgSizeInArg(CoreFoundation.CFDataCreateWithBytesNoCopy, 1, 2)
        data = CoreFoundation.CFDataCreateWithBytesNoCopy(
            None, bytes_data, 5, CoreFoundation.kCFAllocatorNull
        )
        self.assertIsInstance(data, CoreFoundation.CFDataRef)
        del data

        data = CoreFoundation.CFDataCreate(None, b"hello", 5)
        self.assertIsInstance(data, CoreFoundation.CFDataRef)
        cpy = CoreFoundation.CFDataCreateCopy(None, data)
        self.assertIsInstance(cpy, CoreFoundation.CFDataRef)
        cpy2 = CoreFoundation.CFDataCreateMutableCopy(None, 0, data)
        self.assertIsInstance(cpy2, CoreFoundation.CFDataRef)
        mut = CoreFoundation.CFDataCreateMutable(None, 0)
        self.assertIsInstance(mut, CoreFoundation.CFDataRef)

    def testInspection(self):
        data = CoreFoundation.CFDataCreate(None, b"hello", 5)
        self.assertIsInstance(data, CoreFoundation.CFDataRef)
        mutableData = CoreFoundation.CFDataCreateMutableCopy(None, 0, data)
        self.assertIsInstance(mutableData, CoreFoundation.CFDataRef)
        self.assertEqual(CoreFoundation.CFDataGetLength(data), 5)
        self.assertEqual(CoreFoundation.CFDataGetLength(mutableData), 5)
        v = CoreFoundation.CFDataGetBytePtr(data)
        self.assertEqual(CoreFoundation.CFDataGetBytePtr(data)[0], b"h")
        v = CoreFoundation.CFDataGetMutableBytePtr(mutableData)
        self.assertEqual(v[0], b"h")
        v[0] = b"p"

        v = CoreFoundation.CFDataGetBytePtr(mutableData)
        self.assertEqual(v[0], b"p")
        self.assertArgHasType(CoreFoundation.CFDataGetBytes, 2, b"o^v")
        self.assertArgSizeInArg(CoreFoundation.CFDataGetBytes, 2, 1)
        bytes_data = CoreFoundation.CFDataGetBytes(data, (1, 3), None)
        self.assertEqual(bytes_data, b"hello"[1:4])

        CoreFoundation.CFDataSetLength(mutableData, 3)
        self.assertEqual(CoreFoundation.CFDataGetLength(mutableData), 3)
        CoreFoundation.CFDataIncreaseLength(mutableData, 17)
        self.assertEqual(CoreFoundation.CFDataGetLength(mutableData), 20)
        CoreFoundation.CFDataSetLength(mutableData, 3)

        self.assertArgHasType(CoreFoundation.CFDataAppendBytes, 1, b"n^v")
        self.assertArgSizeInArg(CoreFoundation.CFDataAppendBytes, 1, 2)
        CoreFoundation.CFDataAppendBytes(mutableData, b" world", 6)
        self.assertEqual(CoreFoundation.CFDataGetLength(mutableData), 9)
        self.assertEqual(
            CoreFoundation.CFDataGetBytes(mutableData, (0, 9), None), b"pel world"
        )

        self.assertArgHasType(CoreFoundation.CFDataReplaceBytes, 2, b"n^v")
        self.assertArgSizeInArg(CoreFoundation.CFDataReplaceBytes, 2, 3)
        CoreFoundation.CFDataReplaceBytes(mutableData, (0, 3), b"hello", 5)
        self.assertEqual(
            CoreFoundation.CFDataGetBytes(mutableData, (0, 9), None), b"hello world"[:9]
        )

        CoreFoundation.CFDataDeleteBytes(mutableData, (0, 6))
        self.assertEqual(
            CoreFoundation.CFDataGetBytes(mutableData, (0, 5), None), b"world"
        )

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(CoreFoundation.kCFDataSearchBackwards, 1 << 0)
        self.assertEqual(CoreFoundation.kCFDataSearchAnchored, 1 << 1)

    @min_os_level("10.6")
    def testFunctions10_6(self):
        data = CoreFoundation.CFDataCreate(None, b"hello world", 11)
        self.assertIsInstance(data, CoreFoundation.CFDataRef)
        src = CoreFoundation.CFDataCreate(None, b"wor", 3)
        self.assertIsInstance(src, CoreFoundation.CFDataRef)
        self.assertResultHasType(
            CoreFoundation.CFDataFind, CoreFoundation.CFRange.__typestr__
        )
        self.assertArgHasType(
            CoreFoundation.CFDataFind, 2, CoreFoundation.CFRange.__typestr__
        )
        v = CoreFoundation.CFDataFind(data, src, (0, 11), 0)
        self.assertIsInstance(v, CoreFoundation.CFRange)
        self.assertEqual(v, (6, 3))
