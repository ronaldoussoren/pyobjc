from PyObjCTools.TestSupport import TestCase
import Quartz


class TestQCCompositionRepository(TestCase):
    def test_constants(self):
        self.assertIsInstance(Quartz.QCCompositionRepositoryDidUpdateNotification, str)
