import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINStartVideoCallIntentHelper (Intents.NSObject):
        def handleStartVideoCall_completion_(self, intent, completion): pass
        def confirmStartVideoCall_completion_(self, intent, completion): pass
        def resolveContactsForStartVideoCall_withCompletion_(self, intent, completion): pass

    class TestINStartVideoCallIntent (TestCase):
        @min_os_level('10.12')
        def testMethods(self):
            self.assertArgIsBlock(TestINStartVideoCallIntentHelper.handleStartVideoCall_completion_, 1, b'v@')
            self.assertArgIsBlock(TestINStartVideoCallIntentHelper.confirmStartVideoCall_completion_, 1, b'v@')
            self.assertArgIsBlock(TestINStartVideoCallIntentHelper.resolveContactsForStartVideoCall_withCompletion_, 1, b'v@')

        @min_sdk_level('10.12')
        def testProtocols(self):
            objc.protocolNamed('INStartVideoCallIntentHandling')

if __name__ == "__main__":
    main()
