import contextlib
import socket
import objc

from PyObjCTest.test_scnetwork import resolver_available
from PyObjCTools.TestSupport import TestCase, min_os_level, skipUnless
import SystemConfiguration


class TestSCNetworkReachability(TestCase):
    def testTypes(self):
        self.assertIsInstance(
            SystemConfiguration.SCNetworkReachabilityRef, objc.objc_class
        )

    @skipUnless(resolver_available(), "No DNS resolver available")
    def testFunctions(self):
        self.assertResultIsCFRetained(
            SystemConfiguration.SCNetworkReachabilityCreateWithAddressPair
        )
        v = SystemConfiguration.SCNetworkReachabilityCreateWithAddressPair(
            None, ("0.0.0.0", 20990), ("www.python.org", 80)
        )

        with contextlib.closing(
            socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ) as sd:
            sd.listen(5)

            self.assertResultIsCFRetained(
                SystemConfiguration.SCNetworkReachabilityCreateWithAddress
            )
            ref = v = SystemConfiguration.SCNetworkReachabilityCreateWithAddress(
                None, sd.getsockname()
            )
            self.assertIsInstance(v, SystemConfiguration.SCNetworkReachabilityRef)

            self.assertResultIsCFRetained(
                SystemConfiguration.SCNetworkReachabilityCreateWithName
            )
            v = SystemConfiguration.SCNetworkReachabilityCreateWithName(
                None, b"www.python.org"
            )
            self.assertIsInstance(v, SystemConfiguration.SCNetworkReachabilityRef)

            v = SystemConfiguration.SCNetworkReachabilityGetTypeID()
            self.assertIsInstance(v, int)

            self.assertResultIsBOOL(SystemConfiguration.SCNetworkReachabilityGetFlags)
            v, fl = SystemConfiguration.SCNetworkReachabilityGetFlags(ref, None)
            self.assertTrue(v)
            self.assertIsInstance(fl, int)

            lst = []

            def callout(ref, flags, ctx):
                lst.append([ref, flags, ctx])

            ctx = object()
            v = SystemConfiguration.SCNetworkReachabilitySetCallback(ref, callout, ctx)
            self.assertTrue(v is True)

            rl = SystemConfiguration.CFRunLoopGetCurrent()
            self.assertResultIsBOOL(
                SystemConfiguration.SCNetworkReachabilityScheduleWithRunLoop
            )
            SystemConfiguration.SCNetworkReachabilityScheduleWithRunLoop(
                ref, rl, SystemConfiguration.kCFRunLoopCommonModes
            )

            SystemConfiguration.CFRunLoopRunInMode(
                SystemConfiguration.kCFRunLoopDefaultMode, 1.0, False
            )

            self.assertResultIsBOOL(
                SystemConfiguration.SCNetworkReachabilityUnscheduleFromRunLoop
            )
            SystemConfiguration.SCNetworkReachabilityUnscheduleFromRunLoop(
                ref, rl, SystemConfiguration.kCFRunLoopCommonModes
            )

        @min_os_level("10.6")
        def testFunctions10_6(self):
            self.assertResultIsBOOL(
                SystemConfiguration.SCNetworkReachabilitySetDispatchQueue
            )

        def testConstants(self):
            self.assertEqual(
                SystemConfiguration.kSCNetworkReachabilityFlagsTransientConnection,
                1 << 0,
            )
            self.assertEqual(
                SystemConfiguration.kSCNetworkReachabilityFlagsReachable, 1 << 1
            )
            self.assertEqual(
                SystemConfiguration.kSCNetworkReachabilityFlagsConnectionRequired,
                1 << 2,
            )
            self.assertEqual(
                SystemConfiguration.kSCNetworkReachabilityFlagsConnectionOnTraffic,
                1 << 3,
            )
            self.assertEqual(
                SystemConfiguration.kSCNetworkReachabilityFlagsInterventionRequired,
                1 << 4,
            )
            self.assertEqual(
                SystemConfiguration.kSCNetworkReachabilityFlagsConnectionOnDemand,
                1 << 5,
            )
            self.assertEqual(
                SystemConfiguration.kSCNetworkReachabilityFlagsIsLocalAddress, 1 << 16
            )
            self.assertEqual(
                SystemConfiguration.kSCNetworkReachabilityFlagsIsDirect, 1 << 17
            )

            self.assertEqual(
                SystemConfiguration.kSCNetworkReachabilityFlagsConnectionAutomatic,
                SystemConfiguration.kSCNetworkReachabilityFlagsConnectionOnTraffic,
            )
