from PyObjCTools.TestSupport import TestCase

import CompositorServices
import objc


class TestRendererProperties(TestCase):
    def test_types(self):
        self.assertIsOpaquePointer(CompositorServices.cp_texture_topology_t)
        self.assertIsSubclass(
            CompositorServices.cp_layer_renderer_properties_t, objc.objc_object
        )

    def test_functions(self):
        self.assertResultIsRetained(
            CompositorServices.cp_layer_renderer_properties_create_using_configuration
        )
        self.assertArgIsOut(
            CompositorServices.cp_layer_renderer_properties_create_using_configuration,
            1,
        )

        CompositorServices.cp_layer_renderer_properties_get_texture_topology_count
        CompositorServices.cp_layer_renderer_properties_get_texture_topology
        CompositorServices.cp_layer_renderer_properties_get_view_count
        CompositorServices.cp_layer_renderer_properties_get_tracking_areas_max_value
