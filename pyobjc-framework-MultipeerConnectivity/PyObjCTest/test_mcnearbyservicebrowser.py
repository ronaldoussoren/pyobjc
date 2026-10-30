import objc
from PyObjCTools.TestSupport import TestCase, min_os_level
import MultipeerConnectivity


class TestMCNearbyServiceBrowser(TestCase):
    @min_os_level("10.10")
    def test_classes(self):
        self.assertIsInstance(
            MultipeerConnectivity.MCNearbyServiceBrowser, objc.objc_class
        )

    @min_os_level("10.10")
    def test_protocols(self):
        self.assertProtocolExists(
            "MCNearbyServiceBrowserDelegate", MultipeerConnectivity
        )
