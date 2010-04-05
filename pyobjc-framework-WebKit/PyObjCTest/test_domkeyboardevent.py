
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMKeyboardEvent (TestCase):
    def testConstants(self):
        self.assertEqual(DOM_KEY_LOCATION_STANDARD, 0)
        self.assertEqual(DOM_KEY_LOCATION_LEFT, 1)
        self.assertEqual(DOM_KEY_LOCATION_RIGHT, 2)
        self.assertEqual(DOM_KEY_LOCATION_NUMPAD, 3)

    def testMethods(self):
        self.assertResultIsBOOL(DOMKeyboardEvent.ctrlKey)
        self.assertResultIsBOOL(DOMKeyboardEvent.shiftKey)
        self.assertResultIsBOOL(DOMKeyboardEvent.altKey)
        self.assertResultIsBOOL(DOMKeyboardEvent.metaKey)
        self.assertResultIsBOOL(DOMKeyboardEvent.getModifierState_)
        self.assertResultIsBOOL(DOMKeyboardEvent.altGraphKey)

        self.assertArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_, 1)
        self.assertArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_, 2)
        self.assertArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_, 6)
        self.assertArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_, 7)
        self.assertArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_, 8)
        self.assertArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_, 9)
        self.assertArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_, 10)
        self.assertArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_, 1)
        self.assertArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_, 2)
        self.assertArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_, 6)
        self.assertArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_, 7)
        self.assertArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_, 8)
        self.assertArgIsBOOL(DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_, 9)



if __name__ == "__main__":
    main()
