from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKContentRuleListStore(TestCase):
    @min_os_level("10.13")
    def testMethods(self):
        self.assertArgIsBlock(
            WebKit.WKContentRuleListStore.compileContentRuleListForIdentifier_encodedContentRuleList_completionHandler_,  # noqa: B950
            2,
            b"v@@",
        )
        self.assertArgIsBlock(
            WebKit.WKContentRuleListStore.lookUpContentRuleListForIdentifier_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            WebKit.WKContentRuleListStore.removeContentRuleListForIdentifier_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            WebKit.WKContentRuleListStore.getAvailableContentRuleListIdentifiers_,
            0,
            b"v@",
        )
