from PyObjCTools.TestSupport import TestCase

import CompositorServices


class TestDrawableRenderContext(TestCase):
    def test_types(self):
        self.assertIsOpaquePointer(CompositorServices.cp_drawable_render_context_t)

    def test_functions(self):
        CompositorServices.cp_drawable_render_context_draw_mask_on_stencil_attachment
        CompositorServices.cp_drawable_render_context_end_encoding
        CompositorServices.cp_drawable_render_context_mtl4_draw_mask_on_stencil_attachment
        CompositorServices.cp_drawable_render_context_mtl4_end_encoding
