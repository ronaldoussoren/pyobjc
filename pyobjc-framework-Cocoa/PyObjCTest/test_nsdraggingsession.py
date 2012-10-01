from PyObjCTools.TestSupport import *

import AppKit


class TestNSDraggingSession (TestCase):
    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(AppKit.NSDraggingSession.animatesToStartingPositionsOnCancelOrFail)
        self.assertArgIsBOOL(AppKit.NSDraggingSession.setAnimatesToStartingPositionsOnCancelOrFail_, 0)

        self.assertArgIsBlock(AppKit.NSDraggingSession.enumerateDraggingItemsWithOptions_forView_classes_searchOptions_usingBlock_, 4, b'v@' + objc._C_NSInteger + b'o^' + objc._C_NSBOOL)


if __name__ == "__main__":
    main()
