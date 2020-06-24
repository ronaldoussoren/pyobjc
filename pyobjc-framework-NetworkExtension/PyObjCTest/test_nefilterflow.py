from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNEAppProxyFlow(TestCase):
    @min_os_level("10.11")
    def testConstants(self):
        self.assertEqual(NetworkExtension.NEFilterFlowBytesMax, (1 << 64) - 1)
