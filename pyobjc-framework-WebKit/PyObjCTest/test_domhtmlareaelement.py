from PyObjCTools.TestSupport import *
from WebKit import *


class TestDOMHTMLAreaElement(TestCase):
    def testMehods(self):
        self.assertResultIsBOOL(DOMHTMLAreaElement.noHref)
        self.assertArgIsBOOL(DOMHTMLAreaElement.setNoHref_, 0)


if __name__ == "__main__":
    main()
