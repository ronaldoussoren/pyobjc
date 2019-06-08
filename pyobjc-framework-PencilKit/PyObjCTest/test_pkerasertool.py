import sys
from PyObjCTest import *

if sys.maxsize > 2 ** 32:
    import PencilKit

    class TestPKEraserTool (TestCase):
        @min_os_level('10.15')
        def test_constants(self):
            self.assertEqual(PencilKit.PKEraserTypeVector, 0)
            self.assertEqual(PencilKit.PKEraserTypeBitmap, 1)
