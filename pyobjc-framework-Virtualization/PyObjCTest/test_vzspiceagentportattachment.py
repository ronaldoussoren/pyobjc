from PyObjCTools.TestSupport import TestCase, min_os_level, arch_only

import Virtualization


class TestVZSpiceAgentPortAttachment(TestCase):
    @min_os_level("13.0")
    @arch_only("arm64")
    def test_methods13_0(self):
        self.assertResultIsBOOL(
            Virtualization.VZSpiceAgentPortAttachment.sharesClipboard
        )
        self.assertArgIsBOOL(
            Virtualization.VZSpiceAgentPortAttachment.setSharesClipboard_, 0
        )
