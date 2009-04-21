
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMMouseEvent (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMMouseEvent.ctrlKey)
        self.failUnlessResultIsBOOL(DOMMouseEvent.shiftKey)
        self.failUnlessResultIsBOOL(DOMMouseEvent.altKey)
        self.failUnlessResultIsBOOL(DOMMouseEvent.metaKey)

        self.failUnlessArgIsBOOL(DOMMouseEvent.initMouseEvent_canBubble_cancelable_view_detail_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_button_relatedTarget_, 1)
        self.failUnlessArgIsBOOL(DOMMouseEvent.initMouseEvent_canBubble_cancelable_view_detail_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_button_relatedTarget_, 2)
        self.failUnlessArgIsBOOL(DOMMouseEvent.initMouseEvent_canBubble_cancelable_view_detail_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_button_relatedTarget_, 9)
        self.failUnlessArgIsBOOL(DOMMouseEvent.initMouseEvent_canBubble_cancelable_view_detail_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_button_relatedTarget_, 10)
        self.failUnlessArgIsBOOL(DOMMouseEvent.initMouseEvent_canBubble_cancelable_view_detail_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_button_relatedTarget_, 11)
        self.failUnlessArgIsBOOL(DOMMouseEvent.initMouseEvent_canBubble_cancelable_view_detail_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_button_relatedTarget_, 12)

if __name__ == "__main__":
    main()
