
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMUIEvent (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(DOMUIEvent.initUIEvent_canBubble_cancelable_view_detail_, 1)
        self.failUnlessArgIsBOOL(DOMUIEvent.initUIEvent_canBubble_cancelable_view_detail_, 2)
        self.failUnlessArgIsBOOL(DOMUIEvent.initUIEvent_____, 1)
        self.failUnlessArgIsBOOL(DOMUIEvent.initUIEvent_____, 2)

if __name__ == "__main__":
    main()
