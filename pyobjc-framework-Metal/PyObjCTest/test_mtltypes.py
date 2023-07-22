import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level, os_release, os_level_key


class TestMTLTypes(TestCase):
    def test_structs(self):
        v = Metal.MTLOrigin()
        self.assertEqual(v.x, 0)
        self.assertEqual(v.y, 0)
        self.assertEqual(v.z, 0)
        self.assertPickleRoundTrips(v)

        v = Metal.MTLSize()
        self.assertEqual(v.width, 0)
        self.assertEqual(v.height, 0)
        self.assertEqual(v.depth, 0)
        self.assertPickleRoundTrips(v)

        v = Metal.MTLRegion()
        self.assertIsInstance(v.origin, Metal.MTLOrigin)
        self.assertIsInstance(v.size, Metal.MTLSize)
        self.assertPickleRoundTrips(v)

        v = Metal.MTLSamplePosition()
        self.assertEqual(v.x, 0.0)
        self.assertEqual(v.y, 0.0)
        self.assertPickleRoundTrips(v)

        v = Metal.MTLResourceID()
        self.assertEqual(v._impl, 0)

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

    @min_sdk_level("10.13")
    def test_functions10_13(self):
        v = Metal.MTLSamplePositionMake(0.5, 1.5)
        self.assertIsInstance(v, Metal.MTLCoordinate2D)
        self.assertEqual(v, (0.5, 1.5))

    @min_sdk_level("10.15")
    def test_functions10_15(self):
        if os_level_key(os_release()) < os_level_key("10.15"):
            # The latest Xcode that supports macOS 10.14 supports
            # the 10.15 SDK, but not this API
            if not hasattr(Metal, "MTLCoordinate2DMake"):
                return
        v = Metal.MTLCoordinate2DMake(0.5, 1.5)
        self.assertIsInstance(v, Metal.MTLCoordinate2D)
        self.assertEqual(v, (0.5, 1.5))
