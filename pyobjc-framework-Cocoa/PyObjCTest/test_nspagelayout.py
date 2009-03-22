
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPageLayout (TestCase):
    def testMethods(self):
        self.failUnlessArgIsSEL(NSPageLayout.beginSheetWithPrintInfo_modalForWindow_delegate_didEndSelector_contextInfo_, 3, 'v@:@'+objc._C_NSInteger+'^v')
        self.failUnlessArgHasType(NSPageLayout.beginSheetWithPrintInfo_modalForWindow_delegate_didEndSelector_contextInfo_, 4, '^v')


if __name__ == "__main__":
    main()
