
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMHTMLElement (TestCase):
    def testMehods(self):
        self.assertResultIsBOOL(DOMHTMLElement.isContentEditable)

if __name__ == "__main__":
    main()
