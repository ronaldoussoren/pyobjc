from PyObjCTools.TestSupport import *

import Metal


class TestMTLTypes(TestCase):
    def test_structs(self):
        v = Metal.MTLOrigin()
        self.assertEqual(v.x, 0)
        self.assertEqual(v.y, 0)
        self.assertEqual(v.z, 0)

        v = Metal.MTLSize()
        self.assertEqual(v.width, 0)
        self.assertEqual(v.height, 0)
        self.assertEqual(v.depth, 0)

        v = Metal.MTLRegion()
        self.assertIsInstance(v.origin, Metal.MTLOrigin)
        self.assertIsInstance(v.size, Metal.MTLSize)

        v = Metal.MTLSamplePosition()
        self.assertEqual(v.x, 0.0)
        self.assertEqual(v.y, 0.0)

    def test_functions(self):
        v = Metal.MTLOriginMake(1, 2, 3)
        self.assertIsInstance(v, Metal.MTLOrigin)
        self.assertEqual(v, (1, 2, 3))

        v = Metal.MTLSizeMake(1, 2, 3)
        self.assertIsInstance(v, Metal.MTLSize)
        self.assertEqual(v, (1, 2, 3))

        v = Metal.MTLRegionMake1D(1, 2)
        self.assertIsInstance(v, Metal.MTLRegion)

        v = Metal.MTLRegionMake2D(1, 2, 3, 4)
        self.assertIsInstance(v, Metal.MTLRegion)

        v = Metal.MTLRegionMake3D(1, 2, 3, 4, 5, 6)
        self.assertIsInstance(v, Metal.MTLRegion)

        v = Metal.MTLSamplePositionMake(0.5, 1.5)
        self.assertIsInstance(v, Metal.MTLSamplePosition)
        self.assertEqual(v, (0.5, 1.5))
