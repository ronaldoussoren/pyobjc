from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import ModelIO

    class TestMDLMorphDeformer (TestCase):
        @min_sdk_level('10.13')
        def testProtocols(self):
            objc.protocolNamed('MDLMorphDeformerComponent')

        @min_os_level('10.13')
        def testMethods(self):
            self.assertArgIsIn(ModelIO.MDLMorphDeformer.initWithTargetShapes_shapeSetTargetWeights_count_shapeSetTargetCounts_count_, 1)
            self.assertArgSizeInArg(ModelIO.MDLMorphDeformer.initWithTargetShapes_shapeSetTargetWeights_count_shapeSetTargetCounts_count_, 1, 2)
            self.assertArgIsIn(ModelIO.MDLMorphDeformer.initWithTargetShapes_shapeSetTargetWeights_count_shapeSetTargetCounts_count_, 3)
            self.assertArgSizeInArg(ModelIO.MDLMorphDeformer.initWithTargetShapes_shapeSetTargetWeights_count_shapeSetTargetCounts_count_, 3, 4)

            self.assertArgIsOut(ModelIO.MDLMorphDeformer.copyShapeSetTargetWeightsInto_maxCount_, 0)
            self.assertArgSizeInArg(ModelIO.MDLMorphDeformer.copyShapeSetTargetWeightsInto_maxCount_, 0, 1)
            self.assertArgSizeInResult(ModelIO.MDLMorphDeformer.copyShapeSetTargetWeightsInto_maxCount_, 0)

            self.assertArgIsOut(ModelIO.MDLMorphDeformer.copyShapeSetTargetCountsInto_maxCount_, 0)
            self.assertArgSizeInArg(ModelIO.MDLMorphDeformer.copyShapeSetTargetCountsInto_maxCount_, 0, 1)
            self.assertArgSizeInResult(ModelIO.MDLMorphDeformer.copyShapeSetTargetCountsInto_maxCount_, 0)

if __name__ == "__main__":
    main()
