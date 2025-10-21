import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTLResourceViewPoolHelper(Metal.NSObject):
    def baseResourceID(self):
        return 1

    def resourceViewCount(self):
        return 1

    def copyResourceViewsFromPool_sourceRange_destinationIndex_(self, a, b, c):
        return 1


class TestMTLResourceViewPool(TestCase):
    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("MTLResourceViewPool")

    def test_protocol_methods(self):
        self.assertResultHasType(
            TestMTLResourceViewPoolHelper.baseResourceID,
            Metal.MTLResourceID.__typestr__,
        )
        self.assertResultHasType(TestMTLResourceViewPoolHelper.resourceViewCount, b"Q")

        self.assertArgHasType(
            TestMTLResourceViewPoolHelper.copyResourceViewsFromPool_sourceRange_destinationIndex_,
            1,
            Metal.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestMTLResourceViewPoolHelper.copyResourceViewsFromPool_sourceRange_destinationIndex_,
            2,
            b"Q",
        )
