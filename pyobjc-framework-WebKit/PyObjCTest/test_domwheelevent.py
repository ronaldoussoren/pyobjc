from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMWheelEvent(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMWheelEvent.ctrlKey)
        self.assertResultIsBOOL(WebKit.DOMWheelEvent.shiftKey)
        self.assertResultIsBOOL(WebKit.DOMWheelEvent.altKey)
        self.assertResultIsBOOL(WebKit.DOMWheelEvent.metaKey)
        self.assertResultIsBOOL(WebKit.DOMWheelEvent.isHorizontal)

        self.assertArgIsBOOL(
            WebKit.DOMWheelEvent.initWheelEvent_wheelDeltaY_view_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_,  # noqa: B950
            7,
        )
        self.assertArgIsBOOL(
            WebKit.DOMWheelEvent.initWheelEvent_wheelDeltaY_view_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_,  # noqa: B950
            8,
        )
        self.assertArgIsBOOL(
            WebKit.DOMWheelEvent.initWheelEvent_wheelDeltaY_view_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_,  # noqa: B950
            9,
        )
        self.assertArgIsBOOL(
            WebKit.DOMWheelEvent.initWheelEvent_wheelDeltaY_view_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_,  # noqa: B950
            10,
        )

    def testConstants(self):
        self.assertEqual(WebKit.DOM_DOM_DELTA_PIXEL, 0)
        self.assertEqual(WebKit.DOM_DOM_DELTA_LINE, 1)
        self.assertEqual(WebKit.DOM_DOM_DELTA_PAGE, 2)
