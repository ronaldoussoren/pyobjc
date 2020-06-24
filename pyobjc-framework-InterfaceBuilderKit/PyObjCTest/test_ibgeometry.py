import InterfaceBuilderKit
from PyObjCTools.TestSupport import TestCase


class TestIBGeometry(TestCase):
    def testConstants(self):
        self.assertEqual(InterfaceBuilderKit.IBNoDirection, 0)
        self.assertEqual(InterfaceBuilderKit.IBMinXDirection, 1)
        self.assertEqual(InterfaceBuilderKit.IBMaxXDirection, 2)
        self.assertEqual(InterfaceBuilderKit.IBMinYDirection, 4)
        self.assertEqual(InterfaceBuilderKit.IBMaxYDirection, 8)
        self.assertEqual(
            InterfaceBuilderKit.IBMinXMinYDirection,
            (InterfaceBuilderKit.IBMinXDirection | InterfaceBuilderKit.IBMinYDirection),
        )
        self.assertEqual(
            InterfaceBuilderKit.IBMinXMaxYDirection,
            (InterfaceBuilderKit.IBMinXDirection | InterfaceBuilderKit.IBMaxYDirection),
        )
        self.assertEqual(
            InterfaceBuilderKit.IBMaxXMinYDirection,
            (InterfaceBuilderKit.IBMaxXDirection | InterfaceBuilderKit.IBMinYDirection),
        )
        self.assertEqual(
            InterfaceBuilderKit.IBMaxXMaxYDirection,
            (InterfaceBuilderKit.IBMaxXDirection | InterfaceBuilderKit.IBMaxYDirection),
        )

    def testStructs(self):
        o = InterfaceBuilderKit.IBInset()
        self.assertHasAttr(o, "left")
        self.assertHasAttr(o, "top")
        self.assertHasAttr(o, "right")
        self.assertHasAttr(o, "bottom")
        self.assertIsInstance(o.left, float)
        self.assertIsInstance(o.top, float)
        self.assertIsInstance(o.right, float)
        self.assertIsInstance(o.bottom, float)
