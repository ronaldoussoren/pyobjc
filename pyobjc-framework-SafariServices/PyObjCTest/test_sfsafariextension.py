from PyObjCTools.TestSupport import TestCase, min_os_level

import SafariServices


class TestSFSafariExtension(TestCase):
    @min_os_level("10.14.4")
    def test_methods(self):
        self.assertArgIsBlock(
            SafariServices.SFSafariExtension.getBaseURIWithCompletionHandler_, 0, b"v@"
        )
