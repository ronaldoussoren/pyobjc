from PyObjCTools.TestSupport import TestCase

import CompositorServices


class TestLayerRendererConfiguration(TestCase):
    def test_types(self):
        self.assertIsOpaquePointer(CompositorServices.cp_layer_renderer_configuration_t)

    def test_functions(self):
        CompositorServices.cp_layer_renderer_configuration_get_color_format
        CompositorServices.cp_layer_renderer_configuration_set_color_format
        CompositorServices.cp_layer_renderer_configuration_get_color_usage
        CompositorServices.cp_layer_renderer_configuration_set_color_usage
        CompositorServices.cp_layer_renderer_configuration_get_tracking_areas_format
        CompositorServices.cp_layer_renderer_configuration_set_tracking_areas_format
        CompositorServices.cp_layer_renderer_configuration_get_tracking_areas_usage
        CompositorServices.cp_layer_renderer_configuration_set_tracking_areas_usage
        CompositorServices.cp_layer_renderer_configuration_get_depth_format
        CompositorServices.cp_layer_renderer_configuration_set_depth_format
        CompositorServices.cp_layer_renderer_configuration_get_depth_usage
        CompositorServices.cp_layer_renderer_configuration_set_depth_usage
        CompositorServices.cp_layer_renderer_configuration_get_foveation_enabled
        CompositorServices.cp_layer_renderer_configuration_set_foveation_enabled
        CompositorServices.cp_layer_renderer_configuration_get_generate_flipped_rasterization_rate_maps
        CompositorServices.cp_layer_renderer_configuration_set_generate_flipped_rasterization_rate_maps
        CompositorServices.cp_layer_renderer_configuration_get_layout
        CompositorServices.cp_layer_renderer_configuration_set_layout

        # Vector types
        # CompositorServices.cp_layer_renderer_configuration_get_default_depth_range
        # CompositorServices.cp_layer_renderer_configuration_set_default_depth_range
        CompositorServices.cp_layer_renderer_configuration_set_drawable_render_context_stencil_format
        CompositorServices.cp_layer_renderer_configuration_get_drawable_render_context_stencil_format
        CompositorServices.cp_layer_renderer_configuration_get_drawable_render_context_raster_sample_count
        CompositorServices.cp_layer_renderer_configuration_set_drawable_render_context_raster_sample_count
        CompositorServices.cp_layer_renderer_configuration_get_max_render_quality
        CompositorServices.cp_layer_renderer_configuration_set_max_render_quality
        CompositorServices.cp_layer_renderer_configuration_get_supports_mtl4
        CompositorServices.cp_layer_renderer_configuration_set_supports_mtl4
