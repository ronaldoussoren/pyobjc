import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestMTLRenderPass(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Metal.MTLLoadAction)
        self.assertIsEnumType(Metal.MTLMultisampleDepthResolveFilter)
        self.assertIsEnumType(Metal.MTLMultisampleStencilResolveFilter)
        self.assertIsEnumType(Metal.MTLStoreAction)
        self.assertIsEnumType(Metal.MTLStoreActionOptions)

    def test_constants(self):
        self.assertEqual(Metal.MTLCounterDontSample, 0xFFFFFFFFFFFFFFFF)
        self.assertEqual(Metal.MTLMaxRenderPassSampleBuffers, 4)

        self.assertEqual(Metal.MTLLoadActionDontCare, 0)
        self.assertEqual(Metal.MTLLoadActionLoad, 1)
        self.assertEqual(Metal.MTLLoadActionClear, 2)

        self.assertEqual(Metal.MTLStoreActionDontCare, 0)
        self.assertEqual(Metal.MTLStoreActionStore, 1)
        self.assertEqual(Metal.MTLStoreActionMultisampleResolve, 2)
        self.assertEqual(Metal.MTLStoreActionStoreAndMultisampleResolve, 3)
        self.assertEqual(Metal.MTLStoreActionUnknown, 4)
        self.assertEqual(Metal.MTLStoreActionCustomSampleDepthStore, 5)

        self.assertEqual(Metal.MTLStoreActionOptionNone, 0)
        self.assertEqual(Metal.MTLStoreActionOptionCustomSamplePositions, 1 << 0)

        self.assertEqual(Metal.MTLMultisampleDepthResolveFilterSample0, 0)
        self.assertEqual(Metal.MTLMultisampleDepthResolveFilterMin, 1)
        self.assertEqual(Metal.MTLMultisampleDepthResolveFilterMax, 2)

        self.assertEqual(Metal.MTLMultisampleStencilResolveFilterSample0, 0)
        self.assertEqual(Metal.MTLMultisampleStencilResolveFilterDepthResolvedSample, 1)

    def test_structs(self):
        v = Metal.MTLClearColor()
        self.assertEqual(v.red, 0.0)
        self.assertEqual(v.green, 0.0)
        self.assertEqual(v.blue, 0.0)
        self.assertEqual(v.alpha, 0.0)
        self.assertPickleRoundTrips(v)

    def test_functions(self):
        v = Metal.MTLClearColorMake(1, 2, 3, 4)
        self.assertIsInstance(v, Metal.MTLClearColor)
        self.assertEqual(v, (1.0, 2.0, 3.0, 4.0))

    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertArgIsIn(Metal.MTLRenderPassDescriptor.setSamplePositions_count_, 0)
        self.assertArgSizeInArg(
            Metal.MTLRenderPassDescriptor.setSamplePositions_count_, 0, 1
        )

        self.assertArgIsOut(Metal.MTLRenderPassDescriptor.getSamplePositions_count_, 0)
        self.assertArgSizeInArg(
            Metal.MTLRenderPassDescriptor.getSamplePositions_count_, 0, 1
        )
        self.assertArgSizeInResult(
            Metal.MTLRenderPassDescriptor.getSamplePositions_count_, 0
        )
