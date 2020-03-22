import CoreFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestCharacterSet(TestCase):
    def testTypes(self):
        cls = None
        try:
            cls = objc.lookUpClass("__NSCFCharacterSet")
        except objc.error:
            cls = objc.lookUpClass("NSCFCharacterSet")
        if cls is None:
            self.assertIsCFType(CoreFoundation.CFCharacterSetRef)

        else:
            self.assertIs(CoreFoundation.CFCharacterSetRef, cls)

        self.assertIsCFType(CoreFoundation.CFMutableCharacterSetRef)

    def testTypeId(self):
        v = CoreFoundation.CFCharacterSetGetTypeID()
        self.assertIsInstance(v, int)

    def testCreation(self):
        charset = CoreFoundation.CFCharacterSetGetPredefined(
            CoreFoundation.kCFCharacterSetLetter
        )
        self.assertIsInstance(
            charset,
            (CoreFoundation.CFCharacterSetRef, CoreFoundation.CFMutableCharacterSetRef),
        )
        charset = CoreFoundation.CFCharacterSetCreateWithCharactersInRange(
            None, (ord("A"), ord("Z") - ord("A"))
        )
        self.assertIsInstance(
            charset,
            (CoreFoundation.CFCharacterSetRef, CoreFoundation.CFMutableCharacterSetRef),
        )
        charset = CoreFoundation.CFCharacterSetCreateWithCharactersInString(
            None, b"abcdefABCDEF0123456789".decode("latin1")
        )
        self.assertIsInstance(
            charset,
            (CoreFoundation.CFCharacterSetRef, CoreFoundation.CFMutableCharacterSetRef),
        )
        bytes_value = b"0123" * (8192 // 4)
        charset = CoreFoundation.CFCharacterSetCreateWithBitmapRepresentation(
            None, bytes_value
        )
        self.assertIsInstance(
            charset,
            (CoreFoundation.CFCharacterSetRef, CoreFoundation.CFMutableCharacterSetRef),
        )
        charset = CoreFoundation.CFCharacterSetCreateInvertedSet(None, charset)
        self.assertIsInstance(
            charset,
            (CoreFoundation.CFCharacterSetRef, CoreFoundation.CFMutableCharacterSetRef),
        )
        charset = CoreFoundation.CFCharacterSetCreateMutable(None)
        self.assertIsInstance(
            charset,
            (CoreFoundation.CFCharacterSetRef, CoreFoundation.CFMutableCharacterSetRef),
        )
        charset = CoreFoundation.CFCharacterSetCreateCopy(None, charset)
        self.assertIsInstance(
            charset,
            (CoreFoundation.CFCharacterSetRef, CoreFoundation.CFMutableCharacterSetRef),
        )
        charset = CoreFoundation.CFCharacterSetCreateMutableCopy(None, charset)
        self.assertIsInstance(
            charset,
            (CoreFoundation.CFCharacterSetRef, CoreFoundation.CFMutableCharacterSetRef),
        )

    def testInspection(self):
        letters = CoreFoundation.CFCharacterSetGetPredefined(
            CoreFoundation.kCFCharacterSetLetter
        )
        digits = CoreFoundation.CFCharacterSetGetPredefined(
            CoreFoundation.kCFCharacterSetDecimalDigit
        )
        charset = CoreFoundation.CFCharacterSetCreateWithCharactersInString(
            None, b"abcdef".decode("latin1")
        )

        self.assertTrue(CoreFoundation.CFCharacterSetIsSupersetOfSet(letters, charset))
        self.assertFalse(CoreFoundation.CFCharacterSetIsSupersetOfSet(digits, charset))

        self.assertTrue(CoreFoundation.CFCharacterSetHasMemberInPlane(digits, 0))
        self.assertFalse(CoreFoundation.CFCharacterSetHasMemberInPlane(digits, 4))

        self.assertTrue(
            CoreFoundation.CFCharacterSetIsCharacterMember(
                letters, b"A".decode("latin1")
            )
        )
        self.assertFalse(
            CoreFoundation.CFCharacterSetIsCharacterMember(
                letters, b"9".decode("latin1")
            )
        )

        data = CoreFoundation.CFCharacterSetCreateBitmapRepresentation(None, charset)
        self.assertIsInstance(data, CoreFoundation.CFDataRef)

    def testInspectLongUnicode(self):
        letters = CoreFoundation.CFCharacterSetGetPredefined(
            CoreFoundation.kCFCharacterSetLetter
        )
        digits = CoreFoundation.CFCharacterSetGetPredefined(
            CoreFoundation.kCFCharacterSetDecimalDigit
        )
        self.assertTrue(
            CoreFoundation.CFCharacterSetIsLongCharacterMember(
                letters, ord(b"A".decode("latin1"))
            )
        )
        self.assertFalse(
            CoreFoundation.CFCharacterSetIsLongCharacterMember(
                letters, ord(b"9".decode("latin1"))
            )
        )
        self.assertTrue(
            CoreFoundation.CFCharacterSetIsLongCharacterMember(
                digits, ord(b"9".decode("latin1"))
            )
        )
        self.assertFalse(
            CoreFoundation.CFCharacterSetIsLongCharacterMember(
                digits, ord(b"A".decode("latin1"))
            )
        )

    def testMutation(self):
        charset = CoreFoundation.CFCharacterSetCreateWithCharactersInString(
            None, b"abcdef".decode("latin1")
        )
        charset = CoreFoundation.CFCharacterSetCreateMutableCopy(None, charset)

        self.assertFalse(
            CoreFoundation.CFCharacterSetIsCharacterMember(charset, chr(4))
        )
        CoreFoundation.CFCharacterSetAddCharactersInRange(charset, (1, 10))
        self.assertTrue(CoreFoundation.CFCharacterSetIsCharacterMember(charset, chr(4)))

        CoreFoundation.CFCharacterSetRemoveCharactersInRange(set, (4, 2))
        self.assertFalse(CoreFoundation.CFCharacterSetIsCharacterMember(set, chr(4)))

        self.assertFalse(
            CoreFoundation.CFCharacterSetIsCharacterMember(set, b"5".decode("latin1"))
        )
        CoreFoundation.CFCharacterSetAddCharactersInString(
            set, b"012345".decode("latin1")
        )
        self.assertTrue(
            CoreFoundation.CFCharacterSetIsCharacterMember(set, b"5".decode("latin1"))
        )

        self.assertTrue(
            CoreFoundation.CFCharacterSetIsCharacterMember(set, b"a".decode("latin1"))
        )
        CoreFoundation.CFCharacterSetRemoveCharactersInString(
            set, b"ab".decode("latin1")
        )
        self.assertFalse(
            CoreFoundation.CFCharacterSetIsCharacterMember(set, b"a".decode("latin1"))
        )

        self.assertFalse(
            CoreFoundation.CFCharacterSetIsCharacterMember(set, b"9".decode("latin1"))
        )
        CoreFoundation.CFCharacterSetUnion(
            set,
            CoreFoundation.CFCharacterSetGetPredefined(
                CoreFoundation.kCFCharacterSetDecimalDigit
            ),
        )
        self.assertTrue(
            CoreFoundation.CFCharacterSetIsCharacterMember(set, b"9".decode("latin1"))
        )

        CoreFoundation.CFCharacterSetIntersect(
            set,
            CoreFoundation.CFCharacterSetGetPredefined(
                CoreFoundation.kCFCharacterSetLetter
            ),
        )
        self.assertFalse(
            CoreFoundation.CFCharacterSetIsCharacterMember(set, b"9".decode("latin1"))
        )

        CoreFoundation.CFCharacterSetInvert(set)
        self.assertTrue(
            CoreFoundation.CFCharacterSetIsCharacterMember(set, b"9".decode("latin1"))
        )
        self.assertFalse(
            CoreFoundation.CFCharacterSetIsCharacterMember(set, b"e".decode("latin1"))
        )

    def testConstants(self):
        self.assertEqual(CoreFoundation.kCFCharacterSetControl, 1)
        self.assertEqual(CoreFoundation.kCFCharacterSetWhitespace, 2)
        self.assertEqual(CoreFoundation.kCFCharacterSetWhitespaceAndNewline, 3)
        self.assertEqual(CoreFoundation.kCFCharacterSetDecimalDigit, 4)
        self.assertEqual(CoreFoundation.kCFCharacterSetLetter, 5)
        self.assertEqual(CoreFoundation.kCFCharacterSetLowercaseLetter, 6)
        self.assertEqual(CoreFoundation.kCFCharacterSetUppercaseLetter, 7)
        self.assertEqual(CoreFoundation.kCFCharacterSetNonBase, 8)
        self.assertEqual(CoreFoundation.kCFCharacterSetDecomposable, 9)
        self.assertEqual(CoreFoundation.kCFCharacterSetAlphaNumeric, 10)
        self.assertEqual(CoreFoundation.kCFCharacterSetPunctuation, 11)
        self.assertEqual(CoreFoundation.kCFCharacterSetCapitalizedLetter, 13)
        self.assertEqual(CoreFoundation.kCFCharacterSetSymbol, 14)
        self.assertEqual(CoreFoundation.kCFCharacterSetIllegal, 12)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertEqual(CoreFoundation.kCFCharacterSetNewline, 15)
