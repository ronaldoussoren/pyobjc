import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestMTLIOCompressor(TestCase):
    def test_constants(self):
        self.assertIsEnumType(Metal.MTLIOCompressionStatus)
        self.assertEqual(Metal.MTLIOCompressionStatusComplete, 0)
        self.assertEqual(Metal.MTLIOCompressionStatusError, 1)

    @min_os_level("13.0")
    def test_functions(self):
        # XXX: Tweak the "context" type?
        self.assertArgIsIn(Metal.MTLIOCreateCompressionContext, 0)
        self.assertArgIsNullTerminated(Metal.MTLIOCreateCompressionContext, 0)

        self.assertArgIsIn(Metal.MTLIOCompressionContextAppendData, 1)
        self.assertArgSizeInArg(Metal.MTLIOCompressionContextAppendData, 1, 2)

        Metal.MTLIOFlushAndDestroyCompressionContext
        Metal.MTLIOCompressionContextDefaultChunkSize
