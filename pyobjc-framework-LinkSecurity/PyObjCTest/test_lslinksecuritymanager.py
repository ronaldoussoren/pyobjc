from PyObjCTools.TestSupport import TestCase
import LinkSecurity


class TestLSLinkSecurityManager(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(LinkSecurity.LSLinkSecurityManager.hasFlaggedURLs)
        self.assertArgIsBlock(
            LinkSecurity.LSLinkSecurityManager.checkIsFlaggedURL_completion_, 1, b"vZ"
        )
