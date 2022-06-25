import CoreAudioKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestAUCustomViewPersistentData(TestCase):
    def testProtocols(self):
        self.assertProtocolExists("AUCustomViewPersistentData")
