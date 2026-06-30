import Foundation
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestNSItemProviderReadingWritingHelper(Foundation.NSObject):
    def loadDataWithTypeIdentifier_forItemProviderCompletionHandler_(self, ti, ch):
        pass

    def initWithItemProviderData_typeIdentifier_error_(self, d, ti, e):
        pass

    @classmethod
    def objectWithItemProviderData_typeIdentifier_error_(self, d, ti, e):
        pass


class TestNSItemProviderReadingWriting(TestCase):
    @min_sdk_level("10.13")
    def test_protocols(self):
        self.assertProtocolExists("NSItemProviderReading", Foundation)
        self.assertProtocolExists("NSItemProviderWriting", Foundation)

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestNSItemProviderReadingWritingHelper.loadDataWithTypeIdentifier_forItemProviderCompletionHandler_,  # noqa: B950
            1,
            b"v@@",
        )
        self.assertArgIsOut(
            TestNSItemProviderReadingWritingHelper.initWithItemProviderData_typeIdentifier_error_,  # noqa: B950
            2,
        )

        self.assertArgIsOut(
            TestNSItemProviderReadingWritingHelper.objectWithItemProviderData_typeIdentifier_error_,  # noqa: B950
            2,
        )
