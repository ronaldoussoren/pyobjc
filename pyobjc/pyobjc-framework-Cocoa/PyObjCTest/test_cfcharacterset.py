from PyObjCTools.TestSupport import *
from CoreFoundation import *


class TestCharacterSet (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CFCharacterSetRef)
        self.failUnlessIsCFType(CFMutableCharacterSetRef)

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
        self.failUnlessEqual(kCFCharacterSetControl, 1)
        self.failUnlessEqual(kCFCharacterSetWhitespace, 2)
        self.failUnlessEqual(kCFCharacterSetWhitespaceAndNewline, 3)
        self.failUnlessEqual(kCFCharacterSetDecimalDigit, 4)
        self.failUnlessEqual(kCFCharacterSetLetter, 5)
        self.failUnlessEqual(kCFCharacterSetLowercaseLetter, 6)
        self.failUnlessEqual(kCFCharacterSetUppercaseLetter, 7)
        self.failUnlessEqual(kCFCharacterSetNonBase, 8)
        self.failUnlessEqual(kCFCharacterSetDecomposable, 9)
        self.failUnlessEqual(kCFCharacterSetAlphaNumeric, 10)
        self.failUnlessEqual(kCFCharacterSetPunctuation, 11)
        self.failUnlessEqual(kCFCharacterSetCapitalizedLetter, 13)
        self.failUnlessEqual(kCFCharacterSetSymbol, 14)
        self.failUnlessEqual(kCFCharacterSetIllegal, 12)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.failUnlessEqual(kCFCharacterSetNewline, 15)


if __name__ == "__main__":
    main()
