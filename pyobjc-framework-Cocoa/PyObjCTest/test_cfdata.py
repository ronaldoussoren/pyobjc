from PyObjCTools.TestSupport import *
from CoreFoundation import *
from Foundation import NSCFData


class TestData (TestCase):
    def testTypes(self):
        self.failUnless(CFDataRef is NSCFData)

    def testTypeID(self):
        v = CFDataGetTypeID()
        self.failUnless(v, (int, long))

    def testCreation(self):
        self.failUnlessArgHasType(CFDataCreate, 1,  'n^v')
        self.failUnlessArgSizeInArg(CFDataCreate, 1, 2)
        data = CFDataCreate(None, "hello", 5)
        self.failUnless(isinstance(data, CFDataRef))

        bytes = buffer("hello world")
        self.failUnlessArgHasType(CFDataCreateWithBytesNoCopy, 1, 'n^v')
        self.failUnlessArgSizeInArg(CFDataCreateWithBytesNoCopy, 1, 2)
        data = CFDataCreateWithBytesNoCopy(None, bytes, 5, kCFAllocatorNull)
        self.failUnless(isinstance(data, CFDataRef))
        del data

        data = CFDataCreate(None, "hello", 5)
        self.failUnless(isinstance(data, CFDataRef))
        cpy = CFDataCreateCopy(None, data)
        self.failUnless(isinstance(cpy, CFDataRef))

        cpy2 = CFDataCreateMutableCopy(None, 0, data)
        self.failUnless(isinstance(cpy2, CFDataRef))

        mut = CFDataCreateMutable(None, 0)
        self.failUnless(isinstance(mut, CFDataRef))

    def testInspection(self):
        data = CFDataCreate(None, "hello", 5)
        self.failUnless(isinstance(data, CFDataRef))
        mutableData = CFDataCreateMutableCopy(None, 0, data)
        self.failUnless(isinstance(mutableData, CFDataRef))

        self.failUnless(CFDataGetLength(data) == 5)
        self.failUnless(CFDataGetLength(mutableData) == 5)

        v = CFDataGetBytePtr(data)
        self.failUnless(CFDataGetBytePtr(data)[0] == 'h')

        v = CFDataGetMutableBytePtr(mutableData)
        self.failUnless(v[0] == 'h')
        v[0] = 'p'

        v = CFDataGetBytePtr(mutableData)
        self.failUnless(v[0] == 'p')

        self.failUnlessArgHasType(CFDataGetBytes, 2, 'o^v')
        self.failUnlessArgSizeInArg(CFDataGetBytes, 2, 1)
        bytes = CFDataGetBytes(data, (1,3), None)
        self.assertEquals(bytes, 'hello'[1:4])

        CFDataSetLength(mutableData, 3)
        self.failUnless(CFDataGetLength(mutableData) == 3)

        CFDataIncreaseLength(mutableData, 17)
        self.failUnless(CFDataGetLength(mutableData) == 20)
        CFDataSetLength(mutableData, 3)

        self.failUnlessArgHasType(CFDataAppendBytes, 1, 'n^v')
        self.failUnlessArgSizeInArg(CFDataAppendBytes, 1, 2)
        CFDataAppendBytes(mutableData, " world", 6)
        self.failUnless(CFDataGetLength(mutableData) == 9)
        self.assertEquals(CFDataGetBytes(mutableData, (0, 9), None), 'pel world')

        self.failUnlessArgHasType(CFDataReplaceBytes, 2, 'n^v')
        self.failUnlessArgSizeInArg(CFDataReplaceBytes, 2, 3)
        CFDataReplaceBytes(mutableData, (0, 3), "hello", 5)
        self.assertEquals(CFDataGetBytes(mutableData, (0, 9), None), 'hello world'[:9])

        CFDataDeleteBytes(mutableData, (0, 6))
        self.assertEquals(CFDataGetBytes(mutableData, (0, 5), None), 'world')


if __name__ == "__main__":
    main()
