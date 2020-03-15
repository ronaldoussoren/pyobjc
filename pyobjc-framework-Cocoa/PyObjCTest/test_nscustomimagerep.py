import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestNSCustomImageRep(TestCase):
    def testMethods(self):
        self.assertArgIsSEL(
            AppKit.NSCustomImageRep.initWithDrawSelector_delegate_, 0, b"v@:@"
        )

    @min_os_level("10.8")
    def testMethods10_8(self):
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
