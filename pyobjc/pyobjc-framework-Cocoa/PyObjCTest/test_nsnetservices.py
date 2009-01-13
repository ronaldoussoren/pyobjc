from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSNetservices (TestCase):
    def testConstants(self):

        self.failUnless(isinstance(NSNetServicesErrorCode, unicode))
        self.failUnless(isinstance(NSNetServicesErrorDomain, unicode))


        self.assertEquals(NSNetServicesUnknownError, -72000)
        self.assertEquals(NSNetServicesCollisionError, -72001)
        self.assertEquals(NSNetServicesNotFoundError, -72002)
        self.assertEquals(NSNetServicesActivityInProgress, -72003)
        self.assertEquals(NSNetServicesBadArgumentError, -72004)
        self.assertEquals(NSNetServicesCancelledError, -72005)
        self.assertEquals(NSNetServicesInvalidError, -72006)
        self.assertEquals(NSNetServicesTimeoutError, -72007)
        self.assertEquals(NSNetServiceNoAutoRename, 1)

    def testOutput(self):
        o = NSNetService.alloc().init()

        m = o.getInputStream_outputStream_.__metadata__()
        self.assertEquals(m['retval']['type'], 'Z')
        self.assertEquals(m['arguments'][2]['type'], 'o^@')
        self.assertEquals(m['arguments'][3]['type'], 'o^@')

if __name__ == "__main__":
    main()
