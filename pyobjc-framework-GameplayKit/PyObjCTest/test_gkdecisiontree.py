from PyObjCTools.TestSupport import TestCase, min_os_level

import GameplayKit


class TestGKDecisionTree(TestCase):
    @min_os_level("10.13")
    def testMethods(self):
        self.assertResultIsBOOL(GameplayKit.GKDecisionTree.exportToURL_error_)
