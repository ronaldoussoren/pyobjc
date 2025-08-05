from PyObjCTools.TestSupport import TestCase

import CompositorServices


class TestCPError(TestCase):
    def test_constants(self):
        self.assertIsInstance(
            CompositorServices.cp_layer_renderer_configuration_error_domain, str
        )

        self.assertIsEnumType(
            CompositorServices.cp_layer_renderer_configuration_error_code
        )
        self.assertEqual(
            CompositorServices.cp_layer_renderer_configuration_error_code_missing_configuration,
            -20,
        )
        self.assertEqual(
            CompositorServices.cp_layer_renderer_configuration_error_code_unsupported_color_format,
            -4,
        )
        self.assertEqual(
            CompositorServices.cp_layer_renderer_configuration_error_code_unsupported_color_usage,
            -5,
        )
        self.assertEqual(
            CompositorServices.cp_layer_renderer_configuration_error_code_unsupported_depth_format,
            -7,
        )
        self.assertEqual(
            CompositorServices.cp_layer_renderer_configuration_error_code_unsupported_depth_usage,
            -8,
        )
        self.assertEqual(
            CompositorServices.cp_layer_renderer_configuration_error_code_variable_rasterization_rate_is_not_supported,
            -16,
        )
        self.assertEqual(
            CompositorServices.cp_layer_renderer_configuration_error_code_temporal_anti_aliasing_not_supported,
            -17,
        )
        self.assertEqual(
            CompositorServices.cp_layer_renderer_configuration_error_code_not_enough_frames_requested,
            -10,
        )
        self.assertEqual(
            CompositorServices.cp_layer_renderer_configuration_error_code_too_many_frames_requested,
            -11,
        )
        self.assertEqual(
            CompositorServices.cp_layer_renderer_configuration_error_code_unsupported_forward_depth_range,
            -101,
        )
        self.assertEqual(
            CompositorServices.cp_layer_renderer_configuration_error_code_layout_not_supported,
            -6,
        )
        self.assertEqual(
            CompositorServices.cp_layer_renderer_configuration_error_code_unsupported_near_plane_distance,
            -104,
        )
        self.assertEqual(
            CompositorServices.cp_layer_renderer_configuration_error_code_unsupported_tracking_areas_format,
            -21,
        )
        self.assertEqual(
            CompositorServices.cp_layer_renderer_configuration_error_code_unsupported_tracking_areas_usage,
            -22,
        )
        self.assertEqual(
            CompositorServices.cp_layer_renderer_configuration_error_code_unsupported_drawable_render_context_stencil_format,
            -23,
        )
        self.assertEqual(
            CompositorServices.cp_layer_renderer_configuration_error_code_unsupported_render_quality,
            -18,
        )
