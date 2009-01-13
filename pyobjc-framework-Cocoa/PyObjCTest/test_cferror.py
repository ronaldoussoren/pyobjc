from PyObjCTools.TestSupport import *
from CoreFoundation import *
from Foundation import NSString


class TestError (TestCase):

    def testTypeID(self):
        self.failUnless(isinstance(CFErrorGetTypeID(), (int, long)))

    def testCreation(self):
        userInfo = {
                u'foo': u'bar',
        }
        err = CFErrorCreate(None, kCFErrorDomainPOSIX, 42,  userInfo)
        self.failUnless(isinstance(err, CFErrorRef))

        dct = CFErrorCopyUserInfo(err)
        self.assertEquals(dct, userInfo)

        keys = [ u"key1", u"key2"]
        values = [ u"value1", u"value2"]

        keys = [ NSString.stringWithString_(v) for v in keys ]
        values = [ NSString.stringWithString_(v) for v in values ]

        err = CFErrorCreateWithUserInfoKeysAndValues(None, kCFErrorDomainPOSIX, 42, keys, values, 2)
        self.failUnless(isinstance(err, CFErrorRef))
        dct = CFErrorCopyUserInfo(err)
        self.assertEquals(dct, {u'key1': u'value1', u'key2':u'value2'})

    def testInspection(self):
        userInfo = {
                u'foo': u'bar',
                kCFErrorLocalizedFailureReasonKey: "failure reason",
                kCFErrorLocalizedRecoverySuggestionKey: 'recovery suggestion',
        }
        err = CFErrorCreate(None, kCFErrorDomainPOSIX, 42,  userInfo)
        self.failUnless(isinstance(err, CFErrorRef))

        dom = CFErrorGetDomain(err)
        self.assertEquals(dom, kCFErrorDomainPOSIX)

        code = CFErrorGetCode(err)
        self.assertEquals(code, 42)

        v = CFErrorCopyDescription(err)
        self.assertEquals(v, u'Operation could not be completed. failure reason')

        v = CFErrorCopyFailureReason(err)
        self.assertEquals(v, u'failure reason')

        v = CFErrorCopyRecoverySuggestion(err)
        self.assertEquals(v, u'recovery suggestion')

    


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
