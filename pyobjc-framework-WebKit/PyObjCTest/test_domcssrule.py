
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMCSSRule (TestCase):
    def testConstants(self):
        self.assertEqual(DOM_UNKNOWN_RULE, 0)
        self.assertEqual(DOM_STYLE_RULE, 1)
        self.assertEqual(DOM_CHARSET_RULE, 2)
        self.assertEqual(DOM_IMPORT_RULE, 3)
        self.assertEqual(DOM_MEDIA_RULE, 4)
        self.assertEqual(DOM_FONT_FACE_RULE, 5)
        self.assertEqual(DOM_PAGE_RULE, 6)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(DOM_VARIABLES_RULE, 7)
        self.assertEqual(DOM_WEBKIT_KEYFRAMES_RULE, 7)
        self.assertEqual(DOM_WEBKIT_KEYFRAME_RULE, 8)



if __name__ == "__main__":
    main()
