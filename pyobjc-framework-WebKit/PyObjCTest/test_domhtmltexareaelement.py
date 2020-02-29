from PyObjCTools.TestSupport import *
from WebKit import *


class TestDOMHTMLTextAreaElement(TestCase):
    def testMehods(self):
        self.assertResultIsBOOL(DOMHTMLTextAreaElement.willValidate)


if __name__ == "__main__":
    main()
