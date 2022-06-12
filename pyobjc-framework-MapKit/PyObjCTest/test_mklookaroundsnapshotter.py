from PyObjCTools.TestSupport import TestCase, min_os_level

import MapKit


class TestMKLookAroundSnapshotter(TestCase):
    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsBlock(
            MapKit.MKLookAroundSnapshotter.getSnapshotWithCompletionHandler_, 0, b"v@@"
        )

        self.assertResultIsBOOL(MapKit.MKLookAroundSnapshotter.isLoading)
