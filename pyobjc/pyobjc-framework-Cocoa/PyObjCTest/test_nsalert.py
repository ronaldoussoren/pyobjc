
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSAlert (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSWarningAlertStyle, 0)
        self.failUnlessEqual(NSInformationalAlertStyle, 1)
        self.failUnlessEqual(NSCriticalAlertStyle, 2)
        self.failUnlessEqual(NSAlertFirstButtonReturn, 1000)
        self.failUnlessEqual(NSAlertSecondButtonReturn, 1001)
        self.failUnlessEqual(NSAlertThirdButtonReturn, 1002)



    def testMethods(self):
        self.fail("+ (NSAlert *)alertWithMessageText:(NSString *)message defaultButton:(NSString *)defaultButton alternateButton:(NSString *)alternateButton otherButton:(NSString *)otherButton informativeTextWithFormat:(NSString *)format, ...;")
        self.fail("- (void)beginSheetModalForWindow:(NSWindow *)window modalDelegate:(id)delegate didEndSelector:(SEL)didEndSelector contextInfo:(void *)contextInfo; ")





if __name__ == "__main__":
    main()
