import unittest
from CoreFoundation import *


class TestCharacterSet (unittest.TestCase):
    def testTypeId(self):
        v = CFCharacterSetGetTypeID()
        self.failUnless(isinstance(v, (int, long)))

    def testCreation(self):
        set = CFCharacterSetGetPredefined(kCFCharacterSetLetter)
        self.failUnless(isinstance(set, CFCharacterSetRef))

        set = CFCharacterSetCreateWithCharactersInRange(None, (ord('A'), ord('Z')-ord('A')))
        self.failUnless(isinstance(set, CFCharacterSetRef))

        set = CFCharacterSetCreateWithCharactersInString(None, u"abcdefABCDEF0123456789")
        self.failUnless(isinstance(set, CFCharacterSetRef))

        bytes = "0123" * (8192/4)
        bytes = buffer(bytes)
        set = CFCharacterSetCreateWithBitmapRepresentation(None, bytes)
        self.failUnless(isinstance(set, CFCharacterSetRef))

        set = CFCharacterSetCreateInvertedSet(None, set)
        self.failUnless(isinstance(set, CFCharacterSetRef))

        set = CFCharacterSetCreateMutable(None)
        self.failUnless(isinstance(set, CFCharacterSetRef))

        set = CFCharacterSetCreateCopy(None, set)
        self.failUnless(isinstance(set, CFCharacterSetRef))

        set = CFCharacterSetCreateMutableCopy(None, set)
        self.failUnless(isinstance(set, CFCharacterSetRef))



    def testInspection(self):
        letters = CFCharacterSetGetPredefined(kCFCharacterSetLetter)
        digits = CFCharacterSetGetPredefined(kCFCharacterSetDecimalDigit)
        set = CFCharacterSetCreateWithCharactersInString(None, u"abcdef")

        self.failUnless(CFCharacterSetIsSupersetOfSet(letters, set))
        self.failIf(CFCharacterSetIsSupersetOfSet(digits, set))

        self.failUnless(CFCharacterSetHasMemberInPlane(digits, 0))
        self.failIf(CFCharacterSetHasMemberInPlane(digits, 4))

        self.failUnless(CFCharacterSetIsCharacterMember(letters, u'A'))    
        self.failIf(CFCharacterSetIsCharacterMember(letters, u'9'))    

        data = CFCharacterSetCreateBitmapRepresentation(None, set)
        self.failUnless(isinstance(data, CFDataRef))


    def testInspectLongUnicode(self):
        # FIXME: These results aren't quite what I want to have, metadata doesn't
        # allow a better interface at the moment :-(

        letters = CFCharacterSetGetPredefined(kCFCharacterSetLetter)
        digits = CFCharacterSetGetPredefined(kCFCharacterSetDecimalDigit)
        self.failUnless(CFCharacterSetIsLongCharacterMember(letters, ord(u'A')))    
        self.failIf(CFCharacterSetIsLongCharacterMember(letters, ord(u'9')))    

    def testMutation(self):
        set = CFCharacterSetCreateWithCharactersInString(None, u"abcdef")
        set = CFCharacterSetCreateMutableCopy(None, set)

        self.failIf(CFCharacterSetIsCharacterMember(set, unichr(4)))
        CFCharacterSetAddCharactersInRange(set, (1, 10))
        self.failUnless(CFCharacterSetIsCharacterMember(set, unichr(4)))

        CFCharacterSetRemoveCharactersInRange(set, (4, 2))
        self.failIf(CFCharacterSetIsCharacterMember(set, unichr(4)))

        self.failIf(CFCharacterSetIsCharacterMember(set, u"5"))
        CFCharacterSetAddCharactersInString(set, u"012345")
        self.failUnless(CFCharacterSetIsCharacterMember(set, u"5"))

        self.failUnless(CFCharacterSetIsCharacterMember(set, u"a"))
        CFCharacterSetRemoveCharactersInString(set, u"ab")
        self.failIf(CFCharacterSetIsCharacterMember(set, u"a"))

        self.failIf(CFCharacterSetIsCharacterMember(set, u"9"))
        CFCharacterSetUnion(set, CFCharacterSetGetPredefined(kCFCharacterSetDecimalDigit))
        self.failUnless(CFCharacterSetIsCharacterMember(set, u"9"))
    
        CFCharacterSetIntersect(set, CFCharacterSetGetPredefined(kCFCharacterSetLetter))
        self.failIf(CFCharacterSetIsCharacterMember(set, u"9"))

        CFCharacterSetInvert(set)
        self.failUnless(CFCharacterSetIsCharacterMember(set, u"9"))
        self.failIf(CFCharacterSetIsCharacterMember(set, u"e"))




    def testConstants(self):
        self.failUnless(kCFCharacterSetControl == 1)
        self.failUnless(kCFCharacterSetWhitespace == 2)
        self.failUnless(kCFCharacterSetWhitespaceAndNewline == 3)
        self.failUnless(kCFCharacterSetDecimalDigit == 4)
        self.failUnless(kCFCharacterSetLetter == 5)
        self.failUnless(kCFCharacterSetLowercaseLetter == 6)
        self.failUnless(kCFCharacterSetUppercaseLetter == 7)
        self.failUnless(kCFCharacterSetNonBase == 8)
        self.failUnless(kCFCharacterSetDecomposable == 9)
        self.failUnless(kCFCharacterSetAlphaNumeric == 10)
        self.failUnless(kCFCharacterSetPunctuation == 11)
        self.failUnless(kCFCharacterSetCapitalizedLetter == 13)
        self.failUnless(kCFCharacterSetSymbol == 14)
        self.failUnless(kCFCharacterSetNewline == 15)
        self.failUnless(kCFCharacterSetIllegal == 12)



if __name__ == "__main__":
    unittest.main()
