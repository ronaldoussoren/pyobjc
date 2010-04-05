
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMUIEvent (TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(DOMUIEvent.initUIEvent_canBubble_cancelable_view_detail_, 1)
        self.assertArgIsBOOL(DOMUIEvent.initUIEvent_canBubble_cancelable_view_detail_, 2)
        self.assertArgIsBOOL(DOMUIEvent.initUIEvent_____, 1)
        self.assertArgIsBOOL(DOMUIEvent.initUIEvent_____, 2)

if __name__ == "__main__":
    main()
