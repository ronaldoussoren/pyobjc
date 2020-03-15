import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level, onlyOn64Bit


class TestNSExtensionContext(TestCase):
    @min_os_level("10.10")
    @onlyOn64Bit
    def testMethods10_10(self):
        self.assertArgIsBlock(
            Foundation.NSExtensionContext.completeRequestReturningItems_completionHandler_,
            1,
            b"vZ",
        )
        self.assertArgIsBlock(
            Foundation.NSExtensionContext.openURL_completionHandler_, 1, b"vZ"
        )

    @min_os_level("10.10")
    @onlyOn64Bit
    def testConstant10_10(self):
        self.assertIsInstance(Foundation.NSExtensionItemsAndErrorsKey, str)
