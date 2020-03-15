import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSItemProviderReadingWritingHelper(AppKit.NSObject):
    def loadDataWithTypeIdentifier_forItemProviderCompletionHandler_(self, ti, ch):
        pass

    def initWithItemProviderData_typeIdentifier_error_(self, d, ti, e):
        pass

    @classmethod
    def objectWithItemProviderData_typeIdentifier_error_(self, d, ti, e):
        pass


class TestNSItemProviderReadingWriting(TestCase):
    def testMethods(self):
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
