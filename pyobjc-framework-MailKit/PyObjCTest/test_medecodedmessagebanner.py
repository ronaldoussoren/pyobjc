from PyObjCTools.TestSupport import TestCase
import MailKit


class TestMEDecodedMessageBanner(TestCase):
    def test_classes(self):
        self.assertArgIsBOOL(
            MailKit.MEDecodedMessageBanner.initWithTitle_primaryActionTitle_dismissable_,
            2,
        )
