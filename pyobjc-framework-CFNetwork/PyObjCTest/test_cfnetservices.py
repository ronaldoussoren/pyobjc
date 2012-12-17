from CFNetwork import *
import Foundation
import sys
from PyObjCTools.TestSupport import *

if sys.version_info[0] != 2:
    def buffer(value):
        return value.encode('latin1')


try:
    long
except NameError:
    long = int

try:
    unicode
except NameError:
    unicode = str

class TestCFNetServices (TestCase):
    def testTypes(self):
        self.assertIsCFType(CFNetServiceRef)
        self.assertIsCFType(CFNetServiceMonitorRef)
        self.assertIsCFType(CFNetServiceBrowserRef)

    def testConstants(self):
        self.assertIsInstance(kCFStreamErrorDomainMach, (int, long))
        self.assertIsInstance(kCFStreamErrorDomainNetServices, (int, long))

        self.assertEqual(kCFNetServicesErrorUnknown, -72000)
        self.assertEqual(kCFNetServicesErrorCollision, -72001)
        self.assertEqual(kCFNetServicesErrorNotFound, -72002)
        self.assertEqual(kCFNetServicesErrorInProgress, -72003)
        self.assertEqual(kCFNetServicesErrorBadArgument, -72004)
        self.assertEqual(kCFNetServicesErrorCancel, -72005)
        self.assertEqual(kCFNetServicesErrorInvalid, -72006)
        self.assertEqual(kCFNetServicesErrorTimeout, -72007)
        self.assertEqual(kCFNetServiceMonitorTXT, 1)
        self.assertEqual(kCFNetServiceFlagNoAutoRename, 1)
        self.assertEqual(kCFNetServiceFlagMoreComing, 1)
        self.assertEqual(kCFNetServiceFlagIsDomain, 2)
        self.assertEqual(kCFNetServiceFlagIsDefault, 4)
        self.assertEqual(kCFNetServiceFlagIsRegistrationDomain, 4)
        self.assertEqual(kCFNetServiceFlagRemove, 8)

    def testFunctions(self):
        self.assertIsInstance(CFNetServiceGetTypeID(), (int, long))
        self.assertIsInstance(CFNetServiceMonitorGetTypeID(), (int, long))
        self.assertIsInstance(CFNetServiceBrowserGetTypeID(), (int, long))

        self.assertResultIsCFRetained(CFNetServiceCreate)
        serv = CFNetServiceCreate(None, b"pyobjc.local".decode('latin1'), b"ssh".decode('latin1'), b"pyobjc.test.local".decode('latin1'), 9999)
        self.assertIsInstance(serv, CFNetServiceRef)

        self.assertResultIsCFRetained(CFNetServiceCreateCopy)
        v = CFNetServiceCreateCopy(None, serv)
        self.assertIsInstance(v, CFNetServiceRef)

        dom = CFNetServiceGetDomain(serv)
        self.assertIsInstance(dom, unicode)

        dom = CFNetServiceGetType(serv)
        self.assertIsInstance(dom, unicode)

        dom = CFNetServiceGetName(serv)
        self.assertIsInstance(dom, unicode)

        self.assertResultIsBOOL(CFNetServiceRegisterWithOptions)
        self.assertArgIsOut(CFNetServiceRegisterWithOptions, 2)

        ok, err = CFNetServiceRegisterWithOptions(serv, kCFNetServiceFlagNoAutoRename, None)
        self.assertIsInstance(ok, bool)
        if ok:
            self.assertEqual(err, None)
        else:
            self.assertIsInstance(err, CFStreamError)

        self.assertResultIsBOOL(CFNetServiceResolveWithTimeout)
        self.assertArgIsOut(CFNetServiceResolveWithTimeout, 2)
        ok, err = CFNetServiceResolveWithTimeout(serv, 1.0, None)
        self.assertIsInstance(ok, bool)
        if ok:
            self.assertEqual(err, None)
        else:
            self.assertIsInstance(err, CFStreamError)

        host = CFNetServiceGetTargetHost(serv)
        self.assertIsInstance(host, (unicode, type(None)))

        port = CFNetServiceGetPortNumber(serv)
        self.assertIsInstance(port, (int, long))

        v = CFNetServiceGetAddressing(serv)
        self.assertIsInstance(v, (Foundation.NSArray, type(None)))

        v = CFNetServiceGetTXTData(serv)
        self.assertIsInstance(v, (Foundation.NSData, type(None)))

        v = CFNetServiceCreateTXTDataWithDictionary(None, {'key': 'value', 'key2': 'value2'})
        self.assertIsInstance(v, Foundation.NSData)

        v = CFNetServiceCreateDictionaryWithTXTData(None, v)
        self.assertIsInstance(v, Foundation.NSDictionary)

        self.assertResultIsBOOL(CFNetServiceSetTXTData)
        ok = CFNetServiceSetTXTData(serv, buffer("hello"))
        self.assertIsInstance(ok, bool)

        rl = CFRunLoopGetCurrent()
        CFNetServiceScheduleWithRunLoop(serv, rl, kCFRunLoopDefaultMode)
        CFNetServiceUnscheduleFromRunLoop(serv, rl, kCFRunLoopDefaultMode)

        CFNetServiceCancel(serv)

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



if __name__ == "__main__":
    main()
