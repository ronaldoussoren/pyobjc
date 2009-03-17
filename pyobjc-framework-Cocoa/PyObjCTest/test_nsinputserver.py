from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSInputServerHelper (NSObject):
    def doCommandBySelector_client_(self, sel, sender): pass
    def markedTextSelectionChanged_client_(self, sel, sender): pass
    def canBeDisabled(self): return 1
    def wantsToInterpretAllKeystrokes(self): return 1
    def wantsToHandleMouseEvents(self): return 1
    def wantsToDelayTextChangeNotifications(self): return 1
    def activeConversationWillChange_fromOldConversation_(self, s, o): pass
    def activeConversationChanged_toNewConversation_(self, s, n): pass

    def mouseDownOnCharacterIndex_atCoordinate_withModifier_client_(self, i, p, f, s): return 1
    def mouseDraggedOnCharacterIndex_atCoordinate_withModifier_client_(self, i, p, f, s): return 1
    def mouseUpOnCharacterIndex_atCoordinate_withModifier_client_(self, i, p, f, s): pass

class TestNSInputServer (TestCase):
    def testProtocols(self):
        self.failUnlessArgIsSEL(TestNSInputServerHelper.doCommandBySelector_client_, 0, 'v@:@')
        self.failUnlessArgHasType(TestNSInputServerHelper.markedTextSelectionChanged_client_, 0, NSRange.__typestr__)
        self.failUnlessResultIsBOOL(TestNSInputServerHelper.canBeDisabled)
        self.failUnlessResultIsBOOL(TestNSInputServerHelper.wantsToInterpretAllKeystrokes)
        self.failUnlessResultIsBOOL(TestNSInputServerHelper.wantsToHandleMouseEvents)
        self.failUnlessArgHasType(TestNSInputServerHelper.activeConversationWillChange_fromOldConversation_, 1, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSInputServerHelper.activeConversationChanged_toNewConversation_, 1, objc._C_NSInteger)

        self.failUnlessResultIsBOOL(TestNSInputServerHelper.mouseDownOnCharacterIndex_atCoordinate_withModifier_client_)
        self.failUnlessArgHasType(TestNSInputServerHelper.mouseDownOnCharacterIndex_atCoordinate_withModifier_client_, 0, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestNSInputServerHelper.mouseDownOnCharacterIndex_atCoordinate_withModifier_client_, 1, NSPoint.__typestr__)
        self.failUnlessArgHasType(TestNSInputServerHelper.mouseDownOnCharacterIndex_atCoordinate_withModifier_client_, 2, objc._C_NSUInteger)

        self.failUnlessResultIsBOOL(TestNSInputServerHelper.mouseDraggedOnCharacterIndex_atCoordinate_withModifier_client_)
        self.failUnlessArgHasType(TestNSInputServerHelper.mouseDraggedOnCharacterIndex_atCoordinate_withModifier_client_, 0, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestNSInputServerHelper.mouseDownOnCharacterIndex_atCoordinate_withModifier_client_, 1, NSPoint.__typestr__)
        self.failUnlessArgHasType(TestNSInputServerHelper.mouseDownOnCharacterIndex_atCoordinate_withModifier_client_, 2, objc._C_NSUInteger)

        self.failUnlessResultHasType(TestNSInputServerHelper.mouseUpOnCharacterIndex_atCoordinate_withModifier_client_, 'v')
        self.failUnlessArgHasType(TestNSInputServerHelper.mouseUpOnCharacterIndex_atCoordinate_withModifier_client_, 0, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestNSInputServerHelper.mouseUpOnCharacterIndex_atCoordinate_withModifier_client_, 1, NSPoint.__typestr__)
        self.failUnlessArgHasType(TestNSInputServerHelper.mouseUpOnCharacterIndex_atCoordinate_withModifier_client_, 2, objc._C_NSUInteger)



if __name__ == "__main__":
    main()
