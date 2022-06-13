from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCAEDRMetadata(TestCase):
    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(Quartz.CAEDRMetadata.isAvailable)
