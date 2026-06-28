import AppKit
from PyObjCTools.TestSupport import TestCase
import objc


class TestNSDraggingSession(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            AppKit.NSDraggingSession.animatesToStartingPositionsOnCancelOrFail
        )
        self.assertArgIsBOOL(
            AppKit.NSDraggingSession.setAnimatesToStartingPositionsOnCancelOrFail_, 0
        )

        self.assertArgIsBlock(
            AppKit.NSDraggingSession.enumerateDraggingItemsWithOptions_forView_classes_searchOptions_usingBlock_,  # noqa: B950
            4,
            b"v@" + objc._C_NSInteger + b"o^" + objc._C_NSBOOL,
        )
