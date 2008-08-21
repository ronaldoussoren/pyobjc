from Foundation import *
import unittest

class TestEAManager (unittest.TestCase):
    def testSuspension(self):
        self.fail('- (NSAppleEventManagerSuspensionID)suspendCurrentAppleEvent;')
        self.fail('- (NSAppleEventDescriptor *)appleEventForSuspensionID:(NSAppleEventManagerSuspensionID)suspensionID;')
        self.fail('- (NSAppleEventDescriptor *)replyAppleEventForSuspensionID:(NSAppleEventManagerSuspensionID)suspensionID;')
        self.fail('- (void)setCurrentAppleEventAndReplyEventWithSuspensionID:(NSAppleEventManagerSuspensionID)suspensionID;')
        self.fail('- (void)resumeWithSuspensionID:(NSAppleEventManagerSuspensionID)suspensionID;')



if __name__ == "__main__":
    unittest.main()
