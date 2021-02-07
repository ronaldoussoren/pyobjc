import SystemConfiguration
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCaptiveNework(TestCase):
    @min_os_level("10.8")
    def testFunctions10_8(self):
        self.assertResultIsBOOL(SystemConfiguration.CNSetSupportedSSIDs)
        self.assertResultIsBOOL(SystemConfiguration.CNMarkPortalOnline)
        self.assertResultIsBOOL(SystemConfiguration.CNMarkPortalOffline)
        self.assertResultIsCFRetained(SystemConfiguration.CNCopySupportedInterfaces)
