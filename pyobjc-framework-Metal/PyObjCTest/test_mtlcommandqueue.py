import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTLCommandQueueHelper(Metal.NSObject):
    def addResidencySets_count_(self, a, b):
        pass


class TestMTLCommandQueue(TestCase):
    @min_sdk_level("10.11")
    def test_protocols(self):
        self.assertProtocolExists("MTLCommandQueue")

    def test_protocol_methos(self):
        self.assertArgIsIn(TestMTLCommandQueueHelper.addResidencySets_count_, 0)
        self.assertArgSizeInArg(TestMTLCommandQueueHelper.addResidencySets_count_, 0, 1)
        self.assertArgHasType(
            TestMTLCommandQueueHelper.addResidencySets_count_, 1, b"Q"
        )

        self.assertArgIsIn(TestMTLCommandQueueHelper.removeResidencySets_count_, 0)
        self.assertArgSizeInArg(
            TestMTLCommandQueueHelper.removeResidencySets_count_, 0, 1
        )
        self.assertArgHasType(
            TestMTLCommandQueueHelper.removeResidencySets_count_, 1, b"Q"
        )
