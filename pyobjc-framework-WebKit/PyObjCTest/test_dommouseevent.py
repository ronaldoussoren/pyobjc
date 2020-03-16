from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMMouseEvent(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMMouseEvent.ctrlKey)
        self.assertResultIsBOOL(WebKit.DOMMouseEvent.shiftKey)
        self.assertResultIsBOOL(WebKit.DOMMouseEvent.altKey)
        self.assertResultIsBOOL(WebKit.DOMMouseEvent.metaKey)

        self.assertArgIsBOOL(
            WebKit.DOMMouseEvent.initMouseEvent_canBubble_cancelable_view_detail_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_button_relatedTarget_,  # noqa: B950
            1,
        )
        self.assertArgIsBOOL(
            WebKit.DOMMouseEvent.initMouseEvent_canBubble_cancelable_view_detail_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_button_relatedTarget_,  # noqa: B950
            2,
        )
        self.assertArgIsBOOL(
            WebKit.DOMMouseEvent.initMouseEvent_canBubble_cancelable_view_detail_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_button_relatedTarget_,  # noqa: B950
            9,
        )
        self.assertArgIsBOOL(
            WebKit.DOMMouseEvent.initMouseEvent_canBubble_cancelable_view_detail_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_button_relatedTarget_,  # noqa: B950
            10,
        )
        self.assertArgIsBOOL(
            WebKit.DOMMouseEvent.initMouseEvent_canBubble_cancelable_view_detail_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_button_relatedTarget_,  # noqa: B950
            11,
        )
        self.assertArgIsBOOL(
            WebKit.DOMMouseEvent.initMouseEvent_canBubble_cancelable_view_detail_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_button_relatedTarget_,  # noqa: B950
            12,
        )

        self.assertArgIsBOOL(WebKit.DOMMouseEvent.initMouseEvent_______________, 1)
        self.assertArgIsBOOL(WebKit.DOMMouseEvent.initMouseEvent_______________, 2)
        self.assertArgIsBOOL(WebKit.DOMMouseEvent.initMouseEvent_______________, 9)
        self.assertArgIsBOOL(WebKit.DOMMouseEvent.initMouseEvent_______________, 10)
        self.assertArgIsBOOL(WebKit.DOMMouseEvent.initMouseEvent_______________, 11)
        self.assertArgIsBOOL(WebKit.DOMMouseEvent.initMouseEvent_______________, 12)
