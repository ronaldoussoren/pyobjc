from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMRange(TestCase):
    def testConstants(self):
        self.assertEqual(WebKit.DOM_START_TO_START, 0)
        self.assertEqual(WebKit.DOM_START_TO_END, 1)
        self.assertEqual(WebKit.DOM_END_TO_END, 2)
        self.assertEqual(WebKit.DOM_END_TO_START, 3)
        self.assertEqual(WebKit.DOM_NODE_BEFORE, 0)
        self.assertEqual(WebKit.DOM_NODE_AFTER, 1)
        self.assertEqual(WebKit.DOM_NODE_BEFORE_AND_AFTER, 2)
        self.assertEqual(WebKit.DOM_NODE_INSIDE, 3)

    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMRange.collapsed)
        self.assertArgIsBOOL(WebKit.DOMRange.collapse_, 0)

        self.assertResultIsBOOL(WebKit.DOMRange.intersectsNode_)
        self.assertResultIsBOOL(WebKit.DOMRange.isPointInRange_offset_)
