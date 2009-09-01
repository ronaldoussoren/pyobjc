from PyObjCTools.TestSupport import *

from WebKit import *

class TestDOMCSSStyleDeclaration (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMCSSStyleDeclaration.isPropertyImplicit_)


if __name__ == "__main__":
    main()
