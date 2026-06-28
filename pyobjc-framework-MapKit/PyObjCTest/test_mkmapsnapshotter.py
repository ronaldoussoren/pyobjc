from PyObjCTools.TestSupport import TestCase

import MapKit

MKMapSnapshotCompletionHandler = b"v@@"


class TestMKMapSnapshotter(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MapKit.MKMapSnapshotter.isLoading)
        # self.assertArgIsBOOL(MapKit.MKMapSnapshotter.setLoading_, 0)

        self.assertArgIsBlock(
            MapKit.MKMapSnapshotter.startWithCompletionHandler_,
            0,
            MKMapSnapshotCompletionHandler,
        )

        # XXX: Argument 0 is a dispatch queue, not wrapped...
        self.assertArgIsBlock(
            MapKit.MKMapSnapshotter.startWithQueue_completionHandler_,
            1,
            MKMapSnapshotCompletionHandler,
        )
