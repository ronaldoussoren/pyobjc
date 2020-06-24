import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSExtensionItem(TestCase):
    @min_os_level("10.10")
    def testConstant10_10(self):
        self.assertIsInstance(Foundation.NSExtensionItemAttributedTitleKey, str)
        self.assertIsInstance(Foundation.NSExtensionItemAttributedContentTextKey, str)
        self.assertIsInstance(Foundation.NSExtensionItemAttachmentsKey, str)
