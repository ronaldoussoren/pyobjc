from PyObjCTools.TestSupport import TestCase

import FSKit
import objc

FSDirEntryPacker = b"Z@CQQ@Z"


class TestFSVolumeHelper(FSKit.NSObject):
    # FSVolumePathConfOperations
    def maxLinkCount(self):
        return 1

    def maxNameLength(self):
        return 1

    def isChownRestricted(self):
        return 1

    def isLongNameTruncated(self):
        return 1

    def maxXattrSizeInBits(self):
        return 1

    def maxFileSizeInBits(self):
        return 1

    # FSVolumeOperations
    def mountWithOptions_replyHandler_(self, a, b):
        pass

    def unmountWithReplyHandler_(self, a):
        pass

    def synchronizeWithReplyHandler_(self, a):
        pass

    def getAttributes_ofItem_replyHandler_(self, a, b, c):
        pass

    def setAttributes_onItem_replyNadler_(self, a, b, c):
        pass

    def lookupName_inDirectory_replyHandler_(self, a, b, c):
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

    def enumerateDirectory_startingAtCookie_verifier_provideAttributes_usingBlock_replyHandler_(
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

    def xattrNamed_ofItem_replyHandler(self, a, b, c):
        pass

    def setXattrNamed_toData_onItem_policy_replyHandler_(self, a, b, c, d, e):
        pass

    def listXattrsOfItem_replyHandler_(self, a, b):
        pass

    # FSVolumeOpenCloseOperations
    def openItem_withMode_replyHandler_(self, a, b, c):
        pass

    def closeItem_keepingMode_replyHandler_(self, a, b, c):
        pass

    # FSVolumeReadWriteOperations
    def readFromFile_offset_length_intoBuffer_replyHandler_(self, a, b, c, d, e):
        pass

    def writeContents_toFile_atOffset_replyHandler_(self, a, b, c, d):
        pass

    # FSVolumeAccessCheckOperations
    def accessCheckOperationsInhibited(self):
        return 1

    def setAccessCheckOperationsInhibited_(self, a):
        pass

    def checkAccessTo_requestedAccess_replyHandler_(self, a, b, c):
        pass

    # FSVolumeRenameOperations
    def volumeRenameOperationsInhibited(self):
        return 1

    def setVolumeRenameOperationsInhibited_(self, a):
        pass

    def setVolumeName_replyHandler_(self, a, b):
        pass


class TestFSVolume(TestCase):
    def test_enum(self):
        self.assertIsInstance(FSKit.FSDirectoryCookieInitial, int)
        self.assertIsInstance(FSKit.FSDirectoryVerifierInitial, int)
        self.assertIsInstance(FSKit.FSVolumeErrorDomain, str)

        self.assertIsEnumType(FSKit.FSVolumeErrorCode)
        self.assertEqual(FSKit.FSDeactivateOptionsForce, 1 << 0)

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
        self.assertEqual(FSKit.FSAccessReadExtAttributes, 1 << 9)
        self.assertEqual(FSKit.FSAccessWriteExtAttributes, 1 << 10)
        self.assertEqual(FSKit.FSAccessReadSecurity, 1 << 11)
        self.assertEqual(FSKit.FSAccessWriteSecurity, 1 << 12)
        self.assertEqual(FSKit.FSAccessTakeOwnership, 1 << 13)

    def test_protocols(self):
        self.assertProtocolExists("FSVolumePathConfOperations")
        self.assertProtocolExists("FSVolumeOperations")
        self.assertProtocolExists("FSVolumeXattrOperations")
        self.assertProtocolExists("FSVolumeOpenCloseOperations")
        self.assertProtocolExists("FSVolumeReadWriteOperations")
        self.assertProtocolExists("FSVolumeAccessCheckOperations")
        self.assertProtocolExists("FSVolumeRenameOperations")

    def test_protocol_methods(self):
        # FSVolumePathConfOperations
        self.assertResultHasType(TestFSVolumeHelper.maxLinkCount, objc._C_INT)
        self.assertResultHasType(TestFSVolumeHelper.maxNameLength, objc._C_INT)
        self.assertResultIsBOOL(TestFSVolumeHelper.chownRestricted)
        self.assertResultIsBOOL(TestFSVolumeHelper.longNameTruncated)
        self.assertResultHasType(TestFSVolumeHelper.maxXattrSizeInBits, objc._C_INT)
        self.assertResultHasType(TestFSVolumeHelper.maxFileSizeInBits, objc._C_INT)

        # FSVolumeOperations

        self.assertArgIsBlock(
            TestFSVolumeHelper.mountWithOptions_replyHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(TestFSVolumeHelper.unmountWithReplyHandler_, 0, b"v")
        self.assertArgIsBlock(TestFSVolumeHelper.synchronizeWithReplyHandler_, 0, b"v@")
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
            TestFSVolumeHelper.lookupName_inDirectory_replyHandler_, 2, b"v@@"
        )
        self.assertArgIsBlock(TestFSVolumeHelper.reclaimItem_replyHandler_, 1, b"v@")
        self.assertArgIsBlock(
            TestFSVolumeHelper.readSymbolicLink_replyHandler_, 1, b"v@@"
        )

        self.assertArgHasType(
            TestFSVolumeHelper.createItemNamed_type_inDirectory_attributes_replyHandler_,
            1,
            b"C",
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.createItemNamed_type_inDirectory_attributes_replyHandler_,
            4,
            b"v@@",
        )

        self.assertArgIsBlock(
            TestFSVolumeHelper.createSymbolicLinkNamed_inDirectory_attributes_linkContents_replyHandler_,
            4,
            b"v@@",
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.createLinkToItem_named_inDirectory_replyHandler_,
            3,
            b"v@",
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.removeItem_named_fromDirectory_replyHandler_, 3, b"v@"
        )

        self.assertArgIsBlock(
            TestFSVolumeHelper.renameItem_inDirectory_named_toNewName_inDirectory_overItem_withOptions_replyHandler_,
            6,
            b"v@@",
        )

        self.assertArgHasType(
            TestFSVolumeHelper.enumerateDirectory_startingAtCookie_verifier_provideAttributes_attributes_usingBlock_replyHandler_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestFSVolumeHelper.enumerateDirectory_startingAtCookie_verifier_provideAttributes_attributes_usingBlock_replyHandler_,
            2,
            b"Q",
        )
        self.assertArgHasType(
            TestFSVolumeHelper.enumerateDirectory_startingAtCookie_verifier_provideAttributes_attributes_usingBlock_replyHandler_,
            3,
            b"B",
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.enumerateDirectory_startingAtCookie_verifier_provideAttributes_attributes_usingBlock_replyHandler_,
            5,
            FSDirEntryPacker,
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.enumerateDirectory_startingAtCookie_verifier_provideAttributes_attributes_usingBlock_replyHandler_,
            6,
            b"vQ@",
        )

        self.assertArgIsBlock(
            TestFSVolumeHelper.activateWithOptions_replyHandler_, 1, b"v@@"
        )

        self.assertArgHasType(
            TestFSVolumeHelper.deactivateWithOptions_replyHandler_, 0, b"Q"
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.deactivateWithOptions_replyHandler_, 1, b"v@"
        )

        # FSVolumeXattrOperations
        self.assertResultHasType(TestFSVolumeHelper.xattrOperationsInhibited, b"B")
        self.assertArgHasType(TestFSVolumeHelper.setXattrOperationsInhibited_, 0, b"B")

        self.assertArgIsBlock(
            TestFSVolumeHelper.xattrNamed_ofItem_replyHandler_, 2, b"v@@"
        )

        self.assertArgHasType(
            TestFSVolumeHelper.setXAttrNamed_toData_onItem_policy_replyHandler_, 3, b"I"
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.setXAttrNamed_toData_onItem_policy_replyHandler_,
            4,
            b"v@",
        )

        self.assertArgIsBlock(
            TestFSVolumeHelper.listXattrsOfItem_replyHandler_, 1, b"v@@"
        )

        # FSVolumeOpenCloseOperations
        self.assertArgHasType(
            TestFSVolumeHelper.openItem_withModes_replyHandler_, 1, b"i"
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.openItem_withModes_replyHandler_, 2, b"v@"
        )

        self.assertArgHasType(
            TestFSVolumeHelper.closeItem_keepingModes_replyHandler_, 1, b"i"
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.closeItem_keepingModes_replyHandler_, 2, b"v@"
        )

        # FSVolumeReadWriteOperations
        self.assertArgHasType(
            TestFSVolumeHelper.readFromFile_offset_length_intoBuffer_replyHandler_,
            1,
            b"Q",
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
            TestFSVolumeHelper.writeContents_toFile_atOffset_replyHandler_, 2, b"Q"
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.writeContents_toFile_atOffset_replyHandler_, 3, b"vQ@"
        )

        # FSVolumeAccessCheckOperations
        self.assertResultIsBOOL(TestFSVolumeHelper.accessCheckOperationsInhibited)
        self.assertArgIsBOOL(TestFSVolumeHelper.setAccessCheckOperationsInhibited_, 0)

        self.assertArgHasType(
            TestFSVolumeHelper.checkAccessToItem_requestedAccess_replyHandler_, 1, b"I"
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.checkAccessToItem_requestedAccess_replyHandler_,
            2,
            b"vi@",
        )

        # FSVolumeRenameOperations
        self.assertResultHasType(
            TestFSVolumeHelper.volumeRenameOperationsInhibited, b"B"
        )
        self.assertArgHasType(
            TestFSVolumeHelper.setVolumeRenameOperationsInhibited_, 0, b"B"
        )

        self.assertArgIsBlock(TestFSVolumeHelper.setVolumeName_replyHandler_, 1, b"v@@")

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

        self.assertResultIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.supportsCaseSensitiveNames
        )
        self.assertArgIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.setSupportsCaseSensitiveNames_, 0
        )

        self.assertResultIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.supportsCasePreservingNames
        )
        self.assertArgIsBOOL(
            FSKit.FSVolumeSupportedCapabilities.setSupportsCasePreservingNames_, 0
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
