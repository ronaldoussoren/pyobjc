from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMStyleSheet(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMStyleSheet.disabled)
        self.assertArgIsBOOL(WebKit.DOMStyleSheet.setDisabled_, 0)
