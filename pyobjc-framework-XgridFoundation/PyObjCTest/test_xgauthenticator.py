
from PyObjCTools.TestSupport import *
from XgridFoundation import *

class TestXGAuthenticator (TestCase):
    def testConstants(self):
        self.failUnlessEqual(XGAuthenticatorStateUnauthenticated, 0)
        self.failUnlessEqual(XGAuthenticatorStateAuthenticating, 1)
        self.failUnlessEqual(XGAuthenticatorStateAuthenticated, 2)
        self.failUnlessEqual(XGAuthenticatorStateFailed, 3)

if __name__ == "__main__":
    main()
