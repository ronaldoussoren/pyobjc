from PyObjCTools.TestSupport import TestCase
import CallKit
import objc


class TestCXProvider(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CallKit.CXCallEndedReason)

    def test_constants(self):
        self.assertEqual(CallKit.CXCallEndedReasonFailed, 1)
        self.assertEqual(CallKit.CXCallEndedReasonRemoteEnded, 2)
        self.assertEqual(CallKit.CXCallEndedReasonUnanswered, 3)
        self.assertEqual(CallKit.CXCallEndedReasonAnsweredElsewhere, 4)
        self.assertEqual(CallKit.CXCallEndedReasonDeclinedElsewhere, 5)

    def test_protocols(self):
        objc.protocolNamed("CXProviderDelegate")

    def test_methods(self):
        self.assertArgIsBlock(
            CallKit.CXProvider.reportNewIncomingCallWithUUID_update_completion_,
            2,
            b"v@",
        )
