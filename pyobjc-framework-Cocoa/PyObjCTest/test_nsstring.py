from PyObjCTools.TestSupport import *
import types
import warnings
import sys

from Foundation import *

class TestNSString(TestCase):
    def testClassTree(self):
        self.assert_(issubclass(objc.pyobjc_unicode, unicode))

    def testCompare(self):
        self.assert_(
            NSString.localizedCaseInsensitiveCompare_(u'foo',u'bar') == 1,
            u"NSString doesn't compare correctly")
        self.assert_(
            NSString.localizedCaseInsensitiveCompare_(u'foo',u'Foo') == 0,
            u"NSString doesn't compare correctly")

    def testFormatting(self):
        # The test on instances is slightly more verbose to avoid warnings
        obj = NSString.alloc().initWithFormat_(u"foo %d", 42)
        self.assertEqual(obj, u"foo 42")

        obj = NSString.alloc().initWithFormat_locale_(u"foo %d", {}, 42)
        self.assertEqual(obj, u"foo 42")


    def testGetCString(self):
        # Custom wrappers
        v = NSString.stringWithString_(u"hello world")
        
        self.assertEqual(v, u"hello world")

        x = v.getCString_maxLength_(None, 16)
        self.assertEqual(x, b"hello world")

        self.assertRaises(objc.error, v.getCString_maxLength_, None, 4)

        x, l = v.getCString_maxLength_range_remainingRange_(None, 4, (1, 4), None)
        self.assertEqual(x, b"ello")
        self.assertEqual(l.location, 5)
        self.assertEqual(l.length, 0)


class TestNSStringBridging(TestCase):
    def setUp(self):
        self.nsUniString = NSString.stringWithString_(u"unifoo")
        self.pyUniString = u"unifoo"

    def testBasicComparison(self):
        self.assertEqual(u"unifoo", NSString.stringWithString_(u"unifoo"))

        u = u'\xc3\xbc\xc3\xb1\xc3\xae\xc3\xa7\xc3\xb8d\xc3\xa8'
        self.assertEqual(u, NSString.stringWithString_(u));

    def testTypesAndClasses(self):
        self.assert_(isinstance(self.nsUniString, unicode))
        self.assert_(isinstance(self.pyUniString, unicode))

    @onlyPython2
    def testStrConversion(self):
        curEnabledFlag = objc.getStrBridgeEnabled()
        objc.setStrBridgeEnabled(True)
        try:
            v = NSString.stringWithString_("hello2")
            self.assert_(isinstance(v, objc.pyobjc_unicode))
            self.assertEqual(v, u"hello2")


            self.assertRaises(UnicodeError, unicode, "\xff")
            # XXX: string bridge now uses the default NSString encoding
            # self.assertRaises(UnicodeError, NSString.stringWithString_, '\xff')

            objc.setStrBridgeEnabled(False)

            warnings.filterwarnings('error', category=objc.PyObjCStrBridgeWarning)
            try:
                #v = NSString.stringWithString_("hello")

                # we need to make sure that the str is unique
                # because an already bridged one might have crossed
                # and would be cached
                newString = type('test_str', (str,), {})('hello2')
                self.assertRaises(objc.PyObjCStrBridgeWarning,
                        NSString.stringWithString_, newString)

            finally:
                del warnings.filters[0]


        finally:
            objc.setStrBridgeEnabled(curEnabledFlag)

    def testNSStringMethodAccess(self):
        self.assert_(isinstance(self.nsUniString, objc.pyobjc_unicode))
        v = self.nsUniString.stringByAppendingString_
        self.assert_(isinstance(v, objc.selector))

class TestMutable(TestCase):
    def testSync(self):
        """
        Test that python and ObjC string representation are not
        automaticly synchronized.
        """
        pyStr = NSMutableString.stringWithString_(u"hello")
        ocStr= pyStr.nsstring()
        self.assertEqual(pyStr, u"hello")
        self.assert_(isinstance(ocStr, NSMutableString))
        ocStr.appendString_(u" world")
        self.assertEqual(pyStr, u"hello")

