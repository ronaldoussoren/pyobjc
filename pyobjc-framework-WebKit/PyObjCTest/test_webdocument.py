from PyObjCTools.TestSupport import TestCase
import WebKit  # noqa: F401


class TestWebDocumentHelper(WebKit.NSObject):
    def setNeedsLayout_(self, v):
        pass

    def searchFor_direction_caseSensitive_wrap_(self, a, b, c, d):
        return 1

    def supportsTextEncoding(self):
        return 1

    def canProvideDocumentSource(self):
        return 1


class TestWebDocument(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("WebDocumentView", WebKit)
        self.assertProtocolExists("WebDocumentSearching", WebKit)
        self.assertProtocolExists("WebDocumentText", WebKit)
        self.assertProtocolExists("WebDocumentRepresentation", WebKit)

    def test_methods(self):
        self.assertArgIsBOOL(TestWebDocumentHelper.setNeedsLayout_, 0)

        self.assertResultIsBOOL(
            TestWebDocumentHelper.searchFor_direction_caseSensitive_wrap_
        )
        self.assertArgIsBOOL(
            TestWebDocumentHelper.searchFor_direction_caseSensitive_wrap_, 1
        )
        self.assertArgIsBOOL(
            TestWebDocumentHelper.searchFor_direction_caseSensitive_wrap_, 2
        )
        self.assertArgIsBOOL(
            TestWebDocumentHelper.searchFor_direction_caseSensitive_wrap_, 3
        )

        self.assertResultIsBOOL(TestWebDocumentHelper.supportsTextEncoding)
        self.assertResultIsBOOL(TestWebDocumentHelper.canProvideDocumentSource)
