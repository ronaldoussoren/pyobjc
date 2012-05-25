from PyObjCTools.TestSupport import *

from Foundation import *

try:
    unicode
except NameError:
    unicode = str

class TestNSConnectionHelper (NSObject):
    def makeNewConnection_sender_(self, a, b): return 1
    def connection_shouldMakeNewConnection_(self, a, b): return 1
    def authenticateComponents_withData_(self, a, b): return 1
    def connection_handleRequest_(self, a, b): return 1

class TestNSConnection (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSConnectionReplyMode, unicode)
        self.assertIsInstance(NSConnectionDidDieNotification, unicode)
        self.assertIsInstance(NSFailedAuthenticationException, unicode)
        self.assertIsInstance(NSConnectionDidInitializeNotification, unicode)

    def testMethods(self):
        self.assertArgIsBOOL(NSConnection.setIndependentConversationQueueing_, 0)
        self.assertResultIsBOOL(NSConnection.independentConversationQueueing)
        self.assertResultIsBOOL(NSConnection.isValid)
        self.assertResultIsBOOL(NSConnection.registerName_)
        self.assertResultIsBOOL(NSConnection.registerName_withNameServer_)
        self.assertResultIsBOOL(NSConnection.multipleThreadsEnabled)

    def testProtocols(self):
        self.assertResultIsBOOL(TestNSConnectionHelper.makeNewConnection_sender_)
        self.assertResultIsBOOL(TestNSConnectionHelper.connection_shouldMakeNewConnection_)
        self.assertResultIsBOOL(TestNSConnectionHelper.authenticateComponents_withData_)
        self.assertResultIsBOOL(TestNSConnectionHelper.connection_handleRequest_)

if __name__ == "__main__":
    main()
