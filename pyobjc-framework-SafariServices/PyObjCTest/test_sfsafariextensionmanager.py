from PyObjCTools.TestSupport import TestCase, min_os_level

import SafariServices


class TestSFSafariExtensionManager(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertArgIsBlock(
            SafariServices.SFSafariExtensionManager.getStateOfSafariExtensionWithIdentifier_completionHandler_,
            1,
            b"v@@",
        )
