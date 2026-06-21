import Foundation
from PyObjCTools.TestSupport import TestCase


class TestEAManager(TestCase):
    def test_constants(self):
        self.assertIsInstance(
            Foundation.NSAppleEventManagerWillProcessFirstEventNotification, str
        )
        self.assertIsInstance(Foundation.NSAppleEventTimeOutDefault, float)
        self.assertIsInstance(Foundation.NSAppleEventTimeOutNone, float)

    def test_opaque(self):
        self.assertHasAttr(Foundation, "NSAppleEventManagerSuspensionID")
        self.assertHasAttr(Foundation.NSAppleEventManagerSuspensionID, "__pointer__")

    def test_methods(self):
        self.assertArgIsSEL(
            Foundation.NSAppleEventManager.setEventHandler_andSelector_forEventClass_andEventID_,  # noqa: B950
            1,
            b"v@:@@",
        )
