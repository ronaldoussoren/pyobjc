import AppKit
import objc
from PyObjCTools.TestSupport import TestCase


class TestNSInputManagerHelper(AppKit.NSObject):
    def doCommandBySelector_(self, s):
        pass

    def setMarkedText_selectedRange_(self, s, r):
        pass

    def hasMarkedText(self):
        return 1

    def conversationIdentifier(self):
        return 1

    def markedRange(self):
        return 1

    def selectedRange(self):
        return 1

    def firstRectForCharacterRange_(self, r):
        return 1

    def characterIndexForPoint_(self, r):
        return 1


class TestNSInputManager(TestCase):
    def testProtocols(self):
        objc.protocolNamed("NSTextInput")
        self.assertArgIsSEL(TestNSInputManagerHelper.doCommandBySelector_, 0, b"v@:@")
        self.assertArgHasType(
            TestNSInputManagerHelper.setMarkedText_selectedRange_,
            1,
            AppKit.NSRange.__typestr__,
        )
        self.assertResultIsBOOL(TestNSInputManagerHelper.hasMarkedText)
        self.assertResultHasType(
            TestNSInputManagerHelper.markedRange, AppKit.NSRange.__typestr__
        )
        self.assertResultHasType(
            TestNSInputManagerHelper.selectedRange, AppKit.NSRange.__typestr__
        )
        self.assertResultHasType(
            TestNSInputManagerHelper.firstRectForCharacterRange_,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSInputManagerHelper.firstRectForCharacterRange_,
            0,
            AppKit.NSRange.__typestr__,
        )
        self.assertResultHasType(
            TestNSInputManagerHelper.characterIndexForPoint_, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestNSInputManagerHelper.characterIndexForPoint_,
            0,
            AppKit.NSPoint.__typestr__,
        )

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSInputManager.wantsToInterpretAllKeystrokes)
        self.assertResultIsBOOL(AppKit.NSInputManager.wantsToHandleMouseEvents)
        self.assertResultIsBOOL(AppKit.NSInputManager.handleMouseEvent_)
        self.assertResultIsBOOL(
            AppKit.NSInputManager.wantsToDelayTextChangeNotifications
        )
