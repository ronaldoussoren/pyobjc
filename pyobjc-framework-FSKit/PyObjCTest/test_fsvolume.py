from PyObjCTools.TestSupport import TestCase

import FSKit
import objc

FSDirEntryPacker = b"i@CQQ@B"


class TestFSVolumeHelper(FSKit.NSObject):
    @objc.objc_method(selector=b"PC_LINK_MAX")
    def PC_LINK_MAX(self):
        return 1

    @objc.objc_method(selector=b"PC_NAME_MAX")
    def PC_NAME_MAX(self):
        return 1

    @objc.objc_method(selector=b"PC_CHOWN_RESTRICTED")
    def PC_CHOWN_RESTRICTED(self):
        return 1

    @objc.objc_method(selector=b"PC_NO_TRUNC")
    def PC_NO_TRUNC(self):
        return 1

    @objc.objc_method(selector=b"PC_CASE_SENSITIVE")
    def PC_CASE_SENSITIVE(self):
        return 1

    @objc.objc_method(selector=b"PC_CASE_PRESERVING")
    def PC_CASE_PRESERVING(self):
        return 1

    @objc.objc_method(selector=b"PC_XATTR_SIZE_BITS")
    def PC_XATTR_SIZE_BITS(self):
        return 1

    @objc.objc_method(selector=b"PC_FILESIZEBITS")
    def PC_FILESIZEBITS(self):
        return 1

    def setNewState_forced_replyHandler_(self, a, b, c):
        pass

    def mount_replyHandler_(self, a, b):
        pass

    def unmount_(self, a):
        pass

    def synchronize_(self, a):
        pass

    def getItemAttributes_requestedAttributes_replyHandler_(self, a, b, c):
        pass

    def setItemAttributes_requestedAttributes_replyHandler_(self, a, b, c):
        pass

    def lookupName_inDirectory_replyHandler_(self, a, b, c):
        pass

    def readSymbolicLink_replyHandler_(self, a, b):
        pass

    def reclaim_replyHandler_(self, a, b):
        pass

    def createItemNamed_type_inDirectory_attributes_replyHandler_(self, a, b, c, d, e):
        pass

    def createSymbolicLinkNamed_inDirectory_attributes_linkContents_replyHandler_(
        self, a, b, c, d, e
    ):
        pass

    def createLinkof_named_inDirectory_replyHandler_(self, a, b, c, d):
        pass

    def removeItem_named_fromDirectory_replyHandler_(self, a, b, c, d):
        pass

    def renameItem_inDirectory_named_toDirectory_newName_overItem_withOptions_replyHandler_(
        self, a, b, c, d, e, f, g, h
    ):
        pass

    def enumerateDirectory_startingAtCookie_verifier_provideAttributes_attributes_usingBlock_replyHandler_(
        self,
        a,
        b,
        c,
        d,
        e,
        f,
        g,
    ):
        pass

    def activate_replyHandler_(self, a, b):
        pass

    def deactivate_replyHandler_(self, a, b):
        pass

    def otherAttributeNamed_of_replyHandler_(self, a, b, c):
        pass

    def setOtherAttributeNamed_of_with_replyHandler_(self, a, b, c, d):
        pass

    def xattrOperationsInhibited(self):
        return 1

    def setXattrOperationsInhibited_(self, a):
        pass

    def xattrOf_named_replyHandler_(self, a, b, c):
        pass

    def setXattrOf_named_value_how_replyHandler_(self, a, b, c, d, e):
        pass

    def listXattrsOf_replyHandler_(self, a, b):
        pass

    def limitedXattrOperationsInhibited(self):
        return 1

    def setLimitedXattrOperationsInhibited_(self, a):
        return 1

    def supportedXattrNamesOf_(self, a):
        pass

    # def xattrOf_named_replyHandler_(self, a, b, c):
    #    pass

    # def setXattrOf_named_value_how_replyHandler_(self, a, b, c, d):
    #    pass

    # def listXattrsOf_replyHandler_(self, a, b):
    #    pass

    def openItem_withMode_replyHandler_(self, a, b, c):
        pass

    def closeItem_keepingMode_replyHandler_(self, a, b, c):
        pass

    def readFromFile_offset_length_buffer_replyHandler_(self, a, b, c, d, e):
        pass

    def writeToFile_offset_buffer_replyHandler_(self, a, b, c, d):
        pass

    def checkAccessTo_requestedAccess_replyHandler_(self, a, b, c):
        pass

    def makeCloneOf_inDirectory_named_attributes_usingFlags_replyHandler_(
        self, a, b, c, d, e, f
    ):
        pass

    def renameOperationsInhibited(self):
        return 1

    def setRenameOperationsInhibited_(self, a):
        return 1

    def renameVolume_replyHandler_(self, a, b):
        pass


