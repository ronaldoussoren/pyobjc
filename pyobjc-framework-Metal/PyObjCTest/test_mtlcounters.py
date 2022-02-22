import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestMTLCountersHelper(Metal.NSObject):
    def sampleCount(self):
        return 1

    def resolveCounterRange_(self, a):
        return 1


class TestMTLCounters(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Metal.MTLCounterSampleBufferError)

    def test_typed_enum(self):
        self.assertIsTypedEnum(Metal.MTLCommonCounter, str)
        self.assertIsTypedEnum(Metal.MTLCommonCounterSet, str)

    def test_constants(self):
        self.assertEqual(Metal.MTLCounterErrorValue, 0xFFFFFFFFFFFFFFFF)

        self.assertEqual(Metal.MTLCounterSampleBufferErrorOutOfMemory, 0)
        self.assertEqual(Metal.MTLCounterSampleBufferErrorInvalid, 1)
        self.assertEqual(Metal.MTLCounterSampleBufferErrorInternal, 2)

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(Metal.MTLCommonCounterTimestamp, str)
        self.assertIsInstance(Metal.MTLCommonCounterTessellationInputPatches, str)
        self.assertIsInstance(Metal.MTLCommonCounterVertexInvocations, str)
        self.assertIsInstance(
            Metal.MTLCommonCounterPostTessellationVertexInvocations, str
        )
        self.assertIsInstance(Metal.MTLCommonCounterClipperInvocations, str)
        self.assertIsInstance(Metal.MTLCommonCounterClipperPrimitivesOut, str)
        self.assertIsInstance(Metal.MTLCommonCounterFragmentInvocations, str)
        self.assertIsInstance(Metal.MTLCommonCounterFragmentsPassed, str)
        self.assertIsInstance(Metal.MTLCommonCounterComputeKernelInvocations, str)
        self.assertIsInstance(Metal.MTLCommonCounterTotalCycles, str)
        self.assertIsInstance(Metal.MTLCommonCounterVertexCycles, str)
        self.assertIsInstance(Metal.MTLCommonCounterTessellationCycles, str)
        self.assertIsInstance(Metal.MTLCommonCounterPostTessellationVertexCycles, str)
        self.assertIsInstance(Metal.MTLCommonCounterFragmentCycles, str)
        self.assertIsInstance(Metal.MTLCommonCounterRenderTargetWriteCycles, str)

        self.assertIsInstance(Metal.MTLCommonCounterSetTimestamp, str)
        self.assertIsInstance(Metal.MTLCommonCounterSetStageUtilization, str)
        self.assertIsInstance(Metal.MTLCommonCounterSetStatistic, str)

        self.assertIsInstance(Metal.MTLCounterErrorDomain, str)

    def test_structs(self):
        v = Metal.MTLCounterResultTimestamp()
        self.assertEqual(v.timestamp, 0)
        self.assertPickleRoundTrips(v)

        v = Metal.MTLCounterResultStageUtilization()
        self.assertEqual(v.totalCycles, 0)
        self.assertEqual(v.vertexCycles, 0)
        self.assertEqual(v.tessellationCycles, 0)
        self.assertEqual(v.postTessellationVertexCycles, 0)
        self.assertEqual(v.fragmentCycles, 0)
        self.assertEqual(v.renderTargetCycles, 0)
        self.assertPickleRoundTrips(v)

        v = Metal.MTLCounterResultStatistic()
        self.assertEqual(v.tessellationInputPatches, 0)
        self.assertEqual(v.vertexInvocations, 0)
        self.assertEqual(v.postTessellationVertexInvocations, 0)
        self.assertEqual(v.clipperInvocations, 0)
        self.assertEqual(v.clipperPrimitivesOut, 0)
        self.assertEqual(v.fragmentInvocations, 0)
        self.assertEqual(v.fragmentsPassed, 0)
        self.assertEqual(v.computeKernelInvocations, 0)
        self.assertPickleRoundTrips(v)

    @min_sdk_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("MTLCounter")
        objc.protocolNamed("MTLCounterSet")
        objc.protocolNamed("MTLCounterSampleBuffer")

    def test_methods(self):
        self.assertResultHasType(TestMTLCountersHelper.sampleCount, objc._C_NSUInteger)
        self.assertArgHasType(
            TestMTLCountersHelper.resolveCounterRange_, 0, Metal.NSRange.__typestr__
        )
