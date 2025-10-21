import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTL4BufferRange(TestCase):
    def test_structs(self):
        v = Metal.MTL4BufferRange()
        self.assertIsInstance(v.bufferAddress, int)
        self.assertIsInstance(v.length, int)

    @min_sdk_level("26.0")
    def test_inline_functions(self):
        Metal.MTL4BufferRangeMake
