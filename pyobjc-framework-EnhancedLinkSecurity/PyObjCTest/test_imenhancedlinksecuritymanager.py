from PyObjCTools.TestSupport import TestCase

import EnhancedLinkSecurity


class TestIMEnhancedLinkSecurityManager(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            EnhancedLinkSecurity.IMEnhancedLinkSecurityManager.hasURLsRequiringEnhancedSecurity
        )
        self.assertResultIsBOOL(
            EnhancedLinkSecurity.IMEnhancedLinkSecurityManager.shouldUseEnhancedSecurityForURL_
        )
        self.assertArgIsBlock(
            EnhancedLinkSecurity.IMEnhancedLinkSecurityManager.shouldUseEnhancedSecurityForURL_completion_,
            1,
            b"vZ",
        )
