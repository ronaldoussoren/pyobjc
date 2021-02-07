from PyObjCTools.TestSupport import TestCase, min_os_level
import Contacts


class TestCNSocialProfile(TestCase):
    @min_os_level("10.11")
    def testConstants(self):
        self.assertIsInstance(Contacts.CNSocialProfileURLStringKey, str)
        self.assertIsInstance(Contacts.CNSocialProfileUsernameKey, str)
        self.assertIsInstance(Contacts.CNSocialProfileUserIdentifierKey, str)
        self.assertIsInstance(Contacts.CNSocialProfileServiceKey, str)
        self.assertIsInstance(Contacts.CNSocialProfileServiceFacebook, str)
        self.assertIsInstance(Contacts.CNSocialProfileServiceFlickr, str)
        self.assertIsInstance(Contacts.CNSocialProfileServiceLinkedIn, str)
        self.assertIsInstance(Contacts.CNSocialProfileServiceMySpace, str)
        self.assertIsInstance(Contacts.CNSocialProfileServiceSinaWeibo, str)
        self.assertIsInstance(Contacts.CNSocialProfileServiceTencentWeibo, str)
        self.assertIsInstance(Contacts.CNSocialProfileServiceTwitter, str)
        self.assertIsInstance(Contacts.CNSocialProfileServiceYelp, str)
        self.assertIsInstance(Contacts.CNSocialProfileServiceGameCenter, str)
