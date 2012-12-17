from PyObjCTools.TestSupport import *
import sys

from Foundation import *
import Foundation

class TestNSByteOrder (TestCase):
    def testConstants(self):
        self.assertEqual(NS_UnknownByteOrder, CFByteOrderUnknown)
        self.assertEqual(NS_LittleEndian, CFByteOrderLittleEndian)
        self.assertEqual(NS_BigEndian, CFByteOrderBigEndian)

    def testInlines(self):
        self.assertEqual(NSHostByteOrder(), CFByteOrderGetCurrent())
        self.assertEqual(NSSwapShort(350), CFSwapInt16(350))
        self.assertEqual(NSSwapInt(350), CFSwapInt32(350))

        if sys.maxsize > 2 ** 32:
            self.assertEqual(NSSwapLong(350), CFSwapInt64(350))
            self.assertEqual(NSSwapBigLongToHost(350), CFSwapInt64BigToHost(350))
            self.assertEqual(NSSwapHostLongToBig(350), CFSwapInt64HostToBig(350))
            self.assertEqual(NSSwapLittleLongToHost(350), CFSwapInt64LittleToHost(350))
            self.assertEqual(NSSwapHostLongToLittle(350), CFSwapInt64HostToLittle(350))
        else:
            self.assertEqual(NSSwapLong(350), CFSwapInt32(350))
            self.assertEqual(NSSwapBigLongToHost(350), CFSwapInt32BigToHost(350))
            self.assertEqual(NSSwapHostLongToBig(350), CFSwapInt32HostToBig(350))
            self.assertEqual(NSSwapLittleLongToHost(350), CFSwapInt32LittleToHost(350))
            self.assertEqual(NSSwapHostLongToLittle(350), CFSwapInt32HostToLittle(350))


        self.assertEqual(NSSwapLongLong(350), CFSwapInt64(350))
        self.assertEqual(NSSwapBigShortToHost(350), CFSwapInt16BigToHost(350))
        self.assertEqual(NSSwapBigIntToHost(350), CFSwapInt32BigToHost(350))
        self.assertEqual(NSSwapBigLongLongToHost(350), CFSwapInt64BigToHost(350))
        self.assertEqual(NSSwapHostShortToBig(350), CFSwapInt16HostToBig(350))
        self.assertEqual(NSSwapHostIntToBig(350), CFSwapInt32HostToBig(350))
        self.assertEqual(NSSwapHostLongLongToBig(350), CFSwapInt64HostToBig(350))
        self.assertEqual(NSSwapLittleShortToHost(350), CFSwapInt16LittleToHost(350))
        self.assertEqual(NSSwapLittleIntToHost(350), CFSwapInt32LittleToHost(350))
        self.assertEqual(NSSwapLittleLongLongToHost(350), CFSwapInt64LittleToHost(350))
        self.assertEqual(NSSwapHostShortToLittle(350), CFSwapInt16HostToLittle(350))
        self.assertEqual(NSSwapHostIntToLittle(350), CFSwapInt32HostToLittle(350))
        self.assertEqual(NSSwapHostLongLongToLittle(350), CFSwapInt64HostToLittle(350))

        v = NSConvertHostFloatToSwapped(55.0)
        self.assertIsInstance(v, NSSwappedFloat)
        n = NSConvertSwappedFloatToHost(v)
        self.assertEqual(n, 55.0)

        v = NSSwapFloat(v)
        self.assertIsInstance(v, NSSwappedFloat)
        v = NSConvertHostDoubleToSwapped(55.0)
        self.assertIsInstance(v, NSSwappedDouble)
        n = NSConvertSwappedDoubleToHost(v)
        self.assertEqual(n, 55.0)

        v = NSSwapDouble(v)
        self.assertIsInstance(v, NSSwappedDouble)
        n = NSSwapBigDoubleToHost(v)
        self.assertIsInstance(n, float)
        n = NSSwapLittleDoubleToHost(v)
        self.assertIsInstance(n, float)
        v = NSConvertHostFloatToSwapped(55.0)
        n = NSSwapBigFloatToHost(v)
        self.assertIsInstance(n, float)
        n = NSSwapLittleFloatToHost(v)
        self.assertIsInstance(n, float)
        v = NSSwapHostDoubleToBig(55.0)
        self.assertIsInstance(v, NSSwappedDouble)
        v = NSSwapHostDoubleToLittle(55.0)
        self.assertIsInstance(v, NSSwappedDouble)
        v = NSSwapHostFloatToBig(55.0)
        self.assertIsInstance(v, NSSwappedFloat)
        v = NSSwapHostFloatToLittle(55.0)
        self.assertIsInstance(v, NSSwappedFloat)

if __name__ == "__main__":
    main()
