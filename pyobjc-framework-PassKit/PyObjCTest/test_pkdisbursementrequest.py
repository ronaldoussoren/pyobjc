from PyObjCTools.TestSupport import TestCase, min_os_level

import PassKit


class TestPKDisbursementRequest(TestCase):
    def test_enums(self):
        self.assertIsEnumType(PassKit.PKDisbursementRequestSchedule)
        self.assertEqual(PassKit.PKDisbursementRequestScheduleOneTime, 0)
        self.assertEqual(PassKit.PKDisbursementRequestScheduleFuture, 1)

    @min_os_level("26.4")
    def test_methods_26_4(self):
        self.assertResultIsBOOL(PassKit.PKDisbursementRequest.isDelegatedRequest)
        self.assertArgIsBOOL(PassKit.PKDisbursementRequest.setIsDelegatedRequest_, 0)
