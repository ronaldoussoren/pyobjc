from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSNetServicesHelper (NSObject):
    def netServiceBrowser_didFindDomain_moreComing_(self, a, b, c): pass
    def netServiceBrowser_didFindService_moreComing_(self, a, b, c): pass
    def netServiceBrowser_didRemoveDomain_moreComing_(self, a, b, c): pass
    def netServiceBrowser_didRemoveService_moreComing_(self, a, b, c): pass


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

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSNetService.getInputStream_outputStream_)
        self.failUnlessArgIsOut(NSNetService.getInputStream_outputStream_, 0)
        self.failUnlessArgIsOut(NSNetService.getInputStream_outputStream_, 1)
        self.failUnlessResultIsBOOL(NSNetService.setTXTRecordData_)

        self.failUnlessArgIsBOOL(TestNSNetServicesHelper.netServiceBrowser_didFindDomain_moreComing_, 2)
        self.failUnlessArgIsBOOL(TestNSNetServicesHelper.netServiceBrowser_didFindService_moreComing_, 2)
        self.failUnlessArgIsBOOL(TestNSNetServicesHelper.netServiceBrowser_didRemoveDomain_moreComing_, 2)
        self.failUnlessArgIsBOOL(TestNSNetServicesHelper.netServiceBrowser_didRemoveService_moreComing_, 2)

if __name__ == "__main__":
    main()
