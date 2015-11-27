from PyObjCTools.TestSupport import *
from SystemConfiguration import *
import socket

from PyObjCTest.test_scnetwork import resolver_available
import contextlib

class TestSCNetworkReachability (TestCase):
    def testTypes(self):
        self.assertIsInstance(SCNetworkReachabilityRef, objc.objc_class)

    @onlyIf(resolver_available(), "No DNS resolver available")
    def testFunctions(self):
        self.assertResultIsCFRetained(SCNetworkReachabilityCreateWithAddressPair)
        v = SCNetworkReachabilityCreateWithAddressPair(None,
                ('0.0.0.0', 20990),
                ('www.python.org', 80))


        with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sd:
            sd.listen(5)

            self.assertResultIsCFRetained(SCNetworkReachabilityCreateWithAddress)
            ref = v = SCNetworkReachabilityCreateWithAddress(None, sd.getsockname())
            self.assertIsInstance(v, SCNetworkReachabilityRef)

            self.assertResultIsCFRetained(SCNetworkReachabilityCreateWithName)
            v = SCNetworkReachabilityCreateWithName(None, b'www.python.org')
            self.assertIsInstance(v, SCNetworkReachabilityRef)

            v = SCNetworkReachabilityGetTypeID()
            self.assertIsInstance(v, (int, long))

            self.assertResultIsBOOL(SCNetworkReachabilityGetFlags)
            v, fl = SCNetworkReachabilityGetFlags(ref, None)
            self.assertTrue(v)
            self.assertIsInstance(fl, (int, long))


            l = []
            def callout(ref, flags, ctx):
                l.append([ref, flags, ctx])
            ctx = object()
            v = SCNetworkReachabilitySetCallback(ref, callout, ctx)
            self.assertTrue(v is True)


            rl = CFRunLoopGetCurrent()
            self.assertResultIsBOOL(SCNetworkReachabilityScheduleWithRunLoop)
            r = SCNetworkReachabilityScheduleWithRunLoop(ref, rl, kCFRunLoopCommonModes)

            CFRunLoopRunInMode(kCFRunLoopDefaultMode, 1.0, False)

            self.assertResultIsBOOL(SCNetworkReachabilityUnscheduleFromRunLoop)
            r = SCNetworkReachabilityUnscheduleFromRunLoop(ref, rl, kCFRunLoopCommonModes)

        @min_os_level('10.6')
        def testFunctions10_6(self):
            self.assertResultIsBOOL(SCNetworkReachabilitySetDispatchQueue)

        def testConstants(self):
            self.assertEqual(kSCNetworkReachabilityFlagsTransientConnection, 1<<0)
            self.assertEqual(kSCNetworkReachabilityFlagsReachable, 1<<1)
            self.assertEqual(kSCNetworkReachabilityFlagsConnectionRequired, 1<<2)
            self.assertEqual(kSCNetworkReachabilityFlagsConnectionOnTraffic, 1<<3)
            self.assertEqual(kSCNetworkReachabilityFlagsInterventionRequired, 1<<4)
            self.assertEqual(kSCNetworkReachabilityFlagsConnectionOnDemand, 1<<5)
            self.assertEqual(kSCNetworkReachabilityFlagsIsLocalAddress, 1<<16)
            self.assertEqual(kSCNetworkReachabilityFlagsIsDirect, 1<<17)

            self.assertEqual(kSCNetworkReachabilityFlagsConnectionAutomatic, kSCNetworkReachabilityFlagsConnectionOnTraffic)

if __name__ == "__main__":
    main()
