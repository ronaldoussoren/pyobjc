from PyObjCTools.TestSupport import *

import Metal


class TestMTLCountersHelper(Metal.NSObject):
    def sampleCount(self):
        return 1

    def resolveCounterRange_(self, a):
        return 1


class TestMTLCounters(TestCase):
    def test_constants(self):
        self.assertEqual(Metal.MTLCounterErrorValue, 0xFFFFFFFFFFFFFFFF)

        self.assertEqual(Metal.MTLCounterSampleBufferErrorOutOfMemory, 0)
        self.assertEqual(Metal.MTLCounterSampleBufferErrorInternal, 1)

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(Metal.MTLCommonCounterTimestamp, unicode)
        self.assertIsInstance(Metal.MTLCommonCounterTessellationInputPatches, unicode)
        self.assertIsInstance(Metal.MTLCommonCounterVertexInvocations, unicode)
        self.assertIsInstance(
            Metal.MTLCommonCounterPostTessellationVertexInvocations, unicode
        )
        self.assertIsInstance(Metal.MTLCommonCounterClipperInvocations, unicode)
        self.assertIsInstance(Metal.MTLCommonCounterClipperPrimitivesOut, unicode)
        self.assertIsInstance(Metal.MTLCommonCounterFragmentInvocations, unicode)
        self.assertIsInstance(Metal.MTLCommonCounterFragmentsPassed, unicode)
        self.assertIsInstance(Metal.MTLCommonCounterComputeKernelInvocations, unicode)
        self.assertIsInstance(Metal.MTLCommonCounterTotalCycles, unicode)
        self.assertIsInstance(Metal.MTLCommonCounterVertexCycles, unicode)
        self.assertIsInstance(Metal.MTLCommonCounterTessellationCycles, unicode)
        self.assertIsInstance(
            Metal.MTLCommonCounterPostTessellationVertexCycles, unicode
        )
        self.assertIsInstance(Metal.MTLCommonCounterFragmentCycles, unicode)
        self.assertIsInstance(Metal.MTLCommonCounterRenderTargetWriteCycles, unicode)

        self.assertIsInstance(Metal.MTLCommonCounterSetTimestamp, unicode)
        self.assertIsInstance(Metal.MTLCommonCounterSetStageUtilization, unicode)
        self.assertIsInstance(Metal.MTLCommonCounterSetStatistic, unicode)

        self.assertIsInstance(Metal.MTLCounterErrorDomain, unicode)

    def test_structs(self):
        v = Metal.MTLCounterResultTimestamp()
        self.assertEqual(v.timestamp, 0)

        v = Metal.MTLCounterResultStageUtilization()
        self.assertEqual(v.totalCycles, 0)
        self.assertEqual(v.vertexCycles, 0)
        self.assertEqual(v.tessellationCycles, 0)
        self.assertEqual(v.postTessellationVertexCycles, 0)
        self.assertEqual(v.fragmentCycles, 0)
        self.assertEqual(v.renderTargetCycles, 0)

        v = Metal.MTLCounterResultStatistic()
        self.assertEqual(v.tessellationInputPatches, 0)
        self.assertEqual(v.vertexInvocations, 0)
        self.assertEqual(v.postTessellationVertexInvocations, 0)
        self.assertEqual(v.clipperInvocations, 0)
        self.assertEqual(v.clipperPrimitivesOut, 0)
        self.assertEqual(v.fragmentInvocations, 0)
        self.assertEqual(v.fragmentsPassed, 0)
        self.assertEqual(v.computeKernelInvocations, 0)

    @min_sdk_level("10.13")
    def test_protocols(self):
        objc.protocolNamed("MTLCounter")
        objc.protocolNamed("MTLCounterSet")
        objc.protocolNamed("MTLCounterSampleBuffer")

    def test_methods(self):
        self.assertResultHasType(TestMTLCountersHelper.sampleCount, objc._C_NSUInteger)
        self.assertArgHasType(
            TestMTLCountersHelper.resolveCounterRange_, 0, Metal.NSRange.__typestr__
        )
