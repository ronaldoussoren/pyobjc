import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import MapKit

    class TestMKGeoJSONSerialization(TestCase):
        @min_os_level("10.15")
        def test_methods(self):
            self.assertArgIsOut(
                MapKit.MKGeoJSONDecoder.geoJSONObjectsWithData_error_, 1
            )

        @min_sdk_level("10.15")
        def test_protocols(self):
            objc.protocolNamed("MKGeoJSONObject")


if __name__ == "__main__":
    main()
