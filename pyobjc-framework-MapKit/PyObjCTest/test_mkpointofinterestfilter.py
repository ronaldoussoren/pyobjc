from PyObjCTools.TestSupport import TestCase, min_os_level

import MapKit


class TestMKPointOfInterestFilter(TestCase):
    @min_os_level("10.15")
    def test_methods(self):
        self.assertResultIsBOOL(MapKit.MKPointOfInterestFilter.includesCategory_)
        self.assertResultIsBOOL(MapKit.MKPointOfInterestFilter.excludesCategory_)
