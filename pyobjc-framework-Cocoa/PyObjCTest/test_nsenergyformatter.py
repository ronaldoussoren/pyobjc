from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSEnergyFormatter (TestCase):
    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertEqual(NSEnergyFormatterUnitJoule, 11)
        self.assertEqual(NSEnergyFormatterUnitKilojoule, 14)
        self.assertEqual(NSEnergyFormatterUnitCalorie, (7 << 8) + 1)
        self.assertEqual(NSEnergyFormatterUnitKilocalorie, (7 << 8) + 2)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(NSEnergyFormatter.isForFoodEnergyUse)
        self.assertArgIsBOOL(NSEnergyFormatter.setForFoodEnergyUse_, 0)

        self.assertResultIsBOOL(NSEnergyFormatter.getObjectValue_forString_errorDescription_)
        self.assertArgIsOut(NSEnergyFormatter.getObjectValue_forString_errorDescription_, 0)
        self.assertArgIsOut(NSEnergyFormatter.getObjectValue_forString_errorDescription_, 2)

if __name__ == "__main__":
    main()
