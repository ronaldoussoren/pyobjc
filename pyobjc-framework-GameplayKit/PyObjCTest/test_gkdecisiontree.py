from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import GameplayKit

    class TestGKDecisionTree (TestCase):
        @min_os_level('10.13')
        def testMethods(self):
            self.assertResultIsBOOL(GameplayKit.GKDecisionTree.exportToURL_error_)

if __name__ == "__main__":
    main()
