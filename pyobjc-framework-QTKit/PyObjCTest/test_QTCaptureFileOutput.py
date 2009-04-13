
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTCaptureFileOutputHelper  (NSObject):
    def captureOutput_shouldChangeOutputFileAtURL_forConnections_dueToError_(self, o, u, c, e):
        return False


class TestQTCaptureFileOutput (TestCase):
    def testConstants(self):
        self.failUnlessEqual(QTCaptureFileOutputBufferDestinationNewFile, 1)
        self.failUnlessEqual(QTCaptureFileOutputBufferDestinationOldFile, 2)

    def testProtocols(self):
        self.failUnlessResultIsBOOL(TestQTCaptureFileOutputHelper.captureOutput_shouldChangeOutputFileAtURL_forConnections_dueToError_)

if __name__ == "__main__":
    main()
