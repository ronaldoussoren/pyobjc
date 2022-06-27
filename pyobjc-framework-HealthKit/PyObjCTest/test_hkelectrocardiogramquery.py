from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKElectrocardiogramQuery(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            HealthKit.HKElectrocardiogramQuery.initWithElectrocardiogram_dataHandler_,
            1,
            b"v@@Z@",
        )
