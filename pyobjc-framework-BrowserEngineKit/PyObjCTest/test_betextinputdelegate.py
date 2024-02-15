import BrowserEngineKit
from PyObjCTools.TestSupport import TestCase


class TestBETextInputDelegateHelper(BrowserEngineKit.NSObject):
    def shouldDeferEventHandlingToSystemForTextInput_context_(self, a, b):
        return 1


class TestBETextInputDelegate(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("BETextInputDelegate")

    def test_protocol_methods(self):
        self.assertResultIsBOOL(
            TestBETextInputDelegateHelper.shouldDeferEventHandlingToSystemForTextInput_context_
        )
