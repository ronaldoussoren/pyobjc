
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMEvent (TestCase):

    def testConstants(self):
        self.assertEqual(DOM_CAPTURING_PHASE, 1)
        self.assertEqual(DOM_AT_TARGET, 2)
        self.assertEqual(DOM_BUBBLING_PHASE, 3)

    def testMethods(self):
        self.assertResultIsBOOL(DOMEvent.bubbles)
        self.assertResultIsBOOL(DOMEvent.cancelable)
        self.assertArgIsBOOL(DOMEvent.initEvent_canBubbleArg_cancelableArg_, 1)
        self.assertArgIsBOOL(DOMEvent.initEvent_canBubbleArg_cancelableArg_, 2)
        self.assertArgIsBOOL(DOMEvent.initEvent___, 1)
        self.assertArgIsBOOL(DOMEvent.initEvent___, 2)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(DOMEvent.returnValue)
        self.assertArgIsBOOL(DOMEvent.setReturnValue_, 0)
        self.assertResultIsBOOL(DOMEvent.cancelBubble)
        self.assertArgIsBOOL(DOMEvent.setCancelBubble_, 0)



if __name__ == "__main__":
    main()
