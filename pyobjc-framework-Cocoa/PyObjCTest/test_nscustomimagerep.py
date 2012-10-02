from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSCustomImageRep (TestCase):
    def testMethods(self):
        self.assertArgIsSEL(NSCustomImageRep.initWithDrawSelector_delegate_, 0,
                b'v@:@')

    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertArgIsBOOL(
                NSCustomImageRep.initWithSize_flipped_drawingHandler_, 1)
        self.assertArgIsBlock(
                NSCustomImageRep.initWithSize_flipped_drawingHandler_, 2,
                objc._C_NSBOOL + NSRect.__typestr__)
        self.assertResultIsBlock(
                NSCustomImageRep.drawingHandler,
                objc._C_NSBOOL + NSRect.__typestr__)


if __name__ == "__main__":
    main()
