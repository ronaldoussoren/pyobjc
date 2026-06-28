from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCAReplicatorLayer(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Quartz.CAReplicatorLayer.preservesDepth)
        self.assertArgIsBOOL(Quartz.CAReplicatorLayer.setPreservesDepth_, 0)
