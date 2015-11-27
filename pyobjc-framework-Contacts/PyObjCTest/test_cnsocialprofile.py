from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2**32:
    import Contacts

    class TestCNSocialProfile (TestCase):
        @min_os_level("10.11")
        def testConstants(self):
            self.assertIsInstance(Contacts.CNSocialProfileURLStringKey, unicode)
            self.assertIsInstance(Contacts.CNSocialProfileUsernameKey, unicode)
            self.assertIsInstance(Contacts.CNSocialProfileUserIdentifierKey, unicode)
            self.assertIsInstance(Contacts.CNSocialProfileServiceKey, unicode)
            self.assertIsInstance(Contacts.CNSocialProfileServiceFacebook, unicode)
            self.assertIsInstance(Contacts.CNSocialProfileServiceFlickr, unicode)
            self.assertIsInstance(Contacts.CNSocialProfileServiceLinkedIn, unicode)
            self.assertIsInstance(Contacts.CNSocialProfileServiceMySpace, unicode)
            self.assertIsInstance(Contacts.CNSocialProfileServiceSinaWeibo, unicode)
            self.assertIsInstance(Contacts.CNSocialProfileServiceTencentWeibo, unicode)
            self.assertIsInstance(Contacts.CNSocialProfileServiceTwitter, unicode)
            self.assertIsInstance(Contacts.CNSocialProfileServiceYelp, unicode)
            self.assertIsInstance(Contacts.CNSocialProfileServiceGameCenter, unicode)

if __name__ == "__main__":
    main()
