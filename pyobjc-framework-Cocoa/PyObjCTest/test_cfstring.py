from PyObjCTools.TestSupport import *
import array
from CoreFoundation import *
import CoreFoundation
from Foundation import NSCFString


class TestString (TestCase):
    def testType(self):
        self.failUnless(CFStringRef is NSCFString)

    def testTypeID(self):
        v = CFStringGetTypeID()
        self.failUnless(isinstance(v, (int, long)))

    def testNoPascalStrings(self):
        self.failIf(hasattr(CoreFoundation, 'CFStringCreateWithPascalString'))
        self.failIf(hasattr(CoreFoundation, 'CFStringCreateWithPascalStringNoCopy'))
        self.failIf(hasattr(CoreFoundation, 'CFStringGetPascalString'))
        self.failIf(hasattr(CoreFoundation, 'CFStringGetPascalStringPtr'))
        self.failIf(hasattr(CoreFoundation, 'CFStringAppendPascalString'))

    def testCreation(self):
        s = CFStringCreateWithCString(None, "hello world", kCFStringEncodingASCII)
        self.failUnless(isinstance(s, objc.pyobjc_unicode))
        self.failUnless(isinstance(s, unicode))
        self.assertEquals(s, u"hello world")

        s = CFStringCreateWithBytes(None, "hello world", 5, kCFStringEncodingASCII, False)
        self.failUnless(isinstance(s, objc.pyobjc_unicode))
        self.failUnless(isinstance(s, unicode))
        self.assertEquals(s, u"hello")

        s = CFStringCreateWithCharacters(None, u"HELLO", 5)
        self.failUnless(isinstance(s, objc.pyobjc_unicode))
        self.failUnless(isinstance(s, unicode))
        self.assertEquals(s, u"HELLO")

        # NOTE: the deallocator must be kCFAllocatorNull
        s = CFStringCreateWithCStringNoCopy(None, "hello world", 
                kCFStringEncodingASCII, kCFAllocatorNull)
        self.failUnless(isinstance(s, objc.pyobjc_unicode))
        self.failUnless(isinstance(s, unicode))
        self.assertEquals(s, u"hello world")

        
        s = CFStringCreateWithBytesNoCopy(None, "hello world", 5, kCFStringEncodingASCII, False, kCFAllocatorNull)
        self.failUnless(isinstance(s, objc.pyobjc_unicode))
        self.failUnless(isinstance(s, unicode))
        self.assertEquals(s, u"hello")

        s = CFStringCreateWithCharactersNoCopy(None, u"HELLO", 5, kCFAllocatorNull)
        self.failUnless(isinstance(s, objc.pyobjc_unicode))
        self.failUnless(isinstance(s, unicode))
        self.assertEquals(s, u"HELLO")

        del s

        s = CFStringCreateWithSubstring(None,
                u"Hello world", CFRange(2, 4))
        self.failUnless(isinstance(s, objc.pyobjc_unicode))
        self.assertEquals(s, u"Hello world"[2:6])

        s = CFStringCreateCopy(None, u"foo the bar")
        self.failUnless(isinstance(s, objc.pyobjc_unicode))
        self.assertEquals(s, u"foo the bar")

        s = CFStringCreateWithFormat(None, None, "hello %s = %d",
                "foo", 52)
        self.failUnless(isinstance(s, objc.pyobjc_unicode))
        self.assertEquals(s, u"hello foo = 52")

        self.failIf(hasattr(CoreFoundation, 
            "CFStringCreateWithFormatAndArguments"))

    def testCreateMutable(self):
        s = CFStringCreateMutable(None, 0)
        self.failUnless(isinstance(s, objc.pyobjc_unicode))
        self.assertEquals(s, u"")

        s = CFStringCreateMutableCopy(None, 0, u"foobar")
        self.failUnless(isinstance(s, objc.pyobjc_unicode))
        self.assertEquals(s, u"foobar")

        b = array.array('u', u"hello world")
        s = CFStringCreateMutableWithExternalCharactersNoCopy(
                None, b, len(b), len(b), kCFAllocatorNull)
        self.failUnless(isinstance(s, objc.pyobjc_unicode))
        self.assertEquals(s, u"hello world")

        b[0] = u'H'


        # The objc_unicode proxy is immutable
        self.assertEquals(s, u"hello world")

        # The changed string can be accessed directly though:
        s = s.nsstring()
        self.assertEquals(s, u"Hello world")

        b2 = array.array('u', u" " * 40)
        CFStringSetExternalCharactersNoCopy(s, b2, len(s), 40)
        self.assertEquals(s, ' ' * len(b))
        b2[0] = u'X'
        self.assertEquals(s, 'X' + (' ' * (len(b)-1)))

    def testFunctions(self):
        v = CFStringGetLength(u"bla bla")
        self.assertEquals(v, 7)

        v = CFStringGetCharacterAtIndex(u"zing", 2)
        self.failUnless(isinstance(v, unicode))
        self.failIf(isinstance(v, objc.pyobjc_unicode))
        self.assertEquals(v, u'n')

        v = CFStringGetCharacters(u"foo", CFRange(0, 3), None)
        self.failUnless(isinstance(v, unicode))
        self.failIf(isinstance(v, objc.pyobjc_unicode))
        self.assertEquals(v, u'foo')

        ok, buf = CFStringGetCString(u"sing along", None, 100, kCFStringEncodingUTF8)
        self.failUnless(ok)

        # Annoyingly metadata cannot represent the exact interface
        if '\0' in buf:
            buf = buf[:buf.index('\0')]
        self.assertEquals(buf, 'sing along')
        self.failUnless(isinstance(buf, str))

        s = CFStringGetCStringPtr(u"apenootjes", kCFStringEncodingASCII)
        if s is not objc.NULL:
            self.assertEquals(s, "apenootjes")
            self.failUnless(isinstance(s, str))

        s = CFStringGetCharactersPtr(u"apenootjes")
        if s is not objc.NULL:
            self.assertEquals(s, "apenootjes")
            self.failUnless(isinstance(s, unicode))

        idx, buf, used = CFStringGetBytes(u"apenootjes",
                CFRange(1, 4), kCFStringEncodingASCII,
                chr(0), True, None, 50, None)
        self.assertEquals(idx, 4)
        self.failUnless(isinstance(buf, str))
        self.assertEquals(buf, 'peno')
        self.assertEquals(used, 4)

        s = CFStringCreateFromExternalRepresentation(None,
                buffer('hello world'), kCFStringEncodingUTF8)
        self.failUnless(isinstance(s, objc.pyobjc_unicode))
        self.assertEquals(s, u"hello world")

        data = CFStringCreateExternalRepresentation(None, s, 
                kCFStringEncodingUTF16BE, chr(0))
        self.failUnless(isinstance(data, CFDataRef))
        val = CFDataGetBytes(data, (0, CFDataGetLength(data)), None)
        self.assertEquals(val, 
                '\0h\0e\0l\0l\0o\0 \0w\0o\0r\0l\0d')

        v = CFStringGetSmallestEncoding(s)
        self.failUnless(isinstance(v, (int, long)))
        v = CFStringGetFastestEncoding(s)
        self.failUnless(isinstance(v, (int, long)))
        v = CFStringGetSystemEncoding()
        self.failUnless(isinstance(v, (int, long)))
        v = CFStringGetMaximumSizeForEncoding(100, kCFStringEncodingUTF8)
        self.failUnless(isinstance(v, (int, long)))

        ok, buf = CFStringGetFileSystemRepresentation(u"/path/to/nowhere.txt",
                None, 100)
        self.failUnless(ok)
        if '\0' in buf:
            buf = buf[:buf.index('\0')]
        self.assertEquals(buf, '/path/to/nowhere.txt')
        self.failUnless(isinstance(buf, str))

        idx = CFStringGetMaximumSizeOfFileSystemRepresentation(u"/tmp")
        self.failUnless(isinstance(idx, (int, long)))

        s = CFStringCreateWithFileSystemRepresentation(None, "/tmp")
        self.failUnless(isinstance(s, objc.pyobjc_unicode))
        self.assertEquals(s, u"/tmp")
        self.assertRaises((TypeError, ValueError),
                CFStringCreateWithFileSystemRepresentation, None, u"/tmp")


        r = CFStringCompareWithOptionsAndLocale(
                u"aas", u"noot", 
                CFRange(0, 3),
                kCFCompareBackwards, CFLocaleCopyCurrent())
        self.assertEquals(r, kCFCompareLessThan)

        r = CFStringCompareWithOptions(u"aap", u"noot", CFRange(0, 3), 0)
        self.assertEquals(r, kCFCompareLessThan)

        r = CFStringCompare(u"aap", u"AAP", kCFCompareCaseInsensitive)
        self.assertEquals(r, kCFCompareEqualTo)

        found, rng = CFStringFindWithOptionsAndLocale(
                u"the longer string", u"longer",
                CFRange(0, 17), 0, CFLocaleCopyCurrent(), None)
        self.failUnless(found is True)
        self.failUnless(isinstance(rng, CFRange))
        self.assertEquals(rng, CFRange(4, 6))

        found, rng = CFStringFindWithOptions(
                u"the longer string", u"longer",
                CFRange(0, 17), 0, None)
        self.failUnless(found is True)
        self.failUnless(isinstance(rng, CFRange))
        self.assertEquals(rng, CFRange(4, 6))

        arr = CFStringCreateArrayWithFindResults(
                None, u"word a world a world",
                u"world", CFRange(0, 20), 0)
        self.failUnless(isinstance(arr, CFArrayRef))
        self.assertEquals(len(arr), 2)

        rng = CFStringFind("hello world", "world", 0)
        self.assertEquals(rng, CFRange(6, 5))

        ok = CFStringHasPrefix(u"hello", u"he")
        self.failUnless(ok is True)
        ok = CFStringHasPrefix(u"hello", u"ge")
        self.failUnless(ok is False)

        ok = CFStringHasSuffix(u"hello", "lo")
        self.failUnless(ok is True)

        rng = CFStringGetRangeOfComposedCharactersAtIndex(
                u"hello world", 5)
        self.failUnless(isinstance(rng, CFRange))

        found, rng = CFStringFindCharacterFromSet("hello  world",
                CFCharacterSetGetPredefined(kCFCharacterSetWhitespace),
                CFRange(0, 12), 0, None)
        self.failUnless(found is True)
        self.failUnless(isinstance(rng, CFRange))

        lineBeginIndex, lineEndIndex, contentsEndIndex = CFStringGetLineBounds(
                u"hello\n\nworld", CFRange(0, 12), None, None, None)
        self.assertEquals(lineBeginIndex, 0)
        self.assertEquals(lineEndIndex, 12)
        self.assertEquals(contentsEndIndex, 12)

        paraBeginIndex, paraEndIndex, contentsEndIndex = CFStringGetParagraphBounds(
                u"hello\n\nworld", CFRange(0, 12), None, None, None)
        self.assertEquals(paraBeginIndex, 0)
        self.assertEquals(paraEndIndex, 12)
        self.assertEquals(contentsEndIndex, 12)

        result = CFStringCreateByCombiningStrings(None,
                [u"hello", u"world"], "//")
        self.assertEquals(result, u"hello//world")

        result = CFStringCreateArrayBySeparatingStrings(None,
                "hello world", " ")
        self.assertEquals(result, ["hello", "world"])

        v = CFStringGetIntValue(u"1000")
        self.assertEquals(v, 1000)

        v = CFStringGetDoubleValue(u"1000")
        self.assertEquals(v, 1000.0)

        v = CFStringGetDoubleValue(u"1000.5")
        self.assertEquals(v, 1000.5)

    def testMutableFunctions(self):
        s = CFStringCreateMutable(None, 0)
        # Ensure that we actually see updates:
        s = s.nsstring()

        CFStringAppendCharacters(s, u"hel", 3)
        self.assertEquals(s, u"hel")

        CFStringAppendCString(s, "lo world", kCFStringEncodingUTF8)
        self.assertEquals(s, u"hello world")

        CFStringAppendFormat(s, None, ": %s = %d", "x", 99)
        self.assertEquals(s, u"hello world: x = 99")

        self.failIf(hasattr(CoreFoundation, 'CFStringAppendFormatAndArguments'))

        CFStringInsert(s, 2, "--")
        self.assertEquals(s, u"he--llo world: x = 99")

        CFStringDelete(s, CFRange(0, 8))
        self.assertEquals(s, u"world: x = 99")

        CFStringReplace(s, CFRange(0, 4), "WOR")
        self.assertEquals(s, u"WORd: x = 99")

        CFStringReplaceAll(s, "WHOOPS")
        self.assertEquals(s, u"WHOOPS")

        CFStringReplaceAll(s, u"BLAblaBLAblaBLA")
        self.assertEquals(s, u"BLAblaBLAblaBLA")

        CFStringFindAndReplace(s, "BL", " fo ", CFRange(0, 15), 0)
        self.assertEquals(s, " fo Abla fo Abla fo A")

        CFStringReplaceAll(s, u"abc")
        CFStringPad(s, " ", 9, 0)
        self.assertEquals(s, u"abc      ")

        CFStringReplaceAll(s, u"abc")
        CFStringPad(s, ". ", 9, 1)
        self.assertEquals(s, u"abc . . .")

        CFStringReplaceAll(s, u"abcdef")
        CFStringPad(s, ". ", 3, 0)
        self.assertEquals(s, u"abc")

        CFStringReplaceAll(s, u"aHelloaaa")
        CFStringTrim(s, u'a')
        self.assertEquals(s, u"Hello")

        CFStringReplaceAll(s, u"* * * *abc * ")
        CFStringTrim(s, u'* ')
        self.assertEquals(s, u"*abc ")
        
        
        CFStringReplaceAll(s, u" \tHello world  \t ")
        CFStringTrimWhitespace(s)
        self.assertEquals(s, u"Hello world")


        CFStringReplaceAll(s, u"AbC")
        CFStringLowercase(s, CFLocaleCopyCurrent())
        self.assertEquals(s, u'abc')

        CFStringReplaceAll(s, u"AbC")
        CFStringUppercase(s, CFLocaleCopyCurrent())
        self.assertEquals(s, u'ABC')

        CFStringReplaceAll(s, u"hello world")
        CFStringCapitalize(s, CFLocaleCopyCurrent())
        self.assertEquals(s, u'Hello World')

        CFStringNormalize(s, kCFStringNormalizationFormKD)
        self.assertEquals(s, u'Hello World')

        CFStringFold(s, kCFCompareCaseInsensitive, CFLocaleCopyCurrent())
        self.assertEquals(s, u'hello world')

        CFStringReplaceAll(s, u"A C")
        ok, rng = CFStringTransform(s, CFRange(0, 3), kCFStringTransformToXMLHex, 
                                        False)
        self.assertEquals(s, 'A C') 
        self.failUnless(ok is True)
        self.assertEquals(rng, CFRange(0, 3))

    def testStringEncoding(self):
        ok = CFStringIsEncodingAvailable(kCFStringEncodingUTF8)
        self.failUnless(ok is True)

        encodings = CFStringGetListOfAvailableEncodings()
        self.failUnless(isinstance(encodings, objc.varlist))
        for e in encodings:
            if e == kCFStringEncodingInvalidId:
                break
            self.failUnless(isinstance(e, (int, long)))

        s = CFStringGetNameOfEncoding(kCFStringEncodingUTF8)
        self.assertEquals(s, 'Unicode (UTF-8)')

        v = CFStringConvertEncodingToNSStringEncoding(kCFStringEncodingUTF8)
        self.failUnless(isinstance(v, (int, long)))

        t = CFStringConvertNSStringEncodingToEncoding(v)
        self.assertEquals(t, kCFStringEncodingUTF8)

        v = CFStringConvertEncodingToWindowsCodepage(kCFStringEncodingISOLatin1)
        self.failUnless(isinstance(v, (int, long)))

        t = CFStringConvertWindowsCodepageToEncoding(v)
        self.assertEquals(t, kCFStringEncodingISOLatin1)

        v = CFStringConvertEncodingToIANACharSetName(kCFStringEncodingUTF8)
        self.failUnless(isinstance(v, unicode))
        self.assertEquals(v, 'UTF-8')

        t = CFStringConvertIANACharSetNameToEncoding(v)
        self.assertEquals(t, kCFStringEncodingUTF8)

        v = CFStringGetMostCompatibleMacStringEncoding(kCFStringEncodingWindowsLatin1)
        self.assertEquals(v, kCFStringEncodingMacRoman)

    

        






    def testNoInlineBuffer(self):
        self.failIf(hasattr(CoreFoundation, 'CFStringInlineBuffer'))
        self.failIf(hasattr(CoreFoundation, 'CFStringInitInlineBuffer'))
        self.failIf(hasattr(CoreFoundation, 'CFStringGetCharacterFromInlineBuffer'))


    def testConstants(self):
        self.failUnless(kCFStringEncodingInvalidId == 0xffffffff)
        self.failUnless(kCFStringEncodingMacRoman == 0)
        self.failUnless(kCFStringEncodingWindowsLatin1 == 0x0500)
        self.failUnless(kCFStringEncodingISOLatin1 == 0x0201)
        self.failUnless(kCFStringEncodingNextStepLatin == 0x0B01)
        self.failUnless(kCFStringEncodingASCII == 0x0600)
        self.failUnless(kCFStringEncodingUnicode == 0x0100)
        self.failUnless(kCFStringEncodingUTF8 == 0x08000100)
        self.failUnless(kCFStringEncodingNonLossyASCII == 0x0BFF)
        self.failUnless(kCFStringEncodingUTF16 == 0x0100)
        self.failUnless(kCFStringEncodingUTF16BE == 0x10000100)
        self.failUnless(kCFStringEncodingUTF16LE == 0x14000100)
        self.failUnless(kCFStringEncodingUTF32 == 0x0c000100)
        self.failUnless(kCFStringEncodingUTF32BE == 0x18000100)
        self.failUnless(kCFStringEncodingUTF32LE == 0x1c000100)

        self.failUnless(kCFCompareCaseInsensitive == 1)
        self.failUnless(kCFCompareBackwards == 4)
        self.failUnless(kCFCompareAnchored == 8)
        self.failUnless(kCFCompareNonliteral == 16)
        self.failUnless(kCFCompareLocalized == 32)
        self.failUnless(kCFCompareNumerically == 64)
        self.failUnless(kCFCompareDiacriticInsensitive == 128)
        self.failUnless(kCFCompareWidthInsensitive == 256)
        self.failUnless(kCFCompareForcedOrdering == 512)

        self.failUnless(kCFStringNormalizationFormD == 0)
        self.failUnless(kCFStringNormalizationFormKD == 1)
        self.failUnless(kCFStringNormalizationFormC == 2)
        self.failUnless(kCFStringNormalizationFormKC == 3)


        self.failUnless(isinstance(kCFStringTransformStripCombiningMarks, unicode))
        self.failUnless(isinstance(kCFStringTransformToLatin, unicode))
        self.failUnless(isinstance(kCFStringTransformFullwidthHalfwidth, unicode))
        self.failUnless(isinstance(kCFStringTransformLatinKatakana, unicode))
        self.failUnless(isinstance(kCFStringTransformLatinHiragana, unicode))
        self.failUnless(isinstance(kCFStringTransformHiraganaKatakana, unicode))
        self.failUnless(isinstance(kCFStringTransformMandarinLatin, unicode))
        self.failUnless(isinstance(kCFStringTransformLatinHangul, unicode))
        self.failUnless(isinstance(kCFStringTransformLatinArabic, unicode))
        self.failUnless(isinstance(kCFStringTransformLatinHebrew, unicode))
        self.failUnless(isinstance(kCFStringTransformLatinThai, unicode))
        self.failUnless(isinstance(kCFStringTransformLatinCyrillic, unicode))
        self.failUnless(isinstance(kCFStringTransformLatinGreek, unicode))
        self.failUnless(isinstance(kCFStringTransformToXMLHex, unicode))
        self.failUnless(isinstance(kCFStringTransformToUnicodeName, unicode))
        self.failUnless(isinstance(kCFStringTransformStripDiacritics, unicode))


    def testNoPrivate(self):
        self.failIf(hasattr(CoreFoundation, 'CFShow'))
        self.failIf(hasattr(CoreFoundation, 'CFShowStr'))
        self.failIf(hasattr(CoreFoundation, '__CFStringMakeConstantString'))

    def testCFSTR(self):
        v = CFSTR(u"hello")
        self.failUnless(isinstance(v, unicode))



