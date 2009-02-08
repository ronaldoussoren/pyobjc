
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTCaptureSession (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(QTCaptureSessionRuntimeErrorNotification, unicode)
        self.failUnlessIsInstance(QTCaptureSessionErrorKey, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(QTCaptureSession.addInput_error_)
        self.failUnlessArgIsOut(QTCaptureSession.addInput_error_, 1)
        self.failUnlessResultIsBOOL(QTCaptureSession.addOutput_error_)
        self.failUnlessArgIsOut(QTCaptureSession.addOutput_error_, 1)
        self.failUnlessResultIsBOOL(QTCaptureSession.isRunning)


if __name__ == "__main__":
    main()
