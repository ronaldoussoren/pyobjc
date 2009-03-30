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
        self.assertEquals(obj, u"foo 42")

        obj = NSString.alloc().initWithFormat_locale_(u"foo %d", {}, 42)
        self.assertEquals(obj, u"foo 42")


    def testGetCString(self):
        # Custom wrappers
        v = NSString.stringWithString_(u"hello world")
        
        self.assertEquals(v, u"hello world")

        x = v.getCString_maxLength_(16)
        self.assertEquals(x, u"hello world")

        self.assertRaises(objc.error, v.getCString_maxLength_, 4)

        x, l = v.getCString_maxLength_range_remainingRange_(4, (1, 4))
        self.assertEquals(x, "ello")
        self.assertEquals(l.location, 5)
        self.assertEquals(l.length, 0)


class TestNSStringBridging(TestCase):
    def setUp(self):
        self.nsUniString = NSString.stringWithString_(u"unifoo")
        self.pyUniString = u"unifoo"

    def testBasicComparison(self):
        self.assertEquals(u"unifoo", NSString.stringWithString_(u"unifoo"))

        u = u'\xc3\xbc\xc3\xb1\xc3\xae\xc3\xa7\xc3\xb8d\xc3\xa8'
        self.assertEquals(u, NSString.stringWithString_(u));

    def testTypesAndClasses(self):
        self.assert_(isinstance(self.nsUniString, unicode))
        self.assert_(isinstance(self.pyUniString, unicode))

    def testStrConversion(self):
        curEnabledFlag = objc.getStrBridgeEnabled()
        objc.setStrBridgeEnabled(True)
        try:
            v = NSString.stringWithString_("hello2")
            self.assert_(isinstance(v, objc.pyobjc_unicode))
            self.assertEquals(v, u"hello2")


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
        self.assertEquals(pyStr, u"hello")
        self.assert_(isinstance(ocStr, NSMutableString))
        ocStr.appendString_(u" world")
        self.assertEquals(pyStr, u"hello")

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
        self.assertEquals(type(v), types.UnicodeType)

        s = pickle.dumps(self.strVal, 1)
        v = pickle.loads(s)
        self.assertEquals(type(v), types.UnicodeType)

        s = pickle.dumps(self.strVal, 2)
        v = pickle.loads(s)
        self.assertEquals(type(v), types.UnicodeType)

    def testCPickle(self):
        """
        Check that ObjC-strings pickle as unicode strings
        """
        import cPickle as pickle

        s = pickle.dumps(self.strVal, 0)
        v = pickle.loads(s)
        self.assertEquals(type(v), types.UnicodeType)

        s = pickle.dumps(self.strVal, 1)
        v = pickle.loads(s)
        self.assertEquals(type(v), types.UnicodeType)

        s = pickle.dumps(self.strVal, 2)
        v = pickle.loads(s)
        self.assertEquals(type(v), types.UnicodeType)

    def testFormat(self):
        v = self.strVal

        d = v.stringByAppendingFormat_(u"hello")
        self.assertEquals(d, v + u'hello')

        d = v.stringByAppendingFormat_(u"hello %s %d", "world", 101)
        self.assertEquals(d, v + u'hello world 101')

        v = NSString.alloc().initWithFormat_("%s %d %s", "a", 44, "cc")
        self.assertEquals(v, "a 44 cc")

        v = NSString.alloc().initWithFormat_locale_("%s %d %s", None, "a", 44, "cc")
        self.assertEquals(v, "a 44 cc")

        v = NSString.stringWithFormat_("aap %s mies", "noot")
        self.assertEquals(v, "aap noot mies")

        v = NSString.localizedStringWithFormat_("aap %s mies", "noot")
        self.assertEquals(v, "aap noot mies")


        v = NSMutableString.stringWithString_("hello")
        v.appendFormat_(" bar %s", "baz")
        self.assertEquals(v.nsstring(), "hello bar baz")


    @min_os_level('10.5')
    def testConstants10_5(self):
        self.failUnlessEqual(NSMaximumStringLength, sys.maxint-1)
        self.failUnlessEqual(NSDiacriticInsensitiveSearch, 128)
        self.failUnlessEqual(NSWidthInsensitiveSearch, 256)
        self.failUnlessEqual(NSForcedOrderingSearch, 512)

        self.failUnlessEqual(NSProprietaryStringEncoding, 65536)

    def testConstants(self):
        self.failUnlessIsInstance(NSParseErrorException, unicode)
        self.failUnlessIsInstance(NSCharacterConversionException, unicode)

        self.failUnlessEqual(NSCaseInsensitiveSearch, 1)
        self.failUnlessEqual(NSLiteralSearch, 2)
        self.failUnlessEqual(NSBackwardsSearch, 4)
        self.failUnlessEqual(NSAnchoredSearch, 8)
        self.failUnlessEqual(NSNumericSearch, 64)
        self.failUnlessEqual(NSASCIIStringEncoding, 1)
        self.failUnlessEqual(NSNEXTSTEPStringEncoding, 2)
        self.failUnlessEqual(NSJapaneseEUCStringEncoding, 3)
        self.failUnlessEqual(NSUTF8StringEncoding, 4)
        self.failUnlessEqual(NSISOLatin1StringEncoding, 5)
        self.failUnlessEqual(NSSymbolStringEncoding, 6)
        self.failUnlessEqual(NSNonLossyASCIIStringEncoding, 7)
        self.failUnlessEqual(NSShiftJISStringEncoding, 8)
        self.failUnlessEqual(NSISOLatin2StringEncoding, 9)
        self.failUnlessEqual(NSUnicodeStringEncoding, 10)
        self.failUnlessEqual(NSWindowsCP1251StringEncoding, 11)
        self.failUnlessEqual(NSWindowsCP1252StringEncoding, 12)
        self.failUnlessEqual(NSWindowsCP1253StringEncoding, 13)
        self.failUnlessEqual(NSWindowsCP1254StringEncoding, 14)
        self.failUnlessEqual(NSWindowsCP1250StringEncoding, 15)
        self.failUnlessEqual(NSISO2022JPStringEncoding, 21)
        self.failUnlessEqual(NSMacOSRomanStringEncoding, 30)
        self.failUnlessEqual(NSUTF16StringEncoding, NSUnicodeStringEncoding)
        self.failUnlessEqual(NSUTF16BigEndianStringEncoding, cast_int(0x90000100))
        self.failUnlessEqual(NSUTF16LittleEndianStringEncoding, cast_int(0x94000100))
        self.failUnlessEqual(NSUTF32StringEncoding, cast_int(0x8c000100))
        self.failUnlessEqual(NSUTF32BigEndianStringEncoding, cast_int(0x98000100))
        self.failUnlessEqual(NSUTF32LittleEndianStringEncoding, cast_int(0x9c000100))
        self.failUnlessEqual(NSStringEncodingConversionAllowLossy, 1)
        self.failUnlessEqual(NSStringEncodingConversionExternalRepresentation, 2)

    def testMethods(self):
        self.failUnlessArgHasType(NSString.getCharacters_range_, 0, 'o^' + objc._C_UNICHAR)
        self.failUnlessArgSizeInArg(NSString.getCharacters_range_, 0, 1)

        self.failUnlessResultIsBOOL(NSString.isEqualToString_)
        self.failUnlessResultIsBOOL(NSString.hasPrefix_)
        self.failUnlessResultIsBOOL(NSString.hasSuffix_)
        self.failUnlessResultIsBOOL(NSString.boolValue)
        self.failUnlessArgIsOut(NSString.getLineStart_end_contentsEnd_forRange_, 0)
        self.failUnlessArgIsOut(NSString.getLineStart_end_contentsEnd_forRange_, 1)
        self.failUnlessArgIsOut(NSString.getLineStart_end_contentsEnd_forRange_, 2)
        self.failUnlessArgIsOut(NSString.getParagraphStart_end_contentsEnd_forRange_, 0)
        self.failUnlessArgIsOut(NSString.getParagraphStart_end_contentsEnd_forRange_, 1)
        self.failUnlessArgIsOut(NSString.getParagraphStart_end_contentsEnd_forRange_, 2)
        self.failUnlessArgIsBOOL(NSString.dataUsingEncoding_allowLossyConversion_, 1)
        self.failUnlessResultIsBOOL(NSString.canBeConvertedToEncoding_)
        self.failUnlessResultIsNullTerminated(NSString.cStringUsingEncoding_)
        self.failUnlessResultHasType(NSString.cStringUsingEncoding_, '^v')
        self.failUnlessResultIsBOOL(NSString.getCString_maxLength_encoding_)
        self.failUnlessArgHasType(NSString.getCString_maxLength_encoding_, 0, 'o^v')
        self.failUnlessArgSizeInArg(NSString.getCString_maxLength_encoding_, 0, 1)

        self.failUnlessResultIsBOOL(NSString.getBytes_maxLength_usedLength_encoding_options_range_remainingRange_)
        self.failUnlessArgHasType(NSString.getBytes_maxLength_usedLength_encoding_options_range_remainingRange_, 0, 'o^v')
        self.failUnlessArgSizeInArg(NSString.getBytes_maxLength_usedLength_encoding_options_range_remainingRange_, 0, (1,2))
        self.failUnlessArgIsOut(NSString.getBytes_maxLength_usedLength_encoding_options_range_remainingRange_, 2)
        self.failUnlessArgIsOut(NSString.getBytes_maxLength_usedLength_encoding_options_range_remainingRange_, 6)

        self.failUnlessResultHasType(NSString.UTF8String, '^' + objc._C_CHAR_AS_TEXT)
        self.failUnlessResultIsNullTerminated(NSString.UTF8String)
        self.failUnlessResultIsNullTerminated(NSString.availableStringEncodings)

        self.failUnlessArgHasType(NSString.initWithCharactersNoCopy_length_freeWhenDone_, 0, 'n^' + objc._C_UNICHAR)
        self.failUnlessArgSizeInArg(NSString.initWithCharactersNoCopy_length_freeWhenDone_, 0, 1)
        self.failUnlessArgIsBOOL(NSString.initWithCharactersNoCopy_length_freeWhenDone_, 2)
        self.failUnlessArgHasType(NSString.initWithCharacters_length_, 0, 'n^' + objc._C_UNICHAR)
        self.failUnlessArgSizeInArg(NSString.initWithCharacters_length_, 0, 1)
        self.failUnlessArgHasType(NSString.initWithUTF8String_, 0, 'n^' + objc._C_CHAR_AS_TEXT)
        self.failUnlessArgIsNullTerminated(NSString.initWithUTF8String_, 0)
        self.failUnlessArgIsPrintf(NSString.initWithFormat_, 0)
        self.failUnlessArgIsPrintf(NSString.initWithFormat_locale_, 0)

        o = NSString.alloc()
        self.failUnlessArgIsIn(o.initWithBytes_length_encoding_, 0)
        self.failUnlessArgSizeInArg(o.initWithBytes_length_encoding_, 0, 1)
        o = o.init()
        self.failUnlessArgIsIn(NSString.initWithBytesNoCopy_length_encoding_freeWhenDone_, 0)
        self.failUnlessArgSizeInArg(NSString.initWithBytesNoCopy_length_encoding_freeWhenDone_, 0, 1)
        self.failUnlessArgIsBOOL(NSString.initWithBytesNoCopy_length_encoding_freeWhenDone_, 3)

        self.failUnlessArgHasType(NSString.stringWithCharacters_length_, 0, 'n^' + objc._C_UNICHAR)
        self.failUnlessArgSizeInArg(NSString.stringWithCharacters_length_, 0, 1)
        self.failUnlessArgHasType(NSString.stringWithUTF8String_, 0, 'n^' + objc._C_CHAR_AS_TEXT)
        self.failUnlessArgIsNullTerminated(NSString.stringWithUTF8String_, 0)
        self.failUnlessArgIsPrintf(NSString.stringWithFormat_, 0)
        self.failUnlessArgIsPrintf(NSString.localizedStringWithFormat_, 0)

        self.failUnlessArgHasType(NSString.initWithCString_encoding_, 0, 'n^t')
        self.failUnlessArgIsNullTerminated(NSString.initWithCString_encoding_, 0)
        self.failUnlessArgHasType(NSString.stringWithCString_encoding_, 0, 'n^t')
        self.failUnlessArgIsNullTerminated(NSString.stringWithCString_encoding_, 0)

        self.failUnlessArgIsOut(NSString.initWithContentsOfURL_encoding_error_, 2)
        self.failUnlessArgIsOut(NSString.initWithContentsOfFile_encoding_error_, 2)
        self.failUnlessArgIsOut(NSString.stringWithContentsOfURL_encoding_error_, 2)
        self.failUnlessArgIsOut(NSString.stringWithContentsOfFile_encoding_error_, 2)

        self.failUnlessArgIsOut(NSString.initWithContentsOfURL_usedEncoding_error_, 1)
        self.failUnlessArgIsOut(NSString.initWithContentsOfURL_usedEncoding_error_, 2)
        self.failUnlessArgIsOut(NSString.initWithContentsOfFile_usedEncoding_error_, 1)
        self.failUnlessArgIsOut(NSString.initWithContentsOfFile_usedEncoding_error_, 2)
        self.failUnlessArgIsOut(NSString.stringWithContentsOfURL_usedEncoding_error_, 1)
        self.failUnlessArgIsOut(NSString.stringWithContentsOfURL_usedEncoding_error_, 2)
        self.failUnlessArgIsOut(NSString.stringWithContentsOfFile_usedEncoding_error_, 1)
        self.failUnlessArgIsOut(NSString.stringWithContentsOfFile_usedEncoding_error_, 2)

        self.failUnlessResultIsBOOL(NSString.writeToURL_atomically_encoding_error_)
        self.failUnlessArgIsBOOL(NSString.writeToURL_atomically_encoding_error_, 1)
        self.failUnlessArgIsOut(NSString.writeToURL_atomically_encoding_error_, 3)
        self.failUnlessResultIsBOOL(NSString.writeToFile_atomically_encoding_error_)
        self.failUnlessArgIsBOOL(NSString.writeToFile_atomically_encoding_error_, 1)
        self.failUnlessArgIsOut(NSString.writeToFile_atomically_encoding_error_, 3)

        self.failUnlessArgIsPrintf(NSMutableString.appendFormat_, 0)

        self.failUnlessResultHasType(NSString.cString, '^t')
        self.failUnlessResultIsNullTerminated(NSString.cString)
        self.failUnlessResultHasType(NSString.lossyCString, '^t')
        self.failUnlessResultIsNullTerminated(NSString.lossyCString)

        self.failUnlessArgHasType(NSString.getCString_maxLength_, 0, 'o^v')
        self.failUnlessArgSizeInArg(NSString.getCString_maxLength_, 0, 1)

        self.failUnlessArgHasType(NSString.getCString_maxLength_range_remainingRange_, 0, 'o^v')
        self.failUnlessArgSizeInArg(NSString.getCString_maxLength_range_remainingRange_, 0, 1)
        self.failUnlessArgIsOut(NSString.getCString_maxLength_range_remainingRange_, 3)

        self.failUnlessResultIsBOOL(NSString.writeToFile_atomically_)
        self.failUnlessArgIsBOOL(NSString.writeToFile_atomically_, 1)
        self.failUnlessResultIsBOOL(NSString.writeToURL_atomically_)
        self.failUnlessArgIsBOOL(NSString.writeToURL_atomically_, 1)

        self.failUnlessArgHasType(NSString.initWithCStringNoCopy_length_freeWhenDone_, 0, 'n^v')
        self.failUnlessArgSizeInArg(NSString.initWithCStringNoCopy_length_freeWhenDone_, 0, 1)
        self.failUnlessArgIsBOOL(NSString.initWithCStringNoCopy_length_freeWhenDone_, 2)
        self.failUnlessArgHasType(NSString.initWithCString_length_, 0, 'n^v')
        self.failUnlessArgSizeInArg(NSString.initWithCString_length_, 0, 1)
        self.failUnlessArgHasType(NSString.initWithCString_, 0, 'n^v')
        self.failUnlessArgIsNullTerminated(NSString.initWithCString_, 0)

        self.failUnlessArgHasType(NSString.stringWithCString_length_, 0, 'n^v')
        self.failUnlessArgSizeInArg(NSString.stringWithCString_length_, 0, 1)
        self.failUnlessArgHasType(NSString.stringWithCString_, 0, 'n^v')
        self.failUnlessArgIsNullTerminated(NSString.stringWithCString_, 0)
    

if __name__ == '__main__':
    main()
