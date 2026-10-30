import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSMeasurementFormatter(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Foundation.NSMeasurementFormatterUnitOptions)
        self.assertEqual(
            Foundation.NSMeasurementFormatterUnitOptionsProvidedUnit, 1 << 0
        )
        self.assertEqual(
            Foundation.NSMeasurementFormatterUnitOptionsNaturalScale, 1 << 1
        )
        self.assertEqual(
            Foundation.NSMeasurementFormatterUnitOptionsTemperatureWithoutUnit, 1 << 2
        )
