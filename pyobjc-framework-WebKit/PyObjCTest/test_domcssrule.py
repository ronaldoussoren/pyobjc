
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
        self.assertEqual(DOM_VARIABLES_RULE, 7) # Removed in 10.10(?)
        self.assertEqual(DOM_KEYFRAMES_RULE, 7)
        self.assertEqual(DOM_WEBKIT_KEYFRAMES_RULE, 7)
        self.assertEqual(DOM_WEBKIT_KEYFRAME_RULE, 8)
        self.assertEqual(DOM_KEYFRAME_RULE, 8)
        self.assertEqual(DOM_SUPPORTS_RULE, 12)
        self.assertEqual(DOM_WEBKIT_REGION_RULE, 16)

        self.assertEqual(DOM_NAMESPACE_RULE, 10)

if __name__ == "__main__":
    main()
