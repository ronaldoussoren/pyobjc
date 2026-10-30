import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSecureTextFieldCell(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSSecureTextFieldCell.echosBullets)
        self.assertArgIsBOOL(AppKit.NSSecureTextFieldCell.setEchosBullets_, 0)