class TestPickle(TestCase):
    """
    Testcases for pickling of Objective-C strings. Those are pickled as
    unicode strings.
    """

    def setUp(self):
        self.strVal = NSTaskDidTerminateNotification

    def testPickle(self):
        """
        Check that ObjC-strings pickle as unicode strings
        """
        import pickle

        s = pickle.dumps(self.strVal, 0)
        v = pickle.loads(s)
        self.assertEqual(type(v), types.UnicodeType)

        s = pickle.dumps(self.strVal, 1)
        v = pickle.loads(s)
        self.assertEqual(type(v), types.UnicodeType)

        s = pickle.dumps(self.strVal, 2)
        v = pickle.loads(s)
        self.assertEqual(type(v), types.UnicodeType)

    def testCPickle(self):
        """
        Check that ObjC-strings pickle as unicode strings
        """
        import cPickle as pickle

        s = pickle.dumps(self.strVal, 0)
        v = pickle.loads(s)
        self.assertEqual(type(v), types.UnicodeType)

        s = pickle.dumps(self.strVal, 1)
        v = pickle.loads(s)
        self.assertEqual(type(v), types.UnicodeType)

        s = pickle.dumps(self.strVal, 2)
        v = pickle.loads(s)
        self.assertEqual(type(v), types.UnicodeType)

    def testFormat(self):
        v = self.strVal

        d = v.stringByAppendingFormat_(u"hello")
        self.assertEqual(d, v + u'hello')

        d = v.stringByAppendingFormat_(u"hello %s %d", b"world", 101)
        self.assertEqual(d, v + u'hello world 101')

        v = NSString.alloc().initWithFormat_("%s %d %s", b"a", 44, b"cc")
        self.assertEqual(v, "a 44 cc")

        v = NSString.alloc().initWithFormat_locale_("%s %d %s", None, b"a", 44, b"cc")
        self.assertEqual(v, "a 44 cc")

        v = NSString.stringWithFormat_("aap %s mies", b"noot")
        self.assertEqual(v, "aap noot mies")

        v = NSString.localizedStringWithFormat_("aap %s mies", b"noot")
        self.assertEqual(v, "aap noot mies")


        v = NSMutableString.stringWithString_("hello")
        v.appendFormat_(" bar %s", b"baz")
        self.assertEqual(v.nsstring(), "hello bar baz")


    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertEqual(NSMaximumStringLength, sys.maxint-1)
        self.assertEqual(NSDiacriticInsensitiveSearch, 128)
        self.assertEqual(NSWidthInsensitiveSearch, 256)
        self.assertEqual(NSForcedOrderingSearch, 512)

        self.assertEqual(NSProprietaryStringEncoding, 65536)

    def testConstants(self):
        self.assertIsInstance(NSParseErrorException, unicode)
        self.assertIsInstance(NSCharacterConversionException, unicode)

        self.assertEqual(NSCaseInsensitiveSearch, 1)
        self.assertEqual(NSLiteralSearch, 2)
        self.assertEqual(NSBackwardsSearch, 4)
        self.assertEqual(NSAnchoredSearch, 8)
        self.assertEqual(NSNumericSearch, 64)
        self.assertEqual(NSASCIIStringEncoding, 1)
        self.assertEqual(NSNEXTSTEPStringEncoding, 2)
        self.assertEqual(NSJapaneseEUCStringEncoding, 3)
        self.assertEqual(NSUTF8StringEncoding, 4)
        self.assertEqual(NSISOLatin1StringEncoding, 5)
        self.assertEqual(NSSymbolStringEncoding, 6)
        self.assertEqual(NSNonLossyASCIIStringEncoding, 7)
        self.assertEqual(NSShiftJISStringEncoding, 8)
        self.assertEqual(NSISOLatin2StringEncoding, 9)
        self.assertEqual(NSUnicodeStringEncoding, 10)
        self.assertEqual(NSWindowsCP1251StringEncoding, 11)
        self.assertEqual(NSWindowsCP1252StringEncoding, 12)
        self.assertEqual(NSWindowsCP1253StringEncoding, 13)
        self.assertEqual(NSWindowsCP1254StringEncoding, 14)
        self.assertEqual(NSWindowsCP1250StringEncoding, 15)
        self.assertEqual(NSISO2022JPStringEncoding, 21)
        self.assertEqual(NSMacOSRomanStringEncoding, 30)
        self.assertEqual(NSUTF16StringEncoding, NSUnicodeStringEncoding)
        self.assertEqual(NSUTF16BigEndianStringEncoding, cast_int(0x90000100))
        self.assertEqual(NSUTF16LittleEndianStringEncoding, cast_int(0x94000100))
        self.assertEqual(NSUTF32StringEncoding, cast_int(0x8c000100))
        self.assertEqual(NSUTF32BigEndianStringEncoding, cast_int(0x98000100))
        self.assertEqual(NSUTF32LittleEndianStringEncoding, cast_int(0x9c000100))
        self.assertEqual(NSStringEncodingConversionAllowLossy, 1)
        self.assertEqual(NSStringEncodingConversionExternalRepresentation, 2)

    def testMethods(self):
        self.assertArgHasType(NSString.getCharacters_range_, 0, b'o^' + objc._C_UNICHAR)
        self.assertArgSizeInArg(NSString.getCharacters_range_, 0, 1)

        self.assertResultIsBOOL(NSString.isEqualToString_)
        self.assertResultIsBOOL(NSString.hasPrefix_)
        self.assertResultIsBOOL(NSString.hasSuffix_)
        self.assertResultIsBOOL(NSString.boolValue)
        self.assertArgIsOut(NSString.getLineStart_end_contentsEnd_forRange_, 0)
        self.assertArgIsOut(NSString.getLineStart_end_contentsEnd_forRange_, 1)
        self.assertArgIsOut(NSString.getLineStart_end_contentsEnd_forRange_, 2)
        self.assertArgIsOut(NSString.getParagraphStart_end_contentsEnd_forRange_, 0)
        self.assertArgIsOut(NSString.getParagraphStart_end_contentsEnd_forRange_, 1)
        self.assertArgIsOut(NSString.getParagraphStart_end_contentsEnd_forRange_, 2)
        self.assertArgIsBOOL(NSString.dataUsingEncoding_allowLossyConversion_, 1)
        self.assertResultIsBOOL(NSString.canBeConvertedToEncoding_)
        self.assertResultIsNullTerminated(NSString.cStringUsingEncoding_)
        self.assertResultHasType(NSString.cStringUsingEncoding_, b'^v')
        self.assertResultIsBOOL(NSString.getCString_maxLength_encoding_)
        self.assertArgHasType(NSString.getCString_maxLength_encoding_, 0, b'o^v')
        self.assertArgSizeInArg(NSString.getCString_maxLength_encoding_, 0, 1)

        self.assertResultIsBOOL(NSString.getBytes_maxLength_usedLength_encoding_options_range_remainingRange_)
        self.assertArgHasType(NSString.getBytes_maxLength_usedLength_encoding_options_range_remainingRange_, 0, b'o^v')
        self.assertArgSizeInArg(NSString.getBytes_maxLength_usedLength_encoding_options_range_remainingRange_, 0, (1,2))
        self.assertArgIsOut(NSString.getBytes_maxLength_usedLength_encoding_options_range_remainingRange_, 2)
        self.assertArgIsOut(NSString.getBytes_maxLength_usedLength_encoding_options_range_remainingRange_, 6)

        self.assertResultHasType(NSString.UTF8String, b'^' + objc._C_CHAR_AS_TEXT)
        self.assertResultIsNullTerminated(NSString.UTF8String)
        self.assertResultIsNullTerminated(NSString.availableStringEncodings)

        self.assertArgHasType(NSString.initWithCharactersNoCopy_length_freeWhenDone_, 0, b'n^' + objc._C_UNICHAR)
        self.assertArgSizeInArg(NSString.initWithCharactersNoCopy_length_freeWhenDone_, 0, 1)
        self.assertArgIsBOOL(NSString.initWithCharactersNoCopy_length_freeWhenDone_, 2)
        self.assertArgHasType(NSString.initWithCharacters_length_, 0, b'n^' + objc._C_UNICHAR)
        self.assertArgSizeInArg(NSString.initWithCharacters_length_, 0, 1)
        self.assertArgHasType(NSString.initWithUTF8String_, 0, b'n^' + objc._C_CHAR_AS_TEXT)
        self.assertArgIsNullTerminated(NSString.initWithUTF8String_, 0)
        self.assertArgIsPrintf(NSString.initWithFormat_, 0)
        self.assertArgIsPrintf(NSString.initWithFormat_locale_, 0)

        o = NSString.alloc()
        self.assertArgIsIn(o.initWithBytes_length_encoding_, 0)
        self.assertArgSizeInArg(o.initWithBytes_length_encoding_, 0, 1)
        o = o.init()
        self.assertArgIsIn(NSString.initWithBytesNoCopy_length_encoding_freeWhenDone_, 0)
        self.assertArgSizeInArg(NSString.initWithBytesNoCopy_length_encoding_freeWhenDone_, 0, 1)
        self.assertArgIsBOOL(NSString.initWithBytesNoCopy_length_encoding_freeWhenDone_, 3)

        self.assertArgHasType(NSString.stringWithCharacters_length_, 0, b'n^' + objc._C_UNICHAR)
        self.assertArgSizeInArg(NSString.stringWithCharacters_length_, 0, 1)
        self.assertArgHasType(NSString.stringWithUTF8String_, 0, b'n^' + objc._C_CHAR_AS_TEXT)
        self.assertArgIsNullTerminated(NSString.stringWithUTF8String_, 0)
        self.assertArgIsPrintf(NSString.stringWithFormat_, 0)
        self.assertArgIsPrintf(NSString.localizedStringWithFormat_, 0)

        self.assertArgHasType(NSString.initWithCString_encoding_, 0, b'n^t')
        self.assertArgIsNullTerminated(NSString.initWithCString_encoding_, 0)
        self.assertArgHasType(NSString.stringWithCString_encoding_, 0, b'n^t')
        self.assertArgIsNullTerminated(NSString.stringWithCString_encoding_, 0)

        self.assertArgIsOut(NSString.initWithContentsOfURL_encoding_error_, 2)
        self.assertArgIsOut(NSString.initWithContentsOfFile_encoding_error_, 2)
        self.assertArgIsOut(NSString.stringWithContentsOfURL_encoding_error_, 2)
        self.assertArgIsOut(NSString.stringWithContentsOfFile_encoding_error_, 2)

        self.assertArgIsOut(NSString.initWithContentsOfURL_usedEncoding_error_, 1)
        self.assertArgIsOut(NSString.initWithContentsOfURL_usedEncoding_error_, 2)
        self.assertArgIsOut(NSString.initWithContentsOfFile_usedEncoding_error_, 1)
        self.assertArgIsOut(NSString.initWithContentsOfFile_usedEncoding_error_, 2)
        self.assertArgIsOut(NSString.stringWithContentsOfURL_usedEncoding_error_, 1)
        self.assertArgIsOut(NSString.stringWithContentsOfURL_usedEncoding_error_, 2)
        self.assertArgIsOut(NSString.stringWithContentsOfFile_usedEncoding_error_, 1)
        self.assertArgIsOut(NSString.stringWithContentsOfFile_usedEncoding_error_, 2)

        self.assertResultIsBOOL(NSString.writeToURL_atomically_encoding_error_)
        self.assertArgIsBOOL(NSString.writeToURL_atomically_encoding_error_, 1)
        self.assertArgIsOut(NSString.writeToURL_atomically_encoding_error_, 3)
        self.assertResultIsBOOL(NSString.writeToFile_atomically_encoding_error_)
        self.assertArgIsBOOL(NSString.writeToFile_atomically_encoding_error_, 1)
        self.assertArgIsOut(NSString.writeToFile_atomically_encoding_error_, 3)

        self.assertArgIsPrintf(NSMutableString.appendFormat_, 0)

        self.assertResultHasType(NSString.cString, b'^t')
        self.assertResultIsNullTerminated(NSString.cString)
        self.assertResultHasType(NSString.lossyCString, b'^t')
        self.assertResultIsNullTerminated(NSString.lossyCString)

        self.assertArgHasType(NSString.getCString_maxLength_, 0, b'o^v')
        self.assertArgSizeInArg(NSString.getCString_maxLength_, 0, 1)

        self.assertArgHasType(NSString.getCString_maxLength_range_remainingRange_, 0, b'o^v')
        self.assertArgSizeInArg(NSString.getCString_maxLength_range_remainingRange_, 0, 1)
        self.assertArgIsOut(NSString.getCString_maxLength_range_remainingRange_, 3)

        self.assertResultIsBOOL(NSString.writeToFile_atomically_)
        self.assertArgIsBOOL(NSString.writeToFile_atomically_, 1)
        self.assertResultIsBOOL(NSString.writeToURL_atomically_)
        self.assertArgIsBOOL(NSString.writeToURL_atomically_, 1)

        self.assertArgHasType(NSString.initWithCStringNoCopy_length_freeWhenDone_, 0, b'n^v')
        self.assertArgSizeInArg(NSString.initWithCStringNoCopy_length_freeWhenDone_, 0, 1)
        self.assertArgIsBOOL(NSString.initWithCStringNoCopy_length_freeWhenDone_, 2)
        self.assertArgHasType(NSString.initWithCString_length_, 0, b'n^v')
        self.assertArgSizeInArg(NSString.initWithCString_length_, 0, 1)
        self.assertArgHasType(NSString.initWithCString_, 0, b'n^v')
        self.assertArgIsNullTerminated(NSString.initWithCString_, 0)

        self.assertArgHasType(NSString.stringWithCString_length_, 0, b'n^v')
        self.assertArgSizeInArg(NSString.stringWithCString_length_, 0, 1)
        self.assertArgHasType(NSString.stringWithCString_, 0, b'n^v')
        self.assertArgIsNullTerminated(NSString.stringWithCString_, 0)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSStringEnumerationByLines, 0)
        self.assertEqual(NSStringEnumerationByParagraphs, 1)
        self.assertEqual(NSStringEnumerationByComposedCharacterSequences, 2)
        self.assertEqual(NSStringEnumerationByWords, 3)
        self.assertEqual(NSStringEnumerationBySentences, 4)
        self.assertEqual(NSStringEnumerationReverse, 1 << 8)
        self.assertEqual(NSStringEnumerationSubstringNotRequired, 1 << 9)
        self.assertEqual(NSStringEnumerationLocalized, 1 << 10)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgHasType(NSString.enumerateSubstringsInRange_options_usingBlock_, 0, 
                NSRange.__typestr__)
        self.assertArgIsBlock(NSString.enumerateSubstringsInRange_options_usingBlock_, 2, b'v@'+NSRange.__typestr__+NSRange.__typestr__+b'o^'+objc._C_NSBOOL)
        self.assertArgIsBlock(NSString.enumerateLinesUsingBlock_, 0, b'v@o^'+objc._C_NSBOOL)

    

if __name__ == '__main__':
    main()
