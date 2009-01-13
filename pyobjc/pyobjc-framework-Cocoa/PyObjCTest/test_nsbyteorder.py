from PyObjCTools.TestSupport import *
import sys

from Foundation import *
import Foundation

class TestNSByteOrder (TestCase):
    def testConstants(self):
        self.assertEquals(NS_UnknownByteOrder, CFByteOrderUnknown)
        self.assertEquals(NS_LittleEndian, CFByteOrderLittleEndian)
        self.assertEquals(NS_BigEndian, CFByteOrderBigEndian)

    def testInlines(self):
        self.assertEquals(NSHostByteOrder(), CFByteOrderGetCurrent())
        self.assertEquals(NSSwapShort(350), CFSwapInt16(350))
        self.assertEquals(NSSwapInt(350), CFSwapInt32(350))
        
        if sys.maxint > 2 ** 32:
            self.assertEquals(NSSwapLong(350), CFSwapInt64(350))
            self.assertEquals(NSSwapBigLongToHost(350), CFSwapInt64BigToHost(350))
            self.assertEquals(NSSwapHostLongToBig(350), CFSwapInt64HostToBig(350))
            self.assertEquals(NSSwapLittleLongToHost(350), CFSwapInt64LittleToHost(350))
            self.assertEquals(NSSwapHostLongToLittle(350), CFSwapInt64HostToLittle(350))
        else:
            self.assertEquals(NSSwapLong(350), CFSwapInt32(350))
            self.assertEquals(NSSwapBigLongToHost(350), CFSwapInt32BigToHost(350))
            self.assertEquals(NSSwapHostLongToBig(350), CFSwapInt32HostToBig(350))
            self.assertEquals(NSSwapLittleLongToHost(350), CFSwapInt32LittleToHost(350))
            self.assertEquals(NSSwapHostLongToLittle(350), CFSwapInt32HostToLittle(350))


        self.assertEquals(NSSwapLongLong(350), CFSwapInt64(350))
        self.assertEquals(NSSwapBigShortToHost(350), CFSwapInt16BigToHost(350))
        self.assertEquals(NSSwapBigIntToHost(350), CFSwapInt32BigToHost(350))
        self.assertEquals(NSSwapBigLongLongToHost(350), CFSwapInt64BigToHost(350))
        self.assertEquals(NSSwapHostShortToBig(350), CFSwapInt16HostToBig(350))
        self.assertEquals(NSSwapHostIntToBig(350), CFSwapInt32HostToBig(350))
        self.assertEquals(NSSwapHostLongLongToBig(350), CFSwapInt64HostToBig(350))
        self.assertEquals(NSSwapLittleShortToHost(350), CFSwapInt16LittleToHost(350))
        self.assertEquals(NSSwapLittleIntToHost(350), CFSwapInt32LittleToHost(350))
        self.assertEquals(NSSwapLittleLongLongToHost(350), CFSwapInt64LittleToHost(350))
        self.assertEquals(NSSwapHostShortToLittle(350), CFSwapInt16HostToLittle(350))
        self.assertEquals(NSSwapHostIntToLittle(350), CFSwapInt32HostToLittle(350))
        self.assertEquals(NSSwapHostLongLongToLittle(350), CFSwapInt64HostToLittle(350))

        v = NSConvertHostFloatToSwapped(55.0)
        self.failUnless(isinstance(v, NSSwappedFloat))

        n = NSConvertSwappedFloatToHost(v)
        self.assertEquals(n, 55.0)

        v = NSSwapFloat(v)
        self.failUnless(isinstance(v, NSSwappedFloat))


        v = NSConvertHostDoubleToSwapped(55.0)
        self.failUnless(isinstance(v, NSSwappedDouble))


        n = NSConvertSwappedDoubleToHost(v)
        self.assertEquals(n, 55.0)

        v = NSSwapDouble(v)
        self.failUnless(isinstance(v, NSSwappedDouble))

        
        n = NSSwapBigDoubleToHost(v)
        self.failUnless(isinstance(n, float))

        n = NSSwapLittleDoubleToHost(v)
        self.failUnless(isinstance(n, float))


        v = NSConvertHostFloatToSwapped(55.0)
        n = NSSwapBigFloatToHost(v)
        self.failUnless(isinstance(n, float))

        n = NSSwapLittleFloatToHost(v)
        self.failUnless(isinstance(n, float))

        v = NSSwapHostDoubleToBig(55.0)
        self.failUnless(isinstance(v, NSSwappedDouble))

        v = NSSwapHostDoubleToLittle(55.0)
        self.failUnless(isinstance(v, NSSwappedDouble))

        v = NSSwapHostFloatToBig(55.0)
        self.failUnless(isinstance(v, NSSwappedFloat))

        v = NSSwapHostFloatToLittle(55.0)
        self.failUnless(isinstance(v, NSSwappedFloat))



if __name__ == "__main__":
    main()
