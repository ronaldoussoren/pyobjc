from PyObjCTools.TestSupport import TestCase, min_os_level

import SafariServices


class TestSFContentBlockerManager(TestCase):
    @min_os_level("10.12")
    def test_methods(self):
        self.assertArgIsBlock(
            SafariServices.SFContentBlockerManager.reloadContentBlockerWithIdentifier_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            SafariServices.SFContentBlockerManager.getStateOfContentBlockerWithIdentifier_completionHandler_,
            1,
            b"v@@",
        )
