import CoreAudioKit  # noqa: F401
import objc
from PyObjCTools.TestSupport import TestCase


class TestAUCustomViewPersistentData(TestCase):
    def testProtocols(self):
        objc.protocolNamed("AUCustomViewPersistentData")
