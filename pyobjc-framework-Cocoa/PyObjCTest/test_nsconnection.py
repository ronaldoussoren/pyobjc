import Foundation
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestNSConnectionHelper(Foundation.NSObject):
    def makeNewConnection_sender_(self, a, b):
        return 1

    def connection_shouldMakeNewConnection_(self, a, b):
        return 1

    def authenticateComponents_withData_(self, a, b):
        return 1

    def connection_handleRequest_(self, a, b):
        return 1


class TestNSConnection(TestCase):
    def testConstants(self):
        self.assertIsInstance(Foundation.NSConnectionReplyMode, str)
        self.assertIsInstance(Foundation.NSConnectionDidDieNotification, str)
        self.assertIsInstance(Foundation.NSFailedAuthenticationException, str)
        self.assertIsInstance(Foundation.NSConnectionDidInitializeNotification, str)

    def testMethods(self):
        self.assertArgIsBOOL(
            Foundation.NSConnection.setIndependentConversationQueueing_, 0
        )
        self.assertResultIsBOOL(Foundation.NSConnection.independentConversationQueueing)
        self.assertResultIsBOOL(Foundation.NSConnection.isValid)
        self.assertResultIsBOOL(Foundation.NSConnection.registerName_)
        self.assertResultIsBOOL(Foundation.NSConnection.registerName_withNameServer_)
        self.assertResultIsBOOL(Foundation.NSConnection.multipleThreadsEnabled)

    def testProtocols(self):
        self.assertResultIsBOOL(TestNSConnectionHelper.makeNewConnection_sender_)
        self.assertResultIsBOOL(
            TestNSConnectionHelper.connection_shouldMakeNewConnection_
        )
        self.assertResultIsBOOL(TestNSConnectionHelper.authenticateComponents_withData_)
        self.assertResultIsBOOL(TestNSConnectionHelper.connection_handleRequest_)

    @min_sdk_level("10.10")
    def testProtocolObjects(self):
        self.assertProtocolExists("NSConnectionDelegate")
