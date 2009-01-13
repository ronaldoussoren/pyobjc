from PyObjCTools.TestSupport import *
import sys
from CoreFoundation import *


class TestByteOrder (TestCase):

    def testConstants(self):
        self.failUnless(CFByteOrderUnknown == 0)
        self.failUnless(CFByteOrderLittleEndian == 1)
        self.failUnless(CFByteOrderBigEndian == 2)

    def testCurrent(self):
        if sys.byteorder == 'little':
            self.failUnless(CFByteOrderGetCurrent(), CFByteOrderLittleEndian)
        else:
            self.failUnless(CFByteOrderGetCurrent(), CFByteOrderBigEndian)

    def testSwap(self):
        v = CFSwapInt16(0x1)
        self.failUnless(v == 1 << 8)
        v = CFSwapInt32(0x1)
        self.failUnless(v == 1 << 24)
        v = CFSwapInt64(0x1)
        self.failUnless(v == 1 << 56)

        if sys.byteorder == 'big':
            v = CFSwapInt16BigToHost(0x1)
            self.assertEquals(v, 1)
            v = CFSwapInt32BigToHost(0x1)
            self.assertEquals(v, 1)
            v = CFSwapInt64BigToHost(0x1)
            self.assertEquals(v, 1)
            v = CFSwapInt16HostToBig(0x1)
            self.assertEquals(v, 1)
            v = CFSwapInt32HostToBig(0x1)
            self.assertEquals(v, 1)
            v = CFSwapInt64HostToBig(0x1)
            self.assertEquals(v, 1)
        else:
            v = CFSwapInt16BigToHost(0x1)
            self.assertEquals(v, 1 << 8)
            v = CFSwapInt32BigToHost(0x1)
            self.assertEquals(v, 1 << 24)
            v = CFSwapInt64BigToHost(0x1)
            self.assertEquals(v, 1 << 56)
            v = CFSwapInt16HostToBig(0x1)
            self.assertEquals(v, 1 << 8)
            v = CFSwapInt32HostToBig(0x1)
            self.assertEquals(v, 1 << 24)
            v = CFSwapInt64HostToBig(0x1)
            self.assertEquals(v, 1 << 56)

        if sys.byteorder == 'little':
            v = CFSwapInt16LittleToHost(0x1)
            self.assertEquals(v, 1)
            v = CFSwapInt32LittleToHost(0x1)
            self.assertEquals(v, 1)
            v = CFSwapInt64LittleToHost(0x1)
            self.assertEquals(v, 1)
            v = CFSwapInt16HostToLittle(0x1)
            self.assertEquals(v, 1)
            v = CFSwapInt32HostToLittle(0x1)
            self.assertEquals(v, 1)
            v = CFSwapInt64HostToLittle(0x1)
            self.assertEquals(v, 1)
        else:
            v = CFSwapInt16LittleToHost(0x1)
            self.assertEquals(v, 1 << 8)
            v = CFSwapInt32LittleToHost(0x1)
            self.assertEquals(v, 1 << 24)
            v = CFSwapInt64LittleToHost(0x1)
            self.assertEquals(v, 1 << 56)
            v = CFSwapInt16HostToLittle(0x1)
            self.assertEquals(v, 1 << 8)
            v = CFSwapInt32HostToLittle(0x1)
            self.assertEquals(v, 1 << 24)
            v = CFSwapInt64HostToLittle(0x1)
            self.assertEquals(v, 1 << 56)

        swapped =  CFConvertFloat32HostToSwapped(2.5)
        self.failUnless(isinstance(swapped, CFSwappedFloat32))
        v = CFConvertFloat32SwappedToHost(swapped)
        self.failUnless(v ==  2.5)
        
        swapped = CFConvertFloat64HostToSwapped(2.5)
        self.failUnless(isinstance(swapped, CFSwappedFloat64))
        v = CFConvertFloat64SwappedToHost(swapped)
        self.failUnless(v ==  2.5)

        swapped = CFConvertFloatHostToSwapped(2.5)
        self.failUnless(isinstance(swapped, CFSwappedFloat32))
        v = CFConvertFloatSwappedToHost(swapped)
        self.failUnless(v ==  2.5)

        swapped = CFConvertDoubleHostToSwapped(2.5)
        self.failUnless(isinstance(swapped, CFSwappedFloat64))
        v = CFConvertDoubleSwappedToHost(swapped)
        self.failUnless(v ==  2.5)


if __name__ == "__main__":
    main()
