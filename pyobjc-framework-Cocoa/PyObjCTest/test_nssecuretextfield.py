import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSecureTextFieldCell(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSSecureTextFieldCell.echosBullets)
        self.assertArgIsBOOL(AppKit.NSSecureTextFieldCell.setEchosBullets_, 0)
