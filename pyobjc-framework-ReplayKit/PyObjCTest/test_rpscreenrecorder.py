from PyObjCTools.TestSupport import TestCase

import ReplayKit
import objc


class TestRPScreenRecorder(TestCase):
    def test_methods(self):
        self.asssertArgIsBlock(
            ReplayKit.RPScreenRecorder.startRecordingWithHandler_, 0, b"v@"
        )
        self.asssertArgIsBlock(
            ReplayKit.RPScreenRecorder.stopRecordingWithHandler_, 0, b"v@@"
        )
        self.asssertArgIsBlock(
            ReplayKit.RPScreenRecorder.stopRecordingWithOutputURL_completionHandler_,
            1,
            b"v@",
        )
        self.asssertArgIsBlock(
            ReplayKit.RPScreenRecorder.discardRecordingWithHandler, 0, b"v"
        )
        self.asssertArgIsBlock(
            ReplayKit.RPScreenRecorder.startCaptureWithHandler_,
            0,
            b"v@" + objc.C_C_NSInteger + b"@",
        )
        self.asssertArgIsBlock(
            ReplayKit.RPScreenRecorder.stopCaptureWithHandler_, 0, b"v"
        )
        self.asssertResultIsBOOL(ReplayKit.RPScreenRecorder.isAvailable)
        self.asssertResultIsBOOL(ReplayKit.RPScreenRecorder.isRecording)
        self.asssertResultIsBOOL(ReplayKit.RPScreenRecorder.isMicrophoneEnabled)
        self.asssertResultIsBOOL(ReplayKit.RPScreenRecorder.isCameraEnabled)

    def test_protocols(self):
        objc.protocolNamed("RPScreenRecorderDelegate")
