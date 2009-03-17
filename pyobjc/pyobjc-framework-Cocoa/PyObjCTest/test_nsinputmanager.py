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
        self.failUnlessArgIsSEL(TestNSInputManagerHelper.doCommandBySelector_, 0, 'v@:@')
        self.failUnlessArgHasType(TestNSInputManagerHelper.setMarkedText_selectedRange_, 1, NSRange.__typestr__)
        self.failUnlessResultIsBOOL(TestNSInputManagerHelper.hasMarkedText)
        self.failUnlessResultHasType(TestNSInputManagerHelper.markedRange, NSRange.__typestr__)
        self.failUnlessResultHasType(TestNSInputManagerHelper.selectedRange, NSRange.__typestr__)
        self.failUnlessResultHasType(TestNSInputManagerHelper.firstRectForCharacterRange_, NSRect.__typestr__)
        self.failUnlessArgHasType(TestNSInputManagerHelper.firstRectForCharacterRange_, 0, NSRange.__typestr__)
        self.failUnlessResultHasType(TestNSInputManagerHelper.characterIndexForPoint_, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestNSInputManagerHelper.characterIndexForPoint_, 0, NSPoint.__typestr__)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSInputManager.wantsToInterpretAllKeystrokes)
        self.failUnlessResultIsBOOL(NSInputManager.wantsToHandleMouseEvents)
        self.failUnlessResultIsBOOL(NSInputManager.handleMouseEvent_)
        self.failUnlessResultIsBOOL(NSInputManager.wantsToDelayTextChangeNotifications)


if __name__ == "__main__":
    main()
