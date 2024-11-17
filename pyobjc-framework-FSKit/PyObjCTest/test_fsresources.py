from PyObjCTools.TestSupport import TestCase, min_os_level

import FSKit


class TestFSResourceHelper(FSKit.NSObject):
    def probeResource_replyHandler_(self, a, b):
        pass

    def startCheckWithTask_parameters_error_(self, a, b, c):
        pass

    def startFormatWithTask_parameters_error_(self, a, b, c):
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
        self.assertProtocolExists("FSBlockDeviceOperations")

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestFSResourceHelper.probeResource_replyHandler_, 1, b"v@@"
        )

        self.assertArgHasType(
            TestFSResourceHelper.startCheckWithTask_parameters_error_, 2, b"o^@"
        )
        self.assertArgHasType(
            TestFSResourceHelper.startFormatWithTask_parameters_error_, 2, b"o^@"
        )

    @min_os_level("15.2")
    def test_methods(self):
        self.assertResultIsBOOL(FSKit.FSResource.isRevoked)
        self.assertResultIsBOOL(FSKit.FSBlockDeviceResource.isWritable)
        self.assertResultIsBOOL(FSKit.FSBlockDeviceResource.isTerminated)

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

        self.assertArgIsInOut(
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

        self.assertArgIsInOut(
            FSKit.FSBlockDeviceResource.metaReadInto_startingAt_length_error_,
            0,
        )
        self.assertArgSizeInArg(
            FSKit.FSBlockDeviceResource.metaReadInto_startingAt_length_error_,
            0,
            2,
        )
        self.assertArgIsOut(
            FSKit.FSBlockDeviceResource.metaReadInto_startingAt_length_error_,
            3,
        )

        self.assertArgIsInOut(
            FSKit.FSBlockDeviceResource.metaReadInto_startingAt_length_readAheadExtents_readAheadCount_,
            0,
        )
        self.assertArgSizeInArg(
            FSKit.FSBlockDeviceResource.metaReadInto_startingAt_length_readAheadExtents_readAheadCount_,
            0,
            2,
        )
        self.assertArgIsInOut(
            FSKit.FSBlockDeviceResource.metaReadInto_startingAt_length_readAheadExtents_readAheadCount_,
            3,
        )
        self.assertArgSizeInArg(
            FSKit.FSBlockDeviceResource.metaReadInto_startingAt_length_readAheadExtents_readAheadCount_,
            3,
            4,
        )

        self.assertArgIsIn(
            FSKit.FSBlockDeviceResource.metaWriteFrom_startingAt_length_, 0
        )
        self.assertArgSizeInArg(
            FSKit.FSBlockDeviceResource.metaWriteFrom_startingAt_length_,
            0,
            2,
        )

        self.assertArgIsIn(
            FSKit.FSBlockDeviceResource.delayedMetaWriteFrom_startingAt_length_,
            0,
        )
        self.assertArgSizeInArg(
            FSKit.FSBlockDeviceResource.delayedMetaWriteFrom_startingAt_length_,
            0,
            2,
        )

        self.assertArgIsBOOL(FSKit.FSBlockDeviceResource.synchronousMetaClear_wait_, 1)
