from PyObjCTools.TestSupport import *
from CoreFoundation import *
from Foundation import NSCFData
import sys


class TestData (TestCase):
    def testTypes(self):
        self.assertIs(CFDataRef, NSCFData)
    def testTypeID(self):
        v = CFDataGetTypeID()
        self.assertTrue(v, (int, long))

    def testCreation(self):
        self.assertArgHasType(CFDataCreate, 1,  b'n^v')
        self.assertArgSizeInArg(CFDataCreate, 1, 2)
        data = CFDataCreate(None, b"hello", 5)
        self.assertIsInstance(data, CFDataRef)
        if sys.version_info[0] == 3:
            bytes = b"hello world"
        else:
            bytes = buffer("hello world")
        self.assertArgHasType(CFDataCreateWithBytesNoCopy, 1, b'n^v')
        self.assertArgSizeInArg(CFDataCreateWithBytesNoCopy, 1, 2)
        data = CFDataCreateWithBytesNoCopy(None, bytes, 5, kCFAllocatorNull)
        self.assertIsInstance(data, CFDataRef)
        del data

        data = CFDataCreate(None, b"hello", 5)
        self.assertIsInstance(data, CFDataRef)
        cpy = CFDataCreateCopy(None, data)
        self.assertIsInstance(cpy, CFDataRef)
        cpy2 = CFDataCreateMutableCopy(None, 0, data)
        self.assertIsInstance(cpy2, CFDataRef)
        mut = CFDataCreateMutable(None, 0)
        self.assertIsInstance(mut, CFDataRef)

    def testInspection(self):
        data = CFDataCreate(None, b"hello", 5)
        self.assertIsInstance(data, CFDataRef)
        mutableData = CFDataCreateMutableCopy(None, 0, data)
        self.assertIsInstance(mutableData, CFDataRef)
        self.assertEqual(CFDataGetLength(data) , 5)
        self.assertEqual(CFDataGetLength(mutableData) , 5)
        v = CFDataGetBytePtr(data)
        self.assertEqual(CFDataGetBytePtr(data)[0] , b'h')
        v = CFDataGetMutableBytePtr(mutableData)
        self.assertEqual(v[0] , b'h')
        v[0] = b'p'

        v = CFDataGetBytePtr(mutableData)
        self.assertEqual(v[0] , b'p')
        self.assertArgHasType(CFDataGetBytes, 2, b'o^v')
        self.assertArgSizeInArg(CFDataGetBytes, 2, 1)
        bytes = CFDataGetBytes(data, (1,3), None)
        self.assertEqual(bytes, b'hello'[1:4])

        CFDataSetLength(mutableData, 3)
        self.assertEqual(CFDataGetLength(mutableData) , 3)
        CFDataIncreaseLength(mutableData, 17)
        self.assertEqual(CFDataGetLength(mutableData) , 20)
        CFDataSetLength(mutableData, 3)

        self.assertArgHasType(CFDataAppendBytes, 1, b'n^v')
        self.assertArgSizeInArg(CFDataAppendBytes, 1, 2)
        CFDataAppendBytes(mutableData, b" world", 6)
        self.assertEqual(CFDataGetLength(mutableData) , 9)
        self.assertEqual(CFDataGetBytes(mutableData, (0, 9), None), b'pel world')

        self.assertArgHasType(CFDataReplaceBytes, 2, b'n^v')
        self.assertArgSizeInArg(CFDataReplaceBytes, 2, 3)
        CFDataReplaceBytes(mutableData, (0, 3), b"hello", 5)
        self.assertEqual(CFDataGetBytes(mutableData, (0, 9), None), b'hello world'[:9])

        CFDataDeleteBytes(mutableData, (0, 6))
        self.assertEqual(CFDataGetBytes(mutableData, (0, 5), None), b'world')

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(kCFDataSearchBackwards, 1<<0)
        self.assertEqual(kCFDataSearchAnchored, 1<<1)

    @min_os_level('10.6')
    def testFunctions10_6(self):
        data = CFDataCreate(None, b"hello world", 11)
        self.assertIsInstance(data, CFDataRef)
        src = CFDataCreate(None, b"wor", 3)
        self.assertIsInstance(src, CFDataRef)
        self.assertResultHasType(CFDataFind, CFRange.__typestr__)
        self.assertArgHasType(CFDataFind, 2, CFRange.__typestr__)
        v = CFDataFind(data, src, (0, 11), 0)
        self.assertIsInstance(v, CFRange)
        self.assertEqual(v, (6, 3))


if __name__ == "__main__":
    main()
