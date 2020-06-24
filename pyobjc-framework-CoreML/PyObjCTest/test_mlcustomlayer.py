import objc

from PyObjCTools.TestSupport import TestCase, min_sdk_level
import CoreML


class TestMLCustomLayerHelper(CoreML.NSObject):
    def initWithParameterDictionary_error_(self, p, e):
        pass

    def setWeightData_error_(self, w, e):
        return 1

    def outputShapesForInputShapes_error_(self, w, e):
        return 1

    def evaluateOnCPUWithInputs_outputs_error_(self, i, o, e):
        return 1

    def encodeToCommandBuffer_inputs_outputs_error_(self, b, i, o, e):
        return 1


class TestMLCustomLayer(TestCase):
    @min_sdk_level("10.13")
    def testProtocols(self):
        objc.protocolNamed("MLCustomLayer")

    def testMethods(self):
        self.assertArgHasType(
            TestMLCustomLayerHelper.initWithParameterDictionary_error_, 1, b"o^@"
        )

        self.assertArgHasType(TestMLCustomLayerHelper.setWeightData_error_, 1, b"o^@")
        self.assertResultIsBOOL(TestMLCustomLayerHelper.setWeightData_error_)

        self.assertArgHasType(
            TestMLCustomLayerHelper.outputShapesForInputShapes_error_, 1, b"o^@"
        )

        self.assertArgHasType(
            TestMLCustomLayerHelper.evaluateOnCPUWithInputs_outputs_error_, 2, b"o^@"
        )
        self.assertResultIsBOOL(
            TestMLCustomLayerHelper.evaluateOnCPUWithInputs_outputs_error_
        )

        self.assertArgHasType(
            TestMLCustomLayerHelper.encodeToCommandBuffer_inputs_outputs_error_,
            3,
            b"o^@",
        )
        self.assertResultIsBOOL(
            TestMLCustomLayerHelper.encodeToCommandBuffer_inputs_outputs_error_
        )
