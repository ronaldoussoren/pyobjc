import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class Presenter(Foundation.NSObject):
    def relinquishPresentedItemToReader_(self, a):
        pass

    def relinquishPresentedItemToWriter_(self, a):
        pass

    def savePresentedItemChangesWithCompletionHandler_(self, a):
        pass

    def accommodatePresentedItemDeletionWithCompletionHandler_(self, a):
        pass

    def accommodatePresentedSubitemDeletionAtURL_completionHandler_(self, a, b):
        pass

    def accommodatePresentedItemEvictionWithCompletionHandler_(self, a):
        pass


class TestNSFilePresenter(TestCase):
    @min_os_level("10.7")
    def testProtocols(self):
        self.assertProtocolExists("NSFilePresenter")

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            Presenter.relinquishPresentedItemToReader_, 0, b"v@?"
        )  # FIXME: Cannot test exact signature at this time
        self.assertArgIsBlock(
            Presenter.relinquishPresentedItemToWriter_, 0, b"v@?"
        )  # FIXME: Cannot test exact signature at this time

        self.assertArgIsBlock(
            Presenter.savePresentedItemChangesWithCompletionHandler_, 0, b"v@"
        )
        self.assertArgIsBlock(
            Presenter.accommodatePresentedItemDeletionWithCompletionHandler_, 0, b"v@"
        )
        self.assertArgIsBlock(
            Presenter.accommodatePresentedSubitemDeletionAtURL_completionHandler_,
            1,
            b"v@",
        )

        self.assertArgIsBlock(
            Presenter.accommodatePresentedItemEvictionWithCompletionHandler_,
            0,
            b"v@",
        )
