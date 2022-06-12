from PyObjCTools.TestSupport import TestCase, min_os_level

import MapKit


class TestMKLookAroundSceneRequest(TestCase):
    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(MapKit.MKLookAroundSceneRequest.isCancelled)
        self.assertResultIsBOOL(MapKit.MKLookAroundSceneRequest.isLoading)
        self.assertArgIsBlock(
            MapKit.MKLookAroundSceneRequest.getSceneWithCompletionHandler_, 0, b"v@@"
        )
