import Foundation
import CFNetwork
from PyObjCTools.TestSupport import TestCase, expectedFailure


class TestCFNetServices(TestCase):
    def testTypes(self):
        self.assertIsCFType(CFNetwork.CFNetServiceRef)
        self.assertIsCFType(CFNetwork.CFNetServiceMonitorRef)
        self.assertIsCFType(CFNetwork.CFNetServiceBrowserRef)

    def testConstants(self):
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

    def testFunctions(self):
        self.assertIsInstance(CFNetwork.CFNetServiceGetTypeID(), int)
        self.assertIsInstance(CFNetwork.CFNetServiceMonitorGetTypeID(), int)
        self.assertIsInstance(CFNetwork.CFNetServiceBrowserGetTypeID(), int)

        self.assertResultIsCFRetained(CFNetwork.CFNetServiceCreate)
        serv = CFNetwork.CFNetServiceCreate(
            None, "pyobjc.local", "ssh", "pyobjc.test.local", 9999
        )
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

    @expectedFailure
    def testMissingTests(self):
        self.fail("CFNetServiceSetClient")
        self.fail("CFNetServiceMonitorCreate")
        self.fail("CFNetServiceMonitorInvalidate")
        self.fail("CFNetServiceMonitorStart")
        self.fail("CFNetServiceMonitorStop")
        self.fail("CFNetServiceMonitorScheduleWithRunLoop")
        self.fail("CFNetServiceMonitorUnscheduleFromRunLoop")
        self.fail("CFNetServiceBrowserCreate")
        self.fail("CFNetServiceBrowserInvalidate")
        self.fail("CFNetServiceBrowserSearchForDomains")
        self.fail("CFNetServiceBrowserSearchForServices")
        self.fail("CFNetServiceBrowserStopSearch")
        self.fail("CFNetServiceBrowserScheduleWithRunLoop")
        self.fail("CFNetServiceBrowserUnscheduleFromRunLoop")
        self.fail("CFNetServiceRegister")
        self.fail("CFNetServiceResolve")
        self.fail("CFNetServiceGetProtocolSpecificInformation")
        self.fail("CFNetServiceSetProtocolSpecificInformation")
