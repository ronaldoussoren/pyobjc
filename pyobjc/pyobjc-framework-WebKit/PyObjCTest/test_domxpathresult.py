
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMXPathResult (TestCase):
    def testConstants(self):
        self.failUnlessEqual(DOM_ANY_TYPE, 0)
        self.failUnlessEqual(DOM_NUMBER_TYPE, 1)
        self.failUnlessEqual(DOM_STRING_TYPE, 2)
        self.failUnlessEqual(DOM_BOOLEAN_TYPE, 3)
        self.failUnlessEqual(DOM_UNORDERED_NODE_ITERATOR_TYPE, 4)
        self.failUnlessEqual(DOM_ORDERED_NODE_ITERATOR_TYPE, 5)
        self.failUnlessEqual(DOM_UNORDERED_NODE_SNAPSHOT_TYPE, 6)
        self.failUnlessEqual(DOM_ORDERED_NODE_SNAPSHOT_TYPE, 7)
        self.failUnlessEqual(DOM_ANY_UNORDERED_NODE_TYPE, 8)
        self.failUnlessEqual(DOM_FIRST_ORDERED_NODE_TYPE, 9)

    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMXPathResult.booleanValue)
        self.failUnlessResultIsBOOL(DOMXPathResult.invalidIteratorState)

if __name__ == "__main__":
    main()
