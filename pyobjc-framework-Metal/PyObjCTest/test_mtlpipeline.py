import Metal
from PyObjCTools.TestSupport import TestCase


class TestMTLPipeline(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Metal.MTLMutability)

    def test_constants(self):
        self.assertEqual(Metal.MTLMutabilityDefault, 0)
        self.assertEqual(Metal.MTLMutabilityMutable, 1)
        self.assertEqual(Metal.MTLMutabilityImmutable, 2)
