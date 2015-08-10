
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTCaptureView (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(QTCaptureView.preservesAspectRatio)
        self.assertArgIsBOOL(QTCaptureView.setPreservesAspectRatio_, 0)

    #def testProtocols(self):
    #    self.assertIsInstance(protocols.QTCaptureView_Delegate, objc.informal_protocol)

if __name__ == "__main__":
    main()
