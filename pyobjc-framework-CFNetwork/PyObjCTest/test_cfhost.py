import socket

import CFNetwork
import objc
from PyObjCTools.TestSupport import TestCase


class TestCFHost(TestCase):
    def testTypes(self):
        self.assertIsCFType(CFNetwork.CFHostRef)

    def testConstants(self):
        self.assertIsInstance(CFNetwork.kCFStreamErrorDomainNetDB, int)
        self.assertIsInstance(CFNetwork.kCFStreamErrorDomainSystemConfiguration, int)
        self.assertEqual(CFNetwork.kCFHostAddresses, 0)
        self.assertEqual(CFNetwork.kCFHostNames, 1)
        self.assertEqual(CFNetwork.kCFHostReachability, 2)

    def testFunctions(self):
        self.assertIsInstance(CFNetwork.CFHostGetTypeID(), int)

        self.assertResultIsCFRetained(CFNetwork.CFHostCreateWithName)
        v = CFNetwork.CFHostCreateWithName(None, "www.python.org")
        self.assertIsInstance(v, CFNetwork.CFHostRef)

        try:
            # value = socket.gethostbyname("www.python.org")
            socket.gethostbyname("www.python.org")
            expected_resolution = True
        except OSError:
            expected_resolution = False

        addr = b" " * 24
        self.assertResultIsCFRetained(CFNetwork.CFHostCreateWithAddress)
        t = CFNetwork.CFHostCreateWithAddress(None, addr)
        self.assertIsInstance(t, CFNetwork.CFHostRef)

        self.assertResultIsBOOL(CFNetwork.CFHostStartInfoResolution)
        self.assertArgIsOut(CFNetwork.CFHostStartInfoResolution, 2)
        ok, error = CFNetwork.CFHostStartInfoResolution(
            v, CFNetwork.kCFHostAddresses, None
        )
        self.assertIs(ok, expected_resolution)
        self.assertIsInstance(error, CFNetwork.CFStreamError)

        self.assertResultIsCFRetained(CFNetwork.CFHostCreateCopy)
        # w = CFNetwork.CFHostCreateCopy(None, v)
        # self.assertIsInstance(w, type(v))

        self.assertArgHasType(
            CFNetwork.CFHostGetReachability, 1, b"o^" + objc._C_NSBOOL
        )
        lst, ok = CFNetwork.CFHostGetReachability(v, None)
        self.assertIsInstance(lst, (CFNetwork.CFDataRef, type(None)))
        self.assertIsInstance(ok, bool)

        CFNetwork.CFHostCancelInfoResolution(v, CFNetwork.kCFHostAddresses)

        rl = CFNetwork.CFRunLoopGetCurrent()
        CFNetwork.CFHostScheduleWithRunLoop(v, rl, CFNetwork.kCFRunLoopDefaultMode)

        CFNetwork.CFHostUnscheduleFromRunLoop(v, rl, CFNetwork.kCFRunLoopDefaultMode)

        self.assertArgHasType(CFNetwork.CFHostGetNames, 1, b"o^" + objc._C_NSBOOL)
        lst, ok = CFNetwork.CFHostGetNames(v, None)
        # print("XXX", lst)
        self.assertIsInstance(lst, CFNetwork.CFArrayRef)
        self.assertIsInstance(ok, bool)
        # self.assertIn(value, lst)

    def testCallbacks(self):
        lst = []
        ctx = object()

        def callback(host, typeinfo, error, ctx):
            lst.append([host, typeinfo, error, ctx])

        host = CFNetwork.CFHostCreateWithName(None, "localhost")
        CFNetwork.CFHostSetClient(host, callback, ctx)

        rl = CFNetwork.CFRunLoopGetCurrent()
        CFNetwork.CFHostScheduleWithRunLoop(host, rl, CFNetwork.kCFRunLoopDefaultMode)

        ok, err = CFNetwork.CFHostStartInfoResolution(
            host, CFNetwork.kCFHostAddresses, None
        )
        self.assertTrue(ok)
        self.assertIsInstance(ok, bool)
        self.assertIsInstance(err, CFNetwork.CFStreamError)

        CFNetwork.CFRunLoopRunInMode(CFNetwork.kCFRunLoopDefaultMode, 4.0, False)

        CFNetwork.CFHostUnscheduleFromRunLoop(host, rl, CFNetwork.kCFRunLoopDefaultMode)
        self.assertEqual(len(lst), 1)
        self.assertIsInstance(lst[0][0], CFNetwork.CFHostRef)
        self.assertIsInstance(lst[0][1], int)
        self.assertIsInstance(lst[0][2], CFNetwork.CFStreamError)
        self.assertIs(lst[0][3], ctx)

        self.assertResultIsNotCFRetained(CFNetwork.CFHostGetAddressing)
        self.assertArgHasType(CFNetwork.CFHostGetAddressing, 1, b"o^Z")
        lst, ok = CFNetwork.CFHostGetAddressing(host, None)
        self.assertIsInstance(lst, CFNetwork.CFArrayRef)
        self.assertIsInstance(lst[0], CFNetwork.CFDataRef)
        self.assertIsInstance(ok, bool)
