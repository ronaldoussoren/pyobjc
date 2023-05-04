import array
import sys

import Foundation
import CoreFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestString(TestCase):
    def testType(self):
        self.assertTrue(issubclass(CoreFoundation.CFStringRef, Foundation.NSString))

    def testTypeID(self):
        v = CoreFoundation.CFStringGetTypeID()
        self.assertIsInstance(v, int)

    def testNoPascalStrings(self):
        self.assertNotHasAttr(CoreFoundation, "CFStringCreateWithPascalString")
        self.assertNotHasAttr(CoreFoundation, "CFStringCreateWithPascalStringNoCopy")
        self.assertNotHasAttr(CoreFoundation, "CFStringGetPascalString")
        self.assertNotHasAttr(CoreFoundation, "CFStringGetPascalStringPtr")
        self.assertNotHasAttr(CoreFoundation, "CFStringAppendPascalString")

    def testCreation(self):
        s = CoreFoundation.CFStringCreateWithCString(
            None, b"hello world", CoreFoundation.kCFStringEncodingASCII
        )
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertIsInstance(s, str)
        self.assertEqual(s, "hello world")

        s = CoreFoundation.CFStringCreateWithBytes(
            None, b"hello world", 5, CoreFoundation.kCFStringEncodingASCII, False
        )
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertIsInstance(s, str)
        self.assertEqual(s, "hello")

        s = CoreFoundation.CFStringCreateWithCharacters(None, "HELLO", 5)
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertIsInstance(s, str)
        self.assertEqual(s, "HELLO")

        # NOTE: the deallocator must be CoreFoundation.kCFAllocatorNull
        s = CoreFoundation.CFStringCreateWithCStringNoCopy(
            None,
            b"hello world",
            CoreFoundation.kCFStringEncodingASCII,
            CoreFoundation.kCFAllocatorNull,
        )
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertIsInstance(s, str)
        self.assertEqual(s, "hello world")

        s = CoreFoundation.CFStringCreateWithBytesNoCopy(
            None,
            b"hello world",
            5,
            CoreFoundation.kCFStringEncodingASCII,
            False,
            CoreFoundation.kCFAllocatorNull,
        )
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertIsInstance(s, str)
        self.assertEqual(s, "hello")

        s = CoreFoundation.CFStringCreateWithCharactersNoCopy(
            None, "HELLO", 5, CoreFoundation.kCFAllocatorNull
        )
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertIsInstance(s, str)
        self.assertEqual(s, "HELLO")

        del s

        s = CoreFoundation.CFStringCreateWithSubstring(
            None, "Hello world", CoreFoundation.CFRange(2, 4)
        )
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertEqual(s, "Hello world"[2:6])

        s = CoreFoundation.CFStringCreateCopy(None, "foo the bar")
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertEqual(s, "foo the bar")

        s = CoreFoundation.CFStringCreateWithFormat(
            None, None, "hello %s = %d", b"foo", 52
        )
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertEqual(s, "hello foo = 52")

        self.assertFalse(
            hasattr(CoreFoundation, "CFStringCreateWithFormatAndArguments")
        )

    def testCreateMutable(self):
        s = CoreFoundation.CFStringCreateMutable(None, 0)
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertEqual(s, "")

        s = CoreFoundation.CFStringCreateMutableCopy(None, 0, "foobar")
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertEqual(s, "foobar")

        if sys.version_info[:2] < (3, 3):
            # See issue15035 on Python's tracker. There currently is
            # no array format code for UCS2 storage (Python 3.3 or later)
            # Therefore these tests can only work for earlier versions
            # of Python.

            b = array.array("u", "hello world")
            s = CoreFoundation.CFStringCreateMutableWithExternalCharactersNoCopy(
                None, b, len(b), len(b), CoreFoundation.kCFAllocatorNull
            )
            self.assertIsInstance(s, objc.pyobjc_unicode)
            self.assertEqual(s, "hello world")

            b[0] = "H"

            # The objc_str proxy is immutable
            self.assertEqual(s, "hello world")

            # The changed string can be accessed directly though:
            s = s.nsstring()
            self.assertEqual(s, "Hello world")

            b2 = array.array("u", " " * 40)
            CoreFoundation.CFStringSetExternalCharactersNoCopy(s, b2, len(s), 40)
            self.assertEqual(s, " " * len(b))
            b2[0] = "X"
            self.assertEqual(s, "X" + (" " * (len(b) - 1)))

    def testFunctions(self):
        self.assertNotHasAttr(
            CoreFoundation, "CFStringCreateStringWithValidatedFormatAndArguments"
        )

        v = CoreFoundation.CFStringGetLength("bla bla")
        self.assertEqual(v, 7)

        v = CoreFoundation.CFStringGetCharacterAtIndex("zing", 2)
        self.assertIsInstance(v, str)
        self.assertNotIsInstance(v, objc.pyobjc_unicode)
        self.assertEqual(v, "n")

        v = CoreFoundation.CFStringGetCharacters(
            "foo", CoreFoundation.CFRange(0, 3), None
        )
        self.assertIsInstance(v, str)
        self.assertNotIsInstance(v, objc.pyobjc_unicode)
        self.assertEqual(v, "foo")

        ok, buf = CoreFoundation.CFStringGetCString(
            "sing along", None, 100, CoreFoundation.kCFStringEncodingUTF8
        )
        self.assertTrue(ok)

        # Annoyingly metadata cannot represent the exact interface
        self.assertIsInstance(buf, bytes)
        if b"\0" in buf:
            buf = buf[: buf.index(b"\0")]
        self.assertEqual(buf, b"sing along")
        s = CoreFoundation.CFStringGetCStringPtr(
            "apenootjes", CoreFoundation.kCFStringEncodingASCII
        )
        if s is not objc.NULL:
            self.assertEqual(s, b"apenootjes")
            self.assertIsInstance(s, str)
        s = CoreFoundation.CFStringGetCharactersPtr("apenootjes")
        if s is not objc.NULL:
            self.assertEqual(s, "apenootjes")
            self.assertIsInstance(s, str)
        idx, buf, used = CoreFoundation.CFStringGetBytes(
            "apenootjes",
            CoreFoundation.CFRange(1, 4),
            CoreFoundation.kCFStringEncodingASCII,
            b"\0",
            True,
            None,
            50,
            None,
        )
        self.assertEqual(idx, 4)
        self.assertIsInstance(buf, bytes)
        self.assertEqual(buf, b"peno")
        self.assertEqual(used, 4)

        s = CoreFoundation.CFStringCreateFromExternalRepresentation(
            None, b"hello world", CoreFoundation.kCFStringEncodingUTF8
        )
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertEqual(s, "hello world")

        data = CoreFoundation.CFStringCreateExternalRepresentation(
            None, s, CoreFoundation.kCFStringEncodingUTF16BE, b"\0"
        )
        self.assertIsInstance(data, CoreFoundation.CFDataRef)
        val = CoreFoundation.CFDataGetBytes(
            data, (0, CoreFoundation.CFDataGetLength(data)), None
        )
        self.assertEqual(val, b"\0h\0e\0l\0l\0o\0 \0w\0o\0r\0l\0d")

        v = CoreFoundation.CFStringGetSmallestEncoding(s)
        self.assertIsInstance(v, int)
        v = CoreFoundation.CFStringGetFastestEncoding(s)
        self.assertIsInstance(v, int)
        v = CoreFoundation.CFStringGetSystemEncoding()
        self.assertIsInstance(v, int)
        v = CoreFoundation.CFStringGetMaximumSizeForEncoding(
            100, CoreFoundation.kCFStringEncodingUTF8
        )
        self.assertIsInstance(v, int)
        ok, buf = CoreFoundation.CFStringGetFileSystemRepresentation(
            "/path/to/nowhere.txt", None, 100
        )
        self.assertTrue(ok)
        if b"\0" in buf:
            buf = buf[: buf.index(b"\0")]
        self.assertEqual(buf, b"/path/to/nowhere.txt")
        self.assertIsInstance(buf, bytes)
        idx = CoreFoundation.CFStringGetMaximumSizeOfFileSystemRepresentation("/tmp")
        self.assertIsInstance(idx, int)
        s = CoreFoundation.CFStringCreateWithFileSystemRepresentation(None, b"/tmp")
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertEqual(s, "/tmp")
        self.assertRaises(
            (TypeError, ValueError),
            CoreFoundation.CFStringCreateWithFileSystemRepresentation,
            None,
            "/tmp",
        )

        r = CoreFoundation.CFStringCompareWithOptionsAndLocale(
            "aas",
            "noot",
            CoreFoundation.CFRange(0, 3),
            CoreFoundation.kCFCompareBackwards,
            CoreFoundation.CFLocaleCopyCurrent(),
        )
        self.assertEqual(r, CoreFoundation.kCFCompareLessThan)

        r = CoreFoundation.CFStringCompareWithOptions(
            "aap", "noot", CoreFoundation.CFRange(0, 3), 0
        )
        self.assertEqual(r, CoreFoundation.kCFCompareLessThan)

        r = CoreFoundation.CFStringCompare(
            "aap", "AAP", CoreFoundation.kCFCompareCaseInsensitive
        )
        self.assertEqual(r, CoreFoundation.kCFCompareEqualTo)

        found, rng = CoreFoundation.CFStringFindWithOptionsAndLocale(
            "the longer string",
            "longer",
            CoreFoundation.CFRange(0, 17),
            0,
            CoreFoundation.CFLocaleCopyCurrent(),
            None,
        )
        self.assertIs(found, True)
        self.assertIsInstance(rng, CoreFoundation.CFRange)
        self.assertEqual(rng, CoreFoundation.CFRange(4, 6))

        found, rng = CoreFoundation.CFStringFindWithOptions(
            "the longer string", "longer", CoreFoundation.CFRange(0, 17), 0, None
        )
        self.assertIs(found, True)
        self.assertIsInstance(rng, CoreFoundation.CFRange)
        self.assertEqual(rng, CoreFoundation.CFRange(4, 6))

        arr = CoreFoundation.CFStringCreateArrayWithFindResults(
            None, "word a world a world", "world", CoreFoundation.CFRange(0, 20), 0
        )
        self.assertIsInstance(arr, CoreFoundation.CFArrayRef)
        self.assertEqual(len(arr), 2)

        rng = CoreFoundation.CFStringFind("hello world", "world", 0)
        self.assertEqual(rng, CoreFoundation.CFRange(6, 5))

        ok = CoreFoundation.CFStringHasPrefix("hello", "he")
        self.assertIs(ok, True)
        ok = CoreFoundation.CFStringHasPrefix("hello", "ge")
        self.assertIs(ok, False)
        ok = CoreFoundation.CFStringHasSuffix("hello", "lo")
        self.assertIs(ok, True)
        rng = CoreFoundation.CFStringGetRangeOfComposedCharactersAtIndex(
            "hello world", 5
        )
        self.assertIsInstance(rng, CoreFoundation.CFRange)
        found, rng = CoreFoundation.CFStringFindCharacterFromSet(
            "hello  world",
            CoreFoundation.CFCharacterSetGetPredefined(
                CoreFoundation.kCFCharacterSetWhitespace
            ),
            CoreFoundation.CFRange(0, 12),
            0,
            None,
        )
        self.assertIs(found, True)
        self.assertIsInstance(rng, CoreFoundation.CFRange)
        (
            lineBeginIndex,
            lineEndIndex,
            contentsEndIndex,
        ) = CoreFoundation.CFStringGetLineBounds(
            "hello\n\nworld", CoreFoundation.CFRange(0, 12), None, None, None
        )
        self.assertEqual(lineBeginIndex, 0)
        self.assertEqual(lineEndIndex, 12)
        self.assertEqual(contentsEndIndex, 12)

        (
            paraBeginIndex,
            paraEndIndex,
            contentsEndIndex,
        ) = CoreFoundation.CFStringGetParagraphBounds(  # noqa: B950
            "hello\n\nworld", CoreFoundation.CFRange(0, 12), None, None, None
        )
        self.assertEqual(paraBeginIndex, 0)
        self.assertEqual(paraEndIndex, 12)
        self.assertEqual(contentsEndIndex, 12)

        result = CoreFoundation.CFStringCreateByCombiningStrings(
            None, ["hello", "world"], "//"
        )
        self.assertEqual(result, "hello//world")

        result = CoreFoundation.CFStringCreateArrayBySeparatingStrings(
            None, "hello world", " "
        )
        self.assertEqual(result, ["hello", "world"])

        v = CoreFoundation.CFStringGetIntValue("1000")
        self.assertEqual(v, 1000)

        v = CoreFoundation.CFStringGetDoubleValue("1000")
        self.assertEqual(v, 1000.0)

        v = CoreFoundation.CFStringGetDoubleValue("1000.5")
        self.assertEqual(v, 1000.5)

    def testMutableFunctions(self):
        s = CoreFoundation.CFStringCreateMutable(None, 0)
        s = s.nsstring()
        CoreFoundation.CFStringAppend(s, "hello")
        self.assertEqual(s, "hello")

        s = CoreFoundation.CFStringCreateMutable(None, 0)
        # Ensure that we actually see updates:
        s = s.nsstring()

        CoreFoundation.CFStringAppendCharacters(s, "hel", 3)
        self.assertEqual(s, "hel")

        CoreFoundation.CFStringAppendCString(
            s, b"lo world", CoreFoundation.kCFStringEncodingUTF8
        )
        self.assertEqual(s, "hello world")

        CoreFoundation.CFStringAppendFormat(s, None, ": %s = %d", b"x", 99)
        self.assertEqual(s, "hello world: x = 99")

        self.assertNotHasAttr(CoreFoundation, "CFStringAppendFormatAndArguments")
        CoreFoundation.CFStringInsert(s, 2, "--")
        self.assertEqual(s, "he--llo world: x = 99")

        CoreFoundation.CFStringDelete(s, CoreFoundation.CFRange(0, 8))
        self.assertEqual(s, "world: x = 99")

        CoreFoundation.CFStringReplace(s, CoreFoundation.CFRange(0, 4), "WOR")
        self.assertEqual(s, "WORd: x = 99")

        CoreFoundation.CFStringReplaceAll(s, "WHOOPS")
        self.assertEqual(s, "WHOOPS")

        CoreFoundation.CFStringReplaceAll(s, "BLAblaBLAblaBLA")
        self.assertEqual(s, "BLAblaBLAblaBLA")

        CoreFoundation.CFStringFindAndReplace(
            s, "BL", " fo ", CoreFoundation.CFRange(0, 15), 0
        )
        self.assertEqual(s, " fo Abla fo Abla fo A")

        CoreFoundation.CFStringReplaceAll(s, "abc")
        CoreFoundation.CFStringPad(s, " ", 9, 0)
        self.assertEqual(s, "abc      ")

        CoreFoundation.CFStringReplaceAll(s, "abc")
        CoreFoundation.CFStringPad(s, ". ", 9, 1)
        self.assertEqual(s, "abc . . .")

        CoreFoundation.CFStringReplaceAll(s, "abcdef")
        CoreFoundation.CFStringPad(s, ". ", 3, 0)
        self.assertEqual(s, "abc")

        CoreFoundation.CFStringReplaceAll(s, "aHelloaaa")
        trim_chars = "a"

        # print s
        CoreFoundation.CFStringTrim(s, trim_chars)
        # print s
        # print(s)
        # CoreFoundation.CFShow(s)
        self.assertEqual(s, "Hello")

        CoreFoundation.CFStringReplaceAll(s, "* * * *abc * ")
        trim_chars = "* "

        trim_chars = CoreFoundation.CFStringCreateWithCString(
            None, b"* ", CoreFoundation.kCFStringEncodingASCII
        )
        CoreFoundation.CFStringTrim(s, trim_chars)
        self.assertEqual(s, "*abc ")

        CoreFoundation.CFStringReplaceAll(s, " \tHello world  \t ")
        CoreFoundation.CFStringTrimWhitespace(s)
        self.assertEqual(s, "Hello world")

        CoreFoundation.CFStringReplaceAll(s, "AbC")
        CoreFoundation.CFStringLowercase(s, CoreFoundation.CFLocaleCopyCurrent())
        self.assertEqual(s, "abc")

        CoreFoundation.CFStringReplaceAll(s, "AbC")
        CoreFoundation.CFStringUppercase(s, CoreFoundation.CFLocaleCopyCurrent())
        self.assertEqual(s, "ABC")

        CoreFoundation.CFStringReplaceAll(s, "hello world")
        CoreFoundation.CFStringCapitalize(s, CoreFoundation.CFLocaleCopyCurrent())
        self.assertEqual(s, "Hello World")

        CoreFoundation.CFStringNormalize(s, CoreFoundation.kCFStringNormalizationFormKD)
        self.assertEqual(s, "Hello World")

        CoreFoundation.CFStringFold(
            s,
            CoreFoundation.kCFCompareCaseInsensitive,
            CoreFoundation.CFLocaleCopyCurrent(),
        )
        self.assertEqual(s, "hello world")

        CoreFoundation.CFStringReplaceAll(s, "A C")
        ok, rng = CoreFoundation.CFStringTransform(
            s,
            CoreFoundation.CFRange(0, 3),
            CoreFoundation.kCFStringTransformToXMLHex,
            False,
        )
        self.assertEqual(s, "A C")
        self.assertIs(ok, True)
        self.assertEqual(rng, CoreFoundation.CFRange(0, 3))

    def testStringEncoding(self):
        ok = CoreFoundation.CFStringIsEncodingAvailable(
            CoreFoundation.kCFStringEncodingUTF8
        )
        self.assertIs(ok, True)
        encodings = CoreFoundation.CFStringGetListOfAvailableEncodings()
        self.assertIsInstance(encodings, objc.varlist)
        for e in encodings:
            if e == CoreFoundation.kCFStringEncodingInvalidId:
                break
            self.assertIsInstance(e, int)
        s = CoreFoundation.CFStringGetNameOfEncoding(
            CoreFoundation.kCFStringEncodingUTF8
        )
        self.assertEqual(s, "Unicode (UTF-8)")

        v = CoreFoundation.CFStringConvertEncodingToNSStringEncoding(
            CoreFoundation.kCFStringEncodingUTF8
        )
        self.assertIsInstance(v, int)
        t = CoreFoundation.CFStringConvertNSStringEncodingToEncoding(v)
        self.assertEqual(t, CoreFoundation.kCFStringEncodingUTF8)

        v = CoreFoundation.CFStringConvertEncodingToWindowsCodepage(
            CoreFoundation.kCFStringEncodingISOLatin1
        )
        self.assertIsInstance(v, int)
        t = CoreFoundation.CFStringConvertWindowsCodepageToEncoding(v)
        self.assertEqual(t, CoreFoundation.kCFStringEncodingISOLatin1)

        v = CoreFoundation.CFStringConvertEncodingToIANACharSetName(
            CoreFoundation.kCFStringEncodingUTF8
        )
        self.assertIsInstance(v, str)
        self.assertIn(v, ("UTF-8", "utf-8"))

        t = CoreFoundation.CFStringConvertIANACharSetNameToEncoding(v)
        self.assertEqual(t, CoreFoundation.kCFStringEncodingUTF8)

        v = CoreFoundation.CFStringGetMostCompatibleMacStringEncoding(
            CoreFoundation.kCFStringEncodingWindowsLatin1
        )
        self.assertEqual(v, CoreFoundation.kCFStringEncodingMacRoman)

    def testNoInlineBuffer(self):
        self.assertNotHasAttr(CoreFoundation, "CFStringInlineBuffer")
        self.assertNotHasAttr(CoreFoundation, "CFStringInitInlineBuffer")
        self.assertNotHasAttr(CoreFoundation, "CFStringGetCharacterFromInlineBuffer")

    def testConstants(self):
        self.assertEqual(CoreFoundation.kCFStringEncodingInvalidId, 0xFFFFFFFF)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacRoman, 0)
        self.assertEqual(CoreFoundation.kCFStringEncodingWindowsLatin1, 0x0500)
        self.assertEqual(CoreFoundation.kCFStringEncodingISOLatin1, 0x0201)
        self.assertEqual(CoreFoundation.kCFStringEncodingNextStepLatin, 0x0B01)
        self.assertEqual(CoreFoundation.kCFStringEncodingASCII, 0x0600)
        self.assertEqual(CoreFoundation.kCFStringEncodingUnicode, 0x0100)
        self.assertEqual(CoreFoundation.kCFStringEncodingUTF8, 0x08000100)
        self.assertEqual(CoreFoundation.kCFStringEncodingNonLossyASCII, 0x0BFF)
        self.assertEqual(CoreFoundation.kCFStringEncodingUTF16, 0x0100)
        self.assertEqual(CoreFoundation.kCFStringEncodingUTF16BE, 0x10000100)
        self.assertEqual(CoreFoundation.kCFStringEncodingUTF16LE, 0x14000100)
        self.assertEqual(CoreFoundation.kCFStringEncodingUTF32, 0x0C000100)
        self.assertEqual(CoreFoundation.kCFStringEncodingUTF32BE, 0x18000100)
        self.assertEqual(CoreFoundation.kCFStringEncodingUTF32LE, 0x1C000100)
        self.assertEqual(CoreFoundation.kCFCompareCaseInsensitive, 1)
        self.assertEqual(CoreFoundation.kCFCompareBackwards, 4)
        self.assertEqual(CoreFoundation.kCFCompareAnchored, 8)
        self.assertEqual(CoreFoundation.kCFCompareNonliteral, 16)
        self.assertEqual(CoreFoundation.kCFCompareLocalized, 32)
        self.assertEqual(CoreFoundation.kCFCompareNumerically, 64)
        self.assertEqual(CoreFoundation.kCFCompareDiacriticInsensitive, 128)
        self.assertEqual(CoreFoundation.kCFCompareWidthInsensitive, 256)
        self.assertEqual(CoreFoundation.kCFCompareForcedOrdering, 512)
        self.assertEqual(CoreFoundation.kCFStringNormalizationFormD, 0)
        self.assertEqual(CoreFoundation.kCFStringNormalizationFormKD, 1)
        self.assertEqual(CoreFoundation.kCFStringNormalizationFormC, 2)
        self.assertEqual(CoreFoundation.kCFStringNormalizationFormKC, 3)
        self.assertIsInstance(CoreFoundation.kCFStringTransformStripCombiningMarks, str)
        self.assertIsInstance(CoreFoundation.kCFStringTransformToLatin, str)
        self.assertIsInstance(CoreFoundation.kCFStringTransformFullwidthHalfwidth, str)
        self.assertIsInstance(CoreFoundation.kCFStringTransformLatinKatakana, str)
        self.assertIsInstance(CoreFoundation.kCFStringTransformLatinHiragana, str)
        self.assertIsInstance(CoreFoundation.kCFStringTransformHiraganaKatakana, str)
        self.assertIsInstance(CoreFoundation.kCFStringTransformMandarinLatin, str)
        self.assertIsInstance(CoreFoundation.kCFStringTransformLatinHangul, str)
        self.assertIsInstance(CoreFoundation.kCFStringTransformLatinArabic, str)
        self.assertIsInstance(CoreFoundation.kCFStringTransformLatinHebrew, str)
        self.assertIsInstance(CoreFoundation.kCFStringTransformLatinThai, str)
        self.assertIsInstance(CoreFoundation.kCFStringTransformLatinCyrillic, str)
        self.assertIsInstance(CoreFoundation.kCFStringTransformLatinGreek, str)
        self.assertIsInstance(CoreFoundation.kCFStringTransformToXMLHex, str)
        self.assertIsInstance(CoreFoundation.kCFStringTransformToUnicodeName, str)
        self.assertIsInstance(CoreFoundation.kCFStringTransformStripDiacritics, str)

    def testNoPrivate(self):
        self.assertNotHasAttr(CoreFoundation, "__CFStringMakeConstantString")

    def testCFSTR(self):
        v = CoreFoundation.CFSTR("hello")
        self.assertIsInstance(v, str)


