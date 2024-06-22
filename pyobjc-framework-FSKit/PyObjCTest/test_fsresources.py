from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSResourceHelper(FSKit.NSObject):
    def checkWithParameters_connection_taskID_replyHandler_(self, a, b, c, d):
        pass

    def formatWithParameters_connection_taskID_replyHandler_(self, a, b, c, d):
        pass

    def probeResource_replyHandler_(self, a, b):
        pass


class TestFSResource(TestCase):
    def test_enum(self):
        self.assertIsEnumType(FSKit.FSMatchResult)
        self.assertEqual(FSKit.FSMatchNotRecognized, 0)
        self.assertEqual(FSKit.FSMatchRecognized, 1)
        self.assertEqual(FSKit.FSMatchUsableButLimited, 2)
        self.assertEqual(FSKit.FSMatchUsable, 3)

        self.assertIsEnumType(FSKit.FSResourceKind)
        self.assertEqual(FSKit.FSResourceKindGeneric, 0)
        self.assertEqual(FSKit.FSResourceKindBlockDevice, 1)
        self.assertEqual(FSKit.FSResourceKindPathURL, 2)
        self.assertEqual(FSKit.FSResourceKindServerURL, 3)

    def test_structs(self):
        v = FSKit.FSMetaReadahead()
        self.assertIsInstance(v.offset, int)
        self.assertIsInstance(v.length, int)

    def test_protocols(self):
        self.assertProtocolExists("FSManageableResourceSimpleMaintenanceOps")
        self.assertProtocolExists("FSBlockDeviceOperations")

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestFSResourceHelper.checkWithParameters_connection_taskID_replyHandler_,
            3,
            b"v@@",
        )
        self.assertArgIsBlock(
            TestFSResourceHelper.formatWithParameters_connection_taskID_replyHandler_,
            3,
            b"v@@",
        )

        self.assertArgIsBlock(
            TestFSResourceHelper.probeResource_replyHandler_, 1, b"vi@@@"
        )

    def test_methods(self):
        self.assertArgIsInOut(
            FSKit.FSBlockDeviceResource.readInto_startingAt_length_replyHandler_, 0
        )
        self.assertArgSizeInArg(
            FSKit.FSBlockDeviceResource.readInto_startingAt_length_replyHandler_, 0, 2
        )
        self.assertArgIsBlock(
            FSKit.FSBlockDeviceResource.readInto_startingAt_length_replyHandler_,
            3,
            b"vQ@",
        )

        self.assertArgIsInOut(
            FSKit.FSBlockDeviceResource.synchronousReadInto_startingAt_length_replyHandler_,
            0,
        )
        self.assertArgSizeInArg(
            FSKit.FSBlockDeviceResource.synchronousReadInto_startingAt_length_replyHandler_,
            0,
            2,
        )
        self.assertArgIsBlock(
            FSKit.FSBlockDeviceResource.synchronousReadInto_startingAt_length_replyHandler_,
            3,
            b"vQ@",
        )

        self.assertArgIsIn(
            FSKit.FSBlockDeviceResource.writeFrom_startingAt_length_replyHandler_, 0
        )
        self.assertArgSizeInArg(
            FSKit.FSBlockDeviceResource.writeFrom_startingAt_length_replyHandler_, 0, 2
        )
        self.assertArgIsBlock(
            FSKit.FSBlockDeviceResource.writeFrom_startingAt_length_replyHandler_,
            3,
            b"vQ@",
        )

        self.assertArgIsIn(
            FSKit.FSBlockDeviceResource.synchronousWriteFrom_startingAt_length_replyHandler_,
            0,
        )
        self.assertArgSizeInArg(
            FSKit.FSBlockDeviceResource.synchronousWriteFrom_startingAt_length_replyHandler_,
            0,
            2,
        )
        self.assertArgIsBlock(
            FSKit.FSBlockDeviceResource.synchronousWriteFrom_startingAt_length_replyHandler_,
            3,
            b"vQ@",
        )

        self.assertArgIsInOut(
            FSKit.FSBlockDeviceResource.synchronousMetaReadInto_startingAt_length_replyHandler_,
            0,
        )
        self.assertArgSizeInArg(
            FSKit.FSBlockDeviceResource.synchronousMetaReadInto_startingAt_length_replyHandler_,
            0,
            2,
        )
        self.assertArgIsBlock(
            FSKit.FSBlockDeviceResource.synchronousMetaReadInto_startingAt_length_replyHandler_,
            3,
            b"v@",
        )

        self.assertArgIsInOut(
            FSKit.FSBlockDeviceResource.synchronousMetaReadInto_startingAt_length_readAheadExtents_readAheadCount_replyHandler_,
            0,
        )
        self.assertArgSizeInArg(
            FSKit.FSBlockDeviceResource.synchronousMetaReadInto_startingAt_length_readAheadExtents_readAheadCount_replyHandler_,
            0,
            2,
        )
        self.assertArgIsInOut(
            FSKit.FSBlockDeviceResource.synchronousMetaReadInto_startingAt_length_readAheadExtents_readAheadCount_replyHandler_,
            3,
        )
        self.assertArgSizeInArg(
            FSKit.FSBlockDeviceResource.synchronousMetaReadInto_startingAt_length_readAheadExtents_readAheadCount_replyHandler_,
            3,
            4,
        )
        self.assertArgIsBlock(
            FSKit.FSBlockDeviceResource.synchronousMetaReadInto_startingAt_length_readAheadExtents_readAheadCount_replyHandler_,
            5,
            b"v@",
        )

        self.assertArgIsIn(
            FSKit.FSBlockDeviceResource.metaWriteFrom_startingAt_length_replyHandler_, 0
        )
        self.assertArgSizeInArg(
            FSKit.FSBlockDeviceResource.metaWriteFrom_startingAt_length_replyHandler_,
            0,
            2,
        )
        self.assertArgIsBlock(
            FSKit.FSBlockDeviceResource.metaWriteFrom_startingAt_length_replyHandler_,
            3,
            b"v@",
        )

        self.assertArgIsIn(
            FSKit.FSBlockDeviceResource.synchronousMetaWriteFrom_startingAt_length_replyHandler_,
            0,
        )
        self.assertArgSizeInArg(
            FSKit.FSBlockDeviceResource.synchronousMetaWriteFrom_startingAt_length_replyHandler_,
            0,
            2,
        )
        self.assertArgIsBlock(
            FSKit.FSBlockDeviceResource.synchronousMetaWriteFrom_startingAt_length_replyHandler_,
            3,
            b"v@",
        )

        self.assertArgIsIn(
            FSKit.FSBlockDeviceResource.synchronousDelayedMetaWriteFrom_startingAt_length_replyHandler_,
            0,
        )
        self.assertArgSizeInArg(
            FSKit.FSBlockDeviceResource.synchronousDelayedMetaWriteFrom_startingAt_length_replyHandler_,
            0,
            2,
        )
        self.assertArgIsBlock(
            FSKit.FSBlockDeviceResource.synchronousDelayedMetaWriteFrom_startingAt_length_replyHandler_,
            3,
            b"v@",
        )

        self.assertArgIsBlock(
            FSKit.FSBlockDeviceResource.synchronousMetaFlushWithReplyHandler_, 0, b"v@"
        )

        self.assertArgIsBlock(
            FSKit.FSBlockDeviceResource.synchronousMetaClear_wait_replyHandler_,
            2,
            b"v@",
        )

        self.assertArgIsBlock(
            FSKit.FSBlockDeviceResource.synchronousMetaPurge_replyHandler_, 1, b"v@"
        )
