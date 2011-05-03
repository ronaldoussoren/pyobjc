
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTCaptureSession (TestCase):
    def testConstants(self):
        self.assertIsInstance(QTCaptureSessionRuntimeErrorNotification, unicode)
        self.assertIsInstance(QTCaptureSessionErrorKey, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(QTCaptureSession.addInput_error_)
        self.assertArgIsOut(QTCaptureSession.addInput_error_, 1)
        self.assertResultIsBOOL(QTCaptureSession.addOutput_error_)
        self.assertArgIsOut(QTCaptureSession.addOutput_error_, 1)
        self.assertResultIsBOOL(QTCaptureSession.isRunning)


if __name__ == "__main__":
    main()
