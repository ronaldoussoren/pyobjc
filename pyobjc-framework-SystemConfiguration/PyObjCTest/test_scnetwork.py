from PyObjCTools.TestSupport import *

from SystemConfiguration import *

class TestSCNetwork (TestCase):
    def testConstants(self):
        self.assertEquals(kSCNetworkFlagsTransientConnection, 1 << 0)
        self.assertEquals(kSCNetworkFlagsReachable, 1<<1)
        self.assertEquals(kSCNetworkFlagsConnectionRequired, 1<<2)
        self.assertEquals(kSCNetworkFlagsConnectionAutomatic, 1<<3)
        self.assertEquals(kSCNetworkFlagsInterventionRequired, 1<<4)
        self.assertEquals(kSCNetworkFlagsIsLocalAddress, 1<<16)
        self.assertEquals(kSCNetworkFlagsIsDirect, 1<<17)

    def testHardFunctions(self):
        b, flags = SCNetworkCheckReachabilityByAddress(
                ('www.python.org', 80), objc._size_sockaddr_ip4, None)
        self.failUnlessIsInstance(b, bool)
        self.failUnlessIsInstance(flags, (int, long))
        self.failUnlessEqual(b, True)
        self.failUnlessEqual(flags, kSCNetworkFlagsReachable)


    def testFunctions(self):
        r, flags = SCNetworkCheckReachabilityByName("www.python.org", None)
        self.failUnless(r is True or r is False)
        self.failUnless(isinstance(flags, (int, long)))

        r = SCNetworkInterfaceRefreshConfiguration("en0")
        self.failUnless(r is True or r is False)


if __name__ == "__main__":
    main()
