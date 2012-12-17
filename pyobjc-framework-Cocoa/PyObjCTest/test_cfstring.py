from PyObjCTools.TestSupport import *
import array
from CoreFoundation import *
import CoreFoundation
import sys
import AppKit

try:
    unicode
except NameError:
    unicode = str


try:
    long
except NameError:
    long = int

try:
    unichr
except NameError:
    unichr = chr

try:
    from Foundation import __NSCFString as NSCFString
except ImportError:
    from Foundation import NSCFString


class TestString (TestCase):
    def testType(self):
        self.assertTrue(issubclass(CFStringRef, NSString))

    def testTypeID(self):
        v = CFStringGetTypeID()
        self.assertIsInstance(v, (int, long))

    def testNoPascalStrings(self):
        self.assertNotHasAttr(CoreFoundation, 'CFStringCreateWithPascalString')
        self.assertNotHasAttr(CoreFoundation, 'CFStringCreateWithPascalStringNoCopy')
        self.assertNotHasAttr(CoreFoundation, 'CFStringGetPascalString')
        self.assertNotHasAttr(CoreFoundation, 'CFStringGetPascalStringPtr')
        self.assertNotHasAttr(CoreFoundation, 'CFStringAppendPascalString')

    def testCreation(self):
        s = CFStringCreateWithCString(None, b"hello world", kCFStringEncodingASCII)
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertIsInstance(s, unicode)
        self.assertEqual(s, b"hello world".decode('ascii'))

        s = CFStringCreateWithBytes(None, b"hello world", 5, kCFStringEncodingASCII, False)
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertIsInstance(s, unicode)
        self.assertEqual(s, b"hello".decode('ascii'))

        s = CFStringCreateWithCharacters(None, b"HELLO".decode('ascii'), 5)
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertIsInstance(s, unicode)
        self.assertEqual(s, b"HELLO".decode('ascii'))

        # NOTE: the deallocator must be kCFAllocatorNull
        s = CFStringCreateWithCStringNoCopy(None, b"hello world",
                kCFStringEncodingASCII, kCFAllocatorNull)
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertIsInstance(s, unicode)
        self.assertEqual(s, b"hello world".decode('ascii'))


        s = CFStringCreateWithBytesNoCopy(None, b"hello world", 5, kCFStringEncodingASCII, False, kCFAllocatorNull)
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertIsInstance(s, unicode)
        self.assertEqual(s, b"hello".decode('ascii'))

        s = CFStringCreateWithCharactersNoCopy(None, b"HELLO".decode('ascii'), 5, kCFAllocatorNull)
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertIsInstance(s, unicode)
        self.assertEqual(s, b"HELLO".decode('ascii'))

        del s

        s = CFStringCreateWithSubstring(None,
                b"Hello world".decode('ascii'), CFRange(2, 4))
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertEqual(s, b"Hello world".decode('ascii')[2:6])

        s = CFStringCreateCopy(None, b"foo the bar".decode('ascii'))
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertEqual(s, b"foo the bar".decode('ascii'))

        s = CFStringCreateWithFormat(None, None, "hello %s = %d",
                b"foo", 52)
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertEqual(s, b"hello foo = 52".decode('ascii'))

        self.assertFalse(hasattr(CoreFoundation,
            "CFStringCreateWithFormatAndArguments"))

    def testCreateMutable(self):
        s = CFStringCreateMutable(None, 0)
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertEqual(s, b"".decode('ascii'))

        s = CFStringCreateMutableCopy(None, 0, b"foobar".decode('ascii'))
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertEqual(s, b"foobar".decode('ascii'))

        if sys.version_info[:2] < (3,3):
            # See issue15035 on Python's tracker. There currently is
            # no array format code for UCS2 storage (Python 3.3 or later)
            # Therefore these tests can only work for earlier versions
            # of Python.

            b = array.array('u', b"hello world".decode('latin1'))
            s = CFStringCreateMutableWithExternalCharactersNoCopy(
                    None, b, len(b), len(b), kCFAllocatorNull)
            self.assertIsInstance(s, objc.pyobjc_unicode)
            self.assertEqual(s, b"hello world".decode('ascii'))

            b[0] = b'H'.decode('ascii')


            # The objc_unicode proxy is immutable
            self.assertEqual(s, b"hello world".decode('ascii'))

            # The changed string can be accessed directly though:
            s = s.nsstring()
            self.assertEqual(s, b"Hello world".decode('ascii'))

            b2 = array.array('u', b" ".decode('ascii') * 40)
            CFStringSetExternalCharactersNoCopy(s, b2, len(s), 40)
            self.assertEqual(s, ' ' * len(b))
            b2[0] = b'X'.decode('ascii')
            self.assertEqual(s, 'X' + (' ' * (len(b)-1)))

    def testFunctions(self):
        v = CFStringGetLength(b"bla bla".decode('ascii'))
        self.assertEqual(v, 7)

        v = CFStringGetCharacterAtIndex(b"zing".decode('ascii'), 2)
        self.assertIsInstance(v, unicode)
        self.assertIsNotInstance(v, objc.pyobjc_unicode)
        self.assertEqual(v, b'n'.decode('ascii'))

        v = CFStringGetCharacters(b"foo".decode('ascii'), CFRange(0, 3), None)
        self.assertIsInstance(v, unicode)
        self.assertIsNotInstance(v, objc.pyobjc_unicode)
        self.assertEqual(v, b'foo'.decode('ascii'))

        ok, buf = CFStringGetCString(b"sing along".decode('ascii'), None, 100, kCFStringEncodingUTF8)
        self.assertTrue(ok)

        # Annoyingly metadata cannot represent the exact interface
        self.assertIsInstance(buf, bytes)
        if b'\0' in buf:
            buf = buf[:buf.index(b'\0')]
        self.assertEqual(buf, b'sing along')
        s = CFStringGetCStringPtr(b"apenootjes".decode('ascii'), kCFStringEncodingASCII)
        if s is not objc.NULL:
            self.assertEqual(s, b"apenootjes")
            self.assertIsInstance(s, str)
        s = CFStringGetCharactersPtr(b"apenootjes".decode('ascii'))
        if s is not objc.NULL:
            self.assertEqual(s, "apenootjes")
            self.assertIsInstance(s, unicode)
        idx, buf, used = CFStringGetBytes(b"apenootjes".decode('ascii'),
                CFRange(1, 4), kCFStringEncodingASCII,
                b'\0', True, None, 50, None)
        self.assertEqual(idx, 4)
        self.assertIsInstance(buf, bytes)
        self.assertEqual(buf, b'peno')
        self.assertEqual(used, 4)

        if sys.version_info[0] == 2:
            s = CFStringCreateFromExternalRepresentation(None,
                    buffer('hello world'), kCFStringEncodingUTF8)
        else:
            s = CFStringCreateFromExternalRepresentation(None,
                    b'hello world', kCFStringEncodingUTF8)
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertEqual(s, b"hello world".decode('ascii'))

        data = CFStringCreateExternalRepresentation(None, s,
                kCFStringEncodingUTF16BE, b'\0')
        self.assertIsInstance(data, CFDataRef)
        val = CFDataGetBytes(data, (0, CFDataGetLength(data)), None)
        self.assertEqual(val,
                b'\0h\0e\0l\0l\0o\0 \0w\0o\0r\0l\0d')

        v = CFStringGetSmallestEncoding(s)
        self.assertIsInstance(v, (int, long))
        v = CFStringGetFastestEncoding(s)
        self.assertIsInstance(v, (int, long))
        v = CFStringGetSystemEncoding()
        self.assertIsInstance(v, (int, long))
        v = CFStringGetMaximumSizeForEncoding(100, kCFStringEncodingUTF8)
        self.assertIsInstance(v, (int, long))
        ok, buf = CFStringGetFileSystemRepresentation(b"/path/to/nowhere.txt".decode('ascii'),
                None, 100)
        self.assertTrue(ok)
        if b'\0' in buf:
            buf = buf[:buf.index(b'\0')]
        self.assertEqual(buf, b'/path/to/nowhere.txt')
        self.assertIsInstance(buf, bytes)
        idx = CFStringGetMaximumSizeOfFileSystemRepresentation(b"/tmp".decode('ascii'))
        self.assertIsInstance(idx, (int, long))
        s = CFStringCreateWithFileSystemRepresentation(None, b"/tmp")
        self.assertIsInstance(s, objc.pyobjc_unicode)
        self.assertEqual(s, b"/tmp".decode('ascii'))
        self.assertRaises((TypeError, ValueError),
                CFStringCreateWithFileSystemRepresentation, None, b"/tmp".decode('ascii'))

        r = CFStringCompareWithOptionsAndLocale(
                b"aas".decode('ascii'), b"noot".decode('ascii'),
                CFRange(0, 3),
                kCFCompareBackwards, CFLocaleCopyCurrent())
        self.assertEqual(r, kCFCompareLessThan)

        r = CFStringCompareWithOptions(b"aap".decode('ascii'), b"noot".decode('ascii'), CFRange(0, 3), 0)
        self.assertEqual(r, kCFCompareLessThan)

        r = CFStringCompare(b"aap".decode('ascii'), b"AAP".decode('ascii'), kCFCompareCaseInsensitive)
        self.assertEqual(r, kCFCompareEqualTo)

        found, rng = CFStringFindWithOptionsAndLocale(
                b"the longer string".decode('ascii'), b"longer".decode('ascii'),
                CFRange(0, 17), 0, CFLocaleCopyCurrent(), None)
        self.assertIs(found, True)
        self.assertIsInstance(rng, CFRange)
        self.assertEqual(rng, CFRange(4, 6))

        found, rng = CFStringFindWithOptions(
                b"the longer string".decode('ascii'), b"longer".decode('ascii'),
                CFRange(0, 17), 0, None)
        self.assertIs(found, True)
        self.assertIsInstance(rng, CFRange)
        self.assertEqual(rng, CFRange(4, 6))

        arr = CFStringCreateArrayWithFindResults(
                None, b"word a world a world".decode('ascii'),
                b"world".decode('ascii'), CFRange(0, 20), 0)
        self.assertIsInstance(arr, CFArrayRef)
        self.assertEqual(len(arr), 2)

        rng = CFStringFind("hello world", "world", 0)
        self.assertEqual(rng, CFRange(6, 5))

        ok = CFStringHasPrefix(b"hello".decode('ascii'), b"he".decode('ascii'))
        self.assertIs(ok, True)
        ok = CFStringHasPrefix(b"hello".decode('ascii'), b"ge".decode('ascii'))
        self.assertIs(ok, False)
        ok = CFStringHasSuffix(b"hello".decode('ascii'), "lo")
        self.assertIs(ok, True)
        rng = CFStringGetRangeOfComposedCharactersAtIndex(
                b"hello world".decode('ascii'), 5)
        self.assertIsInstance(rng, CFRange)
        found, rng = CFStringFindCharacterFromSet("hello  world",
                CFCharacterSetGetPredefined(kCFCharacterSetWhitespace),
                CFRange(0, 12), 0, None)
        self.assertIs(found, True)
        self.assertIsInstance(rng, CFRange)
        lineBeginIndex, lineEndIndex, contentsEndIndex = CFStringGetLineBounds(
                b"hello\n\nworld".decode('ascii'), CFRange(0, 12), None, None, None)
        self.assertEqual(lineBeginIndex, 0)
        self.assertEqual(lineEndIndex, 12)
        self.assertEqual(contentsEndIndex, 12)

        paraBeginIndex, paraEndIndex, contentsEndIndex = CFStringGetParagraphBounds(
                b"hello\n\nworld".decode('ascii'), CFRange(0, 12), None, None, None)
        self.assertEqual(paraBeginIndex, 0)
        self.assertEqual(paraEndIndex, 12)
        self.assertEqual(contentsEndIndex, 12)

        result = CFStringCreateByCombiningStrings(None,
                [b"hello".decode('ascii'), b"world".decode('ascii')], "//")
        self.assertEqual(result, b"hello//world".decode('ascii'))

        result = CFStringCreateArrayBySeparatingStrings(None,
                "hello world", " ")
        self.assertEqual(result, ["hello", "world"])

        v = CFStringGetIntValue(b"1000".decode('ascii'))
        self.assertEqual(v, 1000)

        v = CFStringGetDoubleValue(b"1000".decode('ascii'))
        self.assertEqual(v, 1000.0)

        v = CFStringGetDoubleValue(b"1000.5".decode('ascii'))
        self.assertEqual(v, 1000.5)

    def testMutableFunctions(self):
        s = CFStringCreateMutable(None, 0)
        # Ensure that we actually see updates:
        s = s.nsstring()

        CFStringAppendCharacters(s, b"hel".decode('ascii'), 3)
        self.assertEqual(s, b"hel".decode('ascii'))

        CFStringAppendCString(s, b"lo world", kCFStringEncodingUTF8)
        self.assertEqual(s, b"hello world".decode('ascii'))

        CFStringAppendFormat(s, None, ": %s = %d", b"x", 99)
        self.assertEqual(s, b"hello world: x = 99".decode('ascii'))

        self.assertNotHasAttr(CoreFoundation, 'CFStringAppendFormatAndArguments')
        CFStringInsert(s, 2, "--")
        self.assertEqual(s, b"he--llo world: x = 99".decode('ascii'))

        CFStringDelete(s, CFRange(0, 8))
        self.assertEqual(s, b"world: x = 99".decode('ascii'))

        CFStringReplace(s, CFRange(0, 4), "WOR")
        self.assertEqual(s, b"WORd: x = 99".decode('ascii'))

        CFStringReplaceAll(s, "WHOOPS")
        self.assertEqual(s, b"WHOOPS".decode('ascii'))

        CFStringReplaceAll(s, b"BLAblaBLAblaBLA".decode('ascii'))
        self.assertEqual(s, b"BLAblaBLAblaBLA".decode('ascii'))

        CFStringFindAndReplace(s, "BL", " fo ", CFRange(0, 15), 0)
        self.assertEqual(s, " fo Abla fo Abla fo A")

        CFStringReplaceAll(s, b"abc".decode('ascii'))
        CFStringPad(s, " ", 9, 0)
        self.assertEqual(s, b"abc      ".decode('ascii'))

        CFStringReplaceAll(s, b"abc".decode('ascii'))
        CFStringPad(s, ". ", 9, 1)
        self.assertEqual(s, b"abc . . .".decode('ascii'))

        CFStringReplaceAll(s, b"abcdef".decode('ascii'))
        CFStringPad(s, ". ", 3, 0)
        self.assertEqual(s, b"abc".decode('ascii'))

        CFStringReplaceAll(s, b"aHelloaaa".decode('ascii'))
        trim_chars = b'a'.decode('ascii')

        #print s
        CFStringTrim(s, trim_chars)
        #print s
        self.assertEqual(s, b"Hello".decode('ascii'))

        CFStringReplaceAll(s, b"* * * *abc * ".decode('ascii'))
        trim_chars = b'* '.decode('ascii')

        trim_chars = CFStringCreateWithCString(None, b"* ", kCFStringEncodingASCII)
        CFStringTrim(s, trim_chars)
        self.assertEqual(s, b"*abc ".decode('ascii'))


        CFStringReplaceAll(s, b" \tHello world  \t ".decode('ascii'))
        CFStringTrimWhitespace(s)
        self.assertEqual(s, b"Hello world".decode('ascii'))


        CFStringReplaceAll(s, b"AbC".decode('ascii'))
        CFStringLowercase(s, CFLocaleCopyCurrent())
        self.assertEqual(s, b'abc'.decode('ascii'))

        CFStringReplaceAll(s, b"AbC".decode('ascii'))
        CFStringUppercase(s, CFLocaleCopyCurrent())
        self.assertEqual(s, b'ABC'.decode('ascii'))

        CFStringReplaceAll(s, b"hello world".decode('ascii'))
        CFStringCapitalize(s, CFLocaleCopyCurrent())
        self.assertEqual(s, b'Hello World'.decode('ascii'))

        CFStringNormalize(s, kCFStringNormalizationFormKD)
        self.assertEqual(s, b'Hello World'.decode('ascii'))

        CFStringFold(s, kCFCompareCaseInsensitive, CFLocaleCopyCurrent())
        self.assertEqual(s, b'hello world'.decode('ascii'))

        CFStringReplaceAll(s, b"A C".decode('ascii'))
        ok, rng = CFStringTransform(s, CFRange(0, 3), kCFStringTransformToXMLHex,
                                        False)
        self.assertEqual(s, 'A C')
        self.assertIs(ok, True)
        self.assertEqual(rng, CFRange(0, 3))

    def testStringEncoding(self):
        ok = CFStringIsEncodingAvailable(kCFStringEncodingUTF8)
        self.assertIs(ok, True)
        encodings = CFStringGetListOfAvailableEncodings()
        self.assertIsInstance(encodings, objc.varlist)
        for e in encodings:
            if e == kCFStringEncodingInvalidId:
                break
            self.assertIsInstance(e, (int, long))
        s = CFStringGetNameOfEncoding(kCFStringEncodingUTF8)
        self.assertEqual(s, 'Unicode (UTF-8)')

        v = CFStringConvertEncodingToNSStringEncoding(kCFStringEncodingUTF8)
        self.assertIsInstance(v, (int, long))
        t = CFStringConvertNSStringEncodingToEncoding(v)
        self.assertEqual(t, kCFStringEncodingUTF8)

        v = CFStringConvertEncodingToWindowsCodepage(kCFStringEncodingISOLatin1)
        self.assertIsInstance(v, (int, long))
        t = CFStringConvertWindowsCodepageToEncoding(v)
        self.assertEqual(t, kCFStringEncodingISOLatin1)

        v = CFStringConvertEncodingToIANACharSetName(kCFStringEncodingUTF8)
        self.assertIsInstance(v, unicode)
        self.assertIn(v, ('UTF-8', 'utf-8'))

        t = CFStringConvertIANACharSetNameToEncoding(v)
        self.assertEqual(t, kCFStringEncodingUTF8)

        v = CFStringGetMostCompatibleMacStringEncoding(kCFStringEncodingWindowsLatin1)
        self.assertEqual(v, kCFStringEncodingMacRoman)

    def testNoInlineBuffer(self):
        self.assertNotHasAttr(CoreFoundation, 'CFStringInlineBuffer')
        self.assertNotHasAttr(CoreFoundation, 'CFStringInitInlineBuffer')
        self.assertNotHasAttr(CoreFoundation, 'CFStringGetCharacterFromInlineBuffer')

    def testConstants(self):
        self.assertEqual(kCFStringEncodingInvalidId , 0xffffffff)
        self.assertEqual(kCFStringEncodingMacRoman , 0)
        self.assertEqual(kCFStringEncodingWindowsLatin1 , 0x0500)
        self.assertEqual(kCFStringEncodingISOLatin1 , 0x0201)
        self.assertEqual(kCFStringEncodingNextStepLatin , 0x0B01)
        self.assertEqual(kCFStringEncodingASCII , 0x0600)
        self.assertEqual(kCFStringEncodingUnicode , 0x0100)
        self.assertEqual(kCFStringEncodingUTF8 , 0x08000100)
        self.assertEqual(kCFStringEncodingNonLossyASCII , 0x0BFF)
        self.assertEqual(kCFStringEncodingUTF16 , 0x0100)
        self.assertEqual(kCFStringEncodingUTF16BE , 0x10000100)
        self.assertEqual(kCFStringEncodingUTF16LE , 0x14000100)
        self.assertEqual(kCFStringEncodingUTF32 , 0x0c000100)
        self.assertEqual(kCFStringEncodingUTF32BE , 0x18000100)
        self.assertEqual(kCFStringEncodingUTF32LE , 0x1c000100)
        self.assertEqual(kCFCompareCaseInsensitive , 1)
        self.assertEqual(kCFCompareBackwards , 4)
        self.assertEqual(kCFCompareAnchored , 8)
        self.assertEqual(kCFCompareNonliteral , 16)
        self.assertEqual(kCFCompareLocalized , 32)
        self.assertEqual(kCFCompareNumerically , 64)
        self.assertEqual(kCFCompareDiacriticInsensitive , 128)
        self.assertEqual(kCFCompareWidthInsensitive , 256)
        self.assertEqual(kCFCompareForcedOrdering , 512)
        self.assertEqual(kCFStringNormalizationFormD , 0)
        self.assertEqual(kCFStringNormalizationFormKD , 1)
        self.assertEqual(kCFStringNormalizationFormC , 2)
        self.assertEqual(kCFStringNormalizationFormKC , 3)
        self.assertIsInstance(kCFStringTransformStripCombiningMarks, unicode)
        self.assertIsInstance(kCFStringTransformToLatin, unicode)
        self.assertIsInstance(kCFStringTransformFullwidthHalfwidth, unicode)
        self.assertIsInstance(kCFStringTransformLatinKatakana, unicode)
        self.assertIsInstance(kCFStringTransformLatinHiragana, unicode)
        self.assertIsInstance(kCFStringTransformHiraganaKatakana, unicode)
        self.assertIsInstance(kCFStringTransformMandarinLatin, unicode)
        self.assertIsInstance(kCFStringTransformLatinHangul, unicode)
        self.assertIsInstance(kCFStringTransformLatinArabic, unicode)
        self.assertIsInstance(kCFStringTransformLatinHebrew, unicode)
        self.assertIsInstance(kCFStringTransformLatinThai, unicode)
        self.assertIsInstance(kCFStringTransformLatinCyrillic, unicode)
        self.assertIsInstance(kCFStringTransformLatinGreek, unicode)
        self.assertIsInstance(kCFStringTransformToXMLHex, unicode)
        self.assertIsInstance(kCFStringTransformToUnicodeName, unicode)
        self.assertIsInstance(kCFStringTransformStripDiacritics, unicode)

    def testNoPrivate(self):
        self.assertNotHasAttr(CoreFoundation, '__CFStringMakeConstantString')

    def testCFSTR(self):
        v = CFSTR(b"hello".decode('ascii'))
        self.assertIsInstance(v, unicode)

