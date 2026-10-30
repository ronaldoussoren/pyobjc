from PyObjCTools.TestSupport import TestCase, min_sdk_level

import FSKit


class TestFSVolumeExtentHelper(FSKit.NSObject):
    # FSVolumeKernelOffloadedIOOperations
    def blockmapFile_offset_length_flags_operationID_packer_replyHandler_(
        self, a, b, c, d, e, f, g
    ):
        pass

    def completeIOForFile_offset_length_status_flags_operationID_replyHandler_(
        self, a, b, c, d, e, f, g
    ):
        pass

    def createFileNamed_inDirectory_attributes_packer_replyHandler_(
        self, a, b, c, d, e
    ):
        pass

    def lookupItemNamed_inDirectory_packer_replyHandler_(self, a, b, c, d):
        pass

    def preallocateSpaceForFile_atOffset_length_flags_packer_replyHandler_(
        self, a, b, c, d, e, f
    ):
        pass

    # FSVolumeKernelOffloadedIOHandler
    # blockmapFile_offset_length_flags_operationID_packer_replyHandler_ (see above)
    # completeIOForFile_offset_length_status_flags_operationID_replyHandler_ (see above)
    def createFileNamed_inDirectory_attributes_packer_context_replyHandler_(
        self, a, b, c, d, e, f
    ):
        pass

    def lookupItemNamed_inDirectory_packer_context_replyHandler_(self, a, b, c, d, e):
        pass

    def preallocateSpaceForFile_atOffset_length_flags_packer_context_replyHandler_(
        self, a, b, c, d, e, f, g
    ):
        pass


