import CoreLocation
from PyObjCTools.TestSupport import TestCase
import objc


class TestCLLocationManagerDelegateHelper(CoreLocation.NSObject):
    def locationManagerShouldDisplayHeadingCalibration_(self, manager):
        return 1

    def locationManager_didDetermineState_forRegion_(self, m, s, r):
        pass

    def locationManager_didChangeAuthorizationStatus_(self, m, s):
        pass


class TestCLLocationManagerDelegate(TestCase):
    def testProtocols(self):
        self.assertProtocolExists("CLLocationManagerDelegate")

    def test_protocol_methods(self):
        self.assertResultIsBOOL(
            TestCLLocationManagerDelegateHelper.locationManagerShouldDisplayHeadingCalibration_
        )
        self.assertArgHasType(
            TestCLLocationManagerDelegateHelper.locationManager_didDetermineState_forRegion_,
            1,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestCLLocationManagerDelegateHelper.locationManager_didChangeAuthorizationStatus_,
            1,
            objc._C_INT,
        )
