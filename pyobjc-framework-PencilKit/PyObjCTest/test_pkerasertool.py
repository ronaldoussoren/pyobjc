from PyObjCTools.TestSupport import TestCase

import PencilKit


class TestPKEraserTool(TestCase):
    def test_enums(self):
        self.assertIsEnumType(PencilKit.PKEraserType)
        self.assertEqual(PencilKit.PKEraserTypeVector, 0)
        self.assertEqual(PencilKit.PKEraserTypeBitmap, 1)
        self.assertEqual(PencilKit.PKEraserTypeFixedWidthBitmap, 2)
