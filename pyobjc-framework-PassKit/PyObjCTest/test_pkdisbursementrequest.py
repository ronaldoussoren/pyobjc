from PyObjCTools.TestSupport import TestCase

import PassKit


class TestPKDisbursementRequest(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(PassKit.PKDisbursementRequestSchedule)

    def test_constants(self):
        self.assertEqual(PassKit.PKDisbursementRequestScheduleOneTime, 0)
        self.assertEqual(PassKit.PKDisbursementRequestScheduleFuture, 1)
