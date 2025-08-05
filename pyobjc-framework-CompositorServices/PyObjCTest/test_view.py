from PyObjCTools.TestSupport import TestCase

import CompositorServices


class TestView(TestCase):
    def test_types(self):
        self.assertIsOpaquePointer(CompositorServices.cp_view_texture_map_t)
        self.assertIsOpaquePointer(CompositorServices.cp_view_t)

    def test_functions(self):
        CompositorServices.cp_view_texture_map_get_texture_index
        CompositorServices.cp_view_texture_map_get_slice_index
        CompositorServices.cp_view_texture_map_get_viewport
        CompositorServices.cp_view_get_view_texture_map


# Vector types
# CompositorServices.cp_view_get_transform
