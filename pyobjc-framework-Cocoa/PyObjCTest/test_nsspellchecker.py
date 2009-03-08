
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSpellChecker (TestCase):
    def testMethods(self):
        self.fail("- (NSRange)checkGrammarOfString:(NSString *)stringToCheck startingAt:(NSInteger)startingOffset language:(NSString *)language wrap:(BOOL)wrapFlag inSpellDocumentWithTag:(NSInteger)tag details:(NSArray **)details;")


if __name__ == "__main__":
    main()
