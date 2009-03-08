
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSResponder (TestCase):
    def testMethods(self):
        self.fail("- (void)presentError:(NSError *)error modalForWindow:(NSWindow *)window delegate:(id)delegate didPresentSelector:(SEL)didPresentSelector contextInfo:(void *)contextInfo;")


if __name__ == "__main__":
    main()