class TestStringEncodingExt (TestCase):
    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(kCFStringEncodingUTF7, 0x04000100)
        self.assertEqual(kCFStringEncodingUTF7_IMAP, 0x0A10)

    def testConstants(self):
        self.assertEqual(kCFStringEncodingMacJapanese , 1 )
        self.assertEqual(kCFStringEncodingMacChineseTrad , 2 )
        self.assertEqual(kCFStringEncodingMacKorean , 3 )
        self.assertEqual(kCFStringEncodingMacArabic , 4 )
        self.assertEqual(kCFStringEncodingMacHebrew , 5 )
        self.assertEqual(kCFStringEncodingMacGreek , 6 )
        self.assertEqual(kCFStringEncodingMacCyrillic , 7 )
        self.assertEqual(kCFStringEncodingMacDevanagari , 9 )
        self.assertEqual(kCFStringEncodingMacGurmukhi , 10 )
        self.assertEqual(kCFStringEncodingMacGujarati , 11 )
        self.assertEqual(kCFStringEncodingMacOriya , 12 )
        self.assertEqual(kCFStringEncodingMacBengali , 13 )
        self.assertEqual(kCFStringEncodingMacTamil , 14 )
        self.assertEqual(kCFStringEncodingMacTelugu , 15 )
        self.assertEqual(kCFStringEncodingMacKannada , 16 )
        self.assertEqual(kCFStringEncodingMacMalayalam , 17 )
        self.assertEqual(kCFStringEncodingMacSinhalese , 18 )
        self.assertEqual(kCFStringEncodingMacBurmese , 19 )
        self.assertEqual(kCFStringEncodingMacKhmer , 20 )
        self.assertEqual(kCFStringEncodingMacThai , 21 )
        self.assertEqual(kCFStringEncodingMacLaotian , 22 )
        self.assertEqual(kCFStringEncodingMacGeorgian , 23 )
        self.assertEqual(kCFStringEncodingMacArmenian , 24 )
        self.assertEqual(kCFStringEncodingMacChineseSimp , 25 )
        self.assertEqual(kCFStringEncodingMacTibetan , 26 )
        self.assertEqual(kCFStringEncodingMacMongolian , 27 )
        self.assertEqual(kCFStringEncodingMacEthiopic , 28 )
        self.assertEqual(kCFStringEncodingMacCentralEurRoman , 29 )
        self.assertEqual(kCFStringEncodingMacVietnamese , 30 )
        self.assertEqual(kCFStringEncodingMacExtArabic , 31 )
        self.assertEqual(kCFStringEncodingMacSymbol , 33 )
        self.assertEqual(kCFStringEncodingMacDingbats , 34 )
        self.assertEqual(kCFStringEncodingMacTurkish , 35 )
        self.assertEqual(kCFStringEncodingMacCroatian , 36 )
        self.assertEqual(kCFStringEncodingMacIcelandic , 37 )
        self.assertEqual(kCFStringEncodingMacRomanian , 38 )
        self.assertEqual(kCFStringEncodingMacCeltic , 39 )
        self.assertEqual(kCFStringEncodingMacGaelic , 40, )
        self.assertEqual(kCFStringEncodingMacFarsi , 0x8C )
        self.assertEqual(kCFStringEncodingMacUkrainian , 0x98 )
        self.assertEqual(kCFStringEncodingMacInuit , 0xEC )
        self.assertEqual(kCFStringEncodingMacVT100 , 0xFC )
        self.assertEqual(kCFStringEncodingMacHFS , 0xFF )
        self.assertEqual(kCFStringEncodingISOLatin2 , 0x0202 )
        self.assertEqual(kCFStringEncodingISOLatin3 , 0x0203 )
        self.assertEqual(kCFStringEncodingISOLatin4 , 0x0204 )
        self.assertEqual(kCFStringEncodingISOLatinCyrillic , 0x0205 )
        self.assertEqual(kCFStringEncodingISOLatinArabic , 0x0206 )
        self.assertEqual(kCFStringEncodingISOLatinGreek , 0x0207 )
        self.assertEqual(kCFStringEncodingISOLatinHebrew , 0x0208 )
        self.assertEqual(kCFStringEncodingISOLatin5 , 0x0209 )
        self.assertEqual(kCFStringEncodingISOLatin6 , 0x020A )
        self.assertEqual(kCFStringEncodingISOLatinThai , 0x020B )
        self.assertEqual(kCFStringEncodingISOLatin7 , 0x020D )
        self.assertEqual(kCFStringEncodingISOLatin8 , 0x020E )
        self.assertEqual(kCFStringEncodingISOLatin9 , 0x020F )
        self.assertEqual(kCFStringEncodingISOLatin10 , 0x0210 )
        self.assertEqual(kCFStringEncodingDOSLatinUS , 0x0400 )
        self.assertEqual(kCFStringEncodingDOSGreek , 0x0405 )
        self.assertEqual(kCFStringEncodingDOSBalticRim , 0x0406 )
        self.assertEqual(kCFStringEncodingDOSLatin1 , 0x0410 )
        self.assertEqual(kCFStringEncodingDOSGreek1 , 0x0411 )
        self.assertEqual(kCFStringEncodingDOSLatin2 , 0x0412 )
        self.assertEqual(kCFStringEncodingDOSCyrillic , 0x0413 )
        self.assertEqual(kCFStringEncodingDOSTurkish , 0x0414 )
        self.assertEqual(kCFStringEncodingDOSPortuguese , 0x0415 )
        self.assertEqual(kCFStringEncodingDOSIcelandic , 0x0416 )
        self.assertEqual(kCFStringEncodingDOSHebrew , 0x0417 )
        self.assertEqual(kCFStringEncodingDOSCanadianFrench , 0x0418 )
        self.assertEqual(kCFStringEncodingDOSArabic , 0x0419 )
        self.assertEqual(kCFStringEncodingDOSNordic , 0x041A )
        self.assertEqual(kCFStringEncodingDOSRussian , 0x041B )
        self.assertEqual(kCFStringEncodingDOSGreek2 , 0x041C )
        self.assertEqual(kCFStringEncodingDOSThai , 0x041D )
        self.assertEqual(kCFStringEncodingDOSJapanese , 0x0420 )
        self.assertEqual(kCFStringEncodingDOSChineseSimplif , 0x0421 )
        self.assertEqual(kCFStringEncodingDOSKorean , 0x0422 )
        self.assertEqual(kCFStringEncodingDOSChineseTrad , 0x0423 )
        self.assertEqual(kCFStringEncodingWindowsLatin2 , 0x0501 )
        self.assertEqual(kCFStringEncodingWindowsCyrillic , 0x0502 )
        self.assertEqual(kCFStringEncodingWindowsGreek , 0x0503 )
        self.assertEqual(kCFStringEncodingWindowsLatin5 , 0x0504 )
        self.assertEqual(kCFStringEncodingWindowsHebrew , 0x0505 )
        self.assertEqual(kCFStringEncodingWindowsArabic , 0x0506 )
        self.assertEqual(kCFStringEncodingWindowsBalticRim , 0x0507 )
        self.assertEqual(kCFStringEncodingWindowsVietnamese , 0x0508 )
        self.assertEqual(kCFStringEncodingWindowsKoreanJohab , 0x0510 )
        self.assertEqual(kCFStringEncodingANSEL , 0x0601 )
        self.assertEqual(kCFStringEncodingJIS_X0201_76 , 0x0620 )
        self.assertEqual(kCFStringEncodingJIS_X0208_83 , 0x0621 )
        self.assertEqual(kCFStringEncodingJIS_X0208_90 , 0x0622 )
        self.assertEqual(kCFStringEncodingJIS_X0212_90 , 0x0623 )
        self.assertEqual(kCFStringEncodingJIS_C6226_78 , 0x0624 )
        self.assertEqual(kCFStringEncodingShiftJIS_X0213 , 0x0628 )
        self.assertEqual(kCFStringEncodingShiftJIS_X0213_MenKuTen , 0x0629 )
        self.assertEqual(kCFStringEncodingGB_2312_80 , 0x0630 )
        self.assertEqual(kCFStringEncodingGBK_95 , 0x0631 )
        self.assertEqual(kCFStringEncodingGB_18030_2000 , 0x0632 )
        self.assertEqual(kCFStringEncodingKSC_5601_87 , 0x0640 )
        self.assertEqual(kCFStringEncodingKSC_5601_92_Johab , 0x0641 )
        self.assertEqual(kCFStringEncodingCNS_11643_92_P1 , 0x0651 )
        self.assertEqual(kCFStringEncodingCNS_11643_92_P2 , 0x0652 )
        self.assertEqual(kCFStringEncodingCNS_11643_92_P3 , 0x0653 )
        self.assertEqual(kCFStringEncodingISO_2022_JP , 0x0820 )
        self.assertEqual(kCFStringEncodingISO_2022_JP_2 , 0x0821 )
        self.assertEqual(kCFStringEncodingISO_2022_JP_1 , 0x0822 )
        self.assertEqual(kCFStringEncodingISO_2022_JP_3 , 0x0823 )
        self.assertEqual(kCFStringEncodingISO_2022_CN , 0x0830 )
        self.assertEqual(kCFStringEncodingISO_2022_CN_EXT , 0x0831 )
        self.assertEqual(kCFStringEncodingISO_2022_KR , 0x0840 )
        self.assertEqual(kCFStringEncodingEUC_JP , 0x0920 )
        self.assertEqual(kCFStringEncodingEUC_CN , 0x0930 )
        self.assertEqual(kCFStringEncodingEUC_TW , 0x0931 )
        self.assertEqual(kCFStringEncodingEUC_KR , 0x0940 )
        self.assertEqual(kCFStringEncodingShiftJIS , 0x0A01 )
        self.assertEqual(kCFStringEncodingKOI8_R , 0x0A02 )
        self.assertEqual(kCFStringEncodingBig5 , 0x0A03 )
        self.assertEqual(kCFStringEncodingMacRomanLatin1 , 0x0A04 )
        self.assertEqual(kCFStringEncodingHZ_GB_2312 , 0x0A05 )
        self.assertEqual(kCFStringEncodingBig5_HKSCS_1999 , 0x0A06 )
        self.assertEqual(kCFStringEncodingVISCII , 0x0A07 )
        self.assertEqual(kCFStringEncodingKOI8_U , 0x0A08 )
        self.assertEqual(kCFStringEncodingBig5_E , 0x0A09 )
        self.assertEqual(kCFStringEncodingNextStepJapanese , 0x0B02 )
        self.assertEqual(kCFStringEncodingEBCDIC_US , 0x0C01 )
        self.assertEqual(kCFStringEncodingEBCDIC_CP037 , 0x0C02 )
        self.assertEqual(kCFStringEncodingShiftJIS_X0213_00 , 0x0628 )

    @min_os_level('10.6')
    def testFunctions10_6(self):
        self.assertResultIsBOOL(CFStringIsSurrogateHighCharacter)
        self.assertTrue(CFStringIsSurrogateHighCharacter(unichr(0xD800)))
        self.assertFalse(CFStringIsSurrogateHighCharacter(unichr(0x0600)))
        self.assertTrue(CFStringIsSurrogateLowCharacter(unichr(0xDC00)))
        self.assertFalse(CFStringIsSurrogateLowCharacter(unichr(0x0600)))
        v = CFStringGetLongCharacterForSurrogatePair(
                unichr(0xD801), unichr(0xDC01))
        #self.assertEqual(v, ((1 << 10) | 1) + 0x0010000)
        self.assertEqual(v, 66561)

        self.assertResultIsBOOL(CFStringGetSurrogatePairForLongCharacter)
        ok, chars = CFStringGetSurrogatePairForLongCharacter(v, None)
        self.assertTrue(ok)

        if sys.version_info[:2] < (3,3) == 65535:
            # ucs2 build of python 3.2 or earlier:
            self.assertEqual(len(chars), 2)
            self.assertEqual(chars[0], unichr(0xD801))
            self.assertEqual(chars[1], unichr(0xDC01))

        else:
            # ucs4 build of python 3.2 or earlier; or
            # python 3.3
            #
            # In both cases this function is useless because
            # Python can represent unicode codepoints without using
            # surrogate pairs, and will do so when converting
            # an array of UCS2 codepoints to a Pytho unicode object
            pass

    @min_os_level('10.7')
    def testFunctions10_7(self):
        loc = CFLocaleCopyCurrent()

        self.assertArgIsOut(CFStringGetHyphenationLocationBeforeIndex, 5)
        v, ch = CFStringGetHyphenationLocationBeforeIndex(b"hello world".decode('ascii'), 5, CFRange(0, 10), 0, loc, None)
        self.assertIsInstance(v, (int, long))
        self.assertIsInstance(ch, (int, long))

        self.assertResultIsBOOL(CFStringIsHyphenationAvailableForLocale)
        v = CFStringIsHyphenationAvailableForLocale(loc)
        self.assertIsInstance(v, bool)




if __name__ == "__main__":
    main()
