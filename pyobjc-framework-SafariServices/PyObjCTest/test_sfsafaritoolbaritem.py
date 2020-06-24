from PyObjCTools.TestSupport import TestCase, min_os_level

import SafariServices


class TestSFSafariToolbarItem(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertArgIsBOOL(
            SafariServices.SFSafariToolbarItem.setEnabled_withBadgeText_, 0
        )
        self.assertArgIsBOOL(SafariServices.SFSafariToolbarItem.setEnabled_, 0)
