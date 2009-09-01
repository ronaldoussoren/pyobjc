
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

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessEqual(DOM_VARIABLES_RULE, 7)
        self.failUnlessEqual(DOM_WEBKIT_KEYFRAMES_RULE, 8)
        self.failUnlessEqual(DOM_WEBKIT_KEYFRAME_RULE, 9)



if __name__ == "__main__":
    main()
