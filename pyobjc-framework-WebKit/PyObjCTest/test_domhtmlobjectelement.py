
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLObjectElement (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DOMHTMLObjectElement.declare)
        self.assertArgIsBOOL(DOMHTMLObjectElement.setDeclare_, 0)

if __name__ == "__main__":
    main()
