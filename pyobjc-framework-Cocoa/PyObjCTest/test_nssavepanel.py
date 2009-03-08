
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSavePanel (TestCase):
    def testConstants(self):
        self.failUnlessEquals(NSFileHandlingPanelCancelButton, NSCancelButton)
        self.failUnlessEquals(NSFileHandlingPanelOKButton, NSOKButton)

    def testMethods(self):
        self.fail("- (void)beginSheetForDirectory:(NSString *)path file:(NSString *)name modalForWindow:(NSWindow *)docWindow modalDelegate:(id)delegate didEndSelector:(SEL)didEndSelector contextInfo:(void *)contextInfo;")

if __name__ == "__main__":
    main()
