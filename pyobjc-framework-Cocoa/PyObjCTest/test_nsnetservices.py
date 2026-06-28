import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestNSNetServicesHelper(Foundation.NSObject):
    def netServiceBrowser_didFindDomain_moreComing_(self, a, b, c):
        pass

    def netServiceBrowser_didFindService_moreComing_(self, a, b, c):
        pass

    def netServiceBrowser_didRemoveDomain_moreComing_(self, a, b, c):
        pass

    def netServiceBrowser_didRemoveService_moreComing_(self, a, b, c):
        pass


class TestNSNetservices(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSNetServicesError)
        self.assertEqual(Foundation.NSNetServicesUnknownError, -72000)
        self.assertEqual(Foundation.NSNetServicesCollisionError, -72001)
        self.assertEqual(Foundation.NSNetServicesNotFoundError, -72002)
        self.assertEqual(Foundation.NSNetServicesActivityInProgress, -72003)
        self.assertEqual(Foundation.NSNetServicesBadArgumentError, -72004)
        self.assertEqual(Foundation.NSNetServicesCancelledError, -72005)
        self.assertEqual(Foundation.NSNetServicesInvalidError, -72006)
        self.assertEqual(Foundation.NSNetServicesTimeoutError, -72007)
        self.assertEqual(
            Foundation.NSNetServicesMissingRequiredConfigurationError, -72008
        )

        self.assertIsEnumType(Foundation.NSNetServiceOptions)
        self.assertEqual(Foundation.NSNetServiceNoAutoRename, 1)
        self.assertEqual(Foundation.NSNetServiceListenForConnections, 1 << 1)

    def test_constants(self):
        self.assertIsInstance(Foundation.NSNetServicesErrorCode, str)
        self.assertIsInstance(Foundation.NSNetServicesErrorDomain, str)

    def test_output(self):
        o = Foundation.NSNetService.alloc().initWithDomain_type_name_port_(
            "", "_http._tcp.", "", 0
        )

        m = o.getInputStream_outputStream_.__metadata__()
        self.assertEqual(m["retval"]["type"], b"Z")
        self.assertEqual(m["arguments"][2]["type"], b"o^@")
        self.assertEqual(m["arguments"][3]["type"], b"o^@")

    def test_methods(self):
        self.assertResultIsBOOL(Foundation.NSNetService.getInputStream_outputStream_)
        self.assertArgIsOut(Foundation.NSNetService.getInputStream_outputStream_, 0)
        self.assertArgIsOut(Foundation.NSNetService.getInputStream_outputStream_, 1)
        self.assertResultIsBOOL(Foundation.NSNetService.setTXTRecordData_)

        self.assertArgIsBOOL(
            TestNSNetServicesHelper.netServiceBrowser_didFindDomain_moreComing_, 2
        )
        self.assertArgIsBOOL(
            TestNSNetServicesHelper.netServiceBrowser_didFindService_moreComing_, 2
        )
        self.assertArgIsBOOL(
            TestNSNetServicesHelper.netServiceBrowser_didRemoveDomain_moreComing_, 2
        )
        self.assertArgIsBOOL(
            TestNSNetServicesHelper.netServiceBrowser_didRemoveService_moreComing_, 2
        )

    @min_os_level("10.10")
    def test_methods10_10(self):
        self.assertResultIsBOOL(Foundation.NSNetService.includesPeerToPeer)
        self.assertArgIsBOOL(Foundation.NSNetService.setIncludesPeerToPeer_, 0)

        self.assertResultIsBOOL(Foundation.NSNetServiceBrowser.includesPeerToPeer)
        self.assertArgIsBOOL(Foundation.NSNetServiceBrowser.setIncludesPeerToPeer_, 0)

    @min_sdk_level("10.10")
    def test_protocols(self):
        self.assertProtocolExists("NSNetServiceDelegate", Foundation)
        self.assertProtocolExists("NSNetServiceBrowserDelegate", Foundation)
