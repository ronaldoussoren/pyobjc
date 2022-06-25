from Foundation import NSObject
from PyObjCTools.TestSupport import TestCase, min_sdk_level

import Quartz  # noqa: F401

QLPreviewItemLoadingBlock = b"v@"


class TestQLPreviewingControllerHelper(NSObject):
    def preparePreviewOfSearchableItemWithIdentifier_queryString_completionHandler_(
        self, i, q, c
    ):
        pass

    def preparePreviewOfFileAtURL_completionHandler_(self, a, b):
        pass


class TestQLPreviewingController(TestCase):
    @min_sdk_level("10.13")
    def testProtocols(self):
        self.assertProtocolExists("QLPreviewingController")

    def testMethods(self):
        self.assertArgIsBlock(
            TestQLPreviewingControllerHelper.preparePreviewOfSearchableItemWithIdentifier_queryString_completionHandler_,
            2,
            QLPreviewItemLoadingBlock,
        )
        self.assertArgIsBlock(
            TestQLPreviewingControllerHelper.preparePreviewOfFileAtURL_completionHandler_,
            1,
            b"v@",
        )