class TestFSVolume(TestCase):
    def test_enum(self):
        self.assertIsEnumType(FSKit.FSVolumeState)
        self.assertEqual(FSKit.FSVolumeNotReady, 0)
        self.assertEqual(FSKit.FSVolumeReady, 1)
        self.assertEqual(FSKit.FSVolumeActive, 2)

        self.assertIsEnumType(FSKit.FSKitAccessMask)
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

        self.assertIsEnumType(FSKit.FSKitXattrCreateRequirementAndFlags)
        self.assertEqual(FSKit.FSVolumeMustCreateXattr, 0x0002)
        self.assertEqual(FSKit.FSVolumeMustReplaceXattr, 0x0004)
        self.assertEqual(FSKit.FSVolumeAlwaysSetXattr, 0x0006)
        self.assertEqual(FSKit.FSVolumeDeleteXattr, 0x0008)

        self.assertIsEnumType(FSKit.FSKitBlockmapFlags)
        self.assertEqual(FSKit.FSBlockmapRead, 0x000100)
        self.assertEqual(FSKit.FSBlockmapWrite, 0x000200)
        self.assertEqual(FSKit.FSBlockmapAsync, 0x000400)
        self.assertEqual(FSKit.FSBlockmapNoCache, 0x000800)
        self.assertEqual(FSKit.FSBlockmapFileIssued, 0x001000)

        self.assertIsEnumType(FSKit.FSKitPreallocateFlags)
        self.assertEqual(FSKit.FSPreallocateAll, 0x00000002)
        self.assertEqual(FSKit.FSPreallocateContig, 0x00000004)
        self.assertEqual(FSKit.FSPreallocateFromEOF, 0x00000010)
        self.assertEqual(FSKit.FSPreallocateFromVol, 0x00000020)

        self.assertIsEnumType(FSKit.FSRenameItemOptions)
        self.assertEqual(FSKit.FSRenameItemOptionReserved, 1)

    def test_protocols(self):
        self.assertProtocolExists("FSVolumePathConfOperations")
        self.assertProtocolExists("FSVolumeOperations")
        self.assertProtocolExists("FSVolumeXattrOperations")
        self.assertProtocolExists("FSVolumeLimitedXattrOperations")
        self.assertProtocolExists("FSVolumeOpenCloseOperations")
        self.assertProtocolExists("FSVolumeReadWriteOperations")
        self.assertProtocolExists("FSVolumeAccessCheckOperations")
        self.assertProtocolExists("FSVolumeCloneOperations")
        self.assertProtocolExists("FSVolumeRenameOperations")

    def test_protocol_methods(self):
        self.assertResultHasType(TestFSVolumeHelper.PC_LINK_MAX, objc._C_INT)
        self.assertResultHasType(TestFSVolumeHelper.PC_NAME_MAX, objc._C_INT)
        self.assertResultHasType(TestFSVolumeHelper.PC_CHOWN_RESTRICTED, objc._C_INT)
        self.assertResultHasType(TestFSVolumeHelper.PC_NO_TRUNC, objc._C_INT)
        self.assertResultHasType(TestFSVolumeHelper.PC_CASE_SENSITIVE, objc._C_INT)
        self.assertResultHasType(TestFSVolumeHelper.PC_CASE_PRESERVING, objc._C_INT)
        self.assertResultHasType(TestFSVolumeHelper.PC_XATTR_SIZE_BITS, objc._C_INT)
        self.assertResultHasType(TestFSVolumeHelper.PC_FILESIZEBITS, objc._C_INT)

        self.assertArgHasType(
            TestFSVolumeHelper.setNewState_forced_replyHandler_, 1, objc._C_BOOL
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.setNewState_forced_replyHandler_, 2, b"vi@"
        )

        self.assertArgIsBlock(TestFSVolumeHelper.mount_replyHandler_, 1, b"v@@")
        self.assertArgIsBlock(TestFSVolumeHelper.unmount_, 0, b"v")
        self.assertArgIsBlock(TestFSVolumeHelper.synchronize_, 0, b"v@")
        self.assertArgIsBlock(
            TestFSVolumeHelper.getItemAttributes_requestedAttributes_replyHandler_,
            2,
            b"v@@",
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.setItemAttributes_requestedAttributes_replyHandler_,
            2,
            b"v@@",
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.lookupName_inDirectory_replyHandler_, 2, b"v@@"
        )
        self.assertArgIsBlock(TestFSVolumeHelper.reclaim_replyHandler_, 1, b"v@")
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
            TestFSVolumeHelper.createLinkof_named_inDirectory_replyHandler_, 3, b"v@"
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.removeItem_named_fromDirectory_replyHandler_, 3, b"v@"
        )

        self.assertArgHasType(
            TestFSVolumeHelper.renameItem_inDirectory_named_toDirectory_newName_overItem_withOptions_replyHandler_,
            6,
            b"Q",
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.renameItem_inDirectory_named_toDirectory_newName_overItem_withOptions_replyHandler_,
            7,
            b"v@",
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

        self.assertArgIsBlock(TestFSVolumeHelper.activate_replyHandler_, 1, b"v@@")

        self.assertArgHasType(TestFSVolumeHelper.deactivate_replyHandler_, 0, b"Q")
        self.assertArgIsBlock(TestFSVolumeHelper.deactivate_replyHandler_, 1, b"v@")

        self.assertArgIsBlock(
            TestFSVolumeHelper.otherAttributeNamed_of_replyHandler_, 2, b"v@@"
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.setOtherAttributeNamed_of_with_replyHandler_, 3, b"v@@"
        )

        self.assertResultHasType(TestFSVolumeHelper.xattrOperationsInhibited, b"B")
        self.assertArgHasType(TestFSVolumeHelper.setXattrOperationsInhibited_, 0, b"B")

        self.assertArgIsBlock(TestFSVolumeHelper.xattrOf_named_replyHandler_, 2, b"v@@")

        self.assertArgHasType(
            TestFSVolumeHelper.setXattrOf_named_value_how_replyHandler_, 3, b"I"
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.setXattrOf_named_value_how_replyHandler_, 4, b"v@"
        )

        self.assertArgIsBlock(TestFSVolumeHelper.listXattrsOf_replyHandler_, 1, b"v@@")

        self.assertResultHasType(
            TestFSVolumeHelper.limitedXattrOperationsInhibited, b"B"
        )
        self.assertArgHasType(
            TestFSVolumeHelper.setLimitedXattrOperationsInhibited_, 0, b"B"
        )

        self.assertArgIsBlock(TestFSVolumeHelper.xattrOf_named_replyHandler_, 2, b"v@@")

        self.assertArgHasType(
            TestFSVolumeHelper.setXattrOf_named_value_how_replyHandler_, 3, b"I"
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.setXattrOf_named_value_how_replyHandler_, 4, b"v@"
        )

        self.assertArgIsBlock(TestFSVolumeHelper.listXattrsOf_replyHandler_, 1, b"v@@")

        self.assertArgHasType(
            TestFSVolumeHelper.openItem_withMode_replyHandler_, 1, b"i"
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.openItem_withMode_replyHandler_, 2, b"v@"
        )

        self.assertArgHasType(
            TestFSVolumeHelper.closeItem_keepingMode_replyHandler_, 1, b"i"
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.closeItem_keepingMode_replyHandler_, 2, b"v@"
        )

        self.assertArgHasType(
            TestFSVolumeHelper.readFromFile_offset_length_buffer_replyHandler_, 1, b"Q"
        )
        self.assertArgHasType(
            TestFSVolumeHelper.readFromFile_offset_length_buffer_replyHandler_, 2, b"Q"
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.readFromFile_offset_length_buffer_replyHandler_,
            4,
            b"vQ@",
        )

        self.assertArgHasType(
            TestFSVolumeHelper.writeToFile_offset_buffer_replyHandler_, 1, b"Q"
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.writeToFile_offset_buffer_replyHandler_, 3, b"vQ@"
        )

        self.assertArgHasType(
            TestFSVolumeHelper.checkAccessTo_requestedAccess_replyHandler_, 1, b"I"
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.checkAccessTo_requestedAccess_replyHandler_, 2, b"vi@"
        )

        self.assertArgHasType(
            TestFSVolumeHelper.makeCloneOf_inDirectory_named_attributes_usingFlags_replyHandler_,
            4,
            b"I",
        )
        self.assertArgIsBlock(
            TestFSVolumeHelper.makeCloneOf_inDirectory_named_attributes_usingFlags_replyHandler_,
            5,
            b"v@@",
        )

        self.assertResultHasType(TestFSVolumeHelper.renameOperationsInhibited, b"B")
        self.assertArgHasType(TestFSVolumeHelper.setRenameOperationsInhibited_, 0, b"B")

        self.assertArgIsBlock(TestFSVolumeHelper.renameVolume_replyHandler_, 1, b"v@@")
