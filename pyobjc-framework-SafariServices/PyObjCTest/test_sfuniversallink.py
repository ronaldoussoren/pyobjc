from PyObjCTools.TestSupport import TestCase, min_os_level

import SafariServices


class TestSFUniversalLink(TestCase):
    @min_os_level("10.15")
    def testMethods(self):
        self.assertResultIsBOOL(SafariServices.SFUniversalLink.isEnabled)
        self.assertArgIsBOOL(SafariServices.SFUniversalLink.setEnabled_, 0)
