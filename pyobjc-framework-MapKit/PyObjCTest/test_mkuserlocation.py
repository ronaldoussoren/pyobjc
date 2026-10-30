from PyObjCTools.TestSupport import TestCase

import MapKit


class TestMKUserLocation(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MapKit.MKUserLocation.isUpdating)
