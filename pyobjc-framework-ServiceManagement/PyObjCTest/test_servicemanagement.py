from PyObjCTools.TestSupport import TestCase, min_os_level
import ServiceManagement


class TestServiceManagement(TestCase):
    @min_os_level("10.6")
    def testConstants(self):
        self.assertEqual(
            ServiceManagement.kSMRightBlessPrivilegedHelper,
            b"com.apple.ServiceManagement.blesshelper",
        )
        self.assertEqual(
            ServiceManagement.kSMRightModifySystemDaemons,
            b"com.apple.ServiceManagement.daemons.modify",
        )

        self.assertIsInstance(ServiceManagement.kSMDomainSystemLaunchd, str)
        self.assertIsInstance(ServiceManagement.kSMDomainUserLaunchd, str)
        self.assertIsInstance(ServiceManagement.kSMInfoKeyPrivilegedExecutables, str)
        self.assertIsInstance(ServiceManagement.kSMInfoKeyAuthorizedClients, str)

    @min_os_level("10.6")
    def testFunctions(self):
        self.assertResultHasType(
            ServiceManagement.SMJobCopyDictionary, b"^{__CFDictionary=}"
        )
        self.assertArgHasType(
            ServiceManagement.SMJobCopyDictionary, 0, b"^{__CFString=}"
        )
        self.assertArgHasType(
            ServiceManagement.SMJobCopyDictionary, 1, b"^{__CFString=}"
        )
        self.assertResultIsCFRetained(ServiceManagement.SMJobCopyDictionary)
        v = ServiceManagement.SMJobCopyDictionary(
            ServiceManagement.kSMDomainUserLaunchd, "com.apple.Dock.agent"
        )
        self.assertIsInstance(v, ServiceManagement.NSDictionary)

        self.assertResultHasType(
            ServiceManagement.SMCopyAllJobDictionaries, b"^{__CFArray=}"
        )
        self.assertArgHasType(
            ServiceManagement.SMCopyAllJobDictionaries, 0, b"^{__CFString=}"
        )
        self.assertResultIsCFRetained(ServiceManagement.SMCopyAllJobDictionaries)
        v = ServiceManagement.SMCopyAllJobDictionaries(
            ServiceManagement.kSMDomainUserLaunchd
        )
        self.assertIsInstance(v, ServiceManagement.CFArrayRef)

        self.assertResultIsBOOL(ServiceManagement.SMJobSubmit)
        self.assertArgHasType(ServiceManagement.SMJobSubmit, 0, b"^{__CFString=}")
        self.assertArgHasType(ServiceManagement.SMJobSubmit, 1, b"^{__CFDictionary=}")
        self.assertArgHasType(
            ServiceManagement.SMJobSubmit, 2, b"^{AuthorizationOpaqueRef=}"
        )
        self.assertArgHasType(ServiceManagement.SMJobSubmit, 3, b"o^^{__CFError}")

        self.assertResultIsBOOL(ServiceManagement.SMJobRemove)
        self.assertArgHasType(ServiceManagement.SMJobRemove, 0, b"^{__CFString=}")
        self.assertArgHasType(ServiceManagement.SMJobRemove, 1, b"^{__CFString=}")
        self.assertArgHasType(
            ServiceManagement.SMJobRemove, 2, b"^{AuthorizationOpaqueRef=}"
        )
        self.assertArgIsBOOL(ServiceManagement.SMJobRemove, 3)
        self.assertArgHasType(ServiceManagement.SMJobRemove, 4, b"o^^{__CFError}")

        self.assertResultIsBOOL(ServiceManagement.SMJobBless)
        self.assertArgHasType(ServiceManagement.SMJobBless, 0, b"^{__CFString=}")
        self.assertArgHasType(ServiceManagement.SMJobBless, 1, b"^{__CFString=}")
        self.assertArgHasType(
            ServiceManagement.SMJobBless, 2, b"^{AuthorizationOpaqueRef=}"
        )
        self.assertArgHasType(ServiceManagement.SMJobBless, 3, b"o^^{__CFError}")
