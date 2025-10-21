from PyObjCTools.TestSupport import TestCase

import ARKit


class TestDataProvider(TestCase):
    def test_types(self):
        # These are not concrete types in ObjC:
        # self.assertIsSubclass(ARKit.ar_data_provider_t, objc.objc_object)
        # self.assertIsSubclass(ARKit.ar_data_providers_t, objc.objc_object)
        pass

    def test_enum(self):
        self.assertIsEnumType(ARKit.ar_data_provider_state_t)
        self.assertEqual(ARKit.ar_data_provider_state_initialized, 0)
        self.assertEqual(ARKit.ar_data_provider_state_running, 1)
        self.assertEqual(ARKit.ar_data_provider_state_paused, 2)
        self.assertEqual(ARKit.ar_data_provider_state_stopped, 3)

    def test_functions(self):
        ARKit.ar_data_provider_get_state
        ARKit.ar_data_provider_get_required_authorization_type
        self.assertResultIsRetained(ARKit.ar_data_providers_create)
        self.assertResultIsRetained(ARKit.ar_data_providers_create_with_data_providers)
        self.assertIsNullTerminated(ARKit.ar_data_providers_create_with_data_providers)
        ARKit.ar_data_providers_add_data_provider
        ARKit.ar_data_providers_add_data_providers
        ARKit.ar_data_providers_remove_data_provider
        ARKit.ar_data_providers_get_count

        self.assertArgIsBlock(
            ARKit.ar_data_providers_enumerate_data_providers, 1, b"B@"
        )
        self.assertArgIsFunction(
            ARKit.ar_data_providers_enumerate_data_providers_f, 2, b"B^v@", False
        )
