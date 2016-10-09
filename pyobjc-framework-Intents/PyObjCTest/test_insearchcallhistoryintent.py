import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINSearchCallHistoryIntentHelper (Intents.NSObject):
        def handleSearchCallHistory_completion_(self, intent, completion): pass
        def confirmSearchCallHistory_completion_(self, intent, completion): pass
        def resolveCallTypeForSearchCallHistory_withCompletion_(self, intent, completion): pass
        def resolveRecipientForSearchCallHistory_withCompletion_(self, intent, completion): pass
        def resolveCallCapabilitiesForSearchCallHistory_withCompletion_(self, intent, completion): pass

    class TestINSearchCallHistoryIntent (TestCase):
        @min_os_level('10.12')
        def testMethods(self):
            self.assertArgIsBlock(TestINSearchCallHistoryIntentHelper.handleSearchCallHistory_completion_, 1, b'v@')
            self.assertArgIsBlock(TestINSearchCallHistoryIntentHelper.confirmSearchCallHistory_completion_, 1, b'v@')
            self.assertArgIsBlock(TestINSearchCallHistoryIntentHelper.resolveCallTypeForSearchCallHistory_withCompletion_, 1, b'v@')
            self.assertArgIsBlock(TestINSearchCallHistoryIntentHelper.resolveRecipientForSearchCallHistory_withCompletion_, 1, b'v@')
            self.assertArgIsBlock(TestINSearchCallHistoryIntentHelper.resolveCallCapabilitiesForSearchCallHistory_withCompletion_, 1, b'v@')

        @min_sdk_level('10.12')
        def testProtocols(self):
            objc.protocolNamed('INSearchCallHistoryIntentHandling')


if __name__ == "__main__":
    main()
