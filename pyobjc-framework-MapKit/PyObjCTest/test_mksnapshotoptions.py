import sys

from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import MapKit

    class TestMKMapSnapshotOptions (TestCase):
        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(MapKit.MKMapSnapshotOptions, objc.objc_class)

            self.assertResultIsBOOL(MapKit.MKMapSnapshotOptions.showsPointsOfInterest)
            self.assertArgIsBOOL(MapKit.MKMapSnapshotOptions.setShowsPointsOfInterest_, 0)

            self.assertResultIsBOOL(MapKit.MKMapSnapshotOptions.showsBuildings)
            self.assertArgIsBOOL(MapKit.MKMapSnapshotOptions.setShowsBuildings_, 0)

if __name__ == "__main__":
    main()
