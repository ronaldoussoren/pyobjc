import objc
from PyObjCTools.TestSupport import TestCase, min_os_level
import MultipeerConnectivity


class TestMCBrowserViewControllerHelper(MultipeerConnectivity.NSObject):
    def browserViewController_shouldPresentNearbyPeer_withDiscoveryInfo_(
        self, vc, p, i
    ):
        return 1


class TestMCBrowserViewController(TestCase):
    @min_os_level("10.10")
    def testClasses(self):
        self.assertIsInstance(
            MultipeerConnectivity.MCBrowserViewController, objc.objc_class
        )

    @min_os_level("10.10")
    def testProtocols(self):
        self.assertIsInstance(
            objc.protocolNamed("MCBrowserViewControllerDelegate"), objc.formal_protocol
        )

        self.assertResultIsBOOL(
            TestMCBrowserViewControllerHelper.browserViewController_shouldPresentNearbyPeer_withDiscoveryInfo_
        )
