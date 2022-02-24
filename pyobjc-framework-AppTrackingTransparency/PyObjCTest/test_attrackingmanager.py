from PyObjCTools.TestSupport import TestCase

import AppTrackingTransparency
import objc


class TestATTrackingManager(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(
            AppTrackingTransparency.ATTrackingManagerAuthorizationStatus
        )

    def test_constants(self):
        self.assertEqual(
            AppTrackingTransparency.ATTrackingManagerAuthorizationStatusNotDetermined, 0
        )
        self.assertEqual(
            AppTrackingTransparency.ATTrackingManagerAuthorizationStatusRestricted, 1
        )
        self.assertEqual(
            AppTrackingTransparency.ATTrackingManagerAuthorizationStatusDenied, 2
        )
        self.assertEqual(
            AppTrackingTransparency.ATTrackingManagerAuthorizationStatusAuthorized, 3
        )

    def test_methods(self):
        self.assertArgIsBlock(
            AppTrackingTransparency.ATTrackingManager.requestTrackingAuthorizationWithCompletionHandler_,
            0,
            b"v" + objc._C_NSUInteger,
        )
