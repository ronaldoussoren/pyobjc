
from PyObjCTools.TestSupport import *
from InterfaceBuilderKit import *

class TestIBGeometry (TestCase):
    def testConstants(self):
        self.assertEqual(IBNoDirection, 0)
        self.assertEqual(IBMinXDirection, 1)
        self.assertEqual(IBMaxXDirection, 2)
        self.assertEqual(IBMinYDirection, 4)
        self.assertEqual(IBMaxYDirection, 8)
        self.assertEqual(IBMinXMinYDirection, (IBMinXDirection | IBMinYDirection))
        self.assertEqual(IBMinXMaxYDirection, (IBMinXDirection | IBMaxYDirection))
        self.assertEqual(IBMaxXMinYDirection, (IBMaxXDirection | IBMinYDirection))
        self.assertEqual(IBMaxXMaxYDirection, (IBMaxXDirection | IBMaxYDirection))

    def testStructs(self):
        o = IBInset()
        self.assertHasAttr(o, 'left')
        self.assertHasAttr(o, 'top')
        self.assertHasAttr(o, 'right')
        self.assertHasAttr(o, 'bottom')
        self.assertIsInstance(o.left, float)
        self.assertIsInstance(o.top, float)
        self.assertIsInstance(o.right, float)
        self.assertIsInstance(o.bottom, float)

if __name__ == "__main__":
    main()
