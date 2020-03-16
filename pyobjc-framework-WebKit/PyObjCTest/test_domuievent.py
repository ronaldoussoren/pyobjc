from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMUIEvent(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(
            WebKit.DOMUIEvent.initUIEvent_canBubble_cancelable_view_detail_, 1
        )
        self.assertArgIsBOOL(
            WebKit.DOMUIEvent.initUIEvent_canBubble_cancelable_view_detail_, 2
        )
        self.assertArgIsBOOL(WebKit.DOMUIEvent.initUIEvent_____, 1)
        self.assertArgIsBOOL(WebKit.DOMUIEvent.initUIEvent_____, 2)
