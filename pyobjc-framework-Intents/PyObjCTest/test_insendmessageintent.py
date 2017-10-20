import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINSendMessageIntentHelper (Intents.NSObject):
        def handleSendMessage_completion_(self, intent, completion): pass
        def confirmSendMessage_completion_(self, intent, completion): pass
        def resolveRecipientsForSendMessage_withCompletion_(self, intent, completion): pass
        def resolveContentForSendMessage_withCompletion_(self, intent, completion): pass
        def resolveGroupNameForSendMessage_withCompletion_(self, intent, completion): pass
        def resolveServiceNameForSendMessage_withCompletion_(self, intent, completion): pass
        def resolveSenderForSendMessage_withCompletion_(self, intent, completion): pass
        def resolveSpeakableGroupNameForSendMessage_withCompletion_(self, intent, completion): pass
        def resolveRecipientsForSendMessage_completion_(self, intent, completion): pass

    class TestINSendMessageIntent (TestCase):
        @min_os_level('10.12')
        def testMethods(self):
            self.assertArgIsBlock(TestINSendMessageIntentHelper.handleSendMessage_completion_, 1, b'v@')
            self.assertArgIsBlock(TestINSendMessageIntentHelper.confirmSendMessage_completion_, 1, b'v@')
            self.assertArgIsBlock(TestINSendMessageIntentHelper.resolveRecipientsForSendMessage_withCompletion_, 1, b'v@')
            self.assertArgIsBlock(TestINSendMessageIntentHelper.resolveContentForSendMessage_withCompletion_, 1, b'v@')
            self.assertArgIsBlock(TestINSendMessageIntentHelper.resolveContentForSendMessage_withCompletion_, 1, b'v@')
            self.assertArgIsBlock(TestINSendMessageIntentHelper.resolveGroupNameForSendMessage_withCompletion_, 1, b'v@')
            #self.assertArgIsBlock(TestINSendMessageIntentHelper.resolveServiceNameForSendMessage_withCompletion_, 1, b'v@')
            #self.assertArgIsBlock(TestINSendMessageIntentHelper.resolveSenderForSendMessage_withCompletion_, 1, b'v@')
            self.assertArgIsBlock(TestINSendMessageIntentHelper.resolveSpeakableGroupNameForSendMessage_withCompletion_, 1, b'v@')

        @min_os_level('10.13')
        def testMethods10_13(self):
            self.assertArgIsBlock(TestINSendMessageIntentHelper.resolveRecipientsForSendMessage_completion_, 1, b'v@')

        @min_sdk_level('10.12')
        def testProtocols(self):
            objc.protocolNamed('INSendMessageIntentHandling')

if __name__ == "__main__":
    main()
