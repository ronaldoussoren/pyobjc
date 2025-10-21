import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level, min_os_level


class TestMTL4CommandQueueHelper(Metal.NSObject):
    def commit_count_(self, a, b):
        pass

    def commit_count_options_(self, a, b, c):
        pass

    def signalEvent_value_(self, a, b):
        pass

    def waitForEvent_value_(self, a, b):
        pass

    def addResidencySets_count_(self, a, b):
        pass

    def removeResidencySets_count_(self, a, b):
        pass

    def copyTextureMappingsFromTexture_toTexture_operations_count_(self, a, b, c, d):
        pass

    def updateBufferMappings_heap_operations_count_(self, a, b, c, d):
        pass

    def updateTextureMappings_heap_operations_count_(self, a, b, c, d):
        pass

    def copyBufferMappingsFromBuffer_toBuffer_operations_count_(self, a, b, c, d):
        pass


class TestMTL4CommandQueue(TestCase):
    def test_enum(self):
        self.assertIsEnumType(Metal.MTL4CommandQueueError)
        self.assertEqual(Metal.MTL4CommandQueueErrorNone, 0)
        self.assertEqual(Metal.MTL4CommandQueueErrorTimeout, 1)
        self.assertEqual(Metal.MTL4CommandQueueErrorNotPermitted, 2)
        self.assertEqual(Metal.MTL4CommandQueueErrorOutOfMemory, 3)
        self.assertEqual(Metal.MTL4CommandQueueErrorDeviceRemoved, 4)
        self.assertEqual(Metal.MTL4CommandQueueErrorAccessRevoked, 5)
        self.assertEqual(Metal.MTL4CommandQueueErrorInternal, 6)

    def test_structs(self):
        v = Metal.MTL4UpdateSparseTextureMappingOperation()
        self.assertIsInstance(v.mode, int)
        self.assertIsInstance(v.textureRegion, Metal.MTLRegion)
        self.assertIsInstance(v.textureLevel, int)
        self.assertIsInstance(v.textureSlice, int)
        self.assertIsInstance(v.heapOffset, int)

        v = Metal.MTL4CopySparseTextureMappingOperation()
        self.assertIsInstance(v.sourceRegion, Metal.MTLRegion)
        self.assertIsInstance(v.sourceLevel, int)
        self.assertIsInstance(v.sourceSlice, int)
        self.assertIsInstance(v.destinationOrigin, Metal.MTLOrigin)
        self.assertIsInstance(v.destinationLevel, int)
        self.assertIsInstance(v.destinationSlice, int)

        v = Metal.MTL4UpdateSparseBufferMappingOperation()
        self.assertIsInstance(v.mode, int)
        self.assertIsInstance(v.bufferRange, Metal.NSRange)
        self.assertIsInstance(v.heapOffset, int)

        v = Metal.MTL4CopySparseBufferMappingOperation()
        self.assertIsInstance(v.sourceRange, Metal.NSRange)
        self.assertIsInstance(v.destinationOffset, int)

    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("MTLTextureViewPool")
        self.assertProtocolExists("MTL4CommandQueue")

    def test_protocol_methods(self):
        self.assertArgHasType(TestMTL4CommandQueueHelper.commit_count_, 0, b"n^@")
        self.assertArgSizeInArg(TestMTL4CommandQueueHelper.commit_count_, 0, 1)
        self.assertArgHasType(TestMTL4CommandQueueHelper.commit_count_, 1, b"Q")

        self.assertArgHasType(
            TestMTL4CommandQueueHelper.commit_count_options_, 0, b"n^@"
        )
        self.assertArgSizeInArg(TestMTL4CommandQueueHelper.commit_count_options_, 0, 1)
        self.assertArgHasType(TestMTL4CommandQueueHelper.commit_count_options_, 1, b"Q")

        self.assertArgHasType(TestMTL4CommandQueueHelper.signalEvent_value_, 1, b"Q")

        self.assertArgHasType(TestMTL4CommandQueueHelper.waitForEvent_value_, 1, b"Q")

        self.assertArgHasType(
            TestMTL4CommandQueueHelper.addResidencySets_count_, 0, b"n^@"
        )
        self.assertArgSizeInArg(
            TestMTL4CommandQueueHelper.addResidencySets_count_, 0, 1
        )
        self.assertArgHasType(
            TestMTL4CommandQueueHelper.addResidencySets_count_, 1, b"Q"
        )

        self.assertArgHasType(
            TestMTL4CommandQueueHelper.removeResidencySets_count_, 0, b"n^@"
        )
        self.assertArgSizeInArg(
            TestMTL4CommandQueueHelper.removeResidencySets_count_, 0, 1
        )
        self.assertArgHasType(
            TestMTL4CommandQueueHelper.removeResidencySets_count_, 1, b"Q"
        )

        self.assertArgHasType(
            TestMTL4CommandQueueHelper.updateTextureMappings_heap_operations_count_,
            2,
            b"n^" + Metal.MTL4UpdateSparseTextureMappingOperation.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTL4CommandQueueHelper.updateTextureMappings_heap_operations_count_,
            2,
            3,
        )
        self.assertArgHasType(
            TestMTL4CommandQueueHelper.updateTextureMappings_heap_operations_count_,
            3,
            b"Q",
        )

        self.assertArgHasType(
            TestMTL4CommandQueueHelper.copyTextureMappingsFromTexture_toTexture_operations_count_,
            2,
            b"n^" + Metal.MTL4CopySparseTextureMappingOperation.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTL4CommandQueueHelper.copyTextureMappingsFromTexture_toTexture_operations_count_,
            2,
            3,
        )
        self.assertArgHasType(
            TestMTL4CommandQueueHelper.copyTextureMappingsFromTexture_toTexture_operations_count_,
            3,
            b"Q",
        )

        self.assertArgHasType(
            TestMTL4CommandQueueHelper.copyTextureMappingsFromTexture_toTexture_operations_count_,
            2,
            b"n^" + Metal.MTL4CopySparseTextureMappingOperation.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTL4CommandQueueHelper.updateBufferMappings_heap_operations_count_, 2, 3
        )
        self.assertArgHasType(
            TestMTL4CommandQueueHelper.updateBufferMappings_heap_operations_count_,
            3,
            b"Q",
        )

        self.assertArgHasType(
            TestMTL4CommandQueueHelper.copyBufferMappingsFromBuffer_toBuffer_operations_count_,
            2,
            b"n^" + Metal.MTL4CopySparseBufferMappingOperation.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTL4CommandQueueHelper.copyBufferMappingsFromBuffer_toBuffer_operations_count_,
            2,
            3,
        )
        self.assertArgHasType(
            TestMTL4CommandQueueHelper.copyBufferMappingsFromBuffer_toBuffer_operations_count_,
            3,
            b"Q",
        )

    @min_os_level("26.0")
    def test_constants(self):
        self.assertIsInstance(Metal.MTL4CommandQueueErrorDomain, str)

    @min_os_level("26.0")
    def test_methods(self):
        self.assertArgIsBlock(Metal.MTL4CommitOptions.addFeedbackHandler_, 0, b"v@")
