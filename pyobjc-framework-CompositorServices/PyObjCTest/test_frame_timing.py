from PyObjCTools.TestSupport import TestCase

import CompositorServices


class TestFrameTiming(TestCase):
    def test_types(self):
        self.assertIsOpaquePointer(CompositorServices.cp_frame_timing_t)

    def test_functions(self):
        CompositorServices.cp_frame_timing_get_optimal_input_time
        CompositorServices.cp_frame_timing_get_rendering_deadline
        CompositorServices.cp_frame_timing_get_presentation_time
        CompositorServices.cp_frame_timing_get_trackable_anchor_time
