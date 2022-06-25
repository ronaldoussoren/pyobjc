from PyObjCTools.TestSupport import TestCase, min_os_level

import MapKit


class TestMKStandardMapConfiguration(TestCase):
    def test_constants(self):
        self.assertIsEnumType(MapKit.MKStandardMapEmphasisStyle)
        self.assertEqual(MapKit.MKStandardMapEmphasisStyleDefault, 0)
        self.assertEqual(MapKit.MKStandardMapEmphasisStyleMuted, 1)

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(MapKit.MKStandardMapConfiguration.showsTraffic)
        self.assertArgIsBOOL(MapKit.MKStandardMapConfiguration.setShowsTraffic_, 0)
