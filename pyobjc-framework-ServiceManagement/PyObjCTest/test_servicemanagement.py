
from PyObjCTools.TestSupport import *
from ServiceManagement import *

class TestServiceManagement (TestCase):
    @min_os_level('10.6')
    def testConstants(self):
        self.assertEqual(kSMRightBlessPrivilegedHelper, b"com.apple.ServiceManagement.blesshelper")
        self.assertEqual(kSMRightModifySystemDaemons, b"com.apple.ServiceManagement.daemons.modify")

        self.assertIsInstance(kSMDomainSystemLaunchd, unicode)
        self.assertIsInstance(kSMDomainUserLaunchd, unicode)
        self.assertIsInstance(kSMInfoKeyPrivilegedExecutables, unicode)
        self.assertIsInstance(kSMInfoKeyAuthorizedClients, unicode)

    @min_os_level('10.6')
    def testFunctions(self):
        self.assertResultHasType(SMJobCopyDictionary, b'^{__CFDictionary=}')
        self.assertArgHasType(SMJobCopyDictionary, 0, b'^{__CFString=}')
        self.assertArgHasType(SMJobCopyDictionary, 1, b'^{__CFString=}')
        self.assertResultIsCFRetained(SMJobCopyDictionary)
        v = SMJobCopyDictionary(kSMDomainUserLaunchd, u'com.apple.FileSyncAgent')
        self.assertIsInstance(v, CFDictionaryRef)

        self.assertResultHasType(SMCopyAllJobDictionaries, b'^{__CFArray=}')
        self.assertArgHasType(SMCopyAllJobDictionaries, 0, b'^{__CFString=}')
        self.assertResultIsCFRetained(SMCopyAllJobDictionaries)
        v = SMCopyAllJobDictionaries(kSMDomainUserLaunchd)
        self.assertIsInstance(v, CFArrayRef)

        self.assertResultIsBOOL(SMJobSubmit)
        self.assertArgHasType(SMJobSubmit, 0, b'^{__CFString=}')
        self.assertArgHasType(SMJobSubmit, 1, b'^{__CFDictionary=}')
        self.assertArgHasType(SMJobSubmit, 2, b'^{AuthorizationOpaqueRef=}')
        self.assertArgHasType(SMJobSubmit, 3, b'o^^{__CFError}')

        self.assertResultIsBOOL(SMJobRemove)
        self.assertArgHasType(SMJobRemove, 0, b'^{__CFString=}')
        self.assertArgHasType(SMJobRemove, 1, b'^{__CFString=}')
        self.assertArgHasType(SMJobRemove, 2, b'^{AuthorizationOpaqueRef=}')
        self.assertArgIsBOOL(SMJobRemove, 3)
        self.assertArgHasType(SMJobRemove, 4, b'o^^{__CFError}')

        self.assertResultIsBOOL(SMJobBless)
        self.assertArgHasType(SMJobBless, 0, b'^{__CFString=}')
        self.assertArgHasType(SMJobBless, 1, b'^{__CFString=}')
        self.assertArgHasType(SMJobBless, 2, b'^{AuthorizationOpaqueRef=}')
        self.assertArgHasType(SMJobBless, 3, b'o^^{__CFError}')



if __name__ == "__main__":
    main()
