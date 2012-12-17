from PyObjCTools.TestSupport import *
from CoreFoundation import *
from Foundation import *

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


class TestError (TestCase):

    @min_os_level('10.5')
    def testTypes(self):
        try:
            NSCFError = objc.lookUpClass('__NSCFError')
        except objc.error:
            NSCFError = objc.lookUpClass('NSCFError')

        self.assertIs(CFErrorRef, NSCFError)

    @min_os_level('10.5')
    def testTypeID(self):
        self.assertIsInstance(CFErrorGetTypeID(), (int, long))

    @min_os_level('10.5')
    def testCreation(self):
        userInfo = {
                b'foo'.decode('ascii'): b'bar'.decode('ascii'),
        }
        err = CFErrorCreate(None, kCFErrorDomainPOSIX, 42,  userInfo)
        self.assertIsInstance(err, CFErrorRef)
        self.assertResultIsCFRetained(CFErrorCopyUserInfo)
        dct = CFErrorCopyUserInfo(err)
        self.assertEqual(dct, userInfo)

        keys = [ b"key1".decode('ascii'), b"key2".decode('ascii')]
        values = [ b"value1".decode('ascii'), b"value2".decode('ascii')]

        keys = [ NSString.stringWithString_(v) for v in keys ]
        values = [ NSString.stringWithString_(v) for v in values ]

        self.assertArgHasType(CFErrorCreateWithUserInfoKeysAndValues, 3, b'n^@')
        self.assertArgSizeInArg(CFErrorCreateWithUserInfoKeysAndValues, 3, 5)
        self.assertArgHasType(CFErrorCreateWithUserInfoKeysAndValues, 4, b'n^@')
        self.assertArgSizeInArg(CFErrorCreateWithUserInfoKeysAndValues, 4, 5)
        err = CFErrorCreateWithUserInfoKeysAndValues(None, kCFErrorDomainPOSIX, 42, keys, values, 2)
        self.assertIsInstance(err, CFErrorRef)
        dct = CFErrorCopyUserInfo(err)
        self.assertEqual(dct, {b'key1'.decode('ascii'): b'value1'.decode('ascii'), b'key2'.decode('ascii'):b'value2'.decode('ascii')})

    @min_os_level('10.5')
    def testInspection(self):
        userInfo = {
                b'foo'.decode('ascii'): b'bar'.decode('ascii'),
                kCFErrorLocalizedFailureReasonKey: "failure reason",
                kCFErrorLocalizedRecoverySuggestionKey: 'recovery suggestion',
        }
        self.assertResultIsCFRetained(CFErrorCreate)
        err = CFErrorCreate(None, kCFErrorDomainPOSIX, 42,  userInfo)
        self.assertIsInstance(err, CFErrorRef)
        dom = CFErrorGetDomain(err)
        self.assertEqual(dom, kCFErrorDomainPOSIX)

        code = CFErrorGetCode(err)
        self.assertEqual(code, 42)

        self.assertResultIsCFRetained(CFErrorCopyDescription)
        v = CFErrorCopyDescription(err)
        self.assertIn(v, (
            b'Operation could not be completed. failure reason'.decode('ascii'),
            b'The operation couldn%st be completed. failure reason'.decode('ascii')%(unichr(0x2019),)))

        self.assertResultIsCFRetained(CFErrorCopyFailureReason)
        v = CFErrorCopyFailureReason(err)
        self.assertEqual(v, b'failure reason'.decode('ascii'))

        self.assertResultIsCFRetained(CFErrorCopyRecoverySuggestion)
        v = CFErrorCopyRecoverySuggestion(err)
        self.assertEqual(v, b'recovery suggestion'.decode('ascii'))

    @min_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(kCFErrorDomainPOSIX, unicode)
        self.assertIsInstance(kCFErrorDomainOSStatus, unicode)
        self.assertIsInstance(kCFErrorDomainMach, unicode)
        self.assertIsInstance(kCFErrorDomainCocoa, unicode)
        self.assertIsInstance(kCFErrorLocalizedDescriptionKey, unicode)
        self.assertIsInstance(kCFErrorLocalizedFailureReasonKey, unicode)
        self.assertIsInstance(kCFErrorLocalizedRecoverySuggestionKey, unicode)
        self.assertIsInstance(kCFErrorDescriptionKey, unicode)
        self.assertIsInstance(kCFErrorUnderlyingErrorKey, unicode)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(kCFErrorURLKey, unicode)
        self.assertIsInstance(kCFErrorFilePathKey, unicode)

if __name__ == "__main__":
    main()
