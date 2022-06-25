from PyObjCTools.TestSupport import TestCase, min_sdk_level
import WebKit


class TestWebEditingDelegateHelper(WebKit.NSObject):
    def webView_shouldBeginEditingInDOMRange_(self, a, b):
        return 1

    def webView_shouldEndEditingInDOMRange_(self, a, b):
        return 1

    def webView_shouldInsertNode_replacingDOMRange_givenAction_(self, a, b, c, d):
        return 1

    def webView_shouldInsertText_replacingDOMRange_givenAction_(self, a, b, c, d):
        return 1

    def webView_shouldDeleteDOMRange_(self, a, b):
        return 1

    def webView_shouldChangeSelectedDOMRange_toDOMRange_affinity_stillSelecting_(
        self, a, b, c, d, e
    ):
        return 1

    def webView_shouldApplyStyle_toElementsInDOMRange_(self, a, b, c):
        return 1

    def webView_shouldChangeTypingStyle_toStyle_(self, a, b, c):
        return 1

    def webView_doCommandBySelector_(self, a, b):
        return 1


class TestWebEditingDelegate(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(WebKit.WebViewInsertAction)

    @min_sdk_level("10.11")
    def testProtocols(self):
        self.assertProtocolExists("WebEditingDelegate")

    def testConstants(self):
        self.assertEqual(WebKit.WebViewInsertActionTyped, 0)
        self.assertEqual(WebKit.WebViewInsertActionPasted, 1)
        self.assertEqual(WebKit.WebViewInsertActionDropped, 2)

    def testMethods(self):
        self.assertResultIsBOOL(
            TestWebEditingDelegateHelper.webView_shouldBeginEditingInDOMRange_
        )
        self.assertResultIsBOOL(
            TestWebEditingDelegateHelper.webView_shouldEndEditingInDOMRange_
        )
        self.assertResultIsBOOL(
            TestWebEditingDelegateHelper.webView_shouldInsertNode_replacingDOMRange_givenAction_
        )
        self.assertResultIsBOOL(
            TestWebEditingDelegateHelper.webView_shouldInsertText_replacingDOMRange_givenAction_
        )
        self.assertResultIsBOOL(
            TestWebEditingDelegateHelper.webView_shouldDeleteDOMRange_
        )
        self.assertResultIsBOOL(
            TestWebEditingDelegateHelper.webView_shouldChangeSelectedDOMRange_toDOMRange_affinity_stillSelecting_  # noqa: B950
        )
        self.assertArgIsBOOL(
            TestWebEditingDelegateHelper.webView_shouldChangeSelectedDOMRange_toDOMRange_affinity_stillSelecting_,  # noqa: B950
            4,
        )
        self.assertResultIsBOOL(
            TestWebEditingDelegateHelper.webView_shouldApplyStyle_toElementsInDOMRange_
        )
        self.assertResultIsBOOL(
            TestWebEditingDelegateHelper.webView_shouldChangeTypingStyle_toStyle_
        )
        self.assertResultIsBOOL(
            TestWebEditingDelegateHelper.webView_doCommandBySelector_
        )
