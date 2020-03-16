from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestDOMKeyboardEvent(TestCase):
    def testConstants(self):
        self.assertEqual(WebKit.DOM_KEY_LOCATION_STANDARD, 0)
        self.assertEqual(WebKit.DOM_KEY_LOCATION_LEFT, 1)
        self.assertEqual(WebKit.DOM_KEY_LOCATION_RIGHT, 2)
        self.assertEqual(WebKit.DOM_KEY_LOCATION_NUMPAD, 3)

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertResultIsBOOL(WebKit.DOMKeyboardEvent.altGraphKey)

    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMKeyboardEvent.ctrlKey)
        self.assertResultIsBOOL(WebKit.DOMKeyboardEvent.shiftKey)
        self.assertResultIsBOOL(WebKit.DOMKeyboardEvent.altKey)
        self.assertResultIsBOOL(WebKit.DOMKeyboardEvent.metaKey)
        self.assertResultIsBOOL(WebKit.DOMKeyboardEvent.getModifierState_)

        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_,  # noqa: B950
            1,
        )
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_,  # noqa: B950
            2,
        )
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_,  # noqa: B950
            6,
        )
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_,  # noqa: B950
            7,
        )
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_,  # noqa: B950
            8,
        )
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_,  # noqa: B950
            9,
        )
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_,  # noqa: B950
            10,
        )
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_,  # noqa: B950
            1,
        )
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_,  # noqa: B950
            2,
        )
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_,  # noqa: B950
            6,
        )
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_,  # noqa: B950
            7,
        )
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_,  # noqa: B950
            8,
        )
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_keyLocation_ctrlKey_altKey_shiftKey_metaKey_,  # noqa: B950
            9,
        )

    @min_os_level("10.10")
    def test_methods10_10(self):
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_location_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_,  # noqa: B950
            1,
        )
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_location_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_,  # noqa: B950
            2,
        )
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_location_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_,  # noqa: B950
            6,
        )
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_location_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_,  # noqa: B950
            7,
        )
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_location_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_,  # noqa: B950
            8,
        )
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_location_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_,  # noqa: B950
            9,
        )
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_location_ctrlKey_altKey_shiftKey_metaKey_altGraphKey_,  # noqa: B950
            10,
        )
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_location_ctrlKey_altKey_shiftKey_metaKey_,  # noqa: B950
            1,
        )
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_location_ctrlKey_altKey_shiftKey_metaKey_,  # noqa: B950
            2,
        )
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_location_ctrlKey_altKey_shiftKey_metaKey_,  # noqa: B950
            6,
        )
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_location_ctrlKey_altKey_shiftKey_metaKey_,  # noqa: B950
            7,
        )
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_location_ctrlKey_altKey_shiftKey_metaKey_,  # noqa: B950
            8,
        )
        self.assertArgIsBOOL(
            WebKit.DOMKeyboardEvent.initKeyboardEvent_canBubble_cancelable_view_keyIdentifier_location_ctrlKey_altKey_shiftKey_metaKey_,  # noqa: B950
            9,
        )
