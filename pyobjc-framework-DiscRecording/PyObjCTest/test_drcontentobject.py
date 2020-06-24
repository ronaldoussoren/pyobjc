import DiscRecording
from PyObjCTools.TestSupport import TestCase, expectedFailure
import objc


class TestDRContentObject(TestCase):
    @expectedFailure
    def testCFTypes(self):
        self.assertIsCFType(DiscRecording.DRFileRef)
        self.assertIsCFType(DiscRecording.DRFolderRef)

    def testConstants(self):
        self.assertEqual(DiscRecording.kDRFilesystemMaskISO9660, 1 << 0)
        self.assertEqual(DiscRecording.kDRFilesystemMaskJoliet, 1 << 1)
        self.assertEqual(DiscRecording.kDRFilesystemMaskUDF, 1 << 2)
        self.assertEqual(DiscRecording.kDRFilesystemMaskHFSPlus, 1 << 3)
        self.assertEqual(DiscRecording.kDRFilesystemMaskDefault, 0xFFFFFFFF)

    def testFunctions(self):
        self.assertResultIsBOOL(DiscRecording.DRFSObjectIsVirtual)
        self.assertArgHasType(DiscRecording.DRFSObjectIsVirtual, 0, objc._C_ID)

        self.assertArgIsOut(DiscRecording.DRFSObjectGetRealFSRef, 1)
        self.assertArgHasType(DiscRecording.DRFSObjectGetRealFSRef, 0, objc._C_ID)

        self.assertResultIsCFRetained(DiscRecording.DRFSObjectCopyRealURL)
        self.assertArgHasType(DiscRecording.DRFSObjectCopyRealURL, 0, objc._C_ID)

        self.assertArgHasType(DiscRecording.DRFSObjectGetParent, 0, objc._C_ID)

        self.assertResultIsCFRetained(DiscRecording.DRFSObjectCopyBaseName)
        self.assertArgHasType(DiscRecording.DRFSObjectCopyBaseName, 0, objc._C_ID)

        self.assertResultIsCFRetained(DiscRecording.DRFSObjectCopySpecificName)
        self.assertArgHasType(DiscRecording.DRFSObjectCopySpecificName, 0, objc._C_ID)

        self.assertResultIsCFRetained(DiscRecording.DRFSObjectCopySpecificNames)
        self.assertArgHasType(DiscRecording.DRFSObjectCopySpecificNames, 0, objc._C_ID)

        self.assertResultIsCFRetained(DiscRecording.DRFSObjectCopyMangledName)
        self.assertArgHasType(DiscRecording.DRFSObjectCopyMangledName, 0, objc._C_ID)

        self.assertResultIsCFRetained(DiscRecording.DRFSObjectCopyMangledNames)
        self.assertArgHasType(DiscRecording.DRFSObjectCopyMangledNames, 0, objc._C_ID)

        self.assertResultIsCFRetained(DiscRecording.DRFSObjectCopyFilesystemProperty)
        self.assertArgHasType(
            DiscRecording.DRFSObjectCopyFilesystemProperty, 0, objc._C_ID
        )
        self.assertArgIsBOOL(DiscRecording.DRFSObjectCopyFilesystemProperty, 3)

        self.assertResultIsCFRetained(DiscRecording.DRFSObjectCopyFilesystemProperties)
        self.assertArgHasType(
            DiscRecording.DRFSObjectCopyFilesystemProperties, 0, objc._C_ID
        )
        self.assertArgIsBOOL(DiscRecording.DRFSObjectCopyFilesystemProperties, 2)

        self.assertArgHasType(DiscRecording.DRFSObjectGetFilesystemMask, 0, objc._C_ID)
        self.assertArgIsOut(DiscRecording.DRFSObjectGetFilesystemMask, 1)
        self.assertArgIsOut(DiscRecording.DRFSObjectGetFilesystemMask, 2)

        self.assertArgHasType(DiscRecording.DRFSObjectSetBaseName, 0, objc._C_ID)

        self.assertArgHasType(DiscRecording.DRFSObjectSetSpecificName, 0, objc._C_ID)

        self.assertArgHasType(DiscRecording.DRFSObjectSetSpecificNames, 0, objc._C_ID)

        self.assertArgHasType(
            DiscRecording.DRFSObjectSetFilesystemProperty, 0, objc._C_ID
        )

        self.assertArgHasType(
            DiscRecording.DRFSObjectSetFilesystemProperties, 0, objc._C_ID
        )

        self.assertArgHasType(DiscRecording.DRFSObjectSetFilesystemMask, 0, objc._C_ID)
