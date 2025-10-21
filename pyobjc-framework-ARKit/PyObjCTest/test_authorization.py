from PyObjCTools.TestSupport import TestCase

import ARKit


class TestAuthorization(TestCase):
    def test_enum(self):
        self.assertIsEnumType(ARKit.ar_authorization_status_t)
        self.assertEqual(ARKit.ar_authorization_status_not_determined, 0)
        self.assertEqual(ARKit.ar_authorization_status_allowed, 1)
        self.assertEqual(ARKit.ar_authorization_status_denied, 2)

        self.assertIsEnumType(ARKit.ar_authorization_type_t)
        self.assertEqual(ARKit.ar_authorization_type_hand_tracking, 1 << 0)
        self.assertEqual(ARKit.ar_authorization_type_world_sensing, 1 << 1)
        self.assertEqual(ARKit.ar_authorization_type_camera_access, 1 << 3)

    def test_types(self):
        # These are not concrete types in ObjC:
        # self.assertIsSubclass(ARKit.ar_authorization_result_t, objc.objc_object)
        # self.assertIsSubclass(ARKit.ar_authorization_results_t, objc.objc_object)
        pass

    def test_functions(self):
        ARKit.ar_authorization_result_get_authorization_type
        ARKit.ar_authorization_result_get_status
        ARKit.ar_authorization_results_get_count
        self.assertArgIsBlock(
            ARKit.ar_authorization_results_enumerate_results, 1, b"B@"
        )
        self.assertArgIsFunction(
            ARKit.ar_authorization_results_enumerate_results_f, 2, b"B^v@", False
        )
