from PyObjCTools.TestSupport import *
from CoreFoundation import *
import sys

try:
    long
except NameError:
    long = int

try:
    unichr
except NameError:
    unichr = chr


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
        set = CFCharacterSetCreateWithCharactersInString(None, b"abcdefABCDEF0123456789".decode('latin1'))
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
        set = CFCharacterSetCreateWithCharactersInString(None, b"abcdef".decode('latin1'))

        self.assertTrue(CFCharacterSetIsSupersetOfSet(letters, set))
        self.assertFalse(CFCharacterSetIsSupersetOfSet(digits, set))

        self.assertTrue(CFCharacterSetHasMemberInPlane(digits, 0))
        self.assertFalse(CFCharacterSetHasMemberInPlane(digits, 4))

        self.assertTrue(CFCharacterSetIsCharacterMember(letters, b'A'.decode('latin1')))
        self.assertFalse(CFCharacterSetIsCharacterMember(letters, b'9'.decode('latin1')))

        data = CFCharacterSetCreateBitmapRepresentation(None, set)
        self.assertIsInstance(data, CFDataRef)

    def testInspectLongUnicode(self):
        letters = CFCharacterSetGetPredefined(kCFCharacterSetLetter)
        digits = CFCharacterSetGetPredefined(kCFCharacterSetDecimalDigit)
        self.assertTrue(CFCharacterSetIsLongCharacterMember(letters, ord(b'A'.decode('latin1'))))
        self.assertFalse(CFCharacterSetIsLongCharacterMember(letters, ord(b'9'.decode('latin1'))))

    def testMutation(self):
        set = CFCharacterSetCreateWithCharactersInString(None, b"abcdef".decode('latin1'))
        set = CFCharacterSetCreateMutableCopy(None, set)

        self.assertFalse(CFCharacterSetIsCharacterMember(set, unichr(4)))
        CFCharacterSetAddCharactersInRange(set, (1, 10))
        self.assertTrue(CFCharacterSetIsCharacterMember(set, unichr(4)))

        CFCharacterSetRemoveCharactersInRange(set, (4, 2))
        self.assertFalse(CFCharacterSetIsCharacterMember(set, unichr(4)))

        self.assertFalse(CFCharacterSetIsCharacterMember(set, b"5".decode('latin1')))
        CFCharacterSetAddCharactersInString(set, b"012345".decode('latin1'))
        self.assertTrue(CFCharacterSetIsCharacterMember(set, b"5".decode('latin1')))

        self.assertTrue(CFCharacterSetIsCharacterMember(set, b"a".decode('latin1')))
        CFCharacterSetRemoveCharactersInString(set, b"ab".decode('latin1'))
        self.assertFalse(CFCharacterSetIsCharacterMember(set, b"a".decode('latin1')))

        self.assertFalse(CFCharacterSetIsCharacterMember(set, b"9".decode('latin1')))
        CFCharacterSetUnion(set, CFCharacterSetGetPredefined(kCFCharacterSetDecimalDigit))
        self.assertTrue(CFCharacterSetIsCharacterMember(set, b"9".decode('latin1')))

        CFCharacterSetIntersect(set, CFCharacterSetGetPredefined(kCFCharacterSetLetter))
        self.assertFalse(CFCharacterSetIsCharacterMember(set, b"9".decode('latin1')))

        CFCharacterSetInvert(set)
        self.assertTrue(CFCharacterSetIsCharacterMember(set, b"9".decode('latin1')))
        self.assertFalse(CFCharacterSetIsCharacterMember(set, b"e".decode('latin1')))

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
