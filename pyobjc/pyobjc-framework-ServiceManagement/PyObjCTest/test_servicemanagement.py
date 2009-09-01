
from PyObjCTools.TestSupport import *
from ServiceManagement import *

class TestServiceManagement (TestCase):
    @min_os_level('10.6')
    def testConstants(self):
        self.failUnlessEqual(kSMRightBlessPrivilegedHelper, "com.apple.ServiceManagement.blesshelper")
        self.failUnlessEqual(kSMRightModifySystemDaemons, "com.apple.ServiceManagement.daemons.modify")

        self.failUnlessIsInstance(kSMDomainSystemLaunchd, unicode)
        self.failUnlessIsInstance(kSMDomainUserLaunchd, unicode)
        self.failUnlessIsInstance(kSMInfoKeyPrivilegedExecutables, unicode)
        self.failUnlessIsInstance(kSMInfoKeyAuthorizedClients, unicode)

    @min_os_level('10.6')
    def testFunctions(self):
        self.failUnlessResultHasType(SMJobCopyDictionary, '^{__CFDictionary=}')
        self.failUnlessArgHasType(SMJobCopyDictionary, 0, '^{__CFString=}')
        self.failUnlessArgHasType(SMJobCopyDictionary, 1, '^{__CFString=}')
        self.failUnlessResultIsCFRetained(SMJobCopyDictionary)
        v = SMJobCopyDictionary(kSMDomainUserLaunchd, u'com.apple.FileSyncAgent')
        self.failUnlessIsInstance(v, CFDictionaryRef)

        self.failUnlessResultHasType(SMCopyAllJobDictionaries, '^{__CFArray=}')
        self.failUnlessArgHasType(SMCopyAllJobDictionaries, 0, '^{__CFString=}')
        self.failUnlessResultIsCFRetained(SMCopyAllJobDictionaries)
        v = SMCopyAllJobDictionaries(kSMDomainUserLaunchd)
        self.failUnlessIsInstance(v, CFArrayRef)

        self.failUnlessResultIsBOOL(SMJobSubmit)
        self.failUnlessArgHasType(SMJobSubmit, 0, '^{__CFString=}')
        self.failUnlessArgHasType(SMJobSubmit, 1, '^{__CFDictionary=}')
        self.failUnlessArgHasType(SMJobSubmit, 2, '^{AuthorizationOpaqueRef=}')
        self.failUnlessArgHasType(SMJobSubmit, 3, 'o^^{__CFError}')

        self.failUnlessResultIsBOOL(SMJobRemove)
        self.failUnlessArgHasType(SMJobRemove, 0, '^{__CFString=}')
        self.failUnlessArgHasType(SMJobRemove, 1, '^{__CFString=}')
        self.failUnlessArgHasType(SMJobRemove, 2, '^{AuthorizationOpaqueRef=}')
        self.failUnlessArgIsBOOL(SMJobRemove, 3)
        self.failUnlessArgHasType(SMJobRemove, 4, 'o^^{__CFError}')

        self.failUnlessResultIsBOOL(SMJobBless)
        self.failUnlessArgHasType(SMJobBless, 0, '^{__CFString=}')
        self.failUnlessArgHasType(SMJobBless, 1, '^{__CFString=}')
        self.failUnlessArgHasType(SMJobBless, 2, '^{AuthorizationOpaqueRef=}')
        self.failUnlessArgHasType(SMJobBless, 3, 'o^^{__CFError}')



if __name__ == "__main__":
    main()
