
from PyObjCTools.TestSupport import *
from XgridFoundation import *

class TestXGConnection (TestCase):
    def testConstants(self):
        self.failUnlessEqual(XGConnectionStateClosed, 0)
        self.failUnlessEqual(XGConnectionStateOpening, 1)
        self.failUnlessEqual(XGConnectionStateOpen, 2)
        self.failUnlessEqual(XGConnectionStateClosing, 3)

        self.failUnlessIsInstance(XGConnectionKeyIsOpened, unicode)
        self.failUnlessIsInstance(XGConnectionKeyIsClosed, unicode)
        self.failUnlessIsInstance(XGConnectionKeyState, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(XGConnection.isOpened)
        self.failUnlessResultIsBOOL(XGConnection.isClosed)

    def testProtocols(self):
        self.failUnlessIsInstance(protocols.XGConnectionDelegate, objc.informal_protocol)

if __name__ == "__main__":
    main()
