import AppKit
from PyObjCTools.TestSupport import TestCase
import objc


class TestNSCustomImageRep(TestCase):
    def test_methods(self):
        self.assertArgIsSEL(
            AppKit.NSCustomImageRep.initWithDrawSelector_delegate_, 0, b"v@:@"
        )

        self.assertArgIsBOOL(
            AppKit.NSCustomImageRep.initWithSize_flipped_drawingHandler_, 1
        )
        self.assertArgIsBlock(
            AppKit.NSCustomImageRep.initWithSize_flipped_drawingHandler_,
            2,
            objc._C_NSBOOL + AppKit.NSRect.__typestr__,
        )
        self.assertResultIsBlock(
            AppKit.NSCustomImageRep.drawingHandler,
            objc._C_NSBOOL + AppKit.NSRect.__typestr__,
        )
