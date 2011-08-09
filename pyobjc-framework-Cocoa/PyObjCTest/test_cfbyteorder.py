from PyObjCTools.TestSupport import *
import sys
from CoreFoundation import *


class TestByteOrder (TestCase):

    def testConstants(self):
        self.assertEqual(CFByteOrderUnknown , 0)
        self.assertEqual(CFByteOrderLittleEndian , 1)
        self.assertEqual(CFByteOrderBigEndian , 2)

    def testCurrent(self):
        if sys.byteorder == 'little':
            self.assertTrue(CFByteOrderGetCurrent(), CFByteOrderLittleEndian)
        else:
            self.assertTrue(CFByteOrderGetCurrent(), CFByteOrderBigEndian)

    def testSwap(self):
        v = CFSwapInt16(0x1)
        self.assertEqual(v , 1 << 8)
        v = CFSwapInt32(0x1)
        self.assertEqual(v , 1 << 24)
        v = CFSwapInt64(0x1)
        self.assertEqual(v , 1 << 56)
        if sys.byteorder == 'big':
            v = CFSwapInt16BigToHost(0x1)
            self.assertEqual(v, 1)
            v = CFSwapInt32BigToHost(0x1)
            self.assertEqual(v, 1)
            v = CFSwapInt64BigToHost(0x1)
            self.assertEqual(v, 1)
            v = CFSwapInt16HostToBig(0x1)
            self.assertEqual(v, 1)
            v = CFSwapInt32HostToBig(0x1)
            self.assertEqual(v, 1)
            v = CFSwapInt64HostToBig(0x1)
            self.assertEqual(v, 1)
        else:
            v = CFSwapInt16BigToHost(0x1)
            self.assertEqual(v, 1 << 8)
            v = CFSwapInt32BigToHost(0x1)
            self.assertEqual(v, 1 << 24)
            v = CFSwapInt64BigToHost(0x1)
            self.assertEqual(v, 1 << 56)
            v = CFSwapInt16HostToBig(0x1)
            self.assertEqual(v, 1 << 8)
            v = CFSwapInt32HostToBig(0x1)
            self.assertEqual(v, 1 << 24)
            v = CFSwapInt64HostToBig(0x1)
            self.assertEqual(v, 1 << 56)

        if sys.byteorder == 'little':
            v = CFSwapInt16LittleToHost(0x1)
            self.assertEqual(v, 1)
            v = CFSwapInt32LittleToHost(0x1)
            self.assertEqual(v, 1)
            v = CFSwapInt64LittleToHost(0x1)
            self.assertEqual(v, 1)
            v = CFSwapInt16HostToLittle(0x1)
            self.assertEqual(v, 1)
            v = CFSwapInt32HostToLittle(0x1)
            self.assertEqual(v, 1)
            v = CFSwapInt64HostToLittle(0x1)
            self.assertEqual(v, 1)
        else:
            v = CFSwapInt16LittleToHost(0x1)
            self.assertEqual(v, 1 << 8)
            v = CFSwapInt32LittleToHost(0x1)
            self.assertEqual(v, 1 << 24)
            v = CFSwapInt64LittleToHost(0x1)
            self.assertEqual(v, 1 << 56)
            v = CFSwapInt16HostToLittle(0x1)
            self.assertEqual(v, 1 << 8)
            v = CFSwapInt32HostToLittle(0x1)
            self.assertEqual(v, 1 << 24)
            v = CFSwapInt64HostToLittle(0x1)
            self.assertEqual(v, 1 << 56)

        swapped =  CFConvertFloat32HostToSwapped(2.5)
        self.assertIsInstance(swapped, CFSwappedFloat32)
        v = CFConvertFloat32SwappedToHost(swapped)
        self.assertEqual(v , 2.5)
        swapped = CFConvertFloat64HostToSwapped(2.5)
        self.assertIsInstance(swapped, CFSwappedFloat64)
        v = CFConvertFloat64SwappedToHost(swapped)
        self.assertEqual(v , 2.5)
        swapped = CFConvertFloatHostToSwapped(2.5)
        self.assertIsInstance(swapped, CFSwappedFloat32)
        v = CFConvertFloatSwappedToHost(swapped)
        self.assertEqual(v , 2.5)
        swapped = CFConvertDoubleHostToSwapped(2.5)
        self.assertIsInstance(swapped, CFSwappedFloat64)
        v = CFConvertDoubleSwappedToHost(swapped)
        self.assertEqual(v , 2.5)

if __name__ == "__main__":
    main()
