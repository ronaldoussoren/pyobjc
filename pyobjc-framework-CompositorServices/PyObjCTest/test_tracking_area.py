from PyObjCTools.TestSupport import TestCase

import CompositorServices


class TestFrameTiming(TestCase):
    def test_types(self):
        self.assertIsOpaquePointer(CompositorServices.cp_tracking_area_t)
        self.assertIsOpaquePointer(CompositorServices.cp_hover_effect_t)

    def test_constants(self):
        self.assertIsInstance(
            CompositorServices.cp_tracking_area_render_value_invalid, int
        )
        self.assertIsInstance(
            CompositorServices.cp_tracking_area_identifier_invalid, int
        )

    def test_functions(self):
        CompositorServices.cp_tracking_area_get_render_value
        CompositorServices.cp_tracking_area_get_identifier
        CompositorServices.cp_tracking_area_add_automatic_hover_effect
