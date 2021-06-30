from PyObjCTools.TestSupport import TestCase
import Intents


class TestINCallRecordResolutionResult(TestCase):
    def test_constants(self):
        self.assertEqual(
            Intents.INStartCallCallRecordToCallBackUnsupportedReasonNoMatchingCall, 1
        )
