from PyObjCTools.TestSupport import TestCase

import FSKit
import objc

FSDirEntryPacker = b"Z@qQQ@Z"


class TestFSVolumeHelper(FSKit.NSObject):
    # FSVolumePathConfOperations
    def maximumLinkCount(self):
        return 1

    def maximumNameLength(self):
        return 1

    def restrictsOwnershipChanges(self):
        return 1

    def truncatesLongNames(self):
        return 1

    def maximumXattrSize(self):
        return 1

    def maximumXattrSizeInBits(self):
        return 1

    def maximumFileSize(self):
        return 1

    def maximumFileSizeInBits(self):
        return 1

    # FSVolumeOperations
    def mountWithOptions_replyHandler_(self, a, b):
        pass

    def unmountWithReplyHandler_(self, a):
        pass

    def synchronizeWithFlags_replyHandler_(self, a, b):
        pass

    def getAttributes_ofItem_replyHandler_(self, a, b, c):
        pass

    def setAttributes_onItem_replyHandler_(self, a, b, c):
        pass

    def lookupItemNamed_inDirectory_replyHandler_(self, a, b, c):
        pass

    def reclaimItem_replyHandler_(self, a, b):
        pass

    def readSymbolicLink_replyHandler_(self, a, b):
        pass

    def createItemNamed_type_inDirectory_attributes_replyHandler_(self, a, b, c, d, e):
        pass

    def createSymbolicLinkNamed_inDirectory_attributes_linkContents_replyHandler_(
        self, a, b, c, d, e
    ):
        pass

    def createLinkToItem_named_inDirectory_replyHandler_(self, a, b, c, d):
        pass

    def removeItem_named_fromDirectory_replyHandler_(self, a, b, c, d):
        pass

    def renameItem_inDirectory_named_toNewName_inDirectory_overItem_replyHandler_(
        self, a, b, c, d, e, f, g
    ):
        pass

    def enumerateDirectory_startingAtCookie_verifier_providingAttributes_usingPacker_replyHandler_(
        self,
        a,
        b,
        c,
        d,
        e,
        f,
    ):
        pass

    def activateWithOptions_replyHandler_(self, a, b):
        pass

    def deactivateWithOptions_replyHandler_(self, a, b):
        pass

    # FSVolumeXattrOperations
    def xattrOperationsInhibited(self):
        return 1

    def setXattrOperationsInhibited_(self, a):
        pass

    def getXattrNamed_ofItem_replyHandler_(self, a, b, c):
        pass

    def setXattrNamed_toData_onItem_policy_replyHandler_(self, a, b, c, d, e):
        pass

    def listXattrsOfItem_replyHandler_(self, a, b):
        pass

    # FSVolumeOpenCloseOperations
    def isOpenCloseInhibited(self):
        return 1

    def setOpenCloseInhibited_(self, a):
        pass

    def openItem_withModes_replyHandler_(self, a, b, c):
        pass

    def closeItem_keepingModes_replyHandler_(self, a, b, c):
        pass

    def enableOpenUnlinkEmulation(self):
        return 1

    def setEnableOpenUnlinkEmulation_(self, a):
        pass

    # FSVolumeReadWriteOperations
    def readFromFile_offset_length_intoBuffer_replyHandler_(self, a, b, c, d, e):
        pass

    def writeContents_toFile_atOffset_replyHandler_(self, a, b, c, d):
        pass

    # FSVolumeAccessCheckOperations
    def isAccessCheckInhibited(self):
        return 1

    def setAccessCheckInhibited_(self, a):
        pass

    def checkAccessToItem_requestedAccess_replyHandler_(self, a, b, c):
        pass

    # FSVolumeRenameOperations
    def isVolumeRenameInhibited(self):
        return 1

    def setVolumeRenameInhibited_(self, a):
        pass

    def setVolumeName_replyHandler_(self, a, b):
        pass

    # FSVolumePreallocateOperations
    def isPreallocateInhibited(self):
        return 1

    def setPreallocateInhibited_(self, a):
        pass

    def preallocateSpaceForItem_atOffset_length_flags_replyHandler_(
        self, a, b, c, d, e
    ):
        pass

    # FSVolumeItemDeactivation
    def itemDeactivationPolicy(self):
        return 1

    def deactivateItem_replyHandler_(self, a, b):
        pass


