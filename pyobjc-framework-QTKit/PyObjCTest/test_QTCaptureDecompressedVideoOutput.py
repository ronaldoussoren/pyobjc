
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTCaptureDecompressedVideoOutput (TestCase):
    #def testInformalProtocols(self):
        #self.assertIsInstance(protocols.QTCaptureDecompressedVideoOutput_Delegate, objc.informal_protocol)
    pass
    def test_methods(self):
        self.assertResultIsBOOL(QTCaptureDecompressedVideoOutput.automaticallyDropsLateVideoFrames)
        self.assertArgIsBOOL(QTCaptureDecompressedVideoOutput.setAutomaticallyDropsLateVideoFrames_, 0)

if __name__ == "__main__":
    main()
