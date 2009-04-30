from CFNetwork import *
from PyObjCTools.TestSupport import *

class TestCFHost (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CFHostRef)

    def testConstants(self):
        self.failUnlessIsInstance(kCFStreamErrorDomainNetDB, (int, long))
        self.failUnlessIsInstance(kCFStreamErrorDomainSystemConfiguration, (int, long))
        self.failUnlessEqual(kCFHostAddresses, 0)
        self.failUnlessEqual(kCFHostNames, 1)
        self.failUnlessEqual(kCFHostReachability, 2)

    def testFunctions(self):
        self.failUnlessIsInstance(CFHostGetTypeID(), (int, long))

        self.failUnlessResultIsCFRetained(CFHostCreateWithName)
        v = CFHostCreateWithName(None, u"www.python.org")
        self.failUnlessIsInstance(v, CFHostRef)


        addr = ' ' * 24;
        self.failUnlessResultIsCFRetained(CFHostCreateWithAddress)
        t = CFHostCreateWithAddress(None, buffer(addr))
        self.failUnlessIsInstance(t, CFHostRef)

        self.failUnlessResultIsBOOL(CFHostStartInfoResolution)
        self.failUnlessArgIsOut(CFHostStartInfoResolution, 2)
        ok, error = CFHostStartInfoResolution(v, kCFHostAddresses, None)
        self.failUnless(ok is True)
        self.failUnlessIsInstance(error, CFStreamError)

        self.failUnlessResultIsCFRetained(CFHostCreateCopy)
        w = CFHostCreateCopy(None, v)
        self.failUnlessIsInstance(w, (type(None), CFHostRef))
        

        self.failUnlessArgHasType(CFHostGetReachability, 1, 'o^' + objc._C_NSBOOL)
        lst, ok = CFHostGetReachability(v, None)
        self.failUnlessIsInstance(lst, (CFDataRef, type(None)))
        self.failUnlessIsInstance(ok, bool)

        CFHostCancelInfoResolution(v, kCFHostAddresses)

        rl = CFRunLoopGetCurrent()
        CFHostScheduleWithRunLoop(v, rl, kCFRunLoopDefaultMode)

        CFHostUnscheduleFromRunLoop(v, rl, kCFRunLoopDefaultMode)


        self.failUnlessArgHasType(CFHostGetNames, 1, 'o^' + objc._C_NSBOOL)
        lst, ok = CFHostGetNames(v, None)
        self.failUnlessIsInstance(lst, CFArrayRef)
        self.failUnlessIsInstance(ok, bool)

        
    def testCallbacks(self):
        lst = []
        ctx = object()
        def callback(host, typeinfo, error, ctx):
            lst.append([host, typeinfo, error, ctx])

        host = CFHostCreateWithName(None, u"www.python.org")
        CFHostSetClient(host, callback, ctx)

        rl = CFRunLoopGetCurrent()
        CFHostScheduleWithRunLoop(host, rl, kCFRunLoopDefaultMode)

        ok, err = CFHostStartInfoResolution(host, kCFHostAddresses, None)
        self.failUnless(ok)
        self.failUnlessIsInstance(ok, bool)
        self.failUnlessIsInstance(err, CFStreamError)

        CFRunLoopRunInMode(kCFRunLoopDefaultMode, 2.0, True)

        CFHostUnscheduleFromRunLoop(host, rl, kCFRunLoopDefaultMode)
        self.failUnlessEqual(len(lst), 1)
        self.failUnlessIsInstance(lst[0][0], CFHostRef)
        self.failUnlessIsInstance(lst[0][1], (int, long))
        self.failUnlessIsInstance(lst[0][2], CFStreamError)
        self.failUnless(lst[0][3] is ctx)

        self.failIfResultIsCFRetained(CFHostGetAddressing)
        self.failUnlessArgHasType(CFHostGetAddressing, 1, 'o^Z')
        lst, ok = CFHostGetAddressing(host, None)
        self.failUnlessIsInstance(lst, CFArrayRef)
        self.failUnlessIsInstance(lst[0], CFDataRef)
        self.failUnlessIsInstance(ok, bool)



if __name__ == "__main__":
    main()
