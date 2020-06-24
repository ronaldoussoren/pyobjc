from PyObjCTools.TestSupport import TestCase, min_os_level
import QTKit


class TestQTCaptureFileOutputHelper(QTKit.NSObject):
    def captureOutput_shouldChangeOutputFileAtURL_forConnections_dueToError_(
        self, o, u, c, e
    ):
        return False


class TestQTCaptureFileOutput(TestCase):
    def testConstants(self):
        self.assertEqual(QTKit.QTCaptureFileOutputBufferDestinationNewFile, 1)
        self.assertEqual(QTKit.QTCaptureFileOutputBufferDestinationOldFile, 2)

    @min_os_level("10.6")
    def testMethods(self):
        self.assertResultIsBOOL(QTKit.QTCaptureFileOutput.isRecordingPaused)

    def testProtocols(self):
        self.assertResultIsBOOL(
            TestQTCaptureFileOutputHelper.captureOutput_shouldChangeOutputFileAtURL_forConnections_dueToError_
        )
