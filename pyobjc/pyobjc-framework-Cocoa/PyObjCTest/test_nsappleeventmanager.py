from Foundation import *
import Foundation
from PyObjCTools.TestSupport import *

class TestEAManager (TestCase):
    def _testSuspension(self):
        self.fail('- (NSAppleEventManagerSuspensionID)suspendCurrentAppleEvent;')
        self.fail('- (NSAppleEventDescriptor *)appleEventForSuspensionID:(NSAppleEventManagerSuspensionID)suspensionID;')
        self.fail('- (NSAppleEventDescriptor *)replyAppleEventForSuspensionID:(NSAppleEventManagerSuspensionID)suspensionID;')
        self.fail('- (void)setCurrentAppleEventAndReplyEventWithSuspensionID:(NSAppleEventManagerSuspensionID)suspensionID;')
        self.fail('- (void)resumeWithSuspensionID:(NSAppleEventManagerSuspensionID)suspensionID;')

    def testContants(self):
        self.failUnless( isinstance(NSAppleEventManagerWillProcessFirstEventNotification, unicode) )
        self.failUnless( isinstance(NSAppleEventTimeOutDefault, float) )
        self.failUnless( isinstance(NSAppleEventTimeOutNone, float) )

    def testOpaque(self):
        self.failUnless(hasattr(Foundation, 'NSAppleEventManagerSuspensionID'))
        self.failUnless(hasattr(NSAppleEventManagerSuspensionID, '__pointer__'))



if __name__ == "__main__":
    main()
