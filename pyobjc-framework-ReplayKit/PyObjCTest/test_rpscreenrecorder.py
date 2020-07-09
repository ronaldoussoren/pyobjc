from PyObjCTools.TestSupport import TestCase

import ReplayKit
import objc


class TestRPScreenRecorder(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            ReplayKit.RPScreenRecorder.startRecordingWithHandler_, 0, b"v@"
        )
        self.assertArgIsBlock(
            ReplayKit.RPScreenRecorder.stopRecordingWithHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            ReplayKit.RPScreenRecorder.stopRecordingWithOutputURL_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            ReplayKit.RPScreenRecorder.discardRecordingWithHandler_, 0, b"v"
        )
        self.assertArgIsBlock(
            ReplayKit.RPScreenRecorder.startCaptureWithHandler_completionHandler_,
            0,
            b"v^{opaqueCMSampleBuffer=}" + objc._C_NSInteger + b"@",
        )
        self.assertArgIsBlock(
            ReplayKit.RPScreenRecorder.startCaptureWithHandler_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            ReplayKit.RPScreenRecorder.stopCaptureWithHandler_, 0, b"v@"
        )
        self.assertResultIsBOOL(ReplayKit.RPScreenRecorder.isAvailable)
        self.assertResultIsBOOL(ReplayKit.RPScreenRecorder.isRecording)
        self.assertResultIsBOOL(ReplayKit.RPScreenRecorder.isMicrophoneEnabled)
        self.assertResultIsBOOL(ReplayKit.RPScreenRecorder.isCameraEnabled)

    def test_protocols(self):
        objc.protocolNamed("RPScreenRecorderDelegate")
