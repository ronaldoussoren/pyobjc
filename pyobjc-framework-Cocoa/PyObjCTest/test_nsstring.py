import sys
import objc
import warnings

import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level, cast_uint, onlyPython2


class TestNSString(TestCase):
    def testClassTree(self):
        self.assertTrue(issubclass(objc.pyobjc_unicode, str))

    def testCompare(self):
        self.assertTrue(
            Foundation.NSString.localizedCaseInsensitiveCompare_("foo", "bar") == 1,
            b"NSString doesn'.decode('ascii')t compare correctly",
        )
        self.assertTrue(
            Foundation.NSString.localizedCaseInsensitiveCompare_("foo", "Foo") == 0,
            b"NSString doesn'.decode('ascii')t compare correctly",
        )

    def testFormatting(self):
        # The test on instances is slightly more verbose to avoid warnings
        obj = Foundation.NSString.alloc().initWithFormat_("foo %d", 42)
        self.assertEqual(obj, "foo 42")

        obj = Foundation.NSString.alloc().initWithFormat_locale_("foo %d", {}, 42)
        self.assertEqual(obj, "foo 42")

    def testGetCString(self):
        # Custom wrappers
        v = Foundation.NSString.stringWithString_("hello world")

        self.assertEqual(v, "hello world")

        x = v.getCString_maxLength_(None, 16)
        self.assertEqual(x, b"hello world")

        self.assertRaises(objc.error, v.getCString_maxLength_, None, 4)

        x, loc = v.getCString_maxLength_range_remainingRange_(None, 4, (1, 4), None)
        self.assertEqual(x, b"ello")
        self.assertEqual(loc.location, 5)
        self.assertEqual(loc.length, 0)


class TestNSStringBridging(TestCase):
    def setUp(self):
        self.nsUniString = Foundation.NSString.stringWithString_("unifoo")
        self.pyUniString = "unifoo"

    def testBasicComparison(self):
        self.assertEqual("unifoo", Foundation.NSString.stringWithString_("unifoo"))

        u = "\xc3\xbc\xc3\xb1\xc3\xae\xc3\xa7\xc3\xb8d\xc3\xa8"
        self.assertEqual(u, Foundation.NSString.stringWithString_(u))

    def testTypesAndClasses(self):
        self.assertIsInstance(self.nsUniString, str)
        self.assertIsInstance(self.pyUniString, str)

    @onlyPython2
    def testStrConversion(self):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore")

            curEnabledFlag = objc.getStrBridgeEnabled()
            objc.setStrBridgeEnabled(True)
            try:
                v = Foundation.NSString.stringWithString_("hello2")
                self.assertIsInstance(v, objc.pyobjc_unicode)
                self.assertEqual(v, "hello2")

                self.assertRaises(UnicodeError, str, "\xff")
                # XXX: string bridge now uses the default Foundation.NSString encoding
                # self.assertRaises(UnicodeError, Foundation.NSString.stringWithString_, '\xff')

                objc.setStrBridgeEnabled(False)

                warnings.filterwarnings("error", category=objc.PyObjCStrBridgeWarning)
                try:
                    # v = Foundation.NSString.stringWithString_("hello")

                    # we need to make sure that the str is unique
                    # because an already bridged one might have crossed
                    # and would be cached
                    newString = type("test_str", (str,), {})("hello2")
                    self.assertRaises(
                        objc.PyObjCStrBridgeWarning,
                        Foundation.NSString.stringWithString_,
                        newString,
                    )

                finally:
                    del warnings.filters[0]

            finally:
                objc.setStrBridgeEnabled(curEnabledFlag)

    def testNSStringMethodAccess(self):
        self.assertIsInstance(self.nsUniString, objc.pyobjc_unicode)
        v = self.nsUniString.stringByAppendingString_
        self.assertIsInstance(v, objc.selector)


class TestMutable(TestCase):
    def testSync(self):
        """
        Test that python and ObjC string representation are not
        automaticly synchronized.
        """
        pyStr = Foundation.NSMutableString.stringWithString_("hello")
        ocStr = pyStr.nsstring()
        self.assertEqual(pyStr, "hello")
        self.assertIsInstance(ocStr, Foundation.NSMutableString)
        ocStr.appendString_(" world")
        self.assertEqual(pyStr, "hello")


