from PyObjCTools.TestSupport import TestCase

import CompositorServices


class TestLayerRendererLayout(TestCase):
    def test_enum(self):
        self.assertIsEnumType(CompositorServices.cp_layer_renderer_layout)
        self.assertEqual(CompositorServices.cp_layer_renderer_layout_dedicated, 0)
        self.assertEqual(CompositorServices.cp_layer_renderer_layout_shared, 1)
        self.assertEqual(CompositorServices.cp_layer_renderer_layout_layered, 2)
