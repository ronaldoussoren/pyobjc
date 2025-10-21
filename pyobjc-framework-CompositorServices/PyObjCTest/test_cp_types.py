from PyObjCTools.TestSupport import TestCase

import CompositorServices


class TestCPTypes(TestCase):
    def test_enum(self):
        self.assertIsEnumType(CompositorServices.cp_axis_direction_convention)
        self.assertEqual(
            CompositorServices.cp_axis_direction_convention_right_up_back, 0
        )
        self.assertEqual(
            CompositorServices.cp_axis_direction_convention_right_up_forward, 1
        )
        self.assertEqual(
            CompositorServices.cp_axis_direction_convention_right_down_back, 2
        )
        self.assertEqual(
            CompositorServices.cp_axis_direction_convention_right_down_forward, 3
        )

    def test_structs(self):
        v = CompositorServices.cp_time_t()
        self.assertIsInstance(v.cp_mach_abs_time, int)

    def test_functions(self):
        CompositorServices.cp_time_to_cf_time_interval
        CompositorServices.cp_time_wait_until

    def test_types(self):
        self.assertIsOpaquePointer(CompositorServices.cp_drawable_render_context_t)
