import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


import SceneKit

SCNBufferBindingBlock = b"v@@@@"
SCNBindingBlock = b"v" + objc._C_UINT + objc._C_UINT + b"@@"


class TestSCNShadableHelper(SceneKit.NSObject):
    def writeBytes_length_(self, b, l):
        pass

    def handleBindingOfSymbol_usingBlock_(self, s, b):
        pass

    def handleUnbindingOfSymbol_usingBlock_(self, s, b):
        pass

    def program_bindValueForSymbol_atLocation_programID_renderer_(self, p, s, l, pp, r):
        return 1

    def program_unbindValueForSymbol_atLocation_programID_renderer_(
        self, p, s, l, pp, r
    ):
        return 1

    def programIsOpaque_(self, p):
        return 1


class TestSCNShadable(TestCase):
    def test_constants(self):
        self.assertEqual(SceneKit.SCNBufferFrequencyPerFrame, 0)
        self.assertEqual(SceneKit.SCNBufferFrequencyPerNode, 1)
        self.assertEqual(SceneKit.SCNBufferFrequencyPerShadable, 2)

        self.assertIsInstance(SceneKit.SCNProgramMappingChannelKey, str)

    def test_constants10_9(self):
        self.assertIsInstance(SceneKit.SCNShaderModifierEntryPointGeometry, str)
        self.assertIsInstance(SceneKit.SCNShaderModifierEntryPointSurface, str)
        self.assertIsInstance(SceneKit.SCNShaderModifierEntryPointLightingModel, str)
        self.assertIsInstance(SceneKit.SCNShaderModifierEntryPointFragment, str)

    def testProtocols(self):
        objc.protocolNamed("SCNShadable")

    @min_sdk_level("10.10")
    def testProtocols10_10(self):
        objc.protocolNamed("SCNProgramDelegate")

    @min_sdk_level("10.11")
    def testProtocols10_11(self):
        objc.protocolNamed("SCNBufferStream")

    def testMethods(self):
        self.assertArgHasType(TestSCNShadableHelper.writeBytes_length_, 0, b"n^v")
        self.assertArgHasType(
            TestSCNShadableHelper.writeBytes_length_, 1, objc._C_NSUInteger
        )
        self.assertArgSizeInArg(TestSCNShadableHelper.writeBytes_length_, 0, 1)

        self.assertArgIsBlock(
            TestSCNShadableHelper.handleBindingOfSymbol_usingBlock_, 1, SCNBindingBlock
        )
        self.assertArgIsBlock(
            TestSCNShadableHelper.handleUnbindingOfSymbol_usingBlock_,
            1,
            SCNBindingBlock,
        )

        self.assertResultIsBOOL(
            TestSCNShadableHelper.program_bindValueForSymbol_atLocation_programID_renderer_
        )
        self.assertArgHasType(
            TestSCNShadableHelper.program_bindValueForSymbol_atLocation_programID_renderer_,
            2,
            objc._C_UINT,
        )
        self.assertArgHasType(
            TestSCNShadableHelper.program_bindValueForSymbol_atLocation_programID_renderer_,
            3,
            objc._C_UINT,
        )

        self.assertResultIsBOOL(
            TestSCNShadableHelper.program_unbindValueForSymbol_atLocation_programID_renderer_
        )
        self.assertArgHasType(
            TestSCNShadableHelper.program_unbindValueForSymbol_atLocation_programID_renderer_,
            2,
            objc._C_UINT,
        )
        self.assertArgHasType(
            TestSCNShadableHelper.program_unbindValueForSymbol_atLocation_programID_renderer_,
            3,
            objc._C_UINT,
        )

        self.assertResultIsBOOL(TestSCNShadableHelper.programIsOpaque_)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(SceneKit.SCNProgram.isOpaque)
        self.assertArgIsBOOL(SceneKit.SCNProgram.setOpaque_, 0)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertArgIsBlock(
            SceneKit.SCNProgram.handleBindingOfBufferNamed_frequency_usingBlock_,
            2,
            SCNBufferBindingBlock,
        )
