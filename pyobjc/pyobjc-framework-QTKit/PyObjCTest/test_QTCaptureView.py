
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTCaptureView (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(QTCaptureView.preservesAspectRatio)

    def testProtocols(self):
        self.failUnlessIsInstance(protocols.QTCaptureViewDelegate, objc.informal_protocol)

if __name__ == "__main__":
    main()
