from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNEDNSSettings(TestCase):
    @min_os_level("10.11")
    def testMethods(self):
        self.assertResultIsBOOL(
            NetworkExtension.NEDNSSettings.matchDomainsNoSearch, b"Z"
        )
        self.assertArgIsBOOL(
            NetworkExtension.NEDNSSettings.setMatchDomainsNoSearch_, 0, b"Z"
        )
