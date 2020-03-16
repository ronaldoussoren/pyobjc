from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMXPathResult(TestCase):
    def testConstants(self):
        self.assertEqual(WebKit.DOM_ANY_TYPE, 0)
        self.assertEqual(WebKit.DOM_NUMBER_TYPE, 1)
        self.assertEqual(WebKit.DOM_STRING_TYPE, 2)
        self.assertEqual(WebKit.DOM_BOOLEAN_TYPE, 3)
        self.assertEqual(WebKit.DOM_UNORDERED_NODE_ITERATOR_TYPE, 4)
        self.assertEqual(WebKit.DOM_ORDERED_NODE_ITERATOR_TYPE, 5)
        self.assertEqual(WebKit.DOM_UNORDERED_NODE_SNAPSHOT_TYPE, 6)
        self.assertEqual(WebKit.DOM_ORDERED_NODE_SNAPSHOT_TYPE, 7)
        self.assertEqual(WebKit.DOM_ANY_UNORDERED_NODE_TYPE, 8)
        self.assertEqual(WebKit.DOM_FIRST_ORDERED_NODE_TYPE, 9)

    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMXPathResult.booleanValue)
        self.assertResultIsBOOL(WebKit.DOMXPathResult.invalidIteratorState)
