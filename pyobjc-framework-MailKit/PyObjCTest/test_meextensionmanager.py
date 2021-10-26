from PyObjCTools.TestSupport import TestCase
import MailKit


class TestMEExtensionManager(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            MailKit.MEExtensionManager.reloadContentBlockerWithIdentifier_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            MailKit.MEExtensionManager.reloadVisibleMessagesWithCompletionHandler_,
            0,
            b"v@",
        )
