from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSScrubberLayoutHelper (NSObject):
    def scrubber_layout_sizeForItemAtIndex_(self, s, l, i): return 1

class TestNSScrubberLayout (TestCase):
    @min_os_level('10.12')
    def testMethods(self):
        self.assertResultIsBOOL(NSScrubberLayout.shouldInvalidateLayoutForSelectionChange)
        self.assertResultIsBOOL(NSScrubberLayout.shouldInvalidateLayoutForHighlightChange)
        self.assertResultIsBOOL(NSScrubberLayout.shouldInvalidateLayoutForChangeFromVisibleRect_toVisibleRect_)
        self.assertResultIsBOOL(NSScrubberLayout.automaticallyMirrorsInRightToLeftLayout)

        self.assertResultHasType(TestNSScrubberLayoutHelper.scrubber_layout_sizeForItemAtIndex_, NSSize.__typestr__)
        self.assertArgHasType(TestNSScrubberLayoutHelper.scrubber_layout_sizeForItemAtIndex_, 2, objc._C_NSInteger)

    @min_sdk_level('10.12')
    def testProtocols(self):
        objc.protocolNamed('NSScrubberFlowLayoutDelegate')

if __name__ == "__main__":
    main()
