
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMKeyboardEvent (TestCase):
    def testConstants(self):
        self.failUnlessEqual(DOM_KEY_LOCATION_STANDARD, 0)
        self.failUnlessEqual(DOM_KEY_LOCATION_LEFT, 1)
        self.failUnlessEqual(DOM_KEY_LOCATION_RIGHT, 2)
        self.failUnlessEqual(DOM_KEY_LOCATION_NUMPAD, 3)

    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMKeyboardEvent.ctrlKey)
        self.failUnlessResultIsBOOL(DOMKeyboardEvent.shiftKey)
        self.failUnlessResultIsBOOL(DOMKeyboardEvent.altKey)
        self.failUnlessResultIsBOOL(DOMKeyboardEvent.metaKey)
        self.failUnlessResultIsBOOL(DOMKeyboardEvent.getModifierState_)
        self.failUnlessResultIsBOOL(DOMKeyboardEvent.altGraphKey)

        self.failUnlessArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_, 1)
        self.failUnlessArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_, 2)
        self.failUnlessArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_, 6)
        self.failUnlessArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_, 7)
        self.failUnlessArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_, 8)
        self.failUnlessArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_, 9)
        self.failUnlessArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_, 10)
        self.failUnlessArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_, 1)
        self.failUnlessArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_, 2)
        self.failUnlessArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_, 6)
        self.failUnlessArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_, 7)
        self.failUnlessArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_, 8)
        self.failUnlessArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_, 9)



if __name__ == "__main__":
    main()
