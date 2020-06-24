from PyObjCTools.TestSupport import TestCase, min_os_level

import PencilKit


class TestPKDrawing(TestCase):
    @min_os_level("10.15")
    def test_constants(self):
        self.assertIsInstance(PencilKit.PKAppleDrawingTypeIdentifier, str)

    @min_os_level("10.15")
    def test_methods(self):
        self.assertArgIsOut(PencilKit.PKDrawing.initWithData_error_, 1)
