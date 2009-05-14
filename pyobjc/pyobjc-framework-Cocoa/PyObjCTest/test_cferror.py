from PyObjCTools.TestSupport import *
from CoreFoundation import *
from Foundation import *


class TestError (TestCase):

    @min_os_level('10.5')
    def testTypes(self):
        self.failUnless(CFErrorRef is NSCFError)

    @min_os_level('10.5')
    def testTypeID(self):
        self.failUnless(isinstance(CFErrorGetTypeID(), (int, long)))

    @min_os_level('10.5')
    def testCreation(self):
        userInfo = {
                u'foo': u'bar',
        }
        err = CFErrorCreate(None, kCFErrorDomainPOSIX, 42,  userInfo)
        self.failUnless(isinstance(err, CFErrorRef))

        self.failUnlessResultIsCFRetained(CFErrorCopyUserInfo)
        dct = CFErrorCopyUserInfo(err)
        self.assertEquals(dct, userInfo)

        keys = [ u"key1", u"key2"]
        values = [ u"value1", u"value2"]

        keys = [ NSString.stringWithString_(v) for v in keys ]
        values = [ NSString.stringWithString_(v) for v in values ]

        self.failUnlessArgHasType(CFErrorCreateWithUserInfoKeysAndValues, 3, 'n^@')
        self.failUnlessArgSizeInArg(CFErrorCreateWithUserInfoKeysAndValues, 3, 5)
        self.failUnlessArgHasType(CFErrorCreateWithUserInfoKeysAndValues, 4, 'n^@')
        self.failUnlessArgSizeInArg(CFErrorCreateWithUserInfoKeysAndValues, 4, 5)
        err = CFErrorCreateWithUserInfoKeysAndValues(None, kCFErrorDomainPOSIX, 42, keys, values, 2)
        self.failUnless(isinstance(err, CFErrorRef))
        dct = CFErrorCopyUserInfo(err)
        self.assertEquals(dct, {u'key1': u'value1', u'key2':u'value2'})

    @min_os_level('10.5')
    def testInspection(self):
        userInfo = {
                u'foo': u'bar',
                kCFErrorLocalizedFailureReasonKey: "failure reason",
                kCFErrorLocalizedRecoverySuggestionKey: 'recovery suggestion',
        }
        self.failUnlessResultIsCFRetained(CFErrorCreate)
        err = CFErrorCreate(None, kCFErrorDomainPOSIX, 42,  userInfo)
        self.failUnless(isinstance(err, CFErrorRef))

        dom = CFErrorGetDomain(err)
        self.assertEquals(dom, kCFErrorDomainPOSIX)

        code = CFErrorGetCode(err)
        self.assertEquals(code, 42)

        self.failUnlessResultIsCFRetained(CFErrorCopyDescription)
        v = CFErrorCopyDescription(err)
        self.assertEquals(v, u'Operation could not be completed. failure reason')

        self.failUnlessResultIsCFRetained(CFErrorCopyFailureReason)
        v = CFErrorCopyFailureReason(err)
        self.assertEquals(v, u'failure reason')

        self.failUnlessResultIsCFRetained(CFErrorCopyRecoverySuggestion)
        v = CFErrorCopyRecoverySuggestion(err)
        self.assertEquals(v, u'recovery suggestion')


    @min_os_level('10.5')
    def testConstants(self):
        self.failUnless(isinstance(kCFErrorDomainPOSIX, unicode))
        self.failUnless(isinstance(kCFErrorDomainOSStatus, unicode))
        self.failUnless(isinstance(kCFErrorDomainMach, unicode))
        self.failUnless(isinstance(kCFErrorDomainCocoa, unicode))
        self.failUnless(isinstance(kCFErrorLocalizedDescriptionKey, unicode))
        self.failUnless(isinstance(kCFErrorLocalizedFailureReasonKey, unicode))
        self.failUnless(isinstance(kCFErrorLocalizedRecoverySuggestionKey, unicode))
        self.failUnless(isinstance(kCFErrorDescriptionKey, unicode))
        self.failUnless(isinstance(kCFErrorUnderlyingErrorKey, unicode))

if __name__ == "__main__":
    main()
