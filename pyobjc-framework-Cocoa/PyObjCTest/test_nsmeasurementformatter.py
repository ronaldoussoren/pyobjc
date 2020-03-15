import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSMeasurementFormatter(TestCase):
    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(
            Foundation.NSMeasurementFormatterUnitOptionsProvidedUnit, 1 << 0
        )
        self.assertEqual(
            Foundation.NSMeasurementFormatterUnitOptionsNaturalScale, 1 << 1
        )
        self.assertEqual(
            Foundation.NSMeasurementFormatterUnitOptionsTemperatureWithoutUnit, 1 << 2
        )
