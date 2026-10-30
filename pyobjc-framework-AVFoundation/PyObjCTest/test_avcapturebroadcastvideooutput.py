import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestAVCaptureBroadcastVideoOutputHelper(AVFoundation.NSObject):
    def broadcastVideoOutput_didDropVideoFrameWithPresentationTimeStamp_fromConnection_(
        self, a, b, c
    ):
        pass


class TestAVCaptureBroadcastVideoOutput(TestCase):
    def test_enums(self):
        self.assertIsEnumType(
            AVFoundation.AVCaptureBroadcastVideoOutputDroppedFrameReplacementPolicy
        )
        self.assertEqual(
            AVFoundation.AVCaptureBroadcastVideoOutputDroppedFrameReplacementPolicyRepeatPreviousFrame,
            0,
        )
        self.assertEqual(
            AVFoundation.AVCaptureBroadcastVideoOutputDroppedFrameReplacementPolicyBlackFrame,
            1,
        )

    @min_sdk_level("27.0")
    def test_protocols(self):
        self.assertProtocolExists("AVCaptureBroadcastVideoOutputDelegate", AVFoundation)

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestAVCaptureBroadcastVideoOutputHelper.broadcastVideoOutput_didDropVideoFrameWithPresentationTimeStamp_fromConnection_,
            1,
            AVFoundation.CMTime.__typestr__,
        )
