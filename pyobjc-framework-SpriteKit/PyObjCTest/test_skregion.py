import sys

import objc
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import SpriteKit

    class TestSKRegion(TestCase):
        @min_os_level("10.10")
        def testMethods(self):
            self.assertResultIsBOOL(SpriteKit.SKRegion.containsPoint_)


if __name__ == "__main__":
    main()
