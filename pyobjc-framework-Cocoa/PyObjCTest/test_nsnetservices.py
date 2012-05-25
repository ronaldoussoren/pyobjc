from PyObjCTools.TestSupport import *

from Foundation import *

try:
    unicode
except NameError:
    unicode = str

class TestNSNetServicesHelper (NSObject):
    def netServiceBrowser_didFindDomain_moreComing_(self, a, b, c): pass
    def netServiceBrowser_didFindService_moreComing_(self, a, b, c): pass
    def netServiceBrowser_didRemoveDomain_moreComing_(self, a, b, c): pass
    def netServiceBrowser_didRemoveService_moreComing_(self, a, b, c): pass


class TestNSNetservices (TestCase):
    def testConstants(self):

        self.assertIsInstance(NSNetServicesErrorCode, unicode)
        self.assertIsInstance(NSNetServicesErrorDomain, unicode)
        self.assertEqual(NSNetServicesUnknownError, -72000)
        self.assertEqual(NSNetServicesCollisionError, -72001)
        self.assertEqual(NSNetServicesNotFoundError, -72002)
        self.assertEqual(NSNetServicesActivityInProgress, -72003)
        self.assertEqual(NSNetServicesBadArgumentError, -72004)
        self.assertEqual(NSNetServicesCancelledError, -72005)
        self.assertEqual(NSNetServicesInvalidError, -72006)
        self.assertEqual(NSNetServicesTimeoutError, -72007)
        self.assertEqual(NSNetServiceNoAutoRename, 1)

    def testOutput(self):
        o = NSNetService.alloc().init()

        m = o.getInputStream_outputStream_.__metadata__()
        self.assertEqual(m['retval']['type'], b'Z')
        self.assertEqual(m['arguments'][2]['type'], b'o^@')
        self.assertEqual(m['arguments'][3]['type'], b'o^@')

    def testMethods(self):
        self.assertResultIsBOOL(NSNetService.getInputStream_outputStream_)
        self.assertArgIsOut(NSNetService.getInputStream_outputStream_, 0)
        self.assertArgIsOut(NSNetService.getInputStream_outputStream_, 1)
        self.assertResultIsBOOL(NSNetService.setTXTRecordData_)

        self.assertArgIsBOOL(TestNSNetServicesHelper.netServiceBrowser_didFindDomain_moreComing_, 2)
        self.assertArgIsBOOL(TestNSNetServicesHelper.netServiceBrowser_didFindService_moreComing_, 2)
        self.assertArgIsBOOL(TestNSNetServicesHelper.netServiceBrowser_didRemoveDomain_moreComing_, 2)
        self.assertArgIsBOOL(TestNSNetServicesHelper.netServiceBrowser_didRemoveService_moreComing_, 2)

if __name__ == "__main__":
    main()
