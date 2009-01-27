
from PyObjCTools.TestSupport import *
from InterfaceBuilderKit import *

class TestIBGeometry (TestCase):
    def testConstants(self):
        self.failUnlessEqual(IBNoDirection, 0)
        self.failUnlessEqual(IBMinXDirection, 1)
        self.failUnlessEqual(IBMaxXDirection, 2)
        self.failUnlessEqual(IBMinYDirection, 4)
        self.failUnlessEqual(IBMaxYDirection, 8)
        self.failUnlessEqual(IBMinXMinYDirection, (IBMinXDirection | IBMinYDirection))
        self.failUnlessEqual(IBMinXMaxYDirection, (IBMinXDirection | IBMaxYDirection))
        self.failUnlessEqual(IBMaxXMinYDirection, (IBMaxXDirection | IBMinYDirection))
        self.failUnlessEqual(IBMaxXMaxYDirection, (IBMaxXDirection | IBMaxYDirection))

    def testStructs(self):
        o = IBInset()
        self.failUnless(hasattr(o, 'left'))
        self.failUnless(hasattr(o, 'top'))
        self.failUnless(hasattr(o, 'right'))
        self.failUnless(hasattr(o, 'bottom'))
        self.failUnlessIsInstance(o.left, float)
        self.failUnlessIsInstance(o.top, float)
        self.failUnlessIsInstance(o.right, float)
        self.failUnlessIsInstance(o.bottom, float)

if __name__ == "__main__":
    main()
