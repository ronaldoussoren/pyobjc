import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTL4CountersHelper(Metal.NSObject):
    def count(self):
        pass

    def type(self):  # noqa: A003
        pass

    def resolveCounterRange_(self, a):
        return 1

    def invalidateCounterRange_(self, a):
        return 1


class TestMTL4Counters(TestCase):
    def test_enum(self):
        self.assertIsEnumType(Metal.MTL4CounterHeapType)
        self.assertEqual(Metal.MTL4CounterHeapTypeInvalid, 0)
        self.assertEqual(Metal.MTL4CounterHeapTypeTimestamp, 1)

        self.assertIsEnumType(Metal.MTL4TimestampGranularity)
        self.assertEqual(Metal.MTL4TimestampGranularityRelaxed, 0)
        self.assertEqual(Metal.MTL4TimestampGranularityPrecise, 1)

    def test_structs(self):
        v = Metal.MTL4TimestampHeapEntry()
        self.assertIsInstance(v.timestamp, int)

    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("MTL4CounterHeap")

    def test_protocol_methods(self):
        self.assertResultHasType(TestMTL4CountersHelper.count, b"Q")
        self.assertResultHasType(TestMTL4CountersHelper.type, b"q")
        self.assertArgHasType(
            TestMTL4CountersHelper.resolveCounterRange_, 0, Metal.NSRange.__typestr__
        )
        self.assertArgHasType(
            TestMTL4CountersHelper.invalidateCounterRange_, 0, Metal.NSRange.__typestr__
        )