class TestStringEncodingExt (TestCase):
    def testConstants(self):
        self.failUnless( kCFStringEncodingMacJapanese == 1 )
        self.failUnless( kCFStringEncodingMacChineseTrad == 2 )
        self.failUnless( kCFStringEncodingMacKorean == 3 )
        self.failUnless( kCFStringEncodingMacArabic == 4 )
        self.failUnless( kCFStringEncodingMacHebrew == 5 )
        self.failUnless( kCFStringEncodingMacGreek == 6 )
        self.failUnless( kCFStringEncodingMacCyrillic == 7 )
        self.failUnless( kCFStringEncodingMacDevanagari == 9 )
        self.failUnless( kCFStringEncodingMacGurmukhi == 10 )
        self.failUnless( kCFStringEncodingMacGujarati == 11 )
        self.failUnless( kCFStringEncodingMacOriya == 12 )
        self.failUnless( kCFStringEncodingMacBengali == 13 )
        self.failUnless( kCFStringEncodingMacTamil == 14 )
        self.failUnless( kCFStringEncodingMacTelugu == 15 )
        self.failUnless( kCFStringEncodingMacKannada == 16 )
        self.failUnless( kCFStringEncodingMacMalayalam == 17 )
        self.failUnless( kCFStringEncodingMacSinhalese == 18 )
        self.failUnless( kCFStringEncodingMacBurmese == 19 )
        self.failUnless( kCFStringEncodingMacKhmer == 20 )
        self.failUnless( kCFStringEncodingMacThai == 21 )
        self.failUnless( kCFStringEncodingMacLaotian == 22 )
        self.failUnless( kCFStringEncodingMacGeorgian == 23 )
        self.failUnless( kCFStringEncodingMacArmenian == 24 )
        self.failUnless( kCFStringEncodingMacChineseSimp == 25 )
        self.failUnless( kCFStringEncodingMacTibetan == 26 )
        self.failUnless( kCFStringEncodingMacMongolian == 27 )
        self.failUnless( kCFStringEncodingMacEthiopic == 28 )
        self.failUnless( kCFStringEncodingMacCentralEurRoman == 29 )
        self.failUnless( kCFStringEncodingMacVietnamese == 30 )
        self.failUnless( kCFStringEncodingMacExtArabic == 31 )
        self.failUnless( kCFStringEncodingMacSymbol == 33 )
        self.failUnless( kCFStringEncodingMacDingbats == 34 )
        self.failUnless( kCFStringEncodingMacTurkish == 35 )
        self.failUnless( kCFStringEncodingMacCroatian == 36 )
        self.failUnless( kCFStringEncodingMacIcelandic == 37 )
        self.failUnless( kCFStringEncodingMacRomanian == 38 )
        self.failUnless( kCFStringEncodingMacCeltic == 39 )
        self.failUnless( kCFStringEncodingMacGaelic == 40, )
        self.failUnless( kCFStringEncodingMacFarsi == 0x8C )
        self.failUnless( kCFStringEncodingMacUkrainian == 0x98 )
        self.failUnless( kCFStringEncodingMacInuit == 0xEC )
        self.failUnless( kCFStringEncodingMacVT100 == 0xFC )
        self.failUnless( kCFStringEncodingMacHFS == 0xFF )
        self.failUnless( kCFStringEncodingISOLatin2 == 0x0202 )
        self.failUnless( kCFStringEncodingISOLatin3 == 0x0203 )
        self.failUnless( kCFStringEncodingISOLatin4 == 0x0204 )
        self.failUnless( kCFStringEncodingISOLatinCyrillic == 0x0205 )
        self.failUnless( kCFStringEncodingISOLatinArabic == 0x0206 )
        self.failUnless( kCFStringEncodingISOLatinGreek == 0x0207 )
        self.failUnless( kCFStringEncodingISOLatinHebrew == 0x0208 )
        self.failUnless( kCFStringEncodingISOLatin5 == 0x0209 )
        self.failUnless( kCFStringEncodingISOLatin6 == 0x020A )
        self.failUnless( kCFStringEncodingISOLatinThai == 0x020B )
        self.failUnless( kCFStringEncodingISOLatin7 == 0x020D )
        self.failUnless( kCFStringEncodingISOLatin8 == 0x020E )
        self.failUnless( kCFStringEncodingISOLatin9 == 0x020F )
        self.failUnless( kCFStringEncodingISOLatin10 == 0x0210 )
        self.failUnless( kCFStringEncodingDOSLatinUS == 0x0400 )
        self.failUnless( kCFStringEncodingDOSGreek == 0x0405 )
        self.failUnless( kCFStringEncodingDOSBalticRim == 0x0406 )
        self.failUnless( kCFStringEncodingDOSLatin1 == 0x0410 )
        self.failUnless( kCFStringEncodingDOSGreek1 == 0x0411 )
        self.failUnless( kCFStringEncodingDOSLatin2 == 0x0412 )
        self.failUnless( kCFStringEncodingDOSCyrillic == 0x0413 )
        self.failUnless( kCFStringEncodingDOSTurkish == 0x0414 )
        self.failUnless( kCFStringEncodingDOSPortuguese == 0x0415 )
        self.failUnless( kCFStringEncodingDOSIcelandic == 0x0416 )
        self.failUnless( kCFStringEncodingDOSHebrew == 0x0417 )
        self.failUnless( kCFStringEncodingDOSCanadianFrench == 0x0418 )
        self.failUnless( kCFStringEncodingDOSArabic == 0x0419 )
        self.failUnless( kCFStringEncodingDOSNordic == 0x041A )
        self.failUnless( kCFStringEncodingDOSRussian == 0x041B )
        self.failUnless( kCFStringEncodingDOSGreek2 == 0x041C )
        self.failUnless( kCFStringEncodingDOSThai == 0x041D )
        self.failUnless( kCFStringEncodingDOSJapanese == 0x0420 )
        self.failUnless( kCFStringEncodingDOSChineseSimplif == 0x0421 )
        self.failUnless( kCFStringEncodingDOSKorean == 0x0422 )
        self.failUnless( kCFStringEncodingDOSChineseTrad == 0x0423 )
        self.failUnless( kCFStringEncodingWindowsLatin2 == 0x0501 )
        self.failUnless( kCFStringEncodingWindowsCyrillic == 0x0502 )
        self.failUnless( kCFStringEncodingWindowsGreek == 0x0503 )
        self.failUnless( kCFStringEncodingWindowsLatin5 == 0x0504 )
        self.failUnless( kCFStringEncodingWindowsHebrew == 0x0505 )
        self.failUnless( kCFStringEncodingWindowsArabic == 0x0506 )
        self.failUnless( kCFStringEncodingWindowsBalticRim == 0x0507 )
        self.failUnless( kCFStringEncodingWindowsVietnamese == 0x0508 )
        self.failUnless( kCFStringEncodingWindowsKoreanJohab == 0x0510 )
        self.failUnless( kCFStringEncodingANSEL == 0x0601 )
        self.failUnless( kCFStringEncodingJIS_X0201_76 == 0x0620 )
        self.failUnless( kCFStringEncodingJIS_X0208_83 == 0x0621 )
        self.failUnless( kCFStringEncodingJIS_X0208_90 == 0x0622 )
        self.failUnless( kCFStringEncodingJIS_X0212_90 == 0x0623 )
        self.failUnless( kCFStringEncodingJIS_C6226_78 == 0x0624 )
        self.failUnless( kCFStringEncodingShiftJIS_X0213 == 0x0628 )
        self.failUnless( kCFStringEncodingShiftJIS_X0213_MenKuTen == 0x0629 )
        self.failUnless( kCFStringEncodingGB_2312_80 == 0x0630 )
        self.failUnless( kCFStringEncodingGBK_95 == 0x0631 )
        self.failUnless( kCFStringEncodingGB_18030_2000 == 0x0632 )
        self.failUnless( kCFStringEncodingKSC_5601_87 == 0x0640 )
        self.failUnless( kCFStringEncodingKSC_5601_92_Johab == 0x0641 )
        self.failUnless( kCFStringEncodingCNS_11643_92_P1 == 0x0651 )
        self.failUnless( kCFStringEncodingCNS_11643_92_P2 == 0x0652 )
        self.failUnless( kCFStringEncodingCNS_11643_92_P3 == 0x0653 )
        self.failUnless( kCFStringEncodingISO_2022_JP == 0x0820 )
        self.failUnless( kCFStringEncodingISO_2022_JP_2 == 0x0821 )
        self.failUnless( kCFStringEncodingISO_2022_JP_1 == 0x0822 )
        self.failUnless( kCFStringEncodingISO_2022_JP_3 == 0x0823 )
        self.failUnless( kCFStringEncodingISO_2022_CN == 0x0830 )
        self.failUnless( kCFStringEncodingISO_2022_CN_EXT == 0x0831 )
        self.failUnless( kCFStringEncodingISO_2022_KR == 0x0840 )
        self.failUnless( kCFStringEncodingEUC_JP == 0x0920 )
        self.failUnless( kCFStringEncodingEUC_CN == 0x0930 )
        self.failUnless( kCFStringEncodingEUC_TW == 0x0931 )
        self.failUnless( kCFStringEncodingEUC_KR == 0x0940 )
        self.failUnless( kCFStringEncodingShiftJIS == 0x0A01 )
        self.failUnless( kCFStringEncodingKOI8_R == 0x0A02 )
        self.failUnless( kCFStringEncodingBig5 == 0x0A03 )
        self.failUnless( kCFStringEncodingMacRomanLatin1 == 0x0A04 )
        self.failUnless( kCFStringEncodingHZ_GB_2312 == 0x0A05 )
        self.failUnless( kCFStringEncodingBig5_HKSCS_1999 == 0x0A06 )
        self.failUnless( kCFStringEncodingVISCII == 0x0A07 )
        self.failUnless( kCFStringEncodingKOI8_U == 0x0A08 )
        self.failUnless( kCFStringEncodingBig5_E == 0x0A09 )
        self.failUnless( kCFStringEncodingNextStepJapanese == 0x0B02 )
        self.failUnless( kCFStringEncodingEBCDIC_US == 0x0C01 )
        self.failUnless( kCFStringEncodingEBCDIC_CP037 == 0x0C02 )
        self.failUnless( kCFStringEncodingShiftJIS_X0213_00 == 0x0628 )

if __name__ == "__main__":
    main()