class TestStringEncodingExt(TestCase):
    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(CoreFoundation.kCFStringEncodingUTF7, 0x04000100)
        self.assertEqual(CoreFoundation.kCFStringEncodingUTF7_IMAP, 0x0A10)

    def testConstants(self):
        self.assertEqual(CoreFoundation.kCFStringEncodingMacJapanese, 1)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacChineseTrad, 2)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacKorean, 3)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacArabic, 4)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacHebrew, 5)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacGreek, 6)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacCyrillic, 7)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacDevanagari, 9)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacGurmukhi, 10)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacGujarati, 11)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacOriya, 12)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacBengali, 13)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacTamil, 14)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacTelugu, 15)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacKannada, 16)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacMalayalam, 17)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacSinhalese, 18)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacBurmese, 19)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacKhmer, 20)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacThai, 21)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacLaotian, 22)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacGeorgian, 23)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacArmenian, 24)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacChineseSimp, 25)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacTibetan, 26)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacMongolian, 27)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacEthiopic, 28)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacCentralEurRoman, 29)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacVietnamese, 30)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacExtArabic, 31)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacSymbol, 33)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacDingbats, 34)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacTurkish, 35)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacCroatian, 36)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacIcelandic, 37)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacRomanian, 38)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacCeltic, 39)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacGaelic, 40)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacFarsi, 0x8C)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacUkrainian, 0x98)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacInuit, 0xEC)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacVT100, 0xFC)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacHFS, 0xFF)
        self.assertEqual(CoreFoundation.kCFStringEncodingISOLatin2, 0x0202)
        self.assertEqual(CoreFoundation.kCFStringEncodingISOLatin3, 0x0203)
        self.assertEqual(CoreFoundation.kCFStringEncodingISOLatin4, 0x0204)
        self.assertEqual(CoreFoundation.kCFStringEncodingISOLatinCyrillic, 0x0205)
        self.assertEqual(CoreFoundation.kCFStringEncodingISOLatinArabic, 0x0206)
        self.assertEqual(CoreFoundation.kCFStringEncodingISOLatinGreek, 0x0207)
        self.assertEqual(CoreFoundation.kCFStringEncodingISOLatinHebrew, 0x0208)
        self.assertEqual(CoreFoundation.kCFStringEncodingISOLatin5, 0x0209)
        self.assertEqual(CoreFoundation.kCFStringEncodingISOLatin6, 0x020A)
        self.assertEqual(CoreFoundation.kCFStringEncodingISOLatinThai, 0x020B)
        self.assertEqual(CoreFoundation.kCFStringEncodingISOLatin7, 0x020D)
        self.assertEqual(CoreFoundation.kCFStringEncodingISOLatin8, 0x020E)
        self.assertEqual(CoreFoundation.kCFStringEncodingISOLatin9, 0x020F)
        self.assertEqual(CoreFoundation.kCFStringEncodingISOLatin10, 0x0210)
        self.assertEqual(CoreFoundation.kCFStringEncodingDOSLatinUS, 0x0400)
        self.assertEqual(CoreFoundation.kCFStringEncodingDOSGreek, 0x0405)
        self.assertEqual(CoreFoundation.kCFStringEncodingDOSBalticRim, 0x0406)
        self.assertEqual(CoreFoundation.kCFStringEncodingDOSLatin1, 0x0410)
        self.assertEqual(CoreFoundation.kCFStringEncodingDOSGreek1, 0x0411)
        self.assertEqual(CoreFoundation.kCFStringEncodingDOSLatin2, 0x0412)
        self.assertEqual(CoreFoundation.kCFStringEncodingDOSCyrillic, 0x0413)
        self.assertEqual(CoreFoundation.kCFStringEncodingDOSTurkish, 0x0414)
        self.assertEqual(CoreFoundation.kCFStringEncodingDOSPortuguese, 0x0415)
        self.assertEqual(CoreFoundation.kCFStringEncodingDOSIcelandic, 0x0416)
        self.assertEqual(CoreFoundation.kCFStringEncodingDOSHebrew, 0x0417)
        self.assertEqual(CoreFoundation.kCFStringEncodingDOSCanadianFrench, 0x0418)
        self.assertEqual(CoreFoundation.kCFStringEncodingDOSArabic, 0x0419)
        self.assertEqual(CoreFoundation.kCFStringEncodingDOSNordic, 0x041A)
        self.assertEqual(CoreFoundation.kCFStringEncodingDOSRussian, 0x041B)
        self.assertEqual(CoreFoundation.kCFStringEncodingDOSGreek2, 0x041C)
        self.assertEqual(CoreFoundation.kCFStringEncodingDOSThai, 0x041D)
        self.assertEqual(CoreFoundation.kCFStringEncodingDOSJapanese, 0x0420)
        self.assertEqual(CoreFoundation.kCFStringEncodingDOSChineseSimplif, 0x0421)
        self.assertEqual(CoreFoundation.kCFStringEncodingDOSKorean, 0x0422)
        self.assertEqual(CoreFoundation.kCFStringEncodingDOSChineseTrad, 0x0423)
        self.assertEqual(CoreFoundation.kCFStringEncodingWindowsLatin2, 0x0501)
        self.assertEqual(CoreFoundation.kCFStringEncodingWindowsCyrillic, 0x0502)
        self.assertEqual(CoreFoundation.kCFStringEncodingWindowsGreek, 0x0503)
        self.assertEqual(CoreFoundation.kCFStringEncodingWindowsLatin5, 0x0504)
        self.assertEqual(CoreFoundation.kCFStringEncodingWindowsHebrew, 0x0505)
        self.assertEqual(CoreFoundation.kCFStringEncodingWindowsArabic, 0x0506)
        self.assertEqual(CoreFoundation.kCFStringEncodingWindowsBalticRim, 0x0507)
        self.assertEqual(CoreFoundation.kCFStringEncodingWindowsVietnamese, 0x0508)
        self.assertEqual(CoreFoundation.kCFStringEncodingWindowsKoreanJohab, 0x0510)
        self.assertEqual(CoreFoundation.kCFStringEncodingANSEL, 0x0601)
        self.assertEqual(CoreFoundation.kCFStringEncodingJIS_X0201_76, 0x0620)
        self.assertEqual(CoreFoundation.kCFStringEncodingJIS_X0208_83, 0x0621)
        self.assertEqual(CoreFoundation.kCFStringEncodingJIS_X0208_90, 0x0622)
        self.assertEqual(CoreFoundation.kCFStringEncodingJIS_X0212_90, 0x0623)
        self.assertEqual(CoreFoundation.kCFStringEncodingJIS_C6226_78, 0x0624)
        self.assertEqual(CoreFoundation.kCFStringEncodingShiftJIS_X0213, 0x0628)
        self.assertEqual(
            CoreFoundation.kCFStringEncodingShiftJIS_X0213_MenKuTen, 0x0629
        )
        self.assertEqual(CoreFoundation.kCFStringEncodingGB_2312_80, 0x0630)
        self.assertEqual(CoreFoundation.kCFStringEncodingGBK_95, 0x0631)
        self.assertEqual(CoreFoundation.kCFStringEncodingGB_18030_2000, 0x0632)
        self.assertEqual(CoreFoundation.kCFStringEncodingKSC_5601_87, 0x0640)
        self.assertEqual(CoreFoundation.kCFStringEncodingKSC_5601_92_Johab, 0x0641)
        self.assertEqual(CoreFoundation.kCFStringEncodingCNS_11643_92_P1, 0x0651)
        self.assertEqual(CoreFoundation.kCFStringEncodingCNS_11643_92_P2, 0x0652)
        self.assertEqual(CoreFoundation.kCFStringEncodingCNS_11643_92_P3, 0x0653)
        self.assertEqual(CoreFoundation.kCFStringEncodingISO_2022_JP, 0x0820)
        self.assertEqual(CoreFoundation.kCFStringEncodingISO_2022_JP_2, 0x0821)
        self.assertEqual(CoreFoundation.kCFStringEncodingISO_2022_JP_1, 0x0822)
        self.assertEqual(CoreFoundation.kCFStringEncodingISO_2022_JP_3, 0x0823)
        self.assertEqual(CoreFoundation.kCFStringEncodingISO_2022_CN, 0x0830)
        self.assertEqual(CoreFoundation.kCFStringEncodingISO_2022_CN_EXT, 0x0831)
        self.assertEqual(CoreFoundation.kCFStringEncodingISO_2022_KR, 0x0840)
        self.assertEqual(CoreFoundation.kCFStringEncodingEUC_JP, 0x0920)
        self.assertEqual(CoreFoundation.kCFStringEncodingEUC_CN, 0x0930)
        self.assertEqual(CoreFoundation.kCFStringEncodingEUC_TW, 0x0931)
        self.assertEqual(CoreFoundation.kCFStringEncodingEUC_KR, 0x0940)
        self.assertEqual(CoreFoundation.kCFStringEncodingShiftJIS, 0x0A01)
        self.assertEqual(CoreFoundation.kCFStringEncodingKOI8_R, 0x0A02)
        self.assertEqual(CoreFoundation.kCFStringEncodingBig5, 0x0A03)
        self.assertEqual(CoreFoundation.kCFStringEncodingMacRomanLatin1, 0x0A04)
        self.assertEqual(CoreFoundation.kCFStringEncodingHZ_GB_2312, 0x0A05)
        self.assertEqual(CoreFoundation.kCFStringEncodingBig5_HKSCS_1999, 0x0A06)
        self.assertEqual(CoreFoundation.kCFStringEncodingVISCII, 0x0A07)
        self.assertEqual(CoreFoundation.kCFStringEncodingKOI8_U, 0x0A08)
        self.assertEqual(CoreFoundation.kCFStringEncodingBig5_E, 0x0A09)
        self.assertEqual(CoreFoundation.kCFStringEncodingNextStepJapanese, 0x0B02)
        self.assertEqual(CoreFoundation.kCFStringEncodingEBCDIC_US, 0x0C01)
        self.assertEqual(CoreFoundation.kCFStringEncodingEBCDIC_CP037, 0x0C02)
        self.assertEqual(CoreFoundation.kCFStringEncodingShiftJIS_X0213_00, 0x0628)

    @min_os_level("10.6")
    def testFunctions10_6(self):
        self.assertResultIsBOOL(CoreFoundation.CFStringIsSurrogateHighCharacter)
        self.assertTrue(CoreFoundation.CFStringIsSurrogateHighCharacter(chr(0xD800)))
        self.assertFalse(CoreFoundation.CFStringIsSurrogateHighCharacter(chr(0x0600)))
        self.assertTrue(CoreFoundation.CFStringIsSurrogateLowCharacter(chr(0xDC00)))
        self.assertFalse(CoreFoundation.CFStringIsSurrogateLowCharacter(chr(0x0600)))
        v = CoreFoundation.CFStringGetLongCharacterForSurrogatePair(
            chr(0xD801), chr(0xDC01)
        )
        # self.assertEqual(v, ((1 << 10) | 1) + 0x0010000)
        self.assertEqual(v, 66561)

        self.assertResultIsBOOL(CoreFoundation.CFStringGetSurrogatePairForLongCharacter)
        ok, chars = CoreFoundation.CFStringGetSurrogatePairForLongCharacter(v, None)
        self.assertTrue(ok)

        if sys.version_info[:2] < (3, 3) == 65535:
            # ucs2 build of python 3.2 or earlier:
            self.assertEqual(len(chars), 2)
            self.assertEqual(chars[0], chr(0xD801))
            self.assertEqual(chars[1], chr(0xDC01))

        else:
            # ucs4 build of python 3.2 or earlier; or
            # python 3.3
            #
            # In both cases this function is useless because
            # Python can represent str codepoints without using
            # surrogate pairs, and will do so when converting
            # an array of UCS2 codepoints to a Pytho str object
            pass

    @min_os_level("10.7")
    def testFunctions10_7(self):
        loc = CoreFoundation.CFLocaleCopyCurrent()

        self.assertArgIsOut(CoreFoundation.CFStringGetHyphenationLocationBeforeIndex, 5)
        v, ch = CoreFoundation.CFStringGetHyphenationLocationBeforeIndex(
            "hello world", 5, CoreFoundation.CFRange(0, 10), 0, loc, None
        )
        self.assertIsInstance(v, int)
        self.assertIsInstance(ch, int)

        self.assertResultIsBOOL(CoreFoundation.CFStringIsHyphenationAvailableForLocale)
        v = CoreFoundation.CFStringIsHyphenationAvailableForLocale(loc)
        self.assertIsInstance(v, bool)

    @min_os_level("13.0")
    def test_functions13_0(self):
        self.assertArgIsPrintf(
            CoreFoundation.CFStringCreateStringWithValidatedFormat, 3
        )
        self.assertArgIsOut(CoreFoundation.CFStringCreateStringWithValidatedFormat, 4)
