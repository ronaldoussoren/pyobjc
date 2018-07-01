from PyObjCTools.TestSupport import *

import DiscRecording

class TestDRFSObject (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DiscRecording.DRFSObject.isVirtual)

        self.assertArgIsBOOL(DiscRecording.DRFSObject.propertyForKey_inFilesystem_mergeWithOtherFilesystems_, 2)
        self.assertArgIsBOOL(DiscRecording.DRFSObject.propertiesForFilesystem_mergeWithOtherFilesystems_, 1)

    def testConstants(self):
        self.assertEqual(DiscRecording.DRFilesystemInclusionMaskISO9660, 1<<0)
        self.assertEqual(DiscRecording.DRFilesystemInclusionMaskJoliet, 1<<1)
        self.assertEqual(DiscRecording.DRFilesystemInclusionMaskUDF, 1<<2)
        self.assertEqual(DiscRecording.DRFilesystemInclusionMaskHFSPlus, 1<<3)

        self.assertIsInstance(DiscRecording.DRAllFilesystems, unicode)
        self.assertIsInstance(DiscRecording.DRISO9660, unicode)
        self.assertIsInstance(DiscRecording.DRISO9660LevelOne, unicode)
        self.assertIsInstance(DiscRecording.DRISO9660LevelTwo, unicode)
        self.assertIsInstance(DiscRecording.DRJoliet, unicode)
        self.assertIsInstance(DiscRecording.DRHFSPlus, unicode)
        self.assertIsInstance(DiscRecording.DRUDF, unicode)
        self.assertIsInstance(DiscRecording.DRISO9660VersionNumber, unicode)
        self.assertIsInstance(DiscRecording.DRInvisible, unicode)
        self.assertIsInstance(DiscRecording.DRCreationDate, unicode)
        self.assertIsInstance(DiscRecording.DRContentModificationDate, unicode)
        self.assertIsInstance(DiscRecording.DRAttributeModificationDate, unicode)
        self.assertIsInstance(DiscRecording.DRAccessDate, unicode)
        self.assertIsInstance(DiscRecording.DRBackupDate, unicode)
        self.assertIsInstance(DiscRecording.DREffectiveDate, unicode)
        self.assertIsInstance(DiscRecording.DRExpirationDate, unicode)
        self.assertIsInstance(DiscRecording.DRRecordingDate, unicode)
        self.assertIsInstance(DiscRecording.DRPosixFileMode, unicode)
        self.assertIsInstance(DiscRecording.DRPosixUID, unicode)
        self.assertIsInstance(DiscRecording.DRPosixGID, unicode)
        self.assertIsInstance(DiscRecording.DRHFSPlusTextEncodingHint, unicode)
        self.assertIsInstance(DiscRecording.DRHFSPlusCatalogNodeID, unicode)
        self.assertIsInstance(DiscRecording.DRMacFileType, unicode)
        self.assertIsInstance(DiscRecording.DRMacFileCreator, unicode)
        self.assertIsInstance(DiscRecording.DRMacWindowBounds, unicode)
        self.assertIsInstance(DiscRecording.DRMacIconLocation, unicode)
        self.assertIsInstance(DiscRecording.DRMacScrollPosition, unicode)
        self.assertIsInstance(DiscRecording.DRMacWindowView, unicode)
        self.assertIsInstance(DiscRecording.DRMacFinderFlags, unicode)
        self.assertIsInstance(DiscRecording.DRMacExtendedFinderFlags, unicode)
        self.assertIsInstance(DiscRecording.DRMacFinderHideExtension, unicode)
        self.assertIsInstance(DiscRecording.DRUDFWriteVersion, unicode)
        self.assertIsInstance(DiscRecording.DRUDFVersion102, unicode)
        self.assertIsInstance(DiscRecording.DRUDFVersion150, unicode)
        self.assertIsInstance(DiscRecording.DRUDFPrimaryVolumeDescriptorNumber, unicode)
        self.assertIsInstance(DiscRecording.DRUDFVolumeSequenceNumber, unicode)
        self.assertIsInstance(DiscRecording.DRUDFMaxVolumeSequenceNumber, unicode)
        self.assertIsInstance(DiscRecording.DRUDFInterchangeLevel, unicode)
        self.assertIsInstance(DiscRecording.DRUDFMaxInterchangeLevel, unicode)
        self.assertIsInstance(DiscRecording.DRUDFApplicationIdentifierSuffix, unicode)
        self.assertIsInstance(DiscRecording.DRUDFVolumeSetIdentifier, unicode)
        self.assertIsInstance(DiscRecording.DRUDFVolumeSetTimestamp, unicode)
        self.assertIsInstance(DiscRecording.DRUDFVolumeSetImplementationUse, unicode)
        self.assertIsInstance(DiscRecording.DRUDFRealTimeFile, unicode)
        self.assertIsInstance(DiscRecording.DRUDFExtendedFilePermissions, unicode)


if __name__ == "__main__":
    main()
