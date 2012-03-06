
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTCaptureView (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(QTCaptureView.preservesAspectRatio)

    def testProtocols(self):
        self.assertIsInstance(protocols.QTCaptureView_Delegate, objc.informal_protocol)

if __name__ == "__main__":
    main()
