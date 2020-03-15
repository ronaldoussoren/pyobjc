import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSTextInputContext(TestCase):
    @min_os_level("10.6")
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSTextInputContext.acceptsGlyphInfo)
        self.assertArgIsBOOL(AppKit.NSTextInputContext.setAcceptsGlyphInfo_, 0)
        self.assertResultIsBOOL(AppKit.NSTextInputContext.handleEvent_)

    @min_os_level("10.6")
    def testConstants(self):
        self.assertIsInstance(
            AppKit.NSTextInputContextKeyboardSelectionDidChangeNotification, str
        )
