from PyObjCTools.TestSupport import TestCase

import ARKit


class TestWorldTracking(TestCase):
    def test_types(self):
        # Not a concrete type in ObjC:
        # self.assertIsSubclass(ARKit.ar_world_tracking_configuration_t, objc.objc_object)
        # self.assertIsSubclass(ARKit.ar_world_tracking_provider_t, objc.objc_object)
        # self.assertIsSubclass(ARKit.ar_device_anchor_t, objc.objc_object)
        pass

    def test_enum(self):
        self.assertIsEnumType(ARKit.ar_device_anchor_query_status_t)
        self.assertEqual(ARKit.ar_device_anchor_query_status_success, 0)
        self.assertEqual(ARKit.ar_device_anchor_query_status_failure, 1)

        self.assertIsEnumType(ARKit.ar_device_anchor_tracking_state_t)
        self.assertEqual(ARKit.ar_device_anchor_tracking_state_untracked, 0)
        self.assertEqual(ARKit.ar_device_anchor_tracking_state_orientation_tracked, 1)
        self.assertEqual(ARKit.ar_device_anchor_tracking_state_tracked, 2)

    def test_functions(self):
        self.assertResultIsRetained(ARKit.ar_world_tracking_configuration_create)
        self.assertResultIsRetained(ARKit.ar_world_tracking_provider_create)
        self.assertResultIsRetained(ARKit.ar_device_anchor_create)
        # SIMD types
        # ARKit.ar_device_anchor_get_origin_from_anchor_transform
        self.assertArgIsOut(ARKit.ar_device_anchor_get_identifier, 1)
        ARKit.ar_device_anchor_get_timestamp
        ARKit.ar_device_anchor_is_tracked
        ARKit.ar_device_anchor_get_tracking_state
        ARKit.ar_world_tracking_provider_query_device_anchor_at_timestamp
        ARKit.ar_world_tracking_provider_get_required_authorization_type
