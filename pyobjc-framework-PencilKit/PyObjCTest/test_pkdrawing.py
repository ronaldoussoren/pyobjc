import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import PencilKit

    class TestPKDrawing(TestCase):
        @min_os_level("10.15")
        def test_constants(self):
            self.assertIsInstance(PencilKit.PKAppleDrawingTypeIdentifier, unicode)

        @min_os_level("10.15")
        def test_methods(self):
            self.assertArgIsOut(PencilKit.PKDrawing.initWithData_error_, 1)
