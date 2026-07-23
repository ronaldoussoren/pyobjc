import Foundation
import CFNetwork
from PyObjCTools.TestSupport import TestCase, NoObjCClass


class TestCFNetServices(TestCase):
    def test_types(self):
        self.assertIsCFType(CFNetwork.CFNetServiceRef)
        self.assertIsCFType(CFNetwork.CFNetServiceMonitorRef)
        self.assertIsCFType(CFNetwork.CFNetServiceBrowserRef)

    def test_constants(self):
        self.assertIsInstance(CFNetwork.kCFStreamErrorDomainMach, int)
        self.assertIsInstance(CFNetwork.kCFStreamErrorDomainNetServices, int)

        self.assertEqual(CFNetwork.kCFNetServicesErrorUnknown, -72000)
        self.assertEqual(CFNetwork.kCFNetServicesErrorCollision, -72001)
        self.assertEqual(CFNetwork.kCFNetServicesErrorNotFound, -72002)
        self.assertEqual(CFNetwork.kCFNetServicesErrorInProgress, -72003)
        self.assertEqual(CFNetwork.kCFNetServicesErrorBadArgument, -72004)
        self.assertEqual(CFNetwork.kCFNetServicesErrorCancel, -72005)
        self.assertEqual(CFNetwork.kCFNetServicesErrorInvalid, -72006)
        self.assertEqual(CFNetwork.kCFNetServicesErrorTimeout, -72007)
        self.assertEqual(
            CFNetwork.kCFNetServicesErrorMissingRequiredConfiguration, -72008
        )
        self.assertEqual(CFNetwork.kCFNetServiceMonitorTXT, 1)
        self.assertEqual(CFNetwork.kCFNetServiceFlagNoAutoRename, 1)
        self.assertEqual(CFNetwork.kCFNetServiceFlagMoreComing, 1)
        self.assertEqual(CFNetwork.kCFNetServiceFlagIsDomain, 2)
        self.assertEqual(CFNetwork.kCFNetServiceFlagIsDefault, 4)
        self.assertEqual(CFNetwork.kCFNetServiceFlagIsRegistrationDomain, 4)
        self.assertEqual(CFNetwork.kCFNetServiceFlagRemove, 8)

    def test_functions(self):
        self.assertIsInstance(CFNetwork.CFNetServiceGetTypeID(), int)
        self.assertIsInstance(CFNetwork.CFNetServiceMonitorGetTypeID(), int)
        self.assertIsInstance(CFNetwork.CFNetServiceBrowserGetTypeID(), int)
        self.assertArgIsOut(CFNetwork.CFNetServiceBrowserSearchForDomains, 2)
        self.assertArgIsOut(CFNetwork.CFNetServiceBrowserSearchForServices, 3)

        self.assertResultIsCFRetained(CFNetwork.CFNetServiceCreate)
        serv = CFNetwork.CFNetServiceCreate(None, "local.", "ssh", "pyobjc-test", 9999)
        self.assertIsInstance(serv, CFNetwork.CFNetServiceRef)

        self.assertResultIsCFRetained(CFNetwork.CFNetServiceCreateCopy)
        v = CFNetwork.CFNetServiceCreateCopy(None, serv)
        self.assertIsInstance(v, CFNetwork.CFNetServiceRef)

        dom = CFNetwork.CFNetServiceGetDomain(serv)
        self.assertIsInstance(dom, str)

        dom = CFNetwork.CFNetServiceGetType(serv)
        self.assertIsInstance(dom, str)

        dom = CFNetwork.CFNetServiceGetName(serv)
        self.assertIsInstance(dom, str)

        self.assertResultIsBOOL(CFNetwork.CFNetServiceRegisterWithOptions)
        self.assertArgIsOut(CFNetwork.CFNetServiceRegisterWithOptions, 2)

        ok, err = CFNetwork.CFNetServiceRegisterWithOptions(
            serv, CFNetwork.kCFNetServiceFlagNoAutoRename, None
        )
        self.assertIsInstance(ok, bool)
        if ok:
            self.assertEqual(err, None)
        else:
            self.assertIsInstance(err, CFNetwork.CFStreamError)

        self.assertResultIsBOOL(CFNetwork.CFNetServiceResolveWithTimeout)
        self.assertArgIsOut(CFNetwork.CFNetServiceResolveWithTimeout, 2)
        ok, err = CFNetwork.CFNetServiceResolveWithTimeout(serv, 1.0, None)
        self.assertIsInstance(ok, bool)
        if ok:
            self.assertEqual(err, None)
        else:
            self.assertIsInstance(err, CFNetwork.CFStreamError)

        host = CFNetwork.CFNetServiceGetTargetHost(serv)
        self.assertIsInstance(host, (str, type(None)))

        port = CFNetwork.CFNetServiceGetPortNumber(serv)
        self.assertIsInstance(port, int)

        v = CFNetwork.CFNetServiceGetAddressing(serv)
        self.assertIsInstance(v, (Foundation.NSArray, type(None)))

        v = CFNetwork.CFNetServiceGetTXTData(serv)
        self.assertIsInstance(v, (Foundation.NSData, type(None)))

        v = CFNetwork.CFNetServiceCreateTXTDataWithDictionary(
            None, {"key": "value", "key2": "value2"}
        )
        self.assertIsInstance(v, Foundation.NSData)

        v = CFNetwork.CFNetServiceCreateDictionaryWithTXTData(None, v)
        self.assertIsInstance(v, Foundation.NSDictionary)

        self.assertResultIsBOOL(CFNetwork.CFNetServiceSetTXTData)
        ok = CFNetwork.CFNetServiceSetTXTData(serv, b"hello")
        self.assertIsInstance(ok, bool)

        rl = CFNetwork.CFRunLoopGetCurrent()
        CFNetwork.CFNetServiceScheduleWithRunLoop(
            serv, rl, CFNetwork.kCFRunLoopDefaultMode
        )
        CFNetwork.CFNetServiceUnscheduleFromRunLoop(
            serv, rl, CFNetwork.kCFRunLoopDefaultMode
        )

        CFNetwork.CFNetServiceCancel(serv)

    def test_manual(self):
        rl = CFNetwork.CFRunLoopGetCurrent()
        ctx = object()
        lst = []
        domain = None

        def browser_cb(browser, flags, domainOrService, error, info):
            nonlocal domain
            if flags & CFNetwork.kCFNetServiceFlagIsDomain:
                domain = domainOrService

        def browser_cb_raises(browser, flags, domainOrService, error, info):
            raise RuntimeError("callback error")

        with self.assertRaisesRegex(TypeError, "expected 3 arguments, got 0"):
            CFNetwork.CFNetServiceBrowserCreate()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            CFNetwork.CFNetServiceBrowserCreate(NoObjCClass(), browser_cb, None)

        browser = CFNetwork.CFNetServiceBrowserCreate(None, browser_cb, None)
        self.assertIsNot(browser, None)

        CFNetwork.CFNetServiceBrowserScheduleWithRunLoop(
            browser, rl, CFNetwork.kCFRunLoopDefaultMode
        )
        ok, err = CFNetwork.CFNetServiceBrowserSearchForDomains(browser, True, None)
        self.assertIs(ok, True)

        CFNetwork.CFRunLoopRunInMode(CFNetwork.kCFRunLoopDefaultMode, 1.0, False)

        CFNetwork.CFNetServiceBrowserUnscheduleFromRunLoop(
            browser, rl, CFNetwork.kCFRunLoopDefaultMode
        )

        self.assertIsNot(domain, None)

        browser = CFNetwork.CFNetServiceBrowserCreate(None, browser_cb_raises, None)
        self.assertIsNot(browser, None)
        CFNetwork.CFNetServiceBrowserScheduleWithRunLoop(
            browser, rl, CFNetwork.kCFRunLoopDefaultMode
        )
        ok, err = CFNetwork.CFNetServiceBrowserSearchForDomains(browser, True, None)
        self.assertIs(ok, True)
        with self.assertRaisesRegex(RuntimeError, "callback error"):
            CFNetwork.CFRunLoopRunInMode(CFNetwork.kCFRunLoopDefaultMode, 1.0, False)
        CFNetwork.CFNetServiceBrowserUnscheduleFromRunLoop(
            browser, rl, CFNetwork.kCFRunLoopDefaultMode
        )

        svc_lst = []

        def callback(svc, error, context):
            svc_lst.append((svc, error, context))

        def callback_raises(svc, error, context):
            raise RuntimeError("callback error")

        svc = CFNetwork.CFNetServiceCreate(
            None, domain, "_ssh._tcp", "pyobjcmon-test", 9999
        )
        self.assertIsInstance(svc, CFNetwork.CFNetServiceRef)
        CFNetwork.CFNetServiceScheduleWithRunLoop(
            svc, rl, CFNetwork.kCFRunLoopDefaultMode
        )
        ok, err = CFNetwork.CFNetServiceRegisterWithOptions(
            svc, CFNetwork.kCFNetServiceFlagNoAutoRename, None
        )
        self.assertIs(ok, True)

        CFNetwork.CFNetServiceSetClient(svc, callback, ctx)

        with self.assertRaisesRegex(TypeError, "expected 3 arguments, got 0"):
            CFNetwork.CFNetServiceSetClient()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            CFNetwork.CFNetServiceSetClient(NoObjCClass(), callback, ctx)

        CFNetwork.CFRunLoopRunInMode(CFNetwork.kCFRunLoopDefaultMode, 1.0, False)
        self.assertGreater(len(svc_lst), 0)
        for item in svc_lst:
            self.assertIs(item[0], svc)
            self.assertIsInstance(item[1], CFNetwork.CFStreamError)

        svc2 = CFNetwork.CFNetServiceCreate(
            None, domain, "_ssh._tcp", "pyobjcmon-test2", 9999
        )
        CFNetwork.CFNetServiceScheduleWithRunLoop(
            svc2, rl, CFNetwork.kCFRunLoopDefaultMode
        )
        ok, err = CFNetwork.CFNetServiceRegisterWithOptions(
            svc2, CFNetwork.kCFNetServiceFlagNoAutoRename, None
        )
        self.assertIs(ok, True)
        CFNetwork.CFNetServiceSetClient(svc2, callback_raises, ctx)

        with self.assertRaisesRegex(RuntimeError, "callback error"):
            CFNetwork.CFRunLoopRunInMode(CFNetwork.kCFRunLoopDefaultMode, 1.0, False)
        CFNetwork.CFNetServiceUnscheduleFromRunLoop(
            svc2, rl, CFNetwork.kCFRunLoopDefaultMode
        )
        del svc2

        self.assertArgIsOut(CFNetwork.CFNetServiceMonitorStop, 1)

        def callback(mon, svc, typeinfo, rdata, error, info):
            lst.append((mon, svc, typeinfo, rdata, error, info))
            CFNetwork.CFNetServiceMonitorStop(monitor, None)

        def callback_raises(mon, svc, typeinfo, rdata, error, info):
            raise RuntimeError("callback error")

        with self.assertRaisesRegex(TypeError, "expected 4 arguments, got 0"):
            CFNetwork.CFNetServiceMonitorCreate()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            CFNetwork.CFNetServiceMonitorCreate(NoObjCClass(), svc, callback, ctx)

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            CFNetwork.CFNetServiceMonitorCreate(None, NoObjCClass(), callback, ctx)

        monitor = CFNetwork.CFNetServiceMonitorCreate(None, svc, callback, ctx)
        self.assertArgIsOut(CFNetwork.CFNetServiceMonitorStart, 2)
        ok, err = CFNetwork.CFNetServiceMonitorStart(
            monitor, CFNetwork.kCFNetServiceMonitorTXT, None
        )
        self.assertIs(ok, True)

        CFNetwork.CFNetServiceMonitorScheduleWithRunLoop(
            monitor, rl, CFNetwork.kCFRunLoopDefaultMode
        )

        CFNetwork.CFRunLoopRunInMode(CFNetwork.kCFRunLoopDefaultMode, 1.0, False)

        CFNetwork.CFNetServiceMonitorUnscheduleFromRunLoop(
            monitor, rl, CFNetwork.kCFRunLoopDefaultMode
        )
        self.assertGreater(len(lst), 0)
        for entry in lst:
            self.assertIs(entry[0], monitor)
            self.assertIn(entry[1], (svc, None))
            self.assertIsInstance(entry[2], int)
            self.assertIsInstance(entry[3], (Foundation.NSData, type(None)))
            self.assertIsInstance(entry[4], Foundation.CFStreamError)
            self.assertIs(entry[5], ctx)

        CFNetwork.CFNetServiceMonitorInvalidate(monitor)

        monitor = CFNetwork.CFNetServiceMonitorCreate(None, svc, callback_raises, ctx)
        self.assertArgIsOut(CFNetwork.CFNetServiceMonitorStart, 2)
        with self.assertRaisesRegex(RuntimeError, "callback error"):
            CFNetwork.CFNetServiceMonitorStart(
                monitor, CFNetwork.kCFNetServiceMonitorTXT, None
            )
