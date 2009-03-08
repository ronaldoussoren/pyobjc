
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTextInputClient (TestCase):

    @min_os_level("10.5")
    def testMethods(self):
        self.fail("- (NSAttributedString *)attributedSubstringForProposedRange:(NSRange)aRange actualRange:(NSRangePointer)actualRange;")
        self.fail("- (NSRect)firstRectForCharacterRange:(NSRange)aRange actualRange:(NSRangePointer)actualRange;")


if __name__ == "__main__":
    main()
