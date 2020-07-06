from PyObjCTools.TestSupport import TestCase

import PassKit


class TestPKDisbursementRequest(TestCase):
    def test_constants(self):
        self.assertEqual(PassKit.PKDisbursementRequestScheduleOneTime, 0)
        self.assertEqual(PassKit.PKDisbursementRequestScheduleFuture, 1)
