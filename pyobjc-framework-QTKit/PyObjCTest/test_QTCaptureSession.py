from PyObjCTools.TestSupport import TestCase
import QTKit


class TestQTCaptureSession(TestCase):
    def testConstants(self):
        self.assertIsInstance(QTKit.QTCaptureSessionRuntimeErrorNotification, str)
        self.assertIsInstance(QTKit.QTCaptureSessionErrorKey, str)

    def testMethods(self):
        self.assertResultIsBOOL(QTKit.QTCaptureSession.addInput_error_)
        self.assertArgIsOut(QTKit.QTCaptureSession.addInput_error_, 1)
        self.assertResultIsBOOL(QTKit.QTCaptureSession.addOutput_error_)
        self.assertArgIsOut(QTKit.QTCaptureSession.addOutput_error_, 1)
        self.assertResultIsBOOL(QTKit.QTCaptureSession.isRunning)
