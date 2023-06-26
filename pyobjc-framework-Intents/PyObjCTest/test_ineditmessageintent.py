from PyObjCTools.TestSupport import TestCase
import Intents


class TestINEditMessageIntentHelper(Intents.NSObjet):
    def handleEditMessage_completion_(self, a, b):
        pass

    def confirmEditMessage_completion_(self, a, b):
        pass

    def resolveEditedContentForEditMessage_withCompletion_(self, a, b):
        pass


class TestINEditMessageIntent(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("INEditMessageIntentHandling")

    def test_methods(self):
        self.assertArgIsBlock(
            TestINEditMessageIntentHelper.handleEditMessage_completion_, 1, b"v@"
        )
        self.assertArgIsBlock(
            TestINEditMessageIntentHelper.confirmEditMessage_completion_, 1, b"v@"
        )
        self.assertArgIsBlock(
            TestINEditMessageIntentHelper.resolveEditedContentForEditMessage_withCompletion_,
            1,
            b"v@",
        )
