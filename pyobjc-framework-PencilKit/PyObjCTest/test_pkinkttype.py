from PyObjCTools.TestSupport import TestCase, min_os_level

import PencilKit


class TestPKInknType(TestCase):
    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(PencilKit.PKInkTypePen, str)
        self.assertIsInstance(PencilKit.PKInkTypePencil, str)
        self.assertIsInstance(PencilKit.PKInkTypeMarker, str)
