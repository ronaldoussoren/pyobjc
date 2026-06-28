import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSTextInputContext(TestCase):
    def test_constants(self):
        self.assertIsInstance(
            AppKit.NSTextInputContextKeyboardSelectionDidChangeNotification, str
        )

    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSTextInputContext.acceptsGlyphInfo)
        self.assertArgIsBOOL(AppKit.NSTextInputContext.setAcceptsGlyphInfo_, 0)
        self.assertResultIsBOOL(AppKit.NSTextInputContext.handleEvent_)
