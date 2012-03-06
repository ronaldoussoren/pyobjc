
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTCaptureDecompressedVideoOutput (TestCase):
    def testInformalProtocols(self):
        self.assertIsInstance(protocols.QTCaptureDecompressedVideoOutput_Delegate, objc.informal_protocol)

if __name__ == "__main__":
    main()
