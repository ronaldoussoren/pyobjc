from PyObjCTools.TestSupport import *
from CoreFoundation import *
from Foundation import *


class TestError (TestCase):

    @min_os_level('10.5')
    def testTypes(self):
        self.assertIs(CFErrorRef, NSCFError)
    @min_os_level('10.5')
    def testTypeID(self):
        self.assertIsInstance(CFErrorGetTypeID(), (int, long))
    @min_os_level('10.5')
    def testCreation(self):
        userInfo = {
                u'foo': u'bar',
        }
        err = CFErrorCreate(None, kCFErrorDomainPOSIX, 42,  userInfo)
        self.assertIsInstance(err, CFErrorRef)
        self.assertResultIsCFRetained(CFErrorCopyUserInfo)
        dct = CFErrorCopyUserInfo(err)
        self.assertEqual(dct, userInfo)

        keys = [ u"key1", u"key2"]
        values = [ u"value1", u"value2"]

        keys = [ NSString.stringWithString_(v) for v in keys ]
        values = [ NSString.stringWithString_(v) for v in values ]

        self.assertArgHasType(CFErrorCreateWithUserInfoKeysAndValues, 3, b'n^@')
        self.assertArgSizeInArg(CFErrorCreateWithUserInfoKeysAndValues, 3, 5)
        self.assertArgHasType(CFErrorCreateWithUserInfoKeysAndValues, 4, b'n^@')
        self.assertArgSizeInArg(CFErrorCreateWithUserInfoKeysAndValues, 4, 5)
        err = CFErrorCreateWithUserInfoKeysAndValues(None, kCFErrorDomainPOSIX, 42, keys, values, 2)
        self.assertIsInstance(err, CFErrorRef)
        dct = CFErrorCopyUserInfo(err)
        self.assertEqual(dct, {u'key1': u'value1', u'key2':u'value2'})

    @min_os_level('10.5')
    def testInspection(self):
        userInfo = {
                u'foo': u'bar',
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
        self.assertIsIn(v, (
            u'Operation could not be completed. failure reason',
            u'The operation couldn\u2019t be completed. failure reason'))

        self.assertResultIsCFRetained(CFErrorCopyFailureReason)
        v = CFErrorCopyFailureReason(err)
        self.assertEqual(v, u'failure reason')

        self.assertResultIsCFRetained(CFErrorCopyRecoverySuggestion)
        v = CFErrorCopyRecoverySuggestion(err)
        self.assertEqual(v, u'recovery suggestion')


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
if __name__ == "__main__":
    main()
