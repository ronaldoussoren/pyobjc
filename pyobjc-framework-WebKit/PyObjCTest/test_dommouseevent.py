
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMMouseEvent (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DOMMouseEvent.ctrlKey)
        self.assertResultIsBOOL(DOMMouseEvent.shiftKey)
        self.assertResultIsBOOL(DOMMouseEvent.altKey)
        self.assertResultIsBOOL(DOMMouseEvent.metaKey)

        self.assertArgIsBOOL(DOMMouseEvent.initMouseEvent_canBubble_cancelable_view_detail_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_button_relatedTarget_, 1)
        self.assertArgIsBOOL(DOMMouseEvent.initMouseEvent_canBubble_cancelable_view_detail_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_button_relatedTarget_, 2)
        self.assertArgIsBOOL(DOMMouseEvent.initMouseEvent_canBubble_cancelable_view_detail_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_button_relatedTarget_, 9)
        self.assertArgIsBOOL(DOMMouseEvent.initMouseEvent_canBubble_cancelable_view_detail_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_button_relatedTarget_, 10)
        self.assertArgIsBOOL(DOMMouseEvent.initMouseEvent_canBubble_cancelable_view_detail_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_button_relatedTarget_, 11)
        self.assertArgIsBOOL(DOMMouseEvent.initMouseEvent_canBubble_cancelable_view_detail_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_button_relatedTarget_, 12)

if __name__ == "__main__":
    main()
