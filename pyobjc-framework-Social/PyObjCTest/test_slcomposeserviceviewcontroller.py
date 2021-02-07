from PyObjCTools.TestSupport import TestCase, min_os_level

import Social


class TestSLComposeServiceViewController(TestCase):
    @min_os_level("10.10")
    def testMethods(self):
        self.assertResultIsBOOL(Social.SLComposeServiceViewController.isContentValid)
