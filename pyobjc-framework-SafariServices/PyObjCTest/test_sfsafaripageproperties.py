from PyObjCTools.TestSupport import TestCase, min_os_level

import SafariServices


class TestSFSafariPageProperties(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultIsBOOL(
            SafariServices.SFSafariPageProperties.usesPrivateBrowsing
        )
        self.assertResultIsBOOL(SafariServices.SFSafariPageProperties.isActive)
