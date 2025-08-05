import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTL4MachineLearningPipelineHelper(Metal.NSObject):
    def intermediatesHeapSize(self):
        return 1


class TestMTL4MachineLearningPipeline(TestCase):
    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("MTL4MachineLearningPipelineState")

    def test_protocol_methods(self):
        self.assertResultHasType(
            TestMTL4MachineLearningPipelineHelper.intermediatesHeapSize, b"Q"
        )
