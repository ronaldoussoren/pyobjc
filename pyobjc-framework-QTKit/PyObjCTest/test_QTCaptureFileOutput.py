
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTCaptureFileOutputHelper  (NSObject):
    def captureOutput_shouldChangeOutputFileAtURL_forConnections_dueToError_(self, o, u, c, e):
        return False


class TestQTCaptureFileOutput (TestCase):
    def testConstants(self):
        self.assertEqual(QTCaptureFileOutputBufferDestinationNewFile, 1)
        self.assertEqual(QTCaptureFileOutputBufferDestinationOldFile, 2)

    @min_os_level('10.6')
    def testMethods(self):
        self.assertResultIsBOOL(QTCaptureFileOutput.isRecordingPaused)

    def testProtocols(self):
        self.assertResultIsBOOL(TestQTCaptureFileOutputHelper.captureOutput_shouldChangeOutputFileAtURL_forConnections_dueToError_)

if __name__ == "__main__":
    main()
