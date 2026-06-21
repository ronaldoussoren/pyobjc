from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestQCCompositionRepository(TestCase):
    @min_os_level("10.5")
    def test_constants(self):
        self.assertIsInstance(Quartz.QCCompositionRepositoryDidUpdateNotification, str)
