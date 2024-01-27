from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLEvaluationPlan(TestCase):
    @min_os_level("14.4")
    def test_classes(self):
        self.assertTrue(CoreML.MLEvaluationPlan.__objc_final__)

    @min_os_level("14.4")
    def test_methods14_4(self):
        self.assertArgIsOut(
            CoreML.MLEvaluationPlan.evaluationPlanOfModelStructure_configuration_error_,
            2,
        )
