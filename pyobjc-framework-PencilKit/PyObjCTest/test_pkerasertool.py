from PyObjCTools.TestSupport import TestCase

import PencilKit


class TestPKEraserTool(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(PencilKit.PKEraserType)

    def test_constants(self):
        self.assertEqual(PencilKit.PKEraserTypeVector, 0)
        self.assertEqual(PencilKit.PKEraserTypeBitmap, 1)
