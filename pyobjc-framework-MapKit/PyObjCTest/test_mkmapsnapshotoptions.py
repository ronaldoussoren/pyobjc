from PyObjCTools.TestSupport import TestCase, min_os_level

import MapKit


class TestMKMapSnapshotOptions(TestCase):
    @min_os_level("10.9")
    def testProtocols(self):
        self.assertResultIsBOOL(MapKit.MKMapSnapshotOptions.showsPointsOfInterest)
        self.assertArgIsBOOL(MapKit.MKMapSnapshotOptions.setShowsPointsOfInterest_, 0)

        self.assertResultIsBOOL(MapKit.MKMapSnapshotOptions.showsBuildings)
        self.assertArgIsBOOL(MapKit.MKMapSnapshotOptions.setShowsBuildings_, 0)
