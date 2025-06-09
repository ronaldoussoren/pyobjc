from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKSourceRevision(TestCase):
    def test_constants(self):
        self.assertIsInstance(HealthKit.HKSourceRevisionAnyVersion, str)
        self.assertIsInstance(HealthKit.HKSourceRevisionAnyProductType, str)

        self.assertIsInstance(
            HealthKit.HKSourceRevisionAnyOperatingSystem,
            HealthKit.NSOperatingSystemVersion,
        )

    def test_methods(self):
        self.assertArgHasType(
            HealthKit.HKSourceRevision.initWithSource_version_productType_operatingSystemVersion_,
            3,
            HealthKit.NSOperatingSystemVersion.__typestr__,
        )
        self.assertResultHasType(
            HealthKit.HKSourceRevision.operatingSystemVersion,
            HealthKit.NSOperatingSystemVersion.__typestr__,
        )
