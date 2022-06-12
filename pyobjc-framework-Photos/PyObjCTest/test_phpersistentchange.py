from PyObjCTools.TestSupport import TestCase, min_os_level
import Photos


class TestPHPersistentChange(TestCase):
    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsOut(
            Photos.PHPersistentChange.changeDetailsForObjectType_error_, 1
        )
