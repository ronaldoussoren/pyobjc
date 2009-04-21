
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMXPathException (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(DOMXPathException, unicode)

        self.failUnlessEqual(DOM_INVALID_EXPRESSION_ERR, 51)
        self.failUnlessEqual(DOM_TYPE_ERR, 52)


if __name__ == "__main__":
    main()
