from CFNetwork import *
from PyObjCTools.TestSupport import *
import sys
import socket

if sys.version_info[0] != 2:
    def buffer(value):
        return value.encode('latin1')

class TestCFHost (TestCase):
    def testTypes(self):
        self.assertIsCFType(CFHostRef)

    def testConstants(self):
        self.assertIsInstance(kCFStreamErrorDomainNetDB, (int, long))
        self.assertIsInstance(kCFStreamErrorDomainSystemConfiguration, (int, long))
        self.assertEqual(kCFHostAddresses, 0)
        self.assertEqual(kCFHostNames, 1)
        self.assertEqual(kCFHostReachability, 2)

    def testFunctions(self):
        self.assertIsInstance(CFHostGetTypeID(), (int, long))

        self.assertResultIsCFRetained(CFHostCreateWithName)
        v = CFHostCreateWithName(None, u"www.python.org")
        self.assertIsInstance(v, CFHostRef)

        try:
            value = socket.gethostbyname('www.python.org')
            expected_resolution = True
        except socket.error:
            expected_resolution = False



        addr = ' ' * 24;
        self.assertResultIsCFRetained(CFHostCreateWithAddress)
        t = CFHostCreateWithAddress(None, buffer(addr))
        self.assertIsInstance(t, CFHostRef)

        self.assertResultIsBOOL(CFHostStartInfoResolution)
        self.assertArgIsOut(CFHostStartInfoResolution, 2)
        ok, error = CFHostStartInfoResolution(v, kCFHostAddresses, None)
        self.assertIsObject(ok, expected_resolution)
        self.assertIsInstance(error, CFStreamError)

        self.assertResultIsCFRetained(CFHostCreateCopy)
        w = CFHostCreateCopy(None, v)
        self.assertIsInstance(w, (type(None), CFHostRef))
        

        self.assertArgHasType(CFHostGetReachability, 1, b'o^' + objc._C_NSBOOL)
        lst, ok = CFHostGetReachability(v, None)
        self.assertIsInstance(lst, (CFDataRef, type(None)))
        self.assertIsInstance(ok, bool)

        CFHostCancelInfoResolution(v, kCFHostAddresses)

        rl = CFRunLoopGetCurrent()
        CFHostScheduleWithRunLoop(v, rl, kCFRunLoopDefaultMode)

        CFHostUnscheduleFromRunLoop(v, rl, kCFRunLoopDefaultMode)


        self.assertArgHasType(CFHostGetNames, 1, b'o^' + objc._C_NSBOOL)
        lst, ok = CFHostGetNames(v, None)
        self.assertIsInstance(lst, CFArrayRef)
        self.assertIsInstance(ok, bool)

        
    def testCallbacks(self):
        lst = []
        ctx = object()
        def callback(host, typeinfo, error, ctx):
            lst.append([host, typeinfo, error, ctx])

        host = CFHostCreateWithName(None, u"localhost")
        CFHostSetClient(host, callback, ctx)

        rl = CFRunLoopGetCurrent()
        CFHostScheduleWithRunLoop(host, rl, kCFRunLoopDefaultMode)

        ok, err = CFHostStartInfoResolution(host, kCFHostAddresses, None)
        self.assertTrue(ok)
        self.assertIsInstance(ok, bool)
        self.assertIsInstance(err, CFStreamError)

        CFRunLoopRunInMode(kCFRunLoopDefaultMode, 4.0, False)

        CFHostUnscheduleFromRunLoop(host, rl, kCFRunLoopDefaultMode)
        self.assertEqual(len(lst), 1)
        self.assertIsInstance(lst[0][0], CFHostRef)
        self.assertIsInstance(lst[0][1], (int, long))
        self.assertIsInstance(lst[0][2], CFStreamError)
        self.assertIsObject(lst[0][3], ctx)

        self.failIfResultIsCFRetained(CFHostGetAddressing)
        self.assertArgHasType(CFHostGetAddressing, 1, b'o^Z')
        lst, ok = CFHostGetAddressing(host, None)
        self.assertIsInstance(lst, CFArrayRef)
        self.assertIsInstance(lst[0], CFDataRef)
        self.assertIsInstance(ok, bool)


if __name__ == "__main__":
    main()
