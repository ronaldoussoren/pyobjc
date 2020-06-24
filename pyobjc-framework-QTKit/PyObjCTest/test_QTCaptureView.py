from PyObjCTools.TestSupport import TestCase
import QTKit


class TestQTCaptureView(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(QTKit.QTCaptureView.preservesAspectRatio)
        self.assertArgIsBOOL(QTKit.QTCaptureView.setPreservesAspectRatio_, 0)

    # def testProtocols(self):
    #    self.assertIsInstance(protocols.QTCaptureView_Delegate, objc.informal_protocol)
