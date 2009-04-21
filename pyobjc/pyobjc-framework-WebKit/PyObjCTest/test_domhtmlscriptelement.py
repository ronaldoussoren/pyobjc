
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLScriptElement (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMHTMLScriptElement.defer)
        self.failUnlessArgIsBOOL(DOMHTMLScriptElement.setDefer_, 0)

if __name__ == "__main__":
    main()
