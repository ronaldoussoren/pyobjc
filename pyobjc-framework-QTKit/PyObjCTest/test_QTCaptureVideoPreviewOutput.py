
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTCaptureVideoPreviewOutput (TestCase):
    def testProtocols(self):
        self.failUnlessIsInstance(protocols.QTCaptureVideoPreviewOutput, objc.informal_protocol)

if __name__ == "__main__":
    main()
