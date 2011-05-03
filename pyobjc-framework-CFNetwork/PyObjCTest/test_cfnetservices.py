from CFNetwork import *
from PyObjCTools.TestSupport import *


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
        serv = CFNetServiceCreate(None, u"pyobjc.local", u"ssh", u"pyobjc.test.local", 9999)
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


if __name__ == "__main__":
    main()
