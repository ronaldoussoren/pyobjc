from AppKit import *
from PyObjCTools.TestSupport import *


class TestNSInputManagerHelper (NSObject):
    def doCommandBySelector_(self, s): pass
    def setMarkedText_selectedRange_(self, s, r): pass
    def hasMarkedText(self): return 1
    def conversationIdentifier(self): return 1
    def markedRange(self): return 1
    def selectedRange(self): return 1
    def firstRectForCharacterRange_(self, r): return 1
    def characterIndexForPoint_(self, r): return 1

class TestNSInputManager (TestCase):
    def testProtocols(self):
        self.assertArgIsSEL(TestNSInputManagerHelper.doCommandBySelector_, 0, b'v@:@')
        self.assertArgHasType(TestNSInputManagerHelper.setMarkedText_selectedRange_, 1, NSRange.__typestr__)
        self.assertResultIsBOOL(TestNSInputManagerHelper.hasMarkedText)
        self.assertResultHasType(TestNSInputManagerHelper.markedRange, NSRange.__typestr__)
        self.assertResultHasType(TestNSInputManagerHelper.selectedRange, NSRange.__typestr__)
        self.assertResultHasType(TestNSInputManagerHelper.firstRectForCharacterRange_, NSRect.__typestr__)
        self.assertArgHasType(TestNSInputManagerHelper.firstRectForCharacterRange_, 0, NSRange.__typestr__)
        self.assertResultHasType(TestNSInputManagerHelper.characterIndexForPoint_, objc._C_NSUInteger)
        self.assertArgHasType(TestNSInputManagerHelper.characterIndexForPoint_, 0, NSPoint.__typestr__)

    def testMethods(self):
        self.assertResultIsBOOL(NSInputManager.wantsToInterpretAllKeystrokes)
        self.assertResultIsBOOL(NSInputManager.wantsToHandleMouseEvents)
        self.assertResultIsBOOL(NSInputManager.handleMouseEvent_)
        self.assertResultIsBOOL(NSInputManager.wantsToDelayTextChangeNotifications)


if __name__ == "__main__":
    main()
