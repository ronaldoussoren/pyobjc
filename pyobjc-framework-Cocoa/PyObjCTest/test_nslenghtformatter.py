from PyObjCTools.TestSupport import *
from Foundation import *

class TestNSLengthFormatter (TestCase):
    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertEqual(NSLengthFormatterUnitMillimeter, 8)
        self.assertEqual(NSLengthFormatterUnitCentimeter, 9)
        self.assertEqual(NSLengthFormatterUnitMeter, 11)
        self.assertEqual(NSLengthFormatterUnitKilometer, 14)
        self.assertEqual(NSLengthFormatterUnitInch, (5 << 8) + 1)
        self.assertEqual(NSLengthFormatterUnitFoot,(5 << 8) + 2)
        self.assertEqual(NSLengthFormatterUnitYard, (5 << 8) + 3)
        self.assertEqual(NSLengthFormatterUnitMile, (5 << 8) + 4)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(NSLengthFormatter.isForPersonHeightUse)
        self.assertArgIsBOOL(NSLengthFormatter.setForPersonHeightUse_, 0)

        self.assertResultIsBOOL(NSLengthFormatter.getObjectValue_forString_errorDescription_)
        self.assertArgIsOut(NSLengthFormatter.getObjectValue_forString_errorDescription_, 0)
        self.assertArgIsOut(NSLengthFormatter.getObjectValue_forString_errorDescription_, 2)


if __name__ == "__main__":
    main()
