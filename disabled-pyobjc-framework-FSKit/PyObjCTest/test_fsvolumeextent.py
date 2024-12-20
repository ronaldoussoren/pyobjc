from PyObjCTools.TestSupport import TestCase

import FSKit

FSExtentPacker = b"Z@iQQI"


class TestFSVolumeExtentHelper(FSKit.NSObject):
    # FSVolumeKernelOffloadedIOOperations
    def blockmapFile_range_startIO_flags_operationID_usingPacker_replyHandler_(
        self, a, b, c, d, e, f, g
    ):
        pass

    def endIO_range_status_flags_operationID_replyHandler_(self, a, b, c, d, e, f):
        pass

    def createFileNamed_inDirectory_attributes_usingPacker_replyHandler_(
        self, a, b, c, d, e
    ):
        pass

    def lookupItemNamed_inDirectory_usingPacker_replyHandler_(self, a, b, c, d):
        pass

    # FSVolumePreallocateOperations
    def isPreallocateInhibited(self):
        return 1

    def setPreallocateInhibited_(self, a):
        pass

    def preallocateSpaceForItem_offset_length_flags_usingPacker_replyHandler_(
        self, a, b, c, d, e, f
    ):
        pass


class TestFSVolumeExtent(TestCase):
    def test_enum(self):
        self.assertIsEnumType(FSKit.FSBlockmapFlags)
        self.assertEqual(FSKit.FSBlockmapFlagsRead, 0x000100)
        self.assertEqual(FSKit.FSBlockmapFlagsWrite, 0x000200)
        self.assertEqual(FSKit.FSBlockmapFlagsAsync, 0x000400)
        self.assertEqual(FSKit.FSBlockmapFlagsNoCache, 0x000800)
        self.assertEqual(FSKit.FSBlockmapFlagsFileIssued, 0x001000)

        self.assertIsEnumType(FSKit.FSExtentType)
        self.assertEqual(FSKit.FSExtentTypeData, 0)
        self.assertEqual(FSKit.FSExtentTypeZero, 1)

        self.assertIsEnumType(FSKit.FSPreallocateFlags)
        self.assertEqual(FSKit.FSPreallocateContig, 0x00000002)
        self.assertEqual(FSKit.FSPreallocateAll, 0x00000004)
        self.assertEqual(FSKit.FSPreallocateFromEOF, 0x00000010)
        self.assertEqual(FSKit.FSPreallocateFromVol, 0x00000020)

    def test_protocols(self):
        self.assertProtocolExists("FSVolumeKernelOffloadedIOOperations")
        self.assertProtocolExists("FSVolumePreallocateOperations")

    def test_protocol_methods(self):
        # FSVolumeKernelOffloadedIOOperations
        self.assertArgHasType(
            TestFSVolumeExtentHelper.blockmapFile_range_startIO_flags_operationID_usingPacker_replyHandler_,
            1,
            FSKit.NSRange.__typestr__,
        )
        self.assertArgIsBOOL(
            TestFSVolumeExtentHelper.blockmapFile_range_startIO_flags_operationID_usingPacker_replyHandler_,
            2,
        )
        self.assertArgHasType(
            TestFSVolumeExtentHelper.blockmapFile_range_startIO_flags_operationID_usingPacker_replyHandler_,
            3,
            b"I",
        )
        self.assertArgHasType(
            TestFSVolumeExtentHelper.blockmapFile_range_startIO_flags_operationID_usingPacker_replyHandler_,
            4,
            b"Q",
        )
        self.assertArgIsBlock(
            TestFSVolumeExtentHelper.blockmapFile_range_startIO_flags_operationID_usingPacker_replyHandler_,
            5,
            FSExtentPacker,
        )
        self.assertArgIsBlock(
            TestFSVolumeExtentHelper.blockmapFile_range_startIO_flags_operationID_usingPacker_replyHandler_,
            6,
            b"v@",
        )

        self.assertArgHasType(
            TestFSVolumeExtentHelper.endIO_range_status_flags_operationID_replyHandler_,
            1,
            FSKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestFSVolumeExtentHelper.endIO_range_status_flags_operationID_replyHandler_,
            3,
            b"I",
        )
        self.assertArgHasType(
            TestFSVolumeExtentHelper.endIO_range_status_flags_operationID_replyHandler_,
            4,
            b"Q",
        )
        self.assertArgIsBlock(
            TestFSVolumeExtentHelper.createFileNamed_inDirectory_attributes_usingPacker_replyHandler_,
            3,
            FSExtentPacker,
        )
        self.assertArgIsBlock(
            TestFSVolumeExtentHelper.createFileNamed_inDirectory_attributes_usingPacker_replyHandler_,
            4,
            b"v@@@",
        )

        self.assertArgIsBlock(
            TestFSVolumeExtentHelper.lookupItemNamed_inDirectory_usingPacker_replyHandler_,
            2,
            FSExtentPacker,
        )
        self.assertArgIsBlock(
            TestFSVolumeExtentHelper.lookupItemNamed_inDirectory_usingPacker_replyHandler_,
            3,
            b"v@@@",
        )

        # FSVolumePreallocateOperations
        self.assertResultIsBOOL(TestFSVolumeExtentHelper.isPreallocateInhibited)
        self.assertArgIsBOOL(TestFSVolumeExtentHelper.setPreallocateInhibited_, 0)

        self.assertArgHasType(
            TestFSVolumeExtentHelper.preallocateSpaceForItem_offset_length_flags_usingPacker_replyHandler_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestFSVolumeExtentHelper.preallocateSpaceForItem_offset_length_flags_usingPacker_replyHandler_,
            2,
            b"Q",
        )
        self.assertArgHasType(
            TestFSVolumeExtentHelper.preallocateSpaceForItem_offset_length_flags_usingPacker_replyHandler_,
            3,
            b"I",
        )
        self.assertArgIsBlock(
            TestFSVolumeExtentHelper.preallocateSpaceForItem_offset_length_flags_usingPacker_replyHandler_,
            4,
            FSExtentPacker,
        )
        self.assertArgIsBlock(
            TestFSVolumeExtentHelper.preallocateSpaceForItem_offset_length_flags_usingPacker_replyHandler_,
            5,
            b"vQ@",
        )
