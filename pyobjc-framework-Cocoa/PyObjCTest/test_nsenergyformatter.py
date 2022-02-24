import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSEnergyFormatter(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSEnergyFormatterUnit)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertEqual(Foundation.NSEnergyFormatterUnitJoule, 11)
        self.assertEqual(Foundation.NSEnergyFormatterUnitKilojoule, 14)
        self.assertEqual(Foundation.NSEnergyFormatterUnitCalorie, (7 << 8) + 1)
        self.assertEqual(Foundation.NSEnergyFormatterUnitKilocalorie, (7 << 8) + 2)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(Foundation.NSEnergyFormatter.isForFoodEnergyUse)
        self.assertArgIsBOOL(Foundation.NSEnergyFormatter.setForFoodEnergyUse_, 0)

        self.assertResultIsBOOL(
            Foundation.NSEnergyFormatter.getObjectValue_forString_errorDescription_
        )
        self.assertArgIsOut(
            Foundation.NSEnergyFormatter.getObjectValue_forString_errorDescription_, 0
        )
        self.assertArgIsOut(
            Foundation.NSEnergyFormatter.getObjectValue_forString_errorDescription_, 2
        )
