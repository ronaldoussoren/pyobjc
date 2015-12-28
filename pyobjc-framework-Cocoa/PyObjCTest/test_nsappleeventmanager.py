from Foundation import *
import Foundation
from PyObjCTools.TestSupport import *

class TestEAManager (TestCase):
    def testContants(self):
        self.assertIsInstance(NSAppleEventManagerWillProcessFirstEventNotification, unicode)
        self.assertIsInstance(NSAppleEventTimeOutDefault, float)
        self.assertIsInstance(NSAppleEventTimeOutNone, float)

    def testOpaque(self):
        self.assertHasAttr(Foundation, 'NSAppleEventManagerSuspensionID')
        self.assertHasAttr(NSAppleEventManagerSuspensionID, '__pointer__')

    def testMethods(self):
        self.assertArgIsSEL(NSAppleEventManager.setEventHandler_andSelector_forEventClass_andEventID_, 1, b'v@:@@')

if __name__ == "__main__":
    main()
