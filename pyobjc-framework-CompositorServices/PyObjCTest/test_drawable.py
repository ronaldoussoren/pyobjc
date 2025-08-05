from PyObjCTools.TestSupport import TestCase

import CompositorServices


class TestDrawable(TestCase):
    def test_enum(self):
        self.assertIsEnumType(CompositorServices.cp_drawable_state)
        self.assertEqual(CompositorServices.cp_drawable_state_available, 0)
        self.assertEqual(CompositorServices.cp_drawable_state_rendering, 1)
        self.assertEqual(CompositorServices.cp_drawable_state_presenting, 2)

        self.assertIsEnumType(CompositorServices.cp_drawable_target)
        self.assertEqual(CompositorServices.cp_drawable_target_built_in, 0)
        self.assertEqual(CompositorServices.cp_drawable_target_capture, 1)

    def test_types(self):
        self.assertIsOpaquePointer(CompositorServices.cp_drawable_t)
        self.assertIsOpaquePointer(CompositorServices.cp_drawable_array_t)

    def test_functions(self):
        CompositorServices.cp_drawable_get_texture_count
        CompositorServices.cp_drawable_get_tracking_areas_texture_count
        CompositorServices.cp_drawable_get_depth_texture
        CompositorServices.cp_drawable_get_color_texture
        CompositorServices.cp_drawable_get_tracking_areas_texture
        CompositorServices.cp_drawable_add_tracking_area
        CompositorServices.cp_drawable_get_rasterization_rate_map_count
        CompositorServices.cp_drawable_get_rasterization_rate_map
        CompositorServices.cp_drawable_get_flipped_rasterization_rate_map
        CompositorServices.cp_drawable_get_view_count
        CompositorServices.cp_drawable_get_view
        CompositorServices.cp_drawable_set_device_anchor
        CompositorServices.cp_drawable_get_device_anchor
        # Vector types
        # CompositorServices.cp_drawable_get_depth_range
        # CompositorServices.cp_drawable_set_depth_range
        CompositorServices.cp_drawable_encode_present
        CompositorServices.cp_drawable_mtl4_encode_present
        CompositorServices.cp_drawable_get_state
        CompositorServices.cp_drawable_get_target
        CompositorServices.cp_drawable_get_presentation_frame_index
        CompositorServices.cp_drawable_get_frame_timing
        # Vector types
        # CompositorServices.cp_drawable_compute_projection
        CompositorServices.cp_drawable_add_render_context
        CompositorServices.cp_drawable_add_mtl4_render_context
        CompositorServices.cp_drawable_array_get_drawable
        CompositorServices.cp_drawable_array_get_count
