from PyObjCTools.TestSupport import TestCase

import CompositorServices
import objc


class TestRenderer(TestCase):
    def test_enum(self):
        self.assertIsEnumType(CompositorServices.cp_layer_renderer_state)
        self.assertEqual(CompositorServices.cp_layer_renderer_state_paused, 1)
        self.assertEqual(CompositorServices.cp_layer_renderer_state_running, 2)
        self.assertEqual(CompositorServices.cp_layer_renderer_state_invalidated, 3)

    def test_types(self):
        self.assertIsSubclass(CompositorServices.cp_layer_renderer_t, objc.objc_object)

    def test_functions(self):
        CompositorServices.cp_layer_renderer_get_configuration
        CompositorServices.cp_layer_renderer_get_properties
        CompositorServices.cp_layer_renderer_get_device
        CompositorServices.cp_layer_renderer_get_mtl4_command_queue
        CompositorServices.cp_layer_renderer_get_state
        CompositorServices.cp_layer_renderer_wait_until_running
        CompositorServices.cp_layer_renderer_query_next_frame
        CompositorServices.cp_layer_renderer_get_minimum_frame_repeat_count
        CompositorServices.cp_layer_renderer_set_minimum_frame_repeat_count
        CompositorServices.cp_layer_renderer_get_render_quality
        CompositorServices.cp_layer_renderer_set_render_quality
