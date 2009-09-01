
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMEvent (TestCase):

    def testConstants(self):
        self.failUnlessEqual(DOM_CAPTURING_PHASE, 1)
        self.failUnlessEqual(DOM_AT_TARGET, 2)
        self.failUnlessEqual(DOM_BUBBLING_PHASE, 3)

    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMEvent.bubbles)
        self.failUnlessResultIsBOOL(DOMEvent.cancelable)
        self.failUnlessArgIsBOOL(DOMEvent.initEvent_canBubbleArg_cancelableArg_, 1)
        self.failUnlessArgIsBOOL(DOMEvent.initEvent_canBubbleArg_cancelableArg_, 2)
        self.failUnlessArgIsBOOL(DOMEvent.initEvent___, 1)
        self.failUnlessArgIsBOOL(DOMEvent.initEvent___, 2)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultIsBOOL(DOMEvent.returnValue)
        self.failUnlessArgIsBOOL(DOMEvent.setReturnValue_, 0)
        self.failUnlessResultIsBOOL(DOMEvent.cancelBubble)
        self.failUnlessArgIsBOOL(DOMEvent.setCancelBubble_, 0)

    

if __name__ == "__main__":
    main()
