from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSConnectionHelper (NSObject):
    def makeNewConnection_sender_(self, a, b): return 1
    def connection_shouldMakeNewConnection_(self, a, b): return 1
    def authenticateComponents_withData_(self, a, b): return 1
    def connection_handleRequest_(self, a, b): return 1

class TestNSConnection (TestCase):
    def testConstants(self):
        self.failUnless( isinstance(NSConnectionReplyMode, unicode) )
        self.failUnless( isinstance(NSConnectionDidDieNotification, unicode) )

        self.failUnless( isinstance(NSFailedAuthenticationException, unicode) )
        self.failUnless( isinstance(NSConnectionDidInitializeNotification, unicode) )

    def testMethods(self):
        self.failUnlessArgIsBOOL(NSConnection.setIndependentConversationQueueing_, 0)
        self.failUnlessResultIsBOOL(NSConnection.independentConversationQueueing)
        self.failUnlessResultIsBOOL(NSConnection.isValid)
        self.failUnlessResultIsBOOL(NSConnection.registerName_)
        self.failUnlessResultIsBOOL(NSConnection.registerName_withNameServer_)
        self.failUnlessResultIsBOOL(NSConnection.multipleThreadsEnabled)

    def testProtocols(self):
        self.failUnlessResultIsBOOL(TestNSConnectionHelper.makeNewConnection_sender_)
        self.failUnlessResultIsBOOL(TestNSConnectionHelper.connection_shouldMakeNewConnection_)
        self.failUnlessResultIsBOOL(TestNSConnectionHelper.authenticateComponents_withData_)
        self.failUnlessResultIsBOOL(TestNSConnectionHelper.connection_handleRequest_)

if __name__ == "__main__":
    main()
