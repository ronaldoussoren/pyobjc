
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPageLayout (TestCase):
    def testMethods(self):
        self.fail("- (void)beginSheetWithPrintInfo:(NSPrintInfo *)printInfo modalForWindow:(NSWindow *)docWindow delegate:(id)delegate didEndSelector:(SEL)didEndSelector contextInfo:(void *)contextInfo;")


if __name__ == "__main__":
    main()
