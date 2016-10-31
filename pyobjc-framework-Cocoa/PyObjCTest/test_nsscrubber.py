from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSScrubberHelper (NSObject):
    def numberOfItemsForScrubber_(self, s): return 1
    def scrubber_viewForItemAtIndex_(self, s, i): return 1
    def scrubber_didSelectItemAtIndex_(self, s, i): return 1
    def scrubber_didHighlightItemAtIndex_(self, s, i): return 1
    def scrubber_didChangeVisibleRange_(self, s, i): return 1

class TestNSScrubber (TestCase):
    @min_os_level('10.12')
    def testConstants(self):
        self.assertEqual(NSScrubberModeFixed, 0)
        self.assertEqual(NSScrubberModeFree, 1)

        self.assertEqual(NSScrubberAlignmentNone, 0)
        self.assertEqual(NSScrubberAlignmentLeading, 1)
        self.assertEqual(NSScrubberAlignmentTrailing, 2)
        self.assertEqual(NSScrubberAlignmentCenter, 3)

    @min_os_level('10.12')
    def testMethods(self):
        self.assertResultHasType(TestNSScrubberHelper.numberOfItemsForScrubber_, objc._C_NSInteger)
        self.assertArgHasType(TestNSScrubberHelper.scrubber_viewForItemAtIndex_, 1, objc._C_NSInteger)
        self.assertArgHasType(TestNSScrubberHelper.scrubber_didSelectItemAtIndex_, 1, objc._C_NSInteger)
        self.assertArgHasType(TestNSScrubberHelper.scrubber_didHighlightItemAtIndex_, 1, objc._C_NSInteger)
        self.assertArgHasType(TestNSScrubberHelper.scrubber_didChangeVisibleRange_, 1, NSRange.__typestr__)

        self.assertResultIsBOOL(NSScrubber.isContinuous)
        self.assertArgIsBOOL(NSScrubber.setContinuous_, 0)

        self.assertResultIsBOOL(NSScrubber.floatsSelectionViews)
        self.assertArgIsBOOL(NSScrubber.setFloatsSelectionViews_, 0)

        self.assertResultIsBOOL(NSScrubber.showsArrowButtons)
        self.assertArgIsBOOL(NSScrubber.setShowsArrowButtons_, 0)

        self.assertResultIsBOOL(NSScrubber.showsAdditionalContentIndicators)
        self.assertArgIsBOOL(NSScrubber.setShowsAdditionalContentIndicators_, 0)

        self.assertArgIsBlock(NSScrubber.performSequentialBatchUpdates_, 0, b'v')

    @min_sdk_level('10.12')
    def testProtocols(self):
        objc.protocolNamed('NSScrubberDataSource')
        objc.protocolNamed('NSScrubberDelegate')

if __name__ == "__main__":
    main()
