from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSMeasurementFormatter (TestCase):
    @min_os_level('10.12')
    def testConstants(self):
        self.assertEqual(NSMeasurementFormatterUnitOptionsProvidedUnit, 1 << 0)
        self.assertEqual(NSMeasurementFormatterUnitOptionsNaturalScale, 1 << 1)
        self.assertEqual(NSMeasurementFormatterUnitOptionsTemperatureWithoutUnit, 1 << 2)

if __name__ == "__main__":
    main()
