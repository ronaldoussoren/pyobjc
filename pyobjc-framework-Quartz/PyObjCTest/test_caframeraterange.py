from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz
import objc


class TestCAFrameRateRange(TestCase):
    def test_structs(self):
        v = Quartz.CAFrameRateRange()
        self.assertIsInstance(v.minimum, float)
        self.assertIsInstance(v.maximum, float)
        self.assertIsInstance(v.preferred, float)
        self.assertPickleRoundTrips(v)

    @min_os_level("12.0")
    def test_constants(self):
        self.assertIsInstance(Quartz.CAFrameRateRangeDefault, Quartz.CAFrameRateRange)

    @min_os_level("12.0")
    def test_functions_12_0(self):
        self.assertResultHasType(
            Quartz.CAFrameRateRangeMake, Quartz.CAFrameRateRange.__typestr__
        )

        self.assertResultHasType(Quartz.CAFrameRateRangeIsEqualToRange, objc._C_BOOL)
