from PyObjCTools.TestSupport import TestCase

import AVRouting


class TestAVCustomRoutingEvent(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AVRouting.AVCustomRoutingEventReason)
        self.assertEqual(AVRouting.AVCustomRoutingEventReasonActivate, 0)
        self.assertEqual(AVRouting.AVCustomRoutingEventReasonDeactivate, 1)
        self.assertEqual(AVRouting.AVCustomRoutingEventReasonReactivate, 2)
