from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCAReplicatorLayer(TestCase):
    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(Quartz.CAReplicatorLayer.preservesDepth)
        self.assertArgIsBOOL(Quartz.CAReplicatorLayer.setPreservesDepth_, 0)
