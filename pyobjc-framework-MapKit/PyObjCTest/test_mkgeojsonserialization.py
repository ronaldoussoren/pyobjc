from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc

import MapKit


class TestMKGeoJSONSerialization(TestCase):
    @min_os_level("10.15")
    def test_methods(self):
        self.assertArgIsOut(MapKit.MKGeoJSONDecoder.geoJSONObjectsWithData_error_, 1)

    @min_sdk_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("MKGeoJSONObject")
