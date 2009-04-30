from CFNetwork import *
from PyObjCTools.TestSupport import *


class TestCFNetServices (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CFNetServiceRef)
        self.failUnlessIsCFType(CFNetServiceMonitorRef)
        self.failUnlessIsCFType(CFNetServiceBrowserRef)

    def testConstants(self):
        self.failUnlessIsInstance(kCFStreamErrorDomainMach, (int, long))
        self.failUnlessIsInstance(kCFStreamErrorDomainNetServices, (int, long))

        self.failUnlessEqual(kCFNetServicesErrorUnknown, -72000)
        self.failUnlessEqual(kCFNetServicesErrorCollision, -72001)
        self.failUnlessEqual(kCFNetServicesErrorNotFound, -72002)
        self.failUnlessEqual(kCFNetServicesErrorInProgress, -72003)
        self.failUnlessEqual(kCFNetServicesErrorBadArgument, -72004)
        self.failUnlessEqual(kCFNetServicesErrorCancel, -72005)
        self.failUnlessEqual(kCFNetServicesErrorInvalid, -72006)
        self.failUnlessEqual(kCFNetServicesErrorTimeout, -72007)
        self.failUnlessEqual(kCFNetServiceMonitorTXT, 1)
        self.failUnlessEqual(kCFNetServiceFlagNoAutoRename, 1)
        self.failUnlessEqual(kCFNetServiceFlagMoreComing, 1)
        self.failUnlessEqual(kCFNetServiceFlagIsDomain, 2)
        self.failUnlessEqual(kCFNetServiceFlagIsDefault, 4)
        self.failUnlessEqual(kCFNetServiceFlagIsRegistrationDomain, 4)
        self.failUnlessEqual(kCFNetServiceFlagRemove, 8)

    def testFunctions(self):
        self.failUnlessIsInstance(CFNetServiceGetTypeID(), (int, long))
        self.failUnlessIsInstance(CFNetServiceMonitorGetTypeID(), (int, long))
        self.failUnlessIsInstance(CFNetServiceBrowserGetTypeID(), (int, long))

        self.failUnlessResultIsCFRetained(CFNetServiceCreate)
        serv = CFNetServiceCreate(None, u"pyobjc.local", u"ssh", u"pyobjc.test.local", 9999)
        self.failUnlessIsInstance(serv, CFNetServiceRef)

        self.failUnlessResultIsCFRetained(CFNetServiceCreateCopy)
        v = CFNetServiceCreateCopy(None, serv)
        self.failUnlessIsInstance(v, CFNetServiceRef)

        dom = CFNetServiceGetDomain(serv)
        self.failUnlessIsInstance(dom, unicode)

        dom = CFNetServiceGetType(serv)
        self.failUnlessIsInstance(dom, unicode)

        dom = CFNetServiceGetName(serv)
        self.failUnlessIsInstance(dom, unicode)

        self.failUnlessResultIsBOOL(CFNetServiceRegisterWithOptions)
        self.failUnlessArgIsOut(CFNetServiceRegisterWithOptions, 2)

        ok, err = CFNetServiceRegisterWithOptions(serv, kCFNetServiceFlagNoAutoRename, None)
        self.failUnlessIsInstance(ok, bool)
        if ok:
            self.failUnlessEqual(err, None)
        else:
            self.failUnlessIsInstance(err, CFStreamError)


if __name__ == "__main__":
    main()
