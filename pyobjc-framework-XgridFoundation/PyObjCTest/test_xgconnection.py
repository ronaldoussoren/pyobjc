from PyObjCTools.TestSupport import TestCase
import XgridFoundation


class TestXGConnection(TestCase):
    def testConstants(self):
        self.assertEqual(XgridFoundation.XGConnectionStateClosed, 0)
        self.assertEqual(XgridFoundation.XGConnectionStateOpening, 1)
        self.assertEqual(XgridFoundation.XGConnectionStateOpen, 2)
        self.assertEqual(XgridFoundation.XGConnectionStateClosing, 3)

        self.assertIsInstance(XgridFoundation.XGConnectionKeyIsOpened, str)
        self.assertIsInstance(XgridFoundation.XGConnectionKeyIsClosed, str)
        self.assertIsInstance(XgridFoundation.XGConnectionKeyState, str)

    def testMethods(self):
        self.assertResultIsBOOL(XgridFoundation.XGConnection.isOpened)
        self.assertResultIsBOOL(XgridFoundation.XGConnection.isClosed)
