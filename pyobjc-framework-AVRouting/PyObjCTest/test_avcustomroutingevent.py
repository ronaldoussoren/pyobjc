from PyObjCTools.TestSupport import TestCase

import AVRouting


class TestAVCustomRoutingControllerHelper(AVRouting.NSObject):
    def customRoutingController_handleEvent_completionHandler_(self, a, b, c):
        pass


class TestAVCustomRoutingController(TestCase):
    def test_constants(self):
        self.assertIsEnumType(AVRouting.AVCustomRoutingEventReason)
        self.assertEqual(AVRouting.AVCustomRoutingEventReasonActivate, 0)
        self.assertEqual(AVRouting.AVCustomRoutingEventReasonDeactivate, 1)
        self.assertEqual(AVRouting.AVCustomRoutingEventReasonReactivate, 2)
