import Metal  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestTMLFunctionStitching(TestCase):
    def test_enum(self):
        self.assertIsEnumType(Metal.MTLStitchedLibraryOptions)
        self.assertEqual(Metal.MTLStitchedLibraryOptionNone, 0)
        self.assertEqual(Metal.MTLStitchedLibraryOptionFailOnBinaryArchiveMiss, 1 << 0)
        self.assertEqual(
            Metal.MTLStitchedLibraryOptionStoreLibraryInMetalPipelinesScript, 1 << 1
        )

    @min_sdk_level("12.0")
    def test_protocols(self):
        self.assertProtocolExists("MTLFunctionStitchingAttribute")
        self.assertProtocolExists("MTLFunctionStitchingNode")