class TestFSVolumeExtent(TestCase):
    def test_enums(self):
        self.assertIsEnumType(FSKit.FSBlockmapFlags)
        self.assertEqual(FSKit.FSBlockmapFlagsRead, 0x000100)
        self.assertEqual(FSKit.FSBlockmapFlagsWrite, 0x000200)

        self.assertIsEnumType(FSKit.FSCompleteIOFlags)
        self.assertEqual(FSKit.FSCompleteIOFlagsRead, FSKit.FSBlockmapFlagsRead)
        self.assertEqual(FSKit.FSCompleteIOFlagsWrite, FSKit.FSBlockmapFlagsWrite)
        self.assertEqual(FSKit.FSCompleteIOFlagsAsync, 0x000400)

        self.assertIsEnumType(FSKit.FSExtentType)
        self.assertEqual(FSKit.FSExtentTypeData, 0)
        self.assertEqual(FSKit.FSExtentTypeZeroFill, 1)
        self.assertEqual(FSKit.FSExtentTypeReadOnly, 2)

    def test_protocols(self):
        self.assertProtocolExists("FSVolumeKernelOffloadedIOOperations", FSKit)

    @min_sdk_level("27.0")
    def test_protocols27_0(self):
        self.assertProtocolExists("FSVolumeKernelOffloadedIOHandler", FSKit)

    def test_protocol_methods(self):
        with self.subTest("FSVolumeKernelOffloadedIOOperations"):
            self.assertArgHasType(
                TestFSVolumeExtentHelper.blockmapFile_offset_length_flags_operationID_packer_replyHandler_,
                1,
                b"q",
            )
            self.assertArgHasType(
                TestFSVolumeExtentHelper.blockmapFile_offset_length_flags_operationID_packer_replyHandler_,
                2,
                b"Q",
            )
            self.assertArgHasType(
                TestFSVolumeExtentHelper.blockmapFile_offset_length_flags_operationID_packer_replyHandler_,
                3,
                b"Q",
            )
            self.assertArgHasType(
                TestFSVolumeExtentHelper.blockmapFile_offset_length_flags_operationID_packer_replyHandler_,
                4,
                b"Q",
            )
            # XXX: macOS 27 introduced a new protocol with the same selector but different types
            # self.assertArgIsBlock(
            #    TestFSVolumeExtentHelper.blockmapFile_offset_length_flags_operationID_packer_replyHandler_,
            #    6,
            #    b"v@",
            # )

            self.assertArgHasType(
                TestFSVolumeExtentHelper.completeIOForFile_offset_length_status_flags_operationID_replyHandler_,
                1,
                b"q",
            )
            self.assertArgHasType(
                TestFSVolumeExtentHelper.completeIOForFile_offset_length_status_flags_operationID_replyHandler_,
                2,
                b"Q",
            )
            self.assertArgHasType(
                TestFSVolumeExtentHelper.completeIOForFile_offset_length_status_flags_operationID_replyHandler_,
                4,
                b"Q",
            )
            self.assertArgHasType(
                TestFSVolumeExtentHelper.completeIOForFile_offset_length_status_flags_operationID_replyHandler_,
                5,
                b"Q",
            )
            # XXX: macOS 27 introduced a new protocol with the same selector but different types
            # self.assertArgIsBlock(
            #    TestFSVolumeExtentHelper.completeIOForFile_offset_length_status_flags_operationID_replyHandler_,
            #    6,
            #    b"v@",
            # )

            self.assertArgIsBlock(
                TestFSVolumeExtentHelper.createFileNamed_inDirectory_attributes_packer_replyHandler_,
                4,
                b"v@@@",
            )

            self.assertArgIsBlock(
                TestFSVolumeExtentHelper.lookupItemNamed_inDirectory_packer_replyHandler_,
                3,
                b"v@@@",
            )

            self.assertArgHasType(
                TestFSVolumeExtentHelper.preallocateSpaceForFile_atOffset_length_flags_packer_replyHandler_,
                1,
                b"q",
            )
            self.assertArgHasType(
                TestFSVolumeExtentHelper.preallocateSpaceForFile_atOffset_length_flags_packer_replyHandler_,
                2,
                b"Q",
            )
            self.assertArgHasType(
                TestFSVolumeExtentHelper.preallocateSpaceForFile_atOffset_length_flags_packer_replyHandler_,
                3,
                b"Q",
            )
            self.assertArgIsBlock(
                TestFSVolumeExtentHelper.preallocateSpaceForFile_atOffset_length_flags_packer_replyHandler_,
                5,
                b"vQ@",
            )

        with self.subTest("FSVolumeKernelOffloadedIOHandler"):
            self.assertArgHasType(
                TestFSVolumeExtentHelper.blockmapFile_offset_length_flags_operationID_packer_replyHandler_,
                1,
                b"q",
            )
            self.assertArgHasType(
                TestFSVolumeExtentHelper.blockmapFile_offset_length_flags_operationID_packer_replyHandler_,
                2,
                b"Q",
            )
            self.assertArgHasType(
                TestFSVolumeExtentHelper.blockmapFile_offset_length_flags_operationID_packer_replyHandler_,
                3,
                b"Q",
            )
            self.assertArgHasType(
                TestFSVolumeExtentHelper.blockmapFile_offset_length_flags_operationID_packer_replyHandler_,
                4,
                b"Q",
            )
            self.assertArgIsBlock(
                TestFSVolumeExtentHelper.blockmapFile_offset_length_flags_operationID_packer_replyHandler_,
                6,
                b"v@@",
            )

            self.assertArgHasType(
                TestFSVolumeExtentHelper.completeIOForFile_offset_length_status_flags_operationID_replyHandler_,
                1,
                b"q",
            )
            self.assertArgHasType(
                TestFSVolumeExtentHelper.completeIOForFile_offset_length_status_flags_operationID_replyHandler_,
                2,
                b"Q",
            )
            self.assertArgHasType(
                TestFSVolumeExtentHelper.completeIOForFile_offset_length_status_flags_operationID_replyHandler_,
                4,
                b"Q",
            )
            self.assertArgHasType(
                TestFSVolumeExtentHelper.completeIOForFile_offset_length_status_flags_operationID_replyHandler_,
                5,
                b"Q",
            )
            self.assertArgIsBlock(
                TestFSVolumeExtentHelper.completeIOForFile_offset_length_status_flags_operationID_replyHandler_,
                6,
                b"v@@",
            )

            self.assertArgIsBlock(
                TestFSVolumeExtentHelper.createFileNamed_inDirectory_attributes_packer_context_replyHandler_,
                5,
                b"v@@",
            )

            self.assertArgIsBlock(
                TestFSVolumeExtentHelper.lookupItemNamed_inDirectory_packer_context_replyHandler_,
                4,
                b"v@@",
            )

            self.assertArgHasType(
                TestFSVolumeExtentHelper.preallocateSpaceForFile_atOffset_length_flags_packer_context_replyHandler_,
                1,
                b"q",
            )
            self.assertArgHasType(
                TestFSVolumeExtentHelper.preallocateSpaceForFile_atOffset_length_flags_packer_context_replyHandler_,
                2,
                b"Q",
            )
            self.assertArgHasType(
                TestFSVolumeExtentHelper.preallocateSpaceForFile_atOffset_length_flags_packer_context_replyHandler_,
                3,
                b"Q",
            )
            self.assertArgIsBlock(
                TestFSVolumeExtentHelper.preallocateSpaceForFile_atOffset_length_flags_packer_context_replyHandler_,
                6,
                b"v@@",
            )
