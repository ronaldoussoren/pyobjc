from PyObjCTools.TestSupport import TestCase, min_os_level
import Photos


class TestPHPersistentChangeFetchResult(TestCase):
    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsBlock(
            Photos.PHPersistentChangeFetchResult.enumerateChangesWithBlock_, 0, b"v@o^Z"
        )
