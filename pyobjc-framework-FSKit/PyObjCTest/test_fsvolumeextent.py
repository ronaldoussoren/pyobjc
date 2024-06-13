from PyObjCTools.TestSupport import TestCase

import FSKit

FSExtentPacker = b"i@iQQI"


class TestFSVolumeExtentHelper(FSKit.NSObject):
    def blockmapFile_range_startIO_flags_operationID_usingPacker_replyHandler_(
        self, a, b, c, d, e, f, g
    ):
        pass

    def endIO_range_status_flags_operationID_replyHandler_(self, a, b, c, d, e, f):
        pass

    def createItemNamed_type_inDirectory_attributes_usingPacker_replyHandler_(
        self, a, b, c, d, e, f
    ):
        pass

    def lookupName_inDirectory_usingPacker_replyHandler_(self, a, b, c, d):
        pass

    def preallocate_offset_length_flags_usingPacker_replyHandler_(
        self, a, b, c, d, e, f
    ):
        pass


class TestFSVolumeExtent(TestCase):
    def test_enum(self):
        self.assertIsEnumType(FSKit.FSExtentType)
        self.assertEqual(FSKit.FSExtentTypeData, 0)
        self.assertEqual(FSKit.FSExtentTypeZero, 1)

    def test_protocols(self):
        self.assertProtocolExists("FSVolumeKernelOffloadedIOOperations")
        self.assertProtocolExists("FSVolumePreallocateOperations")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestFSVolumeExtentHelper.blockmapFile_range_startIO_flags_operationID_usingPacker_replyHandler,
            1,
            FSKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestFSVolumeExtentHelper.blockmapFile_range_startIO_flags_operationID_usingPacker_replyHandler,
            2,
            b"B",
        )
        self.assertArgHasType(
            TestFSVolumeExtentHelper.blockmapFile_range_startIO_flags_operationID_usingPacker_replyHandler,
            3,
            b"I",
        )
        self.assertArgHasType(
            TestFSVolumeExtentHelper.blockmapFile_range_startIO_flags_operationID_usingPacker_replyHandler,
            4,
            b"Q",
        )
        self.assertArgIsBlock(
            TestFSVolumeExtentHelper.blockmapFile_range_startIO_flags_operationID_usingPacker_replyHandler,
            5,
            FSExtentPacker,
        )
        self.assertArgIsBlock(
            TestFSVolumeExtentHelper.blockmapFile_range_startIO_flags_operationID_usingPacker_replyHandler,
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
            2,
            b"i",
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
            TestFSVolumeExtentHelper.blockmapFile_range_startIO_flags_operationID_usingPacker_replyHandler,
            5,
            b"v@",
        )

        self.assertArgHasType(
            TestFSVolumeExtentHelper.createItemNamed_type_inDirectory_attributes_usingPacker_replyHandler_,
            1,
            b"C",
        )
        self.assertArgIsBlock(
            TestFSVolumeExtentHelper.createItemNamed_type_inDirectory_attributes_usingPacker_replyHandler_,
            4,
            FSExtentPacker,
        )
        self.assertArgIsBlock(
            TestFSVolumeExtentHelper.createItemNamed_type_inDirectory_attributes_usingPacker_replyHandler_,
            5,
            b"v@@",
        )

        self.assertArgIsBlock(
            TestFSVolumeExtentHelper.lookupName_inDirectory_usingPacker_replyHandler_,
            2,
            FSExtentPacker,
        )
        self.assertArgIsBlock(
            TestFSVolumeExtentHelper.createItemNamed_type_inDirectory_attributes_usingPacker_replyHandler_,
            3,
            b"v@@",
        )

        self.assertResultHasType(
            TestFSVolumeExtentHelper.preallocateOperationsInhibited, b"B"
        )
        self.assertArgHasType(
            TestFSVolumeExtentHelper.setRreallocateOperationsInhibited_, 0, b"B"
        )

        self.assertArgHasType(
            TestFSVolumeExtentHelper.preallocate_offset_length_flags_usingPacker_replyHandler_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestFSVolumeExtentHelper.preallocate_offset_length_flags_usingPacker_replyHandler_,
            2,
            b"Q",
        )
        self.assertArgHasType(
            TestFSVolumeExtentHelper.preallocate_offset_length_flags_usingPacker_replyHandler_,
            3,
            b"I",
        )
        self.assertArgIsBlock(
            TestFSVolumeExtentHelper.preallocate_offset_length_flags_usingPacker_replyHandler_,
            4,
            FSExtentPacker,
        )
        self.assertArgIsBlock(
            TestFSVolumeExtentHelper.preallocate_offset_length_flags_usingPacker_replyHandler_,
            5,
            b"vQ@",
        )
