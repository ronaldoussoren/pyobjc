from PyObjCTools.TestSupport import TestCase, min_os_level

import MapKit


class TestMKHybridMapConfiguration(TestCase):
    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(MapKit.MKHybridMapConfiguration.showsTraffic)
        self.assertArgIsBOOL(MapKit.MKHybridMapConfiguration.setShowsTraffic_, 0)
