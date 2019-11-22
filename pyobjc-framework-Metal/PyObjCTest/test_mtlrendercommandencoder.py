from PyObjCTools.TestSupport import *

import Metal

class TestMTLRenderCommandEncoderHelper (Metal.NSObject):
    def setVertexBytes_length_atIndex_(self, a, b, c): pass
    def setVertexBuffer_offset_atIndex_(self, a, b, c): pass
    def setVertexBufferOffset_atIndex_(self, a, b): pass

class TestMTLRenderCommandEncoder (TestCase):
    def test_constants(self):
        self.assertEqual(Metal.MTLPrimitiveTypePoint, 0)
        self.assertEqual(Metal.MTLPrimitiveTypeLine, 1)
        self.assertEqual(Metal.MTLPrimitiveTypeLineStrip, 2)
        self.assertEqual(Metal.MTLPrimitiveTypeTriangle, 3)
        self.assertEqual(Metal.MTLPrimitiveTypeTriangleStrip, 4)

        self.assertEqual(Metal.MTLVisibilityResultModeDisabled, 0)
        self.assertEqual(Metal.MTLVisibilityResultModeBoolean, 1)
        self.assertEqual(Metal.MTLVisibilityResultModeCounting, 2)

        self.assertEqual(Metal.MTLCullModeNone, 0)
        self.assertEqual(Metal.MTLCullModeFront, 1)
        self.assertEqual(Metal.MTLCullModeBack, 2)

        self.assertEqual(Metal.MTLWindingClockwise, 0)
        self.assertEqual(Metal.MTLWindingCounterClockwise, 1)

        self.assertEqual(Metal.MTLDepthClipModeClip, 0)
        self.assertEqual(Metal.MTLDepthClipModeClamp, 1)

        self.assertEqual(Metal.MTLTriangleFillModeFill, 0)
        self.assertEqual(Metal.MTLTriangleFillModeLines, 1)

        self.assertEqual(Metal.MTLRenderStageVertex, 1 << 0)
        self.assertEqual(Metal.MTLRenderStageFragment, 1 << 1)

    def test_structs(self):
        v = Metal.MTLScissorRect()
        self.assertEqual(v.x, 0)
        self.assertEqual(v.y, 0)
        self.assertEqual(v.width, 0)
        self.assertEqual(v.height, 0)

        v = Metal.MTLViewport()
        self.assertEqual(v.originX, 0)
        self.assertEqual(v.originY, 0)
        self.assertEqual(v.width, 0)
        self.assertEqual(v.height, 0)
        self.assertEqual(v.znear, 0)
        self.assertEqual(v.zfar, 0)

        v = Metal.MTLDrawPrimitivesIndirectArguments()
        self.assertEqual(v.vertexCount, 0)
        self.assertEqual(v.instanceCount, 0)
        self.assertEqual(v.vertexStart, 0)
        self.assertEqual(v.baseInstance, 0)

        v = Metal.MTLDrawIndexedPrimitivesIndirectArguments()
        self.assertEqual(v.indexCount, 0)
        self.assertEqual(v.insetanceCount, 0)
        self.assertEqual(v.indexStart, 0)
        self.assertEqual(v.baseVertex, 0)
        self.assertEqual(v.baseInstance, 0)

        v = Metal.MTLDrawPatchIndirectArguments()
        self.assertEqual(v.patchCount, 0)
        self.assertEqual(v.instanceCount, 0)
        self.assertEqual(v.patchStart, 0)
        self.assertEqual(v.baseInstance, 0)

        v = Metal.MTLQuadTessellationFactorsHalf()
        self.assertEqual(v.edgeTessellationFactor, None)
        self.assertEqual(v.insideTessellationFactor, None)

        v = Metal.MTLTriangleTessellationFactorsHalf()
        self.assertEqual(v.edgeTessellationFactor, None)
        self.assertEqual(v.insideTessellationFactor, 0)

    @min_sdk_level('10.11')
    def test_protocols(self):
        objc.protocolNamed('MTLRenderCommandEncoder')

    def test_methods(self):
        self.assertArgHasType(TestMTLRenderCommandEncoderHelper.setVertexBytes_length_atIndex_, 0, b'n^v')
        self.assertArgSizeInArg(TestMTLRenderCommandEncoderHelper.setVertexBytes_length_atIndex_, 0, 1)
        self.assertArgHasType(TestMTLRenderCommandEncoderHelper.setVertexBytes_length_atIndex_, 1, objc._C_NSUInteger)
        self.assertArgHasType(TestMTLRenderCommandEncoderHelper.setVertexBytes_length_atIndex_, 2, objc._C_NSUInteger)

        self.assertArgHasType(TestMTLRenderCommandEncoderHelper.setVertexBuffer_offset_atIndex_, 1, objc._C_NSUInteger)
        self.assertArgHasType(TestMTLRenderCommandEncoderHelper.setVertexBuffer_offset_atIndex_, 2, objc._C_NSUInteger)

        self.assertArgHasType(TestMTLRenderCommandEncoderHelper.setVertexBufferOffset_atIndex_, 0, objc._C_NSUInteger)
        self.assertArgHasType(TestMTLRenderCommandEncoderHelper.setVertexBufferOffset_atIndex_, 1, objc._C_NSUInteger)
        # XXX
