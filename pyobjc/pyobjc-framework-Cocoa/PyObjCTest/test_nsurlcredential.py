from Foundation import *
from PyObjCTools.TestSupport import *


class TestNSURLCredential (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSURLCredentialPersistenceNone, 0)
        self.failUnlessEqual(NSURLCredentialPersistenceForSession, 1)
        self.failUnlessEqual(NSURLCredentialPersistencePermanent, 2)


    def testMethods(self):
        self.failUnlessResultIsBOOL(NSURLCredential.hasPassword)

if __name__ == "__main__":
    main()
