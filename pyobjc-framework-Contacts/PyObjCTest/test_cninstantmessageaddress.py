from PyObjCTools.TestSupport import TestCase, min_os_level
import Contacts


class TestCNInstantMessageAddress(TestCase):
    @min_os_level("10.11")
    def testConstants(self):
        self.assertIsInstance(Contacts.CNInstantMessageAddressUsernameKey, str)
        self.assertIsInstance(Contacts.CNInstantMessageAddressServiceKey, str)
        self.assertIsInstance(Contacts.CNInstantMessageServiceAIM, str)
        self.assertIsInstance(Contacts.CNInstantMessageServiceFacebook, str)
        self.assertIsInstance(Contacts.CNInstantMessageServiceGaduGadu, str)
        self.assertIsInstance(Contacts.CNInstantMessageServiceGoogleTalk, str)
        self.assertIsInstance(Contacts.CNInstantMessageServiceICQ, str)
        self.assertIsInstance(Contacts.CNInstantMessageServiceJabber, str)
        self.assertIsInstance(Contacts.CNInstantMessageServiceMSN, str)
        self.assertIsInstance(Contacts.CNInstantMessageServiceQQ, str)
        self.assertIsInstance(Contacts.CNInstantMessageServiceSkype, str)
        self.assertIsInstance(Contacts.CNInstantMessageServiceYahoo, str)
