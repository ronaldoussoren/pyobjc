import sys

import CoreFoundation
from PyObjCTools.TestSupport import TestCase


class TestByteOrder(TestCase):
    def testConstants(self):
        self.assertEqual(CoreFoundation.CFByteOrderUnknown, 0)
        self.assertEqual(CoreFoundation.CFByteOrderLittleEndian, 1)
        self.assertEqual(CoreFoundation.CFByteOrderBigEndian, 2)

    def testCurrent(self):
        if sys.byteorder == "little":
            self.assertTrue(
                CoreFoundation.CFByteOrderGetCurrent(),
                CoreFoundation.CFByteOrderLittleEndian,
            )
        else:
            self.assertTrue(
                CoreFoundation.CFByteOrderGetCurrent(),
                CoreFoundation.CFByteOrderBigEndian,
            )

    def testSwap(self):
        v = CoreFoundation.CFSwapInt16(0x1)
        self.assertEqual(v, 1 << 8)
        v = CoreFoundation.CFSwapInt32(0x1)
        self.assertEqual(v, 1 << 24)
        v = CoreFoundation.CFSwapInt64(0x1)
        self.assertEqual(v, 1 << 56)
        if sys.byteorder == "big":
            v = CoreFoundation.CFSwapInt16BigToHost(0x1)
            self.assertEqual(v, 1)
            v = CoreFoundation.CFSwapInt32BigToHost(0x1)
            self.assertEqual(v, 1)
            v = CoreFoundation.CFSwapInt64BigToHost(0x1)
            self.assertEqual(v, 1)
            v = CoreFoundation.CFSwapInt16HostToBig(0x1)
            self.assertEqual(v, 1)
            v = CoreFoundation.CFSwapInt32HostToBig(0x1)
            self.assertEqual(v, 1)
            v = CoreFoundation.CFSwapInt64HostToBig(0x1)
            self.assertEqual(v, 1)
        else:
            v = CoreFoundation.CFSwapInt16BigToHost(0x1)
            self.assertEqual(v, 1 << 8)
            v = CoreFoundation.CFSwapInt32BigToHost(0x1)
            self.assertEqual(v, 1 << 24)
            v = CoreFoundation.CFSwapInt64BigToHost(0x1)
            self.assertEqual(v, 1 << 56)
            v = CoreFoundation.CFSwapInt16HostToBig(0x1)
            self.assertEqual(v, 1 << 8)
            v = CoreFoundation.CFSwapInt32HostToBig(0x1)
            self.assertEqual(v, 1 << 24)
            v = CoreFoundation.CFSwapInt64HostToBig(0x1)
            self.assertEqual(v, 1 << 56)

        if sys.byteorder == "little":
            v = CoreFoundation.CFSwapInt16LittleToHost(0x1)
            self.assertEqual(v, 1)
            v = CoreFoundation.CFSwapInt32LittleToHost(0x1)
            self.assertEqual(v, 1)
            v = CoreFoundation.CFSwapInt64LittleToHost(0x1)
            self.assertEqual(v, 1)
            v = CoreFoundation.CFSwapInt16HostToLittle(0x1)
            self.assertEqual(v, 1)
            v = CoreFoundation.CFSwapInt32HostToLittle(0x1)
            self.assertEqual(v, 1)
            v = CoreFoundation.CFSwapInt64HostToLittle(0x1)
            self.assertEqual(v, 1)
        else:
            v = CoreFoundation.CFSwapInt16LittleToHost(0x1)
            self.assertEqual(v, 1 << 8)
            v = CoreFoundation.CFSwapInt32LittleToHost(0x1)
            self.assertEqual(v, 1 << 24)
            v = CoreFoundation.CFSwapInt64LittleToHost(0x1)
            self.assertEqual(v, 1 << 56)
            v = CoreFoundation.CFSwapInt16HostToLittle(0x1)
            self.assertEqual(v, 1 << 8)
            v = CoreFoundation.CFSwapInt32HostToLittle(0x1)
            self.assertEqual(v, 1 << 24)
            v = CoreFoundation.CFSwapInt64HostToLittle(0x1)
            self.assertEqual(v, 1 << 56)

        swapped = CoreFoundation.CFConvertFloat32HostToSwapped(2.5)
        self.assertIsInstance(swapped, CoreFoundation.CFSwappedFloat32)
        v = CoreFoundation.CFConvertFloat32SwappedToHost(swapped)
        self.assertEqual(v, 2.5)
        swapped = CoreFoundation.CFConvertFloat64HostToSwapped(2.5)
        self.assertIsInstance(swapped, CoreFoundation.CFSwappedFloat64)
        v = CoreFoundation.CFConvertFloat64SwappedToHost(swapped)
        self.assertEqual(v, 2.5)
        swapped = CoreFoundation.CFConvertFloatHostToSwapped(2.5)
        self.assertIsInstance(swapped, CoreFoundation.CFSwappedFloat32)
        v = CoreFoundation.CFConvertFloatSwappedToHost(swapped)
        self.assertEqual(v, 2.5)
        swapped = CoreFoundation.CFConvertDoubleHostToSwapped(2.5)
        self.assertIsInstance(swapped, CoreFoundation.CFSwappedFloat64)
        v = CoreFoundation.CFConvertDoubleSwappedToHost(swapped)
        self.assertEqual(v, 2.5)
