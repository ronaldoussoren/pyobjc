import DiscRecording
from PyObjCTools.TestSupport import TestCase


class TestDRFSObject(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DiscRecording.DRFSObject.isVirtual)

        self.assertArgIsBOOL(
            DiscRecording.DRFSObject.propertyForKey_inFilesystem_mergeWithOtherFilesystems_,
            2,
        )
        self.assertArgIsBOOL(
            DiscRecording.DRFSObject.propertiesForFilesystem_mergeWithOtherFilesystems_,
            1,
        )

    def testConstants(self):
        self.assertEqual(DiscRecording.DRFilesystemInclusionMaskISO9660, 1 << 0)
        self.assertEqual(DiscRecording.DRFilesystemInclusionMaskJoliet, 1 << 1)
        self.assertEqual(DiscRecording.DRFilesystemInclusionMaskUDF, 1 << 2)
        self.assertEqual(DiscRecording.DRFilesystemInclusionMaskHFSPlus, 1 << 3)

        self.assertIsInstance(DiscRecording.DRAllFilesystems, str)
        self.assertIsInstance(DiscRecording.DRISO9660, str)
        self.assertIsInstance(DiscRecording.DRISO9660LevelOne, str)
        self.assertIsInstance(DiscRecording.DRISO9660LevelTwo, str)
        self.assertIsInstance(DiscRecording.DRJoliet, str)
        self.assertIsInstance(DiscRecording.DRHFSPlus, str)
        self.assertIsInstance(DiscRecording.DRUDF, str)
        self.assertIsInstance(DiscRecording.DRISO9660VersionNumber, str)
        self.assertIsInstance(DiscRecording.DRInvisible, str)
        self.assertIsInstance(DiscRecording.DRCreationDate, str)
        self.assertIsInstance(DiscRecording.DRContentModificationDate, str)
        self.assertIsInstance(DiscRecording.DRAttributeModificationDate, str)
        self.assertIsInstance(DiscRecording.DRAccessDate, str)
        self.assertIsInstance(DiscRecording.DRBackupDate, str)
        self.assertIsInstance(DiscRecording.DREffectiveDate, str)
        self.assertIsInstance(DiscRecording.DRExpirationDate, str)
        self.assertIsInstance(DiscRecording.DRRecordingDate, str)
        self.assertIsInstance(DiscRecording.DRPosixFileMode, str)
        self.assertIsInstance(DiscRecording.DRPosixUID, str)
        self.assertIsInstance(DiscRecording.DRPosixGID, str)
        self.assertIsInstance(DiscRecording.DRHFSPlusTextEncodingHint, str)
        self.assertIsInstance(DiscRecording.DRHFSPlusCatalogNodeID, str)
        self.assertIsInstance(DiscRecording.DRMacFileType, str)
        self.assertIsInstance(DiscRecording.DRMacFileCreator, str)
        self.assertIsInstance(DiscRecording.DRMacWindowBounds, str)
        self.assertIsInstance(DiscRecording.DRMacIconLocation, str)
        self.assertIsInstance(DiscRecording.DRMacScrollPosition, str)
        self.assertIsInstance(DiscRecording.DRMacWindowView, str)
        self.assertIsInstance(DiscRecording.DRMacFinderFlags, str)
        self.assertIsInstance(DiscRecording.DRMacExtendedFinderFlags, str)
        self.assertIsInstance(DiscRecording.DRMacFinderHideExtension, str)
        self.assertIsInstance(DiscRecording.DRUDFWriteVersion, str)
        self.assertIsInstance(DiscRecording.DRUDFVersion102, str)
        self.assertIsInstance(DiscRecording.DRUDFVersion150, str)
        self.assertIsInstance(DiscRecording.DRUDFPrimaryVolumeDescriptorNumber, str)
        self.assertIsInstance(DiscRecording.DRUDFVolumeSequenceNumber, str)
        self.assertIsInstance(DiscRecording.DRUDFMaxVolumeSequenceNumber, str)
        self.assertIsInstance(DiscRecording.DRUDFInterchangeLevel, str)
        self.assertIsInstance(DiscRecording.DRUDFMaxInterchangeLevel, str)
        self.assertIsInstance(DiscRecording.DRUDFApplicationIdentifierSuffix, str)
        self.assertIsInstance(DiscRecording.DRUDFVolumeSetIdentifier, str)
        self.assertIsInstance(DiscRecording.DRUDFVolumeSetTimestamp, str)
        self.assertIsInstance(DiscRecording.DRUDFVolumeSetImplementationUse, str)
        self.assertIsInstance(DiscRecording.DRUDFRealTimeFile, str)
        self.assertIsInstance(DiscRecording.DRUDFExtendedFilePermissions, str)
