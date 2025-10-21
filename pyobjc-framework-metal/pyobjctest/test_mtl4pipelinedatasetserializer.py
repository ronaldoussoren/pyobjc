import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTL4PipelineDataSetSerializerHelper(Metal.NSObject):
    def serializeAsArchiveAndFlushToURL_error_(self, a, b):
        return 1

    def serializeAsPipelinesScriptWithError_(self, a):
        return 1


class TestMTL4PipelineDataSetSerializer(TestCase):
    def test_enum(self):
        self.assertIsEnumType(Metal.MTL4PipelineDataSetSerializerConfiguration)
        self.assertEqual(
            Metal.MTL4PipelineDataSetSerializerConfigurationCaptureDescriptors, 1 << 0
        )
        self.assertEqual(
            Metal.MTL4PipelineDataSetSerializerConfigurationCaptureBinaries, 1 << 1
        )

    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("MTL4PipelineDataSetSerializer")

    def test_protocol_methods(self):
        self.assertResultIsBOOL(
            TestMTL4PipelineDataSetSerializerHelper.serializeAsArchiveAndFlushToURL_error_
        )
        self.assertArgHasType(
            TestMTL4PipelineDataSetSerializerHelper.serializeAsArchiveAndFlushToURL_error_,
            1,
            b"o^@",
        )

        self.assertArgHasType(
            TestMTL4PipelineDataSetSerializerHelper.serializeAsPipelinesScriptWithError_,
            0,
            b"o^@",
        )
