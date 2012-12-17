from PyObjCTools.TestSupport import *
import CoreFoundation

try:
    long
except NameError:
    long = int


class TestCFFileSecurity (TestCase):
    @min_os_level('10.7')
    def testTypes(self):
        self.assertIsCFType(CoreFoundation.CFFileSecurityRef)

    @min_os_level('10.7')
    def testTypeID(self):
        self.assertIsInstance(CoreFoundation.CFFileSecurityGetTypeID(), (int, long))

    @min_os_level('10.7')
    @expectedFailure
    def testConstants(self):
        self.fail("kCFFileSecurityRemoveACL")

    @min_os_level('10.8')
    @expectedFailure
    def testConstants10_8(self):
        self.assertEqual(kCFFileSecurityClearOwner, 1<<0)
        self.assertEqual(kCFFileSecurityClearGroup, 1<<1)
        self.assertEqual(kCFFileSecurityClearMode, 1<<2)
        self.assertEqual(kCFFileSecurityClearOwnerUUID, 1<<3)
        self.assertEqual(kCFFileSecurityClearGroupUUID, 1<<4)
        self.assertEqual(kCFFileSecurityClearAccessControlList, 1<<5)


    @min_os_level('10.7')
    def testFunctions10_7(self):
        self.assertResultIsCFRetained(CoreFoundation.CFFileSecurityCreate)
        v = CoreFoundation.CFFileSecurityCreate(None)
        self.assertIsInstance(v, CoreFoundation.CFFileSecurityRef)

        self.assertResultIsCFRetained(CoreFoundation.CFFileSecurityCreateCopy)
        o = CoreFoundation.CFFileSecurityCreateCopy(None, v)
        self.assertIsInstance(o, CoreFoundation.CFFileSecurityRef)

        self.assertResultIsBOOL(CoreFoundation.CFFileSecurityCopyOwnerUUID)
        self.assertArgIsOut(CoreFoundation.CFFileSecurityCopyOwnerUUID, 1)
        self.assertResultIsBOOL(CoreFoundation.CFFileSecuritySetOwnerUUID)

        self.assertResultIsBOOL(CoreFoundation.CFFileSecurityCopyGroupUUID)
        self.assertArgIsOut(CoreFoundation.CFFileSecurityCopyGroupUUID, 1)
        self.assertResultIsBOOL(CoreFoundation.CFFileSecuritySetGroupUUID)

        self.assertResultIsBOOL(CoreFoundation.CFFileSecurityGetOwner)
        self.assertArgIsOut(CoreFoundation.CFFileSecurityGetOwner, 1)
        self.assertResultIsBOOL(CoreFoundation.CFFileSecuritySetOwner)

        self.assertResultIsBOOL(CoreFoundation.CFFileSecurityGetGroup)
        self.assertArgIsOut(CoreFoundation.CFFileSecurityGetGroup, 1)
        self.assertResultIsBOOL(CoreFoundation.CFFileSecuritySetGroup)

        self.assertResultIsBOOL(CoreFoundation.CFFileSecurityGetMode)
        self.assertArgIsOut(CoreFoundation.CFFileSecurityGetMode, 1)
        self.assertResultIsBOOL(CoreFoundation.CFFileSecuritySetMode)

        security = CoreFoundation.CFFileSecurityCreate(None)
        self.assertIsInstance(v, CoreFoundation.CFFileSecurityRef)

        ok = CoreFoundation.CFFileSecuritySetOwner(security, 44)
        self.assertTrue(ok)
        ok, v = CoreFoundation.CFFileSecurityGetOwner(security, None)
        self.assertTrue(ok)
        self.assertEqual(v, 44)

        ok = CoreFoundation.CFFileSecuritySetGroup(security, 999)
        self.assertTrue(ok)
        ok, v = CoreFoundation.CFFileSecurityGetGroup(security, None)
        self.assertTrue(ok)
        self.assertEqual(v, 999)

        ok = CoreFoundation.CFFileSecuritySetMode(security, 0o444)
        self.assertTrue(ok)
        ok, v = CoreFoundation.CFFileSecurityGetMode(security, None)
        self.assertTrue(ok)
        self.assertEqual(v, 0o444)

    @min_os_level('10.7')
    @expectedFailure
    def testFunctionsUnwrapped(self):
        # There are no usable wrappers for sys/acl.h at this time
        self.fail("ACL Handling")

    @min_os_level('10.8')
    def testFunctions10_8(self):
        security = CoreFoundation.CFFileSecurityCreate(None)
        self.assertIsInstance(security, CoreFoundation.CFFileSecurityRef)

        CoreFoundation.CFFileSecurityClearProperties(security, CoreFoundation.kCFFileSecurityClearGroup)


if __name__ == "__main__":
    main()
