from PyObjCTools.TestSupport import TestCase

import MapKit


class TestMKMapSnapshotOptions(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MapKit.MKMapSnapshotOptions.showsPointsOfInterest)
        self.assertArgIsBOOL(MapKit.MKMapSnapshotOptions.setShowsPointsOfInterest_, 0)

        self.assertResultIsBOOL(MapKit.MKMapSnapshotOptions.showsBuildings)
        self.assertArgIsBOOL(MapKit.MKMapSnapshotOptions.setShowsBuildings_, 0)

        self.assertResultHasType(
            MapKit.MKMapSnapshotOptions.mapRect, MapKit.MKMapRect.__typestr__
        )
        self.assertResultHasType(
            MapKit.MKMapSnapshotOptions.region, MapKit.MKCoordinateRegion.__typestr__
        )

        self.assertArgHasType(
            MapKit.MKMapSnapshotOptions.setMapRect_, 0, MapKit.MKMapRect.__typestr__
        )
        self.assertArgHasType(
            MapKit.MKMapSnapshotOptions.setRegion_,
            0,
            MapKit.MKCoordinateRegion.__typestr__,
        )
