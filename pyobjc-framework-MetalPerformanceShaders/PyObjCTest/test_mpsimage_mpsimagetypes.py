from PyObjCTools.TestSupport import TestCase

import MetalPerformanceShaders


class TestMPSImage_MPSImageTypes(TestCase):
    def test_constants(self):
        self.assertEqual(MetalPerformanceShaders.MPSAlphaTypeNonPremultiplied, 0)
        self.assertEqual(MetalPerformanceShaders.MPSAlphaTypeAlphaIsOne, 1)
        self.assertEqual(MetalPerformanceShaders.MPSAlphaTypePremultiplied, 2)
