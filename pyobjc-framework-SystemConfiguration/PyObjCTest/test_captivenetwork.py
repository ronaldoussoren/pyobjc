import SystemConfiguration
from PyObjCTools.TestSupport import TestCase


class TestCaptiveNework(TestCase):
    def test_functions(self):
        self.assertResultIsBOOL(SystemConfiguration.CNSetSupportedSSIDs)
        self.assertResultIsBOOL(SystemConfiguration.CNMarkPortalOnline)
        self.assertResultIsBOOL(SystemConfiguration.CNMarkPortalOffline)
        self.assertResultIsCFRetained(SystemConfiguration.CNCopySupportedInterfaces)
