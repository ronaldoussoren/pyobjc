
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMWheelEvent (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DOMWheelEvent.ctrlKey)
        self.assertResultIsBOOL(DOMWheelEvent.shiftKey)
        self.assertResultIsBOOL(DOMWheelEvent.altKey)
        self.assertResultIsBOOL(DOMWheelEvent.metaKey)
        self.assertResultIsBOOL(DOMWheelEvent.isHorizontal)

        self.assertArgIsBOOL(DOMWheelEvent.initWheelEvent_wheelDeltaY_view_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_, 7)
        self.assertArgIsBOOL(DOMWheelEvent.initWheelEvent_wheelDeltaY_view_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_, 8)
        self.assertArgIsBOOL(DOMWheelEvent.initWheelEvent_wheelDeltaY_view_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_, 9)
        self.assertArgIsBOOL(DOMWheelEvent.initWheelEvent_wheelDeltaY_view_screenX_screenY_clientX_clientY_ctrlKey_altKey_shiftKey_metaKey_, 10)

    def testConstants(self):
        self.assertEqual(DOM_DOM_DELTA_PIXEL, 0)
        self.assertEqual(DOM_DOM_DELTA_LINE, 1)
        self.assertEqual(DOM_DOM_DELTA_PAGE, 2)

if __name__ == "__main__":
    main()
