from WebKit import *
from PyObjCTools.TestSupport import *


class TestDOMHTMLTextAreaElement (TestCase):
    def testMehods(self):
        self.assertResultIsBOOL(DOMHTMLTextAreaElement.willValidate)

if __name__ == "__main__":
    main()
