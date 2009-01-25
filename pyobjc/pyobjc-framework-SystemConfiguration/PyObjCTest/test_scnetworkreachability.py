from PyObjCTools.TestSupport import *
from SystemConfiguration import *
import socket

class TestSCNetworkReachability (TestCase):
    def testTypes(self):
        self.failUnlessIsInstance(SCNetworkReachabilityRef, objc.objc_class)

    def testFunctions(self):
        self.failUnlessResultIsCFRetained(SCNetworkReachabilityCreateWithAddressPair)
        v = SCNetworkReachabilityCreateWithAddressPair(None, 
                ('0.0.0.0', 20990),
                ('www.python.org', 80))


        sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sd.listen(5)

        self.failUnlessResultIsCFRetained(SCNetworkReachabilityCreateWithAddress)
        ref = v = SCNetworkReachabilityCreateWithAddress(None, sd.getsockname())
        self.failUnlessIsInstance(v, SCNetworkReachabilityRef)

        self.failUnlessResultIsCFRetained(SCNetworkReachabilityCreateWithName)
        v = SCNetworkReachabilityCreateWithName(None, 'www.python.org')
        self.failUnlessIsInstance(v, SCNetworkReachabilityRef)

        v = SCNetworkReachabilityGetTypeID()
        self.failUnlessIsInstance(v, (int, long))

        self.failUnlessResultIsBOOL(SCNetworkReachabilityGetFlags)
        v, fl = SCNetworkReachabilityGetFlags(ref, None)
        self.failUnless(v)
        self.failUnlessIsInstance(fl, (int, long))


        l = []
        def callout(ref, flags, ctx):
            l.append([ref, flags, ctx])
            print flags
        ctx = object()
        v = SCNetworkReachabilitySetCallback(ref, callout, ctx)
        self.failUnless(v is True)


        rl = CFRunLoopGetCurrent()
        self.failUnlessResultIsBOOL(SCNetworkReachabilityScheduleWithRunLoop)
        r = SCNetworkReachabilityScheduleWithRunLoop(ref, rl, kCFRunLoopCommonModes)

        sd.close()
        CFRunLoopRunInMode(kCFRunLoopDefaultMode, 1.0, False)

        self.failUnlessResultIsBOOL(SCNetworkReachabilityUnscheduleFromRunLoop)
        r = SCNetworkReachabilityUnscheduleFromRunLoop(ref, rl, kCFRunLoopCommonModes)

        








if __name__ == "__main__":
    main()
