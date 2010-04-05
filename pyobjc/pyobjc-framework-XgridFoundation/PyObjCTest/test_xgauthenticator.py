
from PyObjCTools.TestSupport import *
from XgridFoundation import *

class TestXGAuthenticator (TestCase):
    def testConstants(self):
        self.assertEqual(XGAuthenticatorStateUnauthenticated, 0)
        self.assertEqual(XGAuthenticatorStateAuthenticating, 1)
        self.assertEqual(XGAuthenticatorStateAuthenticated, 2)
        self.assertEqual(XGAuthenticatorStateFailed, 3)

if __name__ == "__main__":
    main()
