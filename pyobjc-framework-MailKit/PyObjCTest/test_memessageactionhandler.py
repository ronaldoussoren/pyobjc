from PyObjCTools.TestSupport import TestCase
import MailKit


class TestMEMessageActionHandlerHelper(MailKit.NSObject):
    def decideActionForMessage_completionHandler_(self, a, b):
        pass


class TestMEMessageActionHandler(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("MEMessageActionHandler")

    def test_methods(self):
        self.assertArgIsBlock(
            TestMEMessageActionHandlerHelper.decideActionForMessage_completionHandler_,
            1,
            b"v@",
        )
