from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSConnection (TestCase):
    def testConstants(self):
        self.failUnless( isinstance(NSConnectionReplyMode, unicode) )
        self.failUnless( isinstance(NSConnectionDidDieNotification, unicode) )

        self.failUnless( isinstance(NSFailedAuthenticationException, unicode) )
        self.failUnless( isinstance(NSConnectionDidInitializeNotification, unicode) )

if __name__ == "__main__":
    main()
