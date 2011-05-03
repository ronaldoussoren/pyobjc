
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMXPathResult (TestCase):
    def testConstants(self):
        self.assertEqual(DOM_ANY_TYPE, 0)
        self.assertEqual(DOM_NUMBER_TYPE, 1)
        self.assertEqual(DOM_STRING_TYPE, 2)
        self.assertEqual(DOM_BOOLEAN_TYPE, 3)
        self.assertEqual(DOM_UNORDERED_NODE_ITERATOR_TYPE, 4)
        self.assertEqual(DOM_ORDERED_NODE_ITERATOR_TYPE, 5)
        self.assertEqual(DOM_UNORDERED_NODE_SNAPSHOT_TYPE, 6)
        self.assertEqual(DOM_ORDERED_NODE_SNAPSHOT_TYPE, 7)
        self.assertEqual(DOM_ANY_UNORDERED_NODE_TYPE, 8)
        self.assertEqual(DOM_FIRST_ORDERED_NODE_TYPE, 9)

    def testMethods(self):
        self.assertResultIsBOOL(DOMXPathResult.booleanValue)
        self.assertResultIsBOOL(DOMXPathResult.invalidIteratorState)

if __name__ == "__main__":
    main()
