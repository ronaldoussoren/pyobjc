import objc
from PyObjCTools.TestSupport import TestCase, min_os_level
import MultipeerConnectivity


class TestMCPeerID(TestCase):
    @min_os_level("10.10")
    def testClasses(self):
        self.assertIsInstance(MultipeerConnectivity.MCPeerID, objc.objc_class)
