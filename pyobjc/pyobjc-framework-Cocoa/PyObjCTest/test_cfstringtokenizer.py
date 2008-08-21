import unittest
from CoreFoundation import *


class TestStringTokenizer (unittest.TestCase):
    def testDummy(self):
        self.fail("CFStringTokenizer tests not implemented yet")


    def testConstants(self):

        self.failUnless( kCFStringTokenizerUnitWord                           == 0 )
        self.failUnless( kCFStringTokenizerUnitSentence                       == 1 )
        self.failUnless( kCFStringTokenizerUnitParagraph                      == 2 )
        self.failUnless( kCFStringTokenizerUnitLineBreak                      == 3 )
        self.failUnless( kCFStringTokenizerUnitWordBoundary                   == 4 )
        self.failUnless( kCFStringTokenizerAttributeLatinTranscription        == 1L << 16 )
        self.failUnless( kCFStringTokenizerAttributeLanguage                  == 1L << 17 )

        self.failUnless( kCFStringTokenizerTokenNone                          == 0 )
        self.failUnless( kCFStringTokenizerTokenNormal                        == 1 )
        self.failUnless( kCFStringTokenizerTokenHasSubTokensMask              == 1L << 1 )
        self.failUnless( kCFStringTokenizerTokenHasDerivedSubTokensMask       == 1L << 2 )
        self.failUnless( kCFStringTokenizerTokenHasHasNumbersMask             == 1L << 3 )
        self.failUnless( kCFStringTokenizerTokenHasNonLettersMask             == 1L << 4 )
        self.failUnless( kCFStringTokenizerTokenIsCJWordMask                  == 1L << 5 )


if __name__ == "__main__":
    unittest.main()
