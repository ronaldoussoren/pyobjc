from Foundation import *
from PyObjCTools.TestSupport import *


class TestNSURLCredential (TestCase):
    def testConstants(self):
        self.assertEqual(NSURLCredentialPersistenceNone, 0)
        self.assertEqual(NSURLCredentialPersistenceForSession, 1)
        self.assertEqual(NSURLCredentialPersistencePermanent, 2)


    def testMethods(self):
        self.assertResultIsBOOL(NSURLCredential.hasPassword)

if __name__ == "__main__":
    main()
