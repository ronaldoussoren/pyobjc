from PyObjCTools.TestSupport import TestCase

import MapKit


class TestMKMapSnapshotOptions(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MapKit.MKMapSnapshotOptions.showsPointsOfInterest)
        self.assertArgIsBOOL(MapKit.MKMapSnapshotOptions.setShowsPointsOfInterest_, 0)

        self.assertResultIsBOOL(MapKit.MKMapSnapshotOptions.showsBuildings)
        self.assertArgIsBOOL(MapKit.MKMapSnapshotOptions.setShowsBuildings_, 0)