class TestPickle(TestCase):
    """
    Testcases for pickling of Objective-C strings. Those are pickled as
    str strings.
    """

    def setUp(self):
        self.strVal = Foundation.NSTaskDidTerminateNotification

    def testPickle(self):
        """
        Check that ObjC-strings pickle as str strings
        """
        import pickle

        s = pickle.dumps(self.strVal, 0)
        v = pickle.loads(s)
        self.assertEqual(type(v), str)

        s = pickle.dumps(self.strVal, 1)
        v = pickle.loads(s)
        self.assertEqual(type(v), str)

        s = pickle.dumps(self.strVal, 2)
        v = pickle.loads(s)
        self.assertEqual(type(v), str)

    @onlyPython2
    def testCPickle(self):
        """
        Check that ObjC-strings pickle as str strings
        """
        import cPickle as pickle

        s = pickle.dumps(self.strVal, 0)
        v = pickle.loads(s)
        self.assertEqual(type(v), str)

        s = pickle.dumps(self.strVal, 1)
        v = pickle.loads(s)
        self.assertEqual(type(v), str)

        s = pickle.dumps(self.strVal, 2)
        v = pickle.loads(s)
        self.assertEqual(type(v), str)

    def testFormat(self):
        v = self.strVal

        d = v.stringByAppendingFormat_("hello")
        self.assertEqual(d, v + "hello")

        d = v.stringByAppendingFormat_("hello %s %d", b"world", 101)
        self.assertEqual(d, v + "hello world 101")

        v = Foundation.NSString.alloc().initWithFormat_("%s %d %s", b"a", 44, b"cc")
        self.assertEqual(v, "a 44 cc")

        v = Foundation.NSString.alloc().initWithFormat_locale_(
            "%s %d %s", None, b"a", 44, b"cc"
        )
        self.assertEqual(v, "a 44 cc")

        v = Foundation.NSString.stringWithFormat_("aap %s mies", b"noot")
        self.assertEqual(v, "aap noot mies")

        v = Foundation.NSString.localizedStringWithFormat_("aap %s mies", b"noot")
        self.assertEqual(v, "aap noot mies")

        v = Foundation.NSMutableString.stringWithString_("hello")
        v.appendFormat_(" bar %s", b"baz")
        self.assertEqual(v.nsstring(), "hello bar baz")

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(Foundation.NSRegularExpressionSearch, 1024)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertEqual(Foundation.NSMaximumStringLength, sys.maxsize)
        self.assertEqual(Foundation.NSDiacriticInsensitiveSearch, 128)
        self.assertEqual(Foundation.NSWidthInsensitiveSearch, 256)
        self.assertEqual(Foundation.NSForcedOrderingSearch, 512)

        self.assertEqual(Foundation.NSProprietaryStringEncoding, 65536)

    def testConstants(self):
        self.assertIsInstance(Foundation.NSParseErrorException, str)
        self.assertIsInstance(Foundation.NSCharacterConversionException, str)

        self.assertEqual(Foundation.NSCaseInsensitiveSearch, 1)
        self.assertEqual(Foundation.NSLiteralSearch, 2)
        self.assertEqual(Foundation.NSBackwardsSearch, 4)
        self.assertEqual(Foundation.NSAnchoredSearch, 8)
        self.assertEqual(Foundation.NSNumericSearch, 64)

        self.assertEqual(Foundation.NSASCIIStringEncoding, 1)
        self.assertEqual(Foundation.NSNEXTSTEPStringEncoding, 2)
        self.assertEqual(Foundation.NSJapaneseEUCStringEncoding, 3)
        self.assertEqual(Foundation.NSUTF8StringEncoding, 4)
        self.assertEqual(Foundation.NSISOLatin1StringEncoding, 5)
        self.assertEqual(Foundation.NSSymbolStringEncoding, 6)
        self.assertEqual(Foundation.NSNonLossyASCIIStringEncoding, 7)
        self.assertEqual(Foundation.NSShiftJISStringEncoding, 8)
        self.assertEqual(Foundation.NSISOLatin2StringEncoding, 9)
        self.assertEqual(Foundation.NSUnicodeStringEncoding, 10)
        self.assertEqual(Foundation.NSWindowsCP1251StringEncoding, 11)
        self.assertEqual(Foundation.NSWindowsCP1252StringEncoding, 12)
        self.assertEqual(Foundation.NSWindowsCP1253StringEncoding, 13)
        self.assertEqual(Foundation.NSWindowsCP1254StringEncoding, 14)
        self.assertEqual(Foundation.NSWindowsCP1250StringEncoding, 15)
        self.assertEqual(Foundation.NSISO2022JPStringEncoding, 21)
        self.assertEqual(Foundation.NSMacOSRomanStringEncoding, 30)
        self.assertEqual(
            Foundation.NSUTF16StringEncoding, Foundation.NSUnicodeStringEncoding
        )
        self.assertEqual(
            Foundation.NSUTF16BigEndianStringEncoding, cast_uint(0x90000100)
        )
        self.assertEqual(
            Foundation.NSUTF16LittleEndianStringEncoding, cast_uint(0x94000100)
        )
        self.assertEqual(Foundation.NSUTF32StringEncoding, cast_uint(0x8C000100))
        self.assertEqual(
            Foundation.NSUTF32BigEndianStringEncoding, cast_uint(0x98000100)
        )
        self.assertEqual(
            Foundation.NSUTF32LittleEndianStringEncoding, cast_uint(0x9C000100)
        )

        self.assertEqual(Foundation.NSStringEncodingConversionAllowLossy, 1)
        self.assertEqual(Foundation.NSStringEncodingConversionExternalRepresentation, 2)

    def testMethods(self):
        self.assertArgHasType(
            Foundation.NSString.getCharacters_range_, 0, b"o^" + objc._C_UNICHAR
        )
        self.assertArgSizeInArg(Foundation.NSString.getCharacters_range_, 0, 1)

        self.assertResultIsBOOL(Foundation.NSString.isEqualToString_)
        self.assertResultIsBOOL(Foundation.NSString.hasPrefix_)
        self.assertResultIsBOOL(Foundation.NSString.hasSuffix_)
        self.assertResultIsBOOL(Foundation.NSString.boolValue)
        self.assertArgIsOut(
            Foundation.NSString.getLineStart_end_contentsEnd_forRange_, 0
        )
        self.assertArgIsOut(
            Foundation.NSString.getLineStart_end_contentsEnd_forRange_, 1
        )
        self.assertArgIsOut(
            Foundation.NSString.getLineStart_end_contentsEnd_forRange_, 2
        )
        self.assertArgIsOut(
            Foundation.NSString.getParagraphStart_end_contentsEnd_forRange_, 0
        )
        self.assertArgIsOut(
            Foundation.NSString.getParagraphStart_end_contentsEnd_forRange_, 1
        )
        self.assertArgIsOut(
            Foundation.NSString.getParagraphStart_end_contentsEnd_forRange_, 2
        )
        self.assertArgIsBOOL(
            Foundation.NSString.dataUsingEncoding_allowLossyConversion_, 1
        )
        self.assertResultIsBOOL(Foundation.NSString.canBeConvertedToEncoding_)
        self.assertResultIsNullTerminated(Foundation.NSString.cStringUsingEncoding_)
        self.assertResultHasType(Foundation.NSString.cStringUsingEncoding_, b"^v")
        self.assertResultIsBOOL(Foundation.NSString.getCString_maxLength_encoding_)
        self.assertArgHasType(
            Foundation.NSString.getCString_maxLength_encoding_, 0, b"o^v"
        )
        self.assertArgSizeInArg(
            Foundation.NSString.getCString_maxLength_encoding_, 0, 1
        )

        self.assertResultIsBOOL(
            Foundation.NSString.getBytes_maxLength_usedLength_encoding_options_range_remainingRange_  # noqa: B950
        )
        self.assertArgHasType(
            Foundation.NSString.getBytes_maxLength_usedLength_encoding_options_range_remainingRange_,  # noqa: B950
            0,
            b"o^v",
        )
        self.assertArgSizeInArg(
            Foundation.NSString.getBytes_maxLength_usedLength_encoding_options_range_remainingRange_,  # noqa: B950
            0,
            (1, 2),
        )
        self.assertArgIsOut(
            Foundation.NSString.getBytes_maxLength_usedLength_encoding_options_range_remainingRange_,  # noqa: B950
            2,
        )
        self.assertArgIsOut(
            Foundation.NSString.getBytes_maxLength_usedLength_encoding_options_range_remainingRange_,  # noqa: B950
            6,
        )

        self.assertResultHasType(
            Foundation.NSString.UTF8String, b"^" + objc._C_CHAR_AS_TEXT
        )
        self.assertResultIsNullTerminated(Foundation.NSString.UTF8String)
        self.assertResultIsNullTerminated(Foundation.NSString.availableStringEncodings)

        self.assertArgHasType(
            Foundation.NSString.initWithCharactersNoCopy_length_freeWhenDone_,
            0,
            b"n^" + objc._C_UNICHAR,
        )
        self.assertArgSizeInArg(
            Foundation.NSString.initWithCharactersNoCopy_length_freeWhenDone_, 0, 1
        )
        self.assertArgIsBOOL(
            Foundation.NSString.initWithCharactersNoCopy_length_freeWhenDone_, 2
        )
        self.assertArgHasType(
            Foundation.NSString.initWithCharacters_length_, 0, b"n^" + objc._C_UNICHAR
        )
        self.assertArgSizeInArg(Foundation.NSString.initWithCharacters_length_, 0, 1)
        self.assertArgHasType(
            Foundation.NSString.initWithUTF8String_, 0, b"n^" + objc._C_CHAR_AS_TEXT
        )
        self.assertArgIsNullTerminated(Foundation.NSString.initWithUTF8String_, 0)
        self.assertArgIsPrintf(Foundation.NSString.initWithFormat_, 0)
        self.assertArgIsPrintf(Foundation.NSString.initWithFormat_locale_, 0)

        o = Foundation.NSString.alloc()
        self.assertArgIsIn(o.initWithBytes_length_encoding_, 0)
        self.assertArgSizeInArg(o.initWithBytes_length_encoding_, 0, 1)
        o = o.init()
        self.assertArgIsIn(
            Foundation.NSString.initWithBytesNoCopy_length_encoding_freeWhenDone_, 0
        )
        self.assertArgSizeInArg(
            Foundation.NSString.initWithBytesNoCopy_length_encoding_freeWhenDone_, 0, 1
        )
        self.assertArgIsBOOL(
            Foundation.NSString.initWithBytesNoCopy_length_encoding_freeWhenDone_, 3
        )

        self.assertArgHasType(
            Foundation.NSString.stringWithCharacters_length_, 0, b"n^" + objc._C_UNICHAR
        )
        self.assertArgSizeInArg(Foundation.NSString.stringWithCharacters_length_, 0, 1)
        self.assertArgHasType(
            Foundation.NSString.stringWithUTF8String_, 0, b"n^" + objc._C_CHAR_AS_TEXT
        )
        self.assertArgIsNullTerminated(Foundation.NSString.stringWithUTF8String_, 0)
        self.assertArgIsPrintf(Foundation.NSString.stringWithFormat_, 0)
        self.assertArgIsPrintf(Foundation.NSString.localizedStringWithFormat_, 0)

        self.assertArgHasType(Foundation.NSString.initWithCString_encoding_, 0, b"n^t")
        self.assertArgIsNullTerminated(Foundation.NSString.initWithCString_encoding_, 0)
        self.assertArgHasType(
            Foundation.NSString.stringWithCString_encoding_, 0, b"n^t"
        )
        self.assertArgIsNullTerminated(
            Foundation.NSString.stringWithCString_encoding_, 0
        )

        self.assertArgIsOut(
            Foundation.NSString.initWithContentsOfURL_encoding_error_, 2
        )
        self.assertArgIsOut(
            Foundation.NSString.initWithContentsOfFile_encoding_error_, 2
        )
        self.assertArgIsOut(
            Foundation.NSString.stringWithContentsOfURL_encoding_error_, 2
        )
        self.assertArgIsOut(
            Foundation.NSString.stringWithContentsOfFile_encoding_error_, 2
        )

        self.assertArgIsOut(
            Foundation.NSString.initWithContentsOfURL_usedEncoding_error_, 1
        )
        self.assertArgIsOut(
            Foundation.NSString.initWithContentsOfURL_usedEncoding_error_, 2
        )
        self.assertArgIsOut(
            Foundation.NSString.initWithContentsOfFile_usedEncoding_error_, 1
        )
        self.assertArgIsOut(
            Foundation.NSString.initWithContentsOfFile_usedEncoding_error_, 2
        )
        self.assertArgIsOut(
            Foundation.NSString.stringWithContentsOfURL_usedEncoding_error_, 1
        )
        self.assertArgIsOut(
            Foundation.NSString.stringWithContentsOfURL_usedEncoding_error_, 2
        )
        self.assertArgIsOut(
            Foundation.NSString.stringWithContentsOfFile_usedEncoding_error_, 1
        )
        self.assertArgIsOut(
            Foundation.NSString.stringWithContentsOfFile_usedEncoding_error_, 2
        )

        self.assertResultIsBOOL(
            Foundation.NSString.writeToURL_atomically_encoding_error_
        )
        self.assertArgIsBOOL(
            Foundation.NSString.writeToURL_atomically_encoding_error_, 1
        )
        self.assertArgIsOut(
            Foundation.NSString.writeToURL_atomically_encoding_error_, 3
        )
        self.assertResultIsBOOL(
            Foundation.NSString.writeToFile_atomically_encoding_error_
        )
        self.assertArgIsBOOL(
            Foundation.NSString.writeToFile_atomically_encoding_error_, 1
        )
        self.assertArgIsOut(
            Foundation.NSString.writeToFile_atomically_encoding_error_, 3
        )

        self.assertArgIsPrintf(Foundation.NSMutableString.appendFormat_, 0)

        self.assertResultHasType(Foundation.NSString.cString, b"^t")
        self.assertResultIsNullTerminated(Foundation.NSString.cString)
        self.assertResultHasType(Foundation.NSString.lossyCString, b"^t")
        self.assertResultIsNullTerminated(Foundation.NSString.lossyCString)

        self.assertArgHasType(Foundation.NSString.getCString_maxLength_, 0, b"o^v")
        self.assertArgSizeInArg(Foundation.NSString.getCString_maxLength_, 0, 1)

        self.assertArgHasType(
            Foundation.NSString.getCString_maxLength_range_remainingRange_, 0, b"o^v"
        )
        self.assertArgSizeInArg(
            Foundation.NSString.getCString_maxLength_range_remainingRange_, 0, 1
        )
        self.assertArgIsOut(
            Foundation.NSString.getCString_maxLength_range_remainingRange_, 3
        )

        self.assertResultIsBOOL(Foundation.NSString.writeToFile_atomically_)
        self.assertArgIsBOOL(Foundation.NSString.writeToFile_atomically_, 1)
        self.assertResultIsBOOL(Foundation.NSString.writeToURL_atomically_)
        self.assertArgIsBOOL(Foundation.NSString.writeToURL_atomically_, 1)

        self.assertArgHasType(
            Foundation.NSString.initWithCStringNoCopy_length_freeWhenDone_, 0, b"n^v"
        )
        self.assertArgSizeInArg(
            Foundation.NSString.initWithCStringNoCopy_length_freeWhenDone_, 0, 1
        )
        self.assertArgIsBOOL(
            Foundation.NSString.initWithCStringNoCopy_length_freeWhenDone_, 2
        )
        self.assertArgHasType(Foundation.NSString.initWithCString_length_, 0, b"n^v")
        self.assertArgSizeInArg(Foundation.NSString.initWithCString_length_, 0, 1)
        self.assertArgHasType(Foundation.NSString.initWithCString_, 0, b"n^v")
        self.assertArgIsNullTerminated(Foundation.NSString.initWithCString_, 0)

        self.assertArgHasType(Foundation.NSString.stringWithCString_length_, 0, b"n^v")
        self.assertArgSizeInArg(Foundation.NSString.stringWithCString_length_, 0, 1)
        self.assertArgHasType(Foundation.NSString.stringWithCString_, 0, b"n^v")
        self.assertArgIsNullTerminated(Foundation.NSString.stringWithCString_, 0)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(Foundation.NSStringEnumerationByLines, 0)
        self.assertEqual(Foundation.NSStringEnumerationByParagraphs, 1)
        self.assertEqual(Foundation.NSStringEnumerationByComposedCharacterSequences, 2)
        self.assertEqual(Foundation.NSStringEnumerationByWords, 3)
        self.assertEqual(Foundation.NSStringEnumerationBySentences, 4)
        self.assertEqual(Foundation.NSStringEnumerationByCaretPositions, 5)
        self.assertEqual(Foundation.NSStringEnumerationByDeletionClusters, 6)
        self.assertEqual(Foundation.NSStringEnumerationReverse, 1 << 8)
        self.assertEqual(Foundation.NSStringEnumerationSubstringNotRequired, 1 << 9)
        self.assertEqual(Foundation.NSStringEnumerationLocalized, 1 << 10)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgHasType(
            Foundation.NSString.enumerateSubstringsInRange_options_usingBlock_,
            0,
            Foundation.NSRange.__typestr__,
        )
        self.assertArgIsBlock(
            Foundation.NSString.enumerateSubstringsInRange_options_usingBlock_,
            2,
            b"v@"
            + Foundation.NSRange.__typestr__
            + Foundation.NSRange.__typestr__
            + b"o^"
            + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            Foundation.NSString.enumerateLinesUsingBlock_, 0, b"v@o^" + objc._C_NSBOOL
        )

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(
            Foundation.NSStringEncodingDetectionSuggestedEncodingsKey, str
        )
        self.assertIsInstance(
            Foundation.NSStringEncodingDetectionDisallowedEncodingsKey, str
        )
        self.assertIsInstance(
            Foundation.NSStringEncodingDetectionUseOnlySuggestedEncodingsKey, str
        )
        self.assertIsInstance(Foundation.NSStringEncodingDetectionAllowLossyKey, str)
        self.assertIsInstance(Foundation.NSStringEncodingDetectionFromWindowsKey, str)
        self.assertIsInstance(
            Foundation.NSStringEncodingDetectionLossySubstitutionKey, str
        )
        self.assertIsInstance(
            Foundation.NSStringEncodingDetectionLikelyLanguageKey, str
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgHasType(
            Foundation.NSString.stringEncodingForData_encodingOptions_convertedString_usedLossyConversion_,  # noqa: B950
            2,
            b"o^@",
        )
        self.assertArgHasType(
            Foundation.NSString.stringEncodingForData_encodingOptions_convertedString_usedLossyConversion_,  # noqa: B950
            3,
            b"o^Z",
        )

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(Foundation.NSStringTransformLatinToKatakana, str)
        self.assertIsInstance(Foundation.NSStringTransformLatinToHiragana, str)
        self.assertIsInstance(Foundation.NSStringTransformLatinToHangul, str)
        self.assertIsInstance(Foundation.NSStringTransformLatinToArabic, str)
        self.assertIsInstance(Foundation.NSStringTransformLatinToHebrew, str)
        self.assertIsInstance(Foundation.NSStringTransformLatinToThai, str)
        self.assertIsInstance(Foundation.NSStringTransformLatinToCyrillic, str)
        self.assertIsInstance(Foundation.NSStringTransformLatinToGreek, str)
        self.assertIsInstance(Foundation.NSStringTransformToLatin, str)
        self.assertIsInstance(Foundation.NSStringTransformMandarinToLatin, str)
        self.assertIsInstance(Foundation.NSStringTransformHiraganaToKatakana, str)
        self.assertIsInstance(Foundation.NSStringTransformFullwidthToHalfwidth, str)
        self.assertIsInstance(Foundation.NSStringTransformToXMLHex, str)
        self.assertIsInstance(Foundation.NSStringTransformToUnicodeName, str)
        self.assertIsInstance(Foundation.NSStringTransformStripCombiningMarks, str)
        self.assertIsInstance(Foundation.NSStringTransformStripDiacritics, str)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(Foundation.NSString.localizedStandardContainsString_)
        self.assertArgIsBOOL(Foundation.NSString.stringByApplyingTransform_reverse_, 1)

        self.assertArgIsBOOL(
            Foundation.NSMutableString.applyTransform_reverse_range_updatedRange_, 1
        )
        self.assertArgIsOut(
            Foundation.NSMutableString.applyTransform_reverse_range_updatedRange_, 3
        )

    @min_os_level("10.16")
    def test_methods10_16(self):
        # XXX: exposing this not very useful.
        self.assertArgIsBlock(
            Foundation.NSString.initWithCharactersNoCopy_length_deallocator_,
            2,
            b"vn^" + objc._C_UNICHAR + objc._C_NSUInteger,
        )

        self.assertArgIsBlock(
            Foundation.NSString.initWithBytesNoCopy_length_encoding_deallocator_,
            3,
            b"v^v" + objc._C_NSUInteger,
        )
