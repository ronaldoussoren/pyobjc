from PyObjCTools.TestSupport import *
from CoreFoundation import *
import sys


class TestCharacterSet (TestCase):
    def testTypes(self):
        self.assertIsCFType(CFCharacterSetRef)
        self.assertIsCFType(CFMutableCharacterSetRef)

    def testTypeId(self):
        v = CFCharacterSetGetTypeID()
        self.assertIsInstance(v, (int, long))
    def testCreation(self):
        set = CFCharacterSetGetPredefined(kCFCharacterSetLetter)
        self.assertIsInstance(set, CFCharacterSetRef)
        set = CFCharacterSetCreateWithCharactersInRange(None, (ord('A'), ord('Z')-ord('A')))
        self.assertIsInstance(set, CFCharacterSetRef)
        set = CFCharacterSetCreateWithCharactersInString(None, u"abcdefABCDEF0123456789")
        self.assertIsInstance(set, CFCharacterSetRef)
        bytes = b"0123" * (8192//4)
        if sys.version_info[0] == 2:
            bytes = buffer(bytes)
        set = CFCharacterSetCreateWithBitmapRepresentation(None, bytes)
        self.assertIsInstance(set, CFCharacterSetRef)
        set = CFCharacterSetCreateInvertedSet(None, set)
        self.assertIsInstance(set, CFCharacterSetRef)
        set = CFCharacterSetCreateMutable(None)
        self.assertIsInstance(set, CFCharacterSetRef)
        set = CFCharacterSetCreateCopy(None, set)
        self.assertIsInstance(set, CFCharacterSetRef)
        set = CFCharacterSetCreateMutableCopy(None, set)
        self.assertIsInstance(set, CFCharacterSetRef)
    def testInspection(self):
        letters = CFCharacterSetGetPredefined(kCFCharacterSetLetter)
        digits = CFCharacterSetGetPredefined(kCFCharacterSetDecimalDigit)
        set = CFCharacterSetCreateWithCharactersInString(None, u"abcdef")

        self.assertTrue(CFCharacterSetIsSupersetOfSet(letters, set))
        self.assertFalse(CFCharacterSetIsSupersetOfSet(digits, set))

        self.assertTrue(CFCharacterSetHasMemberInPlane(digits, 0))
        self.assertFalse(CFCharacterSetHasMemberInPlane(digits, 4))

        self.assertTrue(CFCharacterSetIsCharacterMember(letters, u'A'))    
        self.assertFalse(CFCharacterSetIsCharacterMember(letters, u'9'))    

        data = CFCharacterSetCreateBitmapRepresentation(None, set)
        self.assertIsInstance(data, CFDataRef)
    def testInspectLongUnicode(self):
        letters = CFCharacterSetGetPredefined(kCFCharacterSetLetter)
        digits = CFCharacterSetGetPredefined(kCFCharacterSetDecimalDigit)
        self.assertTrue(CFCharacterSetIsLongCharacterMember(letters, ord(u'A')))    
        self.assertFalse(CFCharacterSetIsLongCharacterMember(letters, ord(u'9')))    

    def testMutation(self):
        set = CFCharacterSetCreateWithCharactersInString(None, u"abcdef")
        set = CFCharacterSetCreateMutableCopy(None, set)

        self.assertFalse(CFCharacterSetIsCharacterMember(set, unichr(4)))
        CFCharacterSetAddCharactersInRange(set, (1, 10))
        self.assertTrue(CFCharacterSetIsCharacterMember(set, unichr(4)))

        CFCharacterSetRemoveCharactersInRange(set, (4, 2))
        self.assertFalse(CFCharacterSetIsCharacterMember(set, unichr(4)))

        self.assertFalse(CFCharacterSetIsCharacterMember(set, u"5"))
        CFCharacterSetAddCharactersInString(set, u"012345")
        self.assertTrue(CFCharacterSetIsCharacterMember(set, u"5"))

        self.assertTrue(CFCharacterSetIsCharacterMember(set, u"a"))
        CFCharacterSetRemoveCharactersInString(set, u"ab")
        self.assertFalse(CFCharacterSetIsCharacterMember(set, u"a"))

        self.assertFalse(CFCharacterSetIsCharacterMember(set, u"9"))
        CFCharacterSetUnion(set, CFCharacterSetGetPredefined(kCFCharacterSetDecimalDigit))
        self.assertTrue(CFCharacterSetIsCharacterMember(set, u"9"))
    
        CFCharacterSetIntersect(set, CFCharacterSetGetPredefined(kCFCharacterSetLetter))
        self.assertFalse(CFCharacterSetIsCharacterMember(set, u"9"))

        CFCharacterSetInvert(set)
        self.assertTrue(CFCharacterSetIsCharacterMember(set, u"9"))
        self.assertFalse(CFCharacterSetIsCharacterMember(set, u"e"))


    def testConstants(self):
        self.assertEqual(kCFCharacterSetControl, 1)
        self.assertEqual(kCFCharacterSetWhitespace, 2)
        self.assertEqual(kCFCharacterSetWhitespaceAndNewline, 3)
        self.assertEqual(kCFCharacterSetDecimalDigit, 4)
        self.assertEqual(kCFCharacterSetLetter, 5)
        self.assertEqual(kCFCharacterSetLowercaseLetter, 6)
        self.assertEqual(kCFCharacterSetUppercaseLetter, 7)
        self.assertEqual(kCFCharacterSetNonBase, 8)
        self.assertEqual(kCFCharacterSetDecomposable, 9)
        self.assertEqual(kCFCharacterSetAlphaNumeric, 10)
        self.assertEqual(kCFCharacterSetPunctuation, 11)
        self.assertEqual(kCFCharacterSetCapitalizedLetter, 13)
        self.assertEqual(kCFCharacterSetSymbol, 14)
        self.assertEqual(kCFCharacterSetIllegal, 12)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertEqual(kCFCharacterSetNewline, 15)


if __name__ == "__main__":
    main()