class TestFSVolume(TestCase):
    def test_enum(self):
        self.assertIsInstance(FSKit.FSDirectoryCookieInitial, int)
        self.assertIsInstance(FSKit.FSDirectoryVerifierInitial, int)

        self.assertIsEnumType(FSKit.FSSyncFlags)
        self.assertEqual(FSKit.FSSyncFlagsWait, 1)
        self.assertEqual(FSKit.FSSyncFlagsNoWait, 2)
        self.assertEqual(FSKit.FSSyncFlagsDWait, 4)

        self.assertIsEnumType(FSKit.FSVolumeCaseFormat)
        self.assertEqual(FSKit.FSVolumeCaseFormatSensitive, 0)
        self.assertEqual(FSKit.FSVolumeCaseFormatInsensitive, 1)
        self.assertEqual(FSKit.FSVolumeCaseFormatInsensitiveCasePreserving, 2)

        self.assertIsEnumType(FSKit.FSSetXattrPolicy)
        self.assertEqual(FSKit.FSSetXattrPolicyAlwaysSet, 0)
        self.assertEqual(FSKit.FSSetXattrPolicyMustCreate, 1)
        self.assertEqual(FSKit.FSSetXattrPolicyMustReplace, 2)
        self.assertEqual(FSKit.FSSetXattrPolicyDelete, 3)

        self.assertIsEnumType(FSKit.FSVolumeOpenModes)
        self.assertEqual(FSKit.FSVolumeOpenModesRead, 1)
        self.assertEqual(FSKit.FSVolumeOpenModesWrite, 2)

        self.assertIsEnumType(FSKit.FSAccessMask)
        self.assertEqual(FSKit.FSAccessReadData, 1 << 1)
        self.assertEqual(FSKit.FSAccessListDirectory, FSKit.FSAccessReadData)
        self.assertEqual(FSKit.FSAccessWriteData, 1 << 2)
        self.assertEqual(FSKit.FSAccessAddFile, FSKit.FSAccessWriteData)
        self.assertEqual(FSKit.FSAccessExecute, 1 << 3)
        self.assertEqual(FSKit.FSAccessSearch, FSKit.FSAccessExecute)
        self.assertEqual(FSKit.FSAccessDelete, 1 << 4)
        self.assertEqual(FSKit.FSAccessAppendData, 1 << 5)
        self.assertEqual(FSKit.FSAccessAddSubdirectory, FSKit.FSAccessAppendData)
        self.assertEqual(FSKit.FSAccessDeleteChild, 1 << 6)
        self.assertEqual(FSKit.FSAccessReadAttributes, 1 << 7)
        self.assertEqual(FSKit.FSAccessWriteAttributes, 1 << 8)
        self.assertEqual(FSKit.FSAccessReadXattr, 1 << 9)
        self.assertEqual(FSKit.FSAccessWriteXattr, 1 << 10)
        self.assertEqual(FSKit.FSAccessReadSecurity, 1 << 11)
        self.assertEqual(FSKit.FSAccessWriteSecurity, 1 << 12)
        self.assertEqual(FSKit.FSAccessTakeOwnership, 1 << 13)

        self.assertIsEnumType(FSKit.FSPreallocateFlags)
        self.assertEqual(FSKit.FSPreallocateFlagsContiguous, 0x00000002)
        self.assertEqual(FSKit.FSPreallocateFlagsAll, 0x00000004)
        self.assertEqual(FSKit.FSPreallocateFlagsPersist, 0x00000008)
        self.assertEqual(FSKit.FSPreallocateFlagsFromEOF, 0x00000010)

        self.assertIsEnumType(FSKit.FSItemDeactivationOptions)
        self.assertEqual(FSKit.FSItemDeactivationNever, 0)
        self.assertEqual(FSKit.FSItemDeactivationAlways, 0xFFFFFFFFFFFFFFFF)
        self.assertEqual(FSKit.FSItemDeactivationForRemovedItems, 1 << 0)
        self.assertEqual(FSKit.FSItemDeactivationForPreallocatedItems, 1 << 1)

    def test_protocols(self):
        self.assertProtocolExists("FSVolumePathConfOperations")
        self.assertProtocolExists("FSVolumeOperations")
        self.assertProtocolExists("FSVolumeXattrOperations")
        self.assertProtocolExists("FSVolumeOpenCloseOperations")
        self.assertProtocolExists("FSVolumeReadWriteOperations")
        self.assertProtocolExists("FSVolumeAccessCheckOperations")
        self.assertProtocolExists("FSVolumeRenameOperations")
        self.assertProtocolExists("FSVolumePreallocateOperations")
        self.assertProtocolExists("FSVolumeItemDeactivation")

    def test_protocol_methods(self):
        # FSVolumePathConfOperations
        self.assertResultHasType(TestFSVolumeHelper.maximumLinkCount, objc._C_NSInteger)
        self.assertResultHasType(
            TestFSVolumeHelper.maximumNameLength, objc._C_NSInteger
        )
        self.assertResultIsBOOL(TestFSVolumeHelper.restrictsOwnershipChanges)
        self.assertResultIsBOOL(TestFSVolumeHelper.truncatesLongNames)
        self.assertResultHasType(TestFSVolumeHelper.maximumXattrSize, objc._C_NSInteger)
        self.assertResultHasType(
            TestFSVolumeHelper.maximumXattrSizeInBits, objc._C_NSInteger
        )
        self.assertResultHasType(TestFSVolumeHelper.maximumFileSize, objc._C_NSUInteger)
        self.assertResultHasType(
            TestFSVolumeHelper.maximumFileSizeInBits, objc._C_NSInteger
        )

        # FSVolumeOperations

        self.assertArgIsBlock(
            TestFSVolumeHelper.mountWithOptions_replyHandler_, 1, b"v@"
        )
        self.assertArgIsBlock(TestFSVolumeHelper.unmountWithReplyHandler_, 0, b"v")

        self.assertArgHasType(
            TestFSVolumeHelper.synchronizeWithFlags_replyHandler_, 0, objc._C_NSInteger
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.synchronizeWithFlags_replyHandler_, 1, b"v@"
        )

        self.assertArgIsBlock(
            TestFSVolumeHelper.getAttributes_ofItem_replyHandler_,
            2,
            b"v@@",
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.setAttributes_onItem_replyHandler_,
            2,
            b"v@@",
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.lookupItemNamed_inDirectory_replyHandler_, 2, b"v@@@"
        )
        self.assertArgIsBlock(TestFSVolumeHelper.reclaimItem_replyHandler_, 1, b"v@")
        self.assertArgIsBlock(
            TestFSVolumeHelper.readSymbolicLink_replyHandler_, 1, b"v@@"
        )

        self.assertArgHasType(
            TestFSVolumeHelper.createItemNamed_type_inDirectory_attributes_replyHandler_,
            1,
            objc._C_NSInteger,
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.createItemNamed_type_inDirectory_attributes_replyHandler_,
            4,
            b"v@@@",
        )

        self.assertArgIsBlock(
            TestFSVolumeHelper.createSymbolicLinkNamed_inDirectory_attributes_linkContents_replyHandler_,
            4,
            b"v@@@",
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.createLinkToItem_named_inDirectory_replyHandler_,
            3,
            b"v@@",
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.removeItem_named_fromDirectory_replyHandler_, 3, b"v@"
        )

        self.assertArgIsBlock(
            TestFSVolumeHelper.renameItem_inDirectory_named_toNewName_inDirectory_overItem_replyHandler_,
            6,
            b"v@@",
        )

        self.assertArgHasType(
            TestFSVolumeHelper.enumerateDirectory_startingAtCookie_verifier_providingAttributes_usingPacker_replyHandler_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestFSVolumeHelper.enumerateDirectory_startingAtCookie_verifier_providingAttributes_usingPacker_replyHandler_,
            2,
            b"Q",
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.enumerateDirectory_startingAtCookie_verifier_providingAttributes_usingPacker_replyHandler_,
            5,
            b"vQ@",
        )

        self.assertArgIsBlock(
            TestFSVolumeHelper.activateWithOptions_replyHandler_, 1, b"v@@"
        )

        self.assertArgIsBlock(
            TestFSVolumeHelper.deactivateWithOptions_replyHandler_, 1, b"v@"
        )

        self.assertResultIsBOOL(TestFSVolumeHelper.enableOpenUnlinkEmulation)
        self.assertArgIsBOOL(TestFSVolumeHelper.setEnableOpenUnlinkEmulation_, 0)

        # FSVolumeXattrOperations
        self.assertResultIsBOOL(TestFSVolumeHelper.xattrOperationsInhibited)
        self.assertArgIsBOOL(TestFSVolumeHelper.setXattrOperationsInhibited_, 0)

        self.assertArgIsBlock(
            TestFSVolumeHelper.getXattrNamed_ofItem_replyHandler_, 2, b"v@@"
        )

        self.assertArgHasType(
            TestFSVolumeHelper.setXattrNamed_toData_onItem_policy_replyHandler_,
            3,
            objc._C_NSUInteger,
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.setXattrNamed_toData_onItem_policy_replyHandler_,
            4,
            b"v@",
        )

        self.assertArgIsBlock(
            TestFSVolumeHelper.listXattrsOfItem_replyHandler_, 1, b"v@@"
        )

        # FSVolumeOpenCloseOperations
        self.assertResultIsBOOL(TestFSVolumeHelper.isOpenCloseInhibited)
        self.assertArgIsBOOL(TestFSVolumeHelper.setOpenCloseInhibited_, 0)

        self.assertArgHasType(
            TestFSVolumeHelper.openItem_withModes_replyHandler_, 1, objc._C_NSUInteger
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.openItem_withModes_replyHandler_, 2, b"v@"
        )

        self.assertArgHasType(
            TestFSVolumeHelper.closeItem_keepingModes_replyHandler_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.closeItem_keepingModes_replyHandler_, 2, b"v@"
        )

        # FSVolumeReadWriteOperations
        self.assertArgHasType(
            TestFSVolumeHelper.readFromFile_offset_length_intoBuffer_replyHandler_,
            1,
            b"q",
        )
        self.assertArgHasType(
            TestFSVolumeHelper.readFromFile_offset_length_intoBuffer_replyHandler_,
            2,
            b"Q",
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.readFromFile_offset_length_intoBuffer_replyHandler_,
            4,
            b"vQ@",
        )

        self.assertArgHasType(
            TestFSVolumeHelper.writeContents_toFile_atOffset_replyHandler_, 2, b"q"
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.writeContents_toFile_atOffset_replyHandler_, 3, b"vQ@"
        )

        # FSVolumeAccessCheckOperations
        self.assertResultIsBOOL(TestFSVolumeHelper.isAccessCheckInhibited)
        self.assertArgIsBOOL(TestFSVolumeHelper.setAccessCheckInhibited_, 0)

        self.assertArgHasType(
            TestFSVolumeHelper.checkAccessToItem_requestedAccess_replyHandler_, 1, b"Q"
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.checkAccessToItem_requestedAccess_replyHandler_,
            2,
            b"vZ@",
        )

        # FSVolumeRenameOperations
        self.assertResultIsBOOL(TestFSVolumeHelper.isVolumeRenameInhibited)
        self.assertArgIsBOOL(TestFSVolumeHelper.setVolumeRenameInhibited_, 0)

        self.assertArgIsBlock(TestFSVolumeHelper.setVolumeName_replyHandler_, 1, b"v@@")

        # FSVolumePreallocateOperations
        self.assertResultIsBOOL(TestFSVolumeHelper.isPreallocateInhibited)
        self.assertArgIsBOOL(TestFSVolumeHelper.setPreallocateInhibited_, 0)
        self.assertArgHasType(
            TestFSVolumeHelper.preallocateSpaceForItem_atOffset_length_flags_replyHandler_,
            1,
            b"q",
        )
        self.assertArgHasType(
            TestFSVolumeHelper.preallocateSpaceForItem_atOffset_length_flags_replyHandler_,
            2,
            b"Q",
        )
        self.assertArgHasType(
            TestFSVolumeHelper.preallocateSpaceForItem_atOffset_length_flags_replyHandler_,
            3,
            b"Q",
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.preallocateSpaceForItem_atOffset_length_flags_replyHandler_,
            4,
            b"vQ@",
        )

        # FSVolumeItemDeactivation
        self.assertResultHasType(TestFSVolumeHelper.itemDeactivationPolicy, b"Q")
        self.assertArgIsBlock(TestFSVolumeHelper.deactivateItem_replyHandler_, 1, b"v@")

    def test_methods(self):
        self.assertResultIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.supportsPersistentObjectIDs
        )
        self.assertArgIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.setSupportsPersistentObjectIDs_, 0
        )

        self.assertResultIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.supportsSymbolicLinks
        )
        self.assertArgIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.setSupportsSymbolicLinks_, 0
        )

        self.assertResultIsBOOL(FSKit.FSVolumeSupportedCapabilities.supportsHardLinks)
        self.assertArgIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.setSupportsHardLinks_, 0
        )

        self.assertResultIsBOOL(FSKit.FSVolumeSupportedCapabilities.supportsJournal)
        self.assertArgIsBOOL(FSKit.FSVolumeSupportedCapabilities.setSupportsJournal_, 0)

        self.assertResultIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.supportsActiveJournal
        )
        self.assertArgIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.setSupportsActiveJournal_, 0
        )

        self.assertResultIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.doesNotSupportRootTimes
        )
        self.assertArgIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.setDoesNotSupportRootTimes_, 0
        )

        self.assertResultIsBOOL(FSKit.FSVolumeSupportedCapabilities.supportsSparseFiles)
        self.assertArgIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.setSupportsSparseFiles_, 0
        )

        self.assertResultIsBOOL(FSKit.FSVolumeSupportedCapabilities.supportsZeroRuns)
        self.assertArgIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.setSupportsZeroRuns_, 0
        )

        self.assertResultIsBOOL(FSKit.FSVolumeSupportedCapabilities.supportsFastStatFS)
        self.assertArgIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.setSupportsFastStatFS_, 0
        )

        self.assertResultIsBOOL(FSKit.FSVolumeSupportedCapabilities.supports2TBFiles)
        self.assertArgIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.setSupports2TBFiles_, 0
        )

        self.assertResultIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.supportsOpenDenyModes
        )
        self.assertArgIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.setSupportsOpenDenyModes_, 0
        )

        self.assertResultIsBOOL(FSKit.FSVolumeSupportedCapabilities.supportsHiddenFiles)
        self.assertArgIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.setSupportsHiddenFiles_, 0
        )

        self.assertResultIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.doesNotSupportVolumeSizes
        )
        self.assertArgIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.setDoesNotSupportVolumeSizes_, 0
        )

        self.assertResultIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.supports64BitObjectIDs
        )
        self.assertArgIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.setSupports64BitObjectIDs_, 0
        )

        self.assertResultIsBOOL(FSKit.FSVolumeSupportedCapabilities.supportsDocumentID)
        self.assertArgIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.setSupportsDocumentID_, 0
        )

        self.assertResultIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.doesNotSupportImmutableFiles
        )
        self.assertArgIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.setDoesNotSupportImmutableFiles_, 0
        )

        self.assertResultIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.doesNotSupportSettingFilePermissions
        )
        self.assertArgIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.setDoesNotSupportSettingFilePermissions_,
            0,
        )

        self.assertResultIsBOOL(FSKit.FSVolumeSupportedCapabilities.supportsSharedSpace)
        self.assertArgIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.setSupportsSharedSpace_, 0
        )

        self.assertResultIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.supportsVolumeGroups
        )
        self.assertArgIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.setSupportsVolumeGroups_, 0
        )
