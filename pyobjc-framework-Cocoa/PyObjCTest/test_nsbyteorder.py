import Foundation
import CoreFoundation
from PyObjCTools.TestSupport import TestCase


class TestNSByteOrder(TestCase):
    def testConstants(self):
        self.assertEqual(
            Foundation.NS_UnknownByteOrder, CoreFoundation.CFByteOrderUnknown
        )
        self.assertEqual(
            Foundation.NS_LittleEndian, CoreFoundation.CFByteOrderLittleEndian
        )
        self.assertEqual(Foundation.NS_BigEndian, CoreFoundation.CFByteOrderBigEndian)

    def testInlines(self):
        self.assertEqual(
            Foundation.NSHostByteOrder(), CoreFoundation.CFByteOrderGetCurrent()
        )
        self.assertEqual(Foundation.NSSwapShort(350), CoreFoundation.CFSwapInt16(350))
        self.assertEqual(Foundation.NSSwapInt(350), CoreFoundation.CFSwapInt32(350))

        self.assertEqual(Foundation.NSSwapLong(350), CoreFoundation.CFSwapInt64(350))
        self.assertEqual(
            Foundation.NSSwapBigLongToHost(350),
            CoreFoundation.CFSwapInt64BigToHost(350),
        )
        self.assertEqual(
            Foundation.NSSwapHostLongToBig(350),
            CoreFoundation.CFSwapInt64HostToBig(350),
        )
        self.assertEqual(
            Foundation.NSSwapLittleLongToHost(350),
            CoreFoundation.CFSwapInt64LittleToHost(350),
        )
        self.assertEqual(
            Foundation.NSSwapHostLongToLittle(350),
            CoreFoundation.CFSwapInt64HostToLittle(350),
        )

        self.assertEqual(
            Foundation.NSSwapLongLong(350), CoreFoundation.CFSwapInt64(350)
        )
        self.assertEqual(
            Foundation.NSSwapBigShortToHost(350),
            CoreFoundation.CFSwapInt16BigToHost(350),
        )
        self.assertEqual(
            Foundation.NSSwapBigIntToHost(350), CoreFoundation.CFSwapInt32BigToHost(350)
        )
        self.assertEqual(
            Foundation.NSSwapBigLongLongToHost(350),
            CoreFoundation.CFSwapInt64BigToHost(350),
        )
        self.assertEqual(
            Foundation.NSSwapHostShortToBig(350),
            CoreFoundation.CFSwapInt16HostToBig(350),
        )
        self.assertEqual(
            Foundation.NSSwapHostIntToBig(350), CoreFoundation.CFSwapInt32HostToBig(350)
        )
        self.assertEqual(
            Foundation.NSSwapHostLongLongToBig(350),
            CoreFoundation.CFSwapInt64HostToBig(350),
        )
        self.assertEqual(
            Foundation.NSSwapLittleShortToHost(350),
            CoreFoundation.CFSwapInt16LittleToHost(350),
        )
        self.assertEqual(
            Foundation.NSSwapLittleIntToHost(350),
            CoreFoundation.CFSwapInt32LittleToHost(350),
        )
        self.assertEqual(
            Foundation.NSSwapLittleLongLongToHost(350),
            CoreFoundation.CFSwapInt64LittleToHost(350),
        )
        self.assertEqual(
            Foundation.NSSwapHostShortToLittle(350),
            CoreFoundation.CFSwapInt16HostToLittle(350),
        )
        self.assertEqual(
            Foundation.NSSwapHostIntToLittle(350),
            CoreFoundation.CFSwapInt32HostToLittle(350),
        )
        self.assertEqual(
            Foundation.NSSwapHostLongLongToLittle(350),
            CoreFoundation.CFSwapInt64HostToLittle(350),
        )

        v = Foundation.NSConvertHostFloatToSwapped(55.0)
        self.assertIsInstance(v, Foundation.NSSwappedFloat)
        n = Foundation.NSConvertSwappedFloatToHost(v)
        self.assertEqual(n, 55.0)

        v = Foundation.NSSwapFloat(v)
        self.assertIsInstance(v, Foundation.NSSwappedFloat)
        v = Foundation.NSConvertHostDoubleToSwapped(55.0)
        self.assertIsInstance(v, Foundation.NSSwappedDouble)
        n = Foundation.NSConvertSwappedDoubleToHost(v)
        self.assertEqual(n, 55.0)

        v = Foundation.NSSwapDouble(v)
        self.assertIsInstance(v, Foundation.NSSwappedDouble)
        n = Foundation.NSSwapBigDoubleToHost(v)
        self.assertIsInstance(n, float)
        n = Foundation.NSSwapLittleDoubleToHost(v)
        self.assertIsInstance(n, float)
        v = Foundation.NSConvertHostFloatToSwapped(55.0)
        n = Foundation.NSSwapBigFloatToHost(v)
        self.assertIsInstance(n, float)
        n = Foundation.NSSwapLittleFloatToHost(v)
        self.assertIsInstance(n, float)
        v = Foundation.NSSwapHostDoubleToBig(55.0)
        self.assertIsInstance(v, Foundation.NSSwappedDouble)
        v = Foundation.NSSwapHostDoubleToLittle(55.0)
        self.assertIsInstance(v, Foundation.NSSwappedDouble)
        v = Foundation.NSSwapHostFloatToBig(55.0)
        self.assertIsInstance(v, Foundation.NSSwappedFloat)
        v = Foundation.NSSwapHostFloatToLittle(55.0)
        self.assertIsInstance(v, Foundation.NSSwappedFloat)
