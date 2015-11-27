from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2**32:
    import Contacts

    class TestCNInstantMessageAddress (TestCase):
        @min_os_level("10.11")
        def testConstants(self):
            self.assertIsInstance(Contacts.CNInstantMessageAddressUsernameKey, unicode)
            self.assertIsInstance(Contacts.CNInstantMessageAddressServiceKey, unicode)
            self.assertIsInstance(Contacts.CNInstantMessageServiceAIM, unicode)
            self.assertIsInstance(Contacts.CNInstantMessageServiceFacebook, unicode)
            self.assertIsInstance(Contacts.CNInstantMessageServiceGaduGadu, unicode)
            self.assertIsInstance(Contacts.CNInstantMessageServiceGoogleTalk, unicode)
            self.assertIsInstance(Contacts.CNInstantMessageServiceICQ, unicode)
            self.assertIsInstance(Contacts.CNInstantMessageServiceJabber, unicode)
            self.assertIsInstance(Contacts.CNInstantMessageServiceMSN, unicode)
            self.assertIsInstance(Contacts.CNInstantMessageServiceQQ, unicode)
            self.assertIsInstance(Contacts.CNInstantMessageServiceSkype, unicode)
            self.assertIsInstance(Contacts.CNInstantMessageServiceYahoo, unicode)


if __name__ == "__main__":
    main()
