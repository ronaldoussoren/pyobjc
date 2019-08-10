from PyObjCTools.TestSupport import *
import WebKit

NSAttributedStringCompletionHandler = b"v@@@"


class TestWKContentRuleListStore(TestCase):
    @min_os_level("10.15")
    def test_constants(self):
        self.assertIsInstance(WebKit.NSReadAccessURLDocumentOption, unicode)

    @min_os_level("10.15")
    def test_methods(self):
        self.assertArgIsBlock(
            WebKit.NSAttributedString.loadFromHTMLWithRequest_options_completionHandler_,
            2,
            NSAttributedStringCompletionHandler,
        )
        self.assertArgIsBlock(
            WebKit.NSAttributedString.loadFromHTMLWithFileURL_options_completionHandler_,
            2,
            NSAttributedStringCompletionHandler,
        )
        self.assertArgIsBlock(
            WebKit.NSAttributedString.loadFromHTMLWithString_options_completionHandler_,
            2,
            NSAttributedStringCompletionHandler,
        )
        self.assertArgIsBlock(
            WebKit.NSAttributedString.loadFromHTMLWithData_options_completionHandler_,
            2,
            NSAttributedStringCompletionHandler,
        )


if __name__ == "__main__":
    main()
