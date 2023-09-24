from PyObjCTools.TestSupport import TestCase, min_os_level

import PencilKit


class TestPKInkType(TestCase):
    @min_os_level("10.15")
    def test_constants(self):
        self.assertIsTypedEnum(PencilKit.PKInkType, str)

        self.assertIsInstance(PencilKit.PKInkTypePen, str)
        self.assertIsInstance(PencilKit.PKInkTypePencil, str)
        self.assertIsInstance(PencilKit.PKInkTypeMarker, str)

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(PencilKit.PKInkTypeMonoline, str)
        self.assertIsInstance(PencilKit.PKInkTypeFountainPen, str)
        self.assertIsInstance(PencilKit.PKInkTypeWatercolor, str)
        self.assertIsInstance(PencilKit.PKInkTypeCrayon, str)
