from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestDOMEvent(TestCase):
    def testConstants(self):
        self.assertEqual(WebKit.DOM_NONE, 0)
        self.assertEqual(WebKit.DOM_CAPTURING_PHASE, 1)
        self.assertEqual(WebKit.DOM_AT_TARGET, 2)
        self.assertEqual(WebKit.DOM_BUBBLING_PHASE, 3)

    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMEvent.bubbles)
        self.assertResultIsBOOL(WebKit.DOMEvent.cancelable)
        self.assertArgIsBOOL(WebKit.DOMEvent.initEvent_canBubbleArg_cancelableArg_, 1)
        self.assertArgIsBOOL(WebKit.DOMEvent.initEvent_canBubbleArg_cancelableArg_, 2)
        self.assertArgIsBOOL(WebKit.DOMEvent.initEvent___, 1)
        self.assertArgIsBOOL(WebKit.DOMEvent.initEvent___, 2)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(WebKit.DOMEvent.returnValue)
        self.assertArgIsBOOL(WebKit.DOMEvent.setReturnValue_, 0)
        self.assertResultIsBOOL(WebKit.DOMEvent.cancelBubble)
        self.assertArgIsBOOL(WebKit.DOMEvent.setCancelBubble_, 0)
