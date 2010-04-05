
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLScriptElement (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DOMHTMLScriptElement.defer)
        self.assertArgIsBOOL(DOMHTMLScriptElement.setDefer_, 0)

if __name__ == "__main__":
    main()
