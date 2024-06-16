from PyObjCTools.TestSupport import TestCase

import Metal


class TestMTLResidencySetHelper(Metal.NSObject):
    def allocatedSize(self):
        return 1

    def addAllocations_count_(self, a, b):
        pass

    def removeAllocations_count_(self, a, b):
        pass

    def containsAllocation_(self):
        return 1

    def allocationCount(self):
        return 1


class TestMTLResidencySet(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("MTLResidencySet")

    def test_protocol_methods(self):
        self.assertResultHasType(TestMTLResidencySetHelper.allocatedSize, b"Q")

        self.assertArgHasType(
            TestMTLResidencySetHelper.addAllocations_count_, 0, b"n^@"
        )
        self.assertArgHasType(TestMTLResidencySetHelper.addAllocations_count_, 1, b"Q")

        self.assertArgHasType(
            TestMTLResidencySetHelper.removeAllocations_count_, 0, b"n^@"
        )
        self.assertArgHasType(
            TestMTLResidencySetHelper.removeAllocations_count_, 1, b"Q"
        )

        self.assertResultIsBOOL(TestMTLResidencySetHelper.containsAllocation_)
        self.assertResultHasType(TestMTLResidencySetHelper.allocationCount, b"Q")
