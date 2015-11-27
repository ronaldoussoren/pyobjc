from PyObjCTools.TestSupport import *
from Foundation import *

class TestNSMassFormatter (TestCase):
    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertEqual(NSMassFormatterUnitGram, 11)
        self.assertEqual(NSMassFormatterUnitKilogram, 14)
        self.assertEqual(NSMassFormatterUnitOunce, (6 << 8) + 1)
        self.assertEqual(NSMassFormatterUnitPound, (6 << 8) + 2)
        self.assertEqual(NSMassFormatterUnitStone, (6 << 8) + 3)


    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(NSMassFormatter.isForPersonMassUse)
        self.assertArgIsBOOL(NSMassFormatter.setForPersonMassUse_, 0)

        self.assertResultIsBOOL(NSLengthFormatter.getObjectValue_forString_errorDescription_)
        self.assertArgIsOut(NSLengthFormatter.getObjectValue_forString_errorDescription_, 0)
        self.assertArgIsOut(NSLengthFormatter.getObjectValue_forString_errorDescription_, 2)


if __name__ == "__main__":
    main()
