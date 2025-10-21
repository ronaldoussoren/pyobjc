from PyObjCTools.TestSupport import TestCase

import CompositorServices


class TestRendererCapabilities(TestCase):
    def test_enum(self):
        self.assertIsEnumType(CompositorServices.cp_supported_color_formats_options)
        self.assertEqual(CompositorServices.cp_supported_color_formats_options_none, 0)
        self.assertEqual(
            CompositorServices.cp_supported_color_formats_options_progressive_immersion_enabled,
            1 << 0,
        )

        self.assertIsEnumType(CompositorServices.cp_supported_layouts_options)
        self.assertEqual(CompositorServices.cp_supported_layouts_options_none, 0)
        self.assertEqual(
            CompositorServices.cp_supported_layouts_options_foveation_enabled, 1 << 0
        )
        self.assertEqual(
            CompositorServices.cp_supported_layouts_options_progressive_immersion_enabled,
            1 << 1,
        )

    def test_types(self):
        self.assertIsOpaquePointer(CompositorServices.cp_layer_renderer_capabilities_t)

    def test_functions(self):
        CompositorServices.cp_layer_renderer_capabilities_supports_foveation
        CompositorServices.cp_layer_renderer_capabilities_supported_color_formats_count_with_options
        CompositorServices.cp_layer_renderer_capabilities_supported_color_format_with_options
        CompositorServices.cp_layer_renderer_capabilities_supported_depth_formats_count
        CompositorServices.cp_layer_renderer_capabilities_supported_depth_format
        CompositorServices.cp_layer_renderer_capabilities_supported_tracking_areas_formats_count
        CompositorServices.cp_layer_renderer_capabilities_supported_tracking_areas_format
        CompositorServices.cp_layer_renderer_capabilities_supported_layouts_count
        CompositorServices.cp_layer_renderer_capabilities_supported_layout
        CompositorServices.cp_layer_renderer_capabilities_supported_minimum_near_plane_distance
        CompositorServices.cp_layer_renderer_capabilities_drawable_render_context_supported_stencil_formats_count
        CompositorServices.cp_layer_renderer_capabilities_drawable_render_context_supported_stencil_format
        CompositorServices.cp_layer_renderer_capabilities_get_default_render_quality
