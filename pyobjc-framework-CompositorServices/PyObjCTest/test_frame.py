from PyObjCTools.TestSupport import TestCase

import CompositorServices


class TestFrame(TestCase):
    def test_types(self):
        self.assertIsOpaquePointer(CompositorServices.cp_frame_t)

    def test_functions(self):
        CompositorServices.cp_frame_get_frame_index
        CompositorServices.cp_frame_predict_timing
        CompositorServices.cp_frame_query_drawables
        CompositorServices.cp_frame_start_update
        CompositorServices.cp_frame_end_update
        CompositorServices.cp_frame_start_submission
        CompositorServices.cp_frame_end_submission
        # Vector types
        # CompositorServices.cp_frame_monocular_frustum_matrix_for_drawable_target
        # CompositorServices.cp_frame_binocular_frustum_matrix_for_drawable_target
        CompositorServices.cp_frame_get_drawable_target_view_count
        # Vector types
        # CompositorServices.cp_frame_monocular_frustum_matrix
        # CompositorServices.cp_frame_binocular_frustum_matrix
