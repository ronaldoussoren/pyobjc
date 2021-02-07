from PyObjCTools.TestSupport import TestCase

import MLCompute


class TestMLCGraph(TestCase):
    def test_methods(self):
        self.assertArgIsBOOL(MLCompute.MLCGraph.nodeWithLayer_sources_disableUpdate_, 2)

        self.assertResultIsBOOL(
            MLCompute.MLCGraph.bindAndWriteData_forInputs_toDevice_batchSize_synchronous_
        )
        self.assertArgIsBOOL(
            MLCompute.MLCGraph.bindAndWriteData_forInputs_toDevice_batchSize_synchronous_,
            4,
        )

        self.assertResultIsBOOL(
            MLCompute.MLCGraph.bindAndWriteData_forInputs_toDevice_synchronous_
        )
        self.assertArgIsBOOL(
            MLCompute.MLCGraph.bindAndWriteData_forInputs_toDevice_synchronous_, 3
        )
