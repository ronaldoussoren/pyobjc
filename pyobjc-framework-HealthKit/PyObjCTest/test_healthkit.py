from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHealthKit(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(HealthKit)
