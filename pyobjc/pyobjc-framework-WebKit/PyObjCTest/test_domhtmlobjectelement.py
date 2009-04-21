
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLObjectElement (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMHTMLObjectElement.declare)
        self.failUnlessArgIsBOOL(DOMHTMLObjectElement.setDeclare_, 0)

if __name__ == "__main__":
    main()
