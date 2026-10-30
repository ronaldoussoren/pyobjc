import contextlib
import socket
import objc
import subprocess
import os
import time

from PyObjCTest.test_scnetwork import resolver_available
from PyObjCTools.TestSupport import TestCase, skipUnless, NoObjCClass
import SystemConfiguration


class TestSCNetworkReachability(TestCase):
    def test_enums(self):
        self.assertIsEnumType(SystemConfiguration.SCNetworkReachabilityFlags)
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

    def test_types(self):
        self.assertIsInstance(
            SystemConfiguration.SCNetworkReachabilityRef, objc.objc_class
        )

    @skipUnless(resolver_available(), "No DNS resolver available")
    def test_functions(self):
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
                None, ("www.github.com", 443)
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

            def callout_raises(ref, flags, ctx):
                raise RuntimeError("callback error")

            ctx = object()

            with self.assertRaisesRegex(TypeError, "expected 3 arguments, got 0"):
                SystemConfiguration.SCNetworkReachabilitySetCallback()

            with self.assertRaisesRegex(TypeError, "Cannot proxy"):
                SystemConfiguration.SCNetworkReachabilitySetCallback(
                    NoObjCClass(), callout, ctx
                )

            v = SystemConfiguration.SCNetworkReachabilitySetCallback(ref, callout, ctx)
            self.assertTrue(v is True)

            rl = SystemConfiguration.CFRunLoopGetCurrent()
            self.assertResultIsBOOL(
                SystemConfiguration.SCNetworkReachabilityScheduleWithRunLoop
            )
            SystemConfiguration.SCNetworkReachabilityScheduleWithRunLoop(
                ref, rl, SystemConfiguration.kCFRunLoopCommonModes
            )

            if os.geteuid() == 0:
                print("Warning: shutdown interface 'en0' for testing")
                subprocess.check_call(["ifconfig", "en0", "down"])

            SystemConfiguration.CFRunLoopRunInMode(
                SystemConfiguration.kCFRunLoopDefaultMode, 1.0, False
            )

            if os.geteuid() == 0:
                time.sleep(1)
                self.assertGreater(len(lst), 0)

            for item in lst:
                self.assertIs(item[0], ref)
                self.assertIsInstance(item[1], int)
                self.assertIs(item[2], ctx)

            self.assertResultIsBOOL(
                SystemConfiguration.SCNetworkReachabilityUnscheduleFromRunLoop
            )
            SystemConfiguration.SCNetworkReachabilityUnscheduleFromRunLoop(
                ref, rl, SystemConfiguration.kCFRunLoopCommonModes
            )

            self.assertResultIsBOOL(
                SystemConfiguration.SCNetworkReachabilitySetDispatchQueue
            )

            if os.geteuid() == 0:
                lst[:] = []
                v = SystemConfiguration.SCNetworkReachabilitySetCallback(
                    ref, callout_raises, ctx
                )
                SystemConfiguration.SCNetworkReachabilityScheduleWithRunLoop(
                    ref, rl, SystemConfiguration.kCFRunLoopDefaultMode
                )
                subprocess.check_call(["ifconfig", "en0", "up"])

                with self.assertRaisesRegex(RuntimeError, "callback error"):
                    SystemConfiguration.CFRunLoopRunInMode(
                        SystemConfiguration.kCFRunLoopDefaultMode, 15.0, False
                    )

                self.assertEqual(len(lst), 0)

                SystemConfiguration.SCNetworkReachabilityUnscheduleFromRunLoop(
                    ref, rl, SystemConfiguration.kCFRunLoopDefaultMode
                )
                v = SystemConfiguration.SCNetworkReachabilitySetCallback(
                    ref, None, None
                )
