from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMCSSRule(TestCase):
    def testConstants(self):
        self.assertEqual(WebKit.DOM_UNKNOWN_RULE, 0)
        self.assertEqual(WebKit.DOM_STYLE_RULE, 1)
        self.assertEqual(WebKit.DOM_CHARSET_RULE, 2)
        self.assertEqual(WebKit.DOM_IMPORT_RULE, 3)
        self.assertEqual(WebKit.DOM_MEDIA_RULE, 4)
        self.assertEqual(WebKit.DOM_FONT_FACE_RULE, 5)
        self.assertEqual(WebKit.DOM_PAGE_RULE, 6)
        self.assertEqual(WebKit.DOM_VARIABLES_RULE, 7)  # Removed in 10.10(?)
        self.assertEqual(WebKit.DOM_KEYFRAMES_RULE, 7)
        self.assertEqual(WebKit.DOM_WEBKIT_KEYFRAMES_RULE, 7)
        self.assertEqual(WebKit.DOM_WEBKIT_KEYFRAME_RULE, 8)
        self.assertEqual(WebKit.DOM_KEYFRAME_RULE, 8)
        self.assertEqual(WebKit.DOM_SUPPORTS_RULE, 12)
        self.assertEqual(WebKit.DOM_WEBKIT_REGION_RULE, 16)

        self.assertEqual(WebKit.DOM_NAMESPACE_RULE, 10)
