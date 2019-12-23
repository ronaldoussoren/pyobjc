from PyObjCTools.TestSupport import *

import Metal


class TestMTLPipeline(TestCase):
    def test_constants(self):
        self.assertEqual(Metal.MTLMutabilityDefault, 0)
        self.assertEqual(Metal.MTLMutabilityMutable, 1)
        self.assertEqual(Metal.MTLMutabilityImmutable, 2)
