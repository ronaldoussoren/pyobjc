from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSResourceHelper(FSKit.NSObject):

    def startCheckWithTask_options_error_(self, a, b, c):
        pass

    def startFormatWithTask_options_error_(self, a, b, c):
        pass


class TestFSResource(TestCase):
    def test_enum(self):
        self.assertIsEnumType(FSKit.FSMatchResult)
        self.assertEqual(FSKit.FSMatchResultNotRecognized, 0)
        self.assertEqual(FSKit.FSMatchResultRecognized, 1)
        self.assertEqual(FSKit.FSMatchResultUsableButLimited, 2)
        self.assertEqual(FSKit.FSMatchResultUsable, 3)

    def test_structs(self):
        v = FSKit.FSMetadataReadahead()
        self.assertIsInstance(v.offset, int)
        self.assertIsInstance(v.length, int)

    def test_protocols(self):
        self.assertProtocolExists("FSManageableResourceMaintenanceOperations")

    def test_protocol_methods(self):

        self.assertArgHasType(
            TestFSResourceHelper.startCheckWithTask_options_error_, 2, b"o^@"
        )
        self.assertArgHasType(
            TestFSResourceHelper.startFormatWithTask_options_error_, 2, b"o^@"
        )

    def test_methods(self):
        self.assertResultIsBOOL(FSKit.FSResource.isRevoked)
        self.assertResultIsBOOL(FSKit.FSBlockDeviceResource.isWritable)

        self.assertArgIsInOut(
            FSKit.FSBlockDeviceResource.readInto_startingAt_length_completionHandler_, 0
        )
        self.assertArgSizeInArg(
            FSKit.FSBlockDeviceResource.readInto_startingAt_length_completionHandler_,
            0,
            2,
        )
        self.assertArgIsBlock(
            FSKit.FSBlockDeviceResource.readInto_startingAt_length_completionHandler_,
            3,
            b"vQ@",
        )

        self.assertArgIsOut(
            FSKit.FSBlockDeviceResource.readInto_startingAt_length_error_,
            0,
        )
        self.assertArgSizeInArg(
            FSKit.FSBlockDeviceResource.readInto_startingAt_length_error_,
            0,
            2,
        )
        self.assertArgIsOut(
            FSKit.FSBlockDeviceResource.readInto_startingAt_length_error_,
            3,
        )

        self.assertArgIsIn(
            FSKit.FSBlockDeviceResource.writeFrom_startingAt_length_completionHandler_,
            0,
        )
        self.assertArgSizeInArg(
            FSKit.FSBlockDeviceResource.writeFrom_startingAt_length_completionHandler_,
            0,
            2,
        )
        self.assertArgIsBlock(
            FSKit.FSBlockDeviceResource.writeFrom_startingAt_length_completionHandler_,
            3,
            b"vQ@",
        )

        self.assertArgIsIn(
            FSKit.FSBlockDeviceResource.writeFrom_startingAt_length_error_,
            0,
        )
        self.assertArgSizeInArg(
            FSKit.FSBlockDeviceResource.writeFrom_startingAt_length_error_,
            0,
            2,
        )
        self.assertArgIsOut(
            FSKit.FSBlockDeviceResource.writeFrom_startingAt_length_error_,
            3,
        )

        self.assertArgIsOut(
            FSKit.FSBlockDeviceResource.metadataReadInto_startingAt_length_error_,
            0,
        )
        self.assertArgSizeInArg(
            FSKit.FSBlockDeviceResource.metadataReadInto_startingAt_length_error_,
            0,
            2,
        )
        self.assertArgIsOut(
            FSKit.FSBlockDeviceResource.metadataReadInto_startingAt_length_error_,
            3,
        )

        self.assertArgIsIn(
            FSKit.FSBlockDeviceResource.metadataWriteFrom_startingAt_length_error_, 0
        )
        self.assertArgSizeInArg(
            FSKit.FSBlockDeviceResource.metadataWriteFrom_startingAt_length_error_,
            0,
            2,
        )
        self.assertArgIsOut(
            FSKit.FSBlockDeviceResource.metadataWriteFrom_startingAt_length_error_,
            3,
        )

        self.assertArgIsIn(
            FSKit.FSBlockDeviceResource.delayedMetadataWriteFrom_startingAt_length_error_,
            0,
        )
        self.assertArgSizeInArg(
            FSKit.FSBlockDeviceResource.delayedMetadataWriteFrom_startingAt_length_error_,
            0,
            2,
        )
        self.assertArgIsOut(
            FSKit.FSBlockDeviceResource.delayedMetadataWriteFrom_startingAt_length_error_,
            3,
        )

        self.assertResultIsBOOL(FSKit.FSBlockDeviceResource.metadataFlushWithError_)
        self.assertArgIsOut(FSKit.FSBlockDeviceResource.metadataFlushWithError_, 0)

        self.assertResultIsBOOL(
            FSKit.FSBlockDeviceResource.asynchronousMetadataFlushWithError_
        )
        self.assertArgIsOut(
            FSKit.FSBlockDeviceResource.asynchronousMetadataFlushWithError_, 0
        )

        self.assertArgIsBOOL(
            FSKit.FSBlockDeviceResource.metadataClear_withDelayedWrite_error_, 1
        )
        self.assertArgIsOut(
            FSKit.FSBlockDeviceResource.metadataClear_withDelayedWrite_error_, 2
        )

        self.assertArgIsOut(FSKit.FSBlockDeviceResource.metadataPurge_error_, 1)

        self.assertArgIsBOOL(
            FSKit.FSBlockDeviceResource.proxyResourceForBSDName_isWritable_, 1
        )
