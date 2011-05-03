
from PyObjCTools.TestSupport import *
from XgridFoundation import *

class TestXGConnection (TestCase):
    def testConstants(self):
        self.assertEqual(XGConnectionStateClosed, 0)
        self.assertEqual(XGConnectionStateOpening, 1)
        self.assertEqual(XGConnectionStateOpen, 2)
        self.assertEqual(XGConnectionStateClosing, 3)

        self.assertIsInstance(XGConnectionKeyIsOpened, unicode)
        self.assertIsInstance(XGConnectionKeyIsClosed, unicode)
        self.assertIsInstance(XGConnectionKeyState, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(XGConnection.isOpened)
        self.assertResultIsBOOL(XGConnection.isClosed)

    def testProtocols(self):
        self.assertIsInstance(protocols.XGConnectionDelegate, objc.informal_protocol)

if __name__ == "__main__":
    main()
