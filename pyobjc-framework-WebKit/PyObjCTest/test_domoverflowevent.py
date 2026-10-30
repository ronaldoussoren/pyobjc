from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMOverflowEvent(TestCase):
    def test_constants(self):
        self.assertEqual(WebKit.DOM_HORIZONTAL, 0)
        self.assertEqual(WebKit.DOM_VERTICAL, 1)
        self.assertEqual(WebKit.DOM_BOTH, 2)

    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMOverflowEvent.horizontalOverflow)
        self.assertResultIsBOOL(WebKit.DOMOverflowEvent.verticalOverflow)

        self.assertArgIsBOOL(
            WebKit.DOMOverflowEvent.initOverflowEvent_horizontalOverflow_verticalOverflow_,
            1,
        )
        self.assertArgIsBOOL(
            WebKit.DOMOverflowEvent.initOverflowEvent_horizontalOverflow_verticalOverflow_,
            2,
        )
