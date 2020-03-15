import Foundation
from PyObjCTools.TestSupport import TestCase


class TestEAManager(TestCase):
    def testContants(self):
        self.assertIsInstance(
            Foundation.NSAppleEventManagerWillProcessFirstEventNotification, str
        )
        self.assertIsInstance(Foundation.NSAppleEventTimeOutDefault, float)
        self.assertIsInstance(Foundation.NSAppleEventTimeOutNone, float)

    def testOpaque(self):
        self.assertHasAttr(Foundation, "NSAppleEventManagerSuspensionID")
        self.assertHasAttr(Foundation.NSAppleEventManagerSuspensionID, "__pointer__")

    def testMethods(self):
        self.assertArgIsSEL(
            Foundation.NSAppleEventManager.setEventHandler_andSelector_forEventClass_andEventID_,  # noqa: B950
            1,
            b"v@:@@",
        )
