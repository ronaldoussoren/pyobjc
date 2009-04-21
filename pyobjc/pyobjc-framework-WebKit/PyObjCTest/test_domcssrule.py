
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMCSSRule (TestCase):
    def testConstants(self):
        self.failUnlessEqual(DOM_UNKNOWN_RULE, 0)
        self.failUnlessEqual(DOM_STYLE_RULE, 1)
        self.failUnlessEqual(DOM_CHARSET_RULE, 2)
        self.failUnlessEqual(DOM_IMPORT_RULE, 3)
        self.failUnlessEqual(DOM_MEDIA_RULE, 4)
        self.failUnlessEqual(DOM_FONT_FACE_RULE, 5)
        self.failUnlessEqual(DOM_PAGE_RULE, 6)


if __name__ == "__main__":
    main()
