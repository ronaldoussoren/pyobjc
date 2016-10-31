import sys

from PyObjCTools.TestSupport import *
import objc

if sys.maxsize > 2 ** 32:

    import SpriteKit
    class TestSKConstraint (TestCase):

        @min_os_level("10.10")
        def testMethods(self):
            self.assertArgIsBOOL(SpriteKit.SKConstraint.setEnabled_, 0)
            self.assertResultIsBOOL(SpriteKit.SKConstraint.enabled)

if __name__ == "__main__":
    main()
