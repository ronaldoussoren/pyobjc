import CoreAudioKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestAUCustomViewPersistentData(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("AUCustomViewPersistentData", CoreAudioKit)
