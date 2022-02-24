import socket

from PyObjCTools.TestSupport import TestCase, skipUnless
import SystemConfiguration
import objc


def resolver_available():
    try:
        socket.gethostbyname("www.python.org")
        return True
    except OSError:
        return False


class TestSCNetwork(TestCase):
    def testConstants(self):
        self.assertEqual(SystemConfiguration.kSCNetworkFlagsTransientConnection, 1 << 0)
        self.assertEqual(SystemConfiguration.kSCNetworkFlagsReachable, 1 << 1)
        self.assertEqual(SystemConfiguration.kSCNetworkFlagsConnectionRequired, 1 << 2)
        self.assertEqual(SystemConfiguration.kSCNetworkFlagsConnectionAutomatic, 1 << 3)
        self.assertEqual(
            SystemConfiguration.kSCNetworkFlagsInterventionRequired, 1 << 4
        )
        self.assertEqual(SystemConfiguration.kSCNetworkFlagsIsLocalAddress, 1 << 16)
        self.assertEqual(SystemConfiguration.kSCNetworkFlagsIsDirect, 1 << 17)

    def testHardFunctionsNoHost(self):
        self.assertRaises(
            socket.gaierror,
            SystemConfiguration.SCNetworkCheckReachabilityByAddress,
            ("no-such-host.python.org", 80),
            objc._size_sockaddr_ip4,
            None,
        )

    @skipUnless(resolver_available(), "No DNS resolver available")
    def testHardFunctions(self):
        b, flags = SystemConfiguration.SCNetworkCheckReachabilityByAddress(
            ("www.python.org", 80), objc._size_sockaddr_ip4, None
        )
        self.assertIsInstance(b, bool)
        self.assertIsInstance(flags, int)
        self.assertEqual(b, True)
        self.assertEqual(flags, SystemConfiguration.kSCNetworkFlagsReachable)

    @skipUnless(resolver_available(), "No DNS resolver available")
    def testFunctions(self):
        r, flags = SystemConfiguration.SCNetworkCheckReachabilityByName(
            b"www.python.org", None
        )
        self.assertTrue(r is True or r is False)
        self.assertTrue(isinstance(flags, int))

        r = SystemConfiguration.SCNetworkInterfaceRefreshConfiguration("en0")
        self.assertTrue(r is True or r is False)
