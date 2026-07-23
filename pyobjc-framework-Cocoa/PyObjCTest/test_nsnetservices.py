import Foundation
import re
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
from .runloophelper import check_cfrunloop_side_effects


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
    def test_enums(self):
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

    def test_protocol_methods(self):
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

    @check_cfrunloop_side_effects
    def test_manual(self):
        ns1 = Foundation.NSNetService.alloc().initWithDomain_type_name_port_(
            "local.", "_http._tcp", "pyobjctest99", 10000
        )
        ns1.publish()

        ns2 = Foundation.NSNetService.alloc().initWithDomain_type_name_(
            "local.", "_http._tcp", "pyobjctest99"
        )
        ns2.resolve()

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 1"):
            ns1.addresses(42)

        Foundation.CFRunLoopRunInMode(Foundation.kCFRunLoopDefaultMode, 5.0, False)

        a1 = ns1.addresses()
        a2 = ns2.addresses()
        self.assertIsInstance(a1, tuple)
        self.assertIsInstance(a2, tuple)
        self.assertGreater(len(a1) + len(a2), 0)

        for item in a1 + a2:
            self.assertIsInstance(item[0], str)
            for p in item[1:]:
                self.assertIsInstance(p, int)

            if re.match(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", item[0]):
                # IPv4
                self.assertEqual(len(item), 2)
                self.assertEqual(item[1], 10000)
            else:
                self.assertEqual(len(item), 4)
                self.assertEqual(item[1], 10000)
