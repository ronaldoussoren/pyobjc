import objc
from PyObjCTools.TestSupport import TestCase, min_os_level
import MultipeerConnectivity


class TestMCAdvertiserAssistant(TestCase):
    @min_os_level("10.10")
    def test_classes(self):
        self.assertIsInstance(
            MultipeerConnectivity.MCAdvertiserAssistant, objc.objc_class
        )

    @min_os_level("10.10")
    def test_protocols(self):
        self.assertProtocolExists(
            "MCAdvertiserAssistantDelegate", MultipeerConnectivity
        )
