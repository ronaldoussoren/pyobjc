
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTokenFieldCell (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSDefaultTokenStyle, 0)
        self.failUnlessEqual(NSPlainTextTokenStyle, 1)
        self.failUnlessEqual(NSRoundedTokenStyle, 2)

    def testMethods(self):
        self.fail("- (NSArray *)tokenFieldCell:(NSTokenFieldCell *)tokenFieldCell completionsForSubstring:(NSString *)substring indexOfToken:(NSInteger)tokenIndex indexOfSelectedItem:(NSInteger *)selectedIndex;")

if __name__ == "__main__":
    main()
