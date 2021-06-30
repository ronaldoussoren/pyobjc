from PyObjCTools.TestSupport import TestCase

import MetalPerformanceShadersGraph


class TestMPSGraphSparseOps(TestCase):
    def test_constants(self):
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphSparseStorageCOO, 0)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphSparseStorageCSC, 1)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphSparseStorageCSR, 2)
