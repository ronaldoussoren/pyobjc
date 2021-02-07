from PyObjCTools.TestSupport import TestCase

import MLCompute


class TestMLCTensor(TestCase):
    def test_methods(self):
        self.assertArgIsBOOL(
            MLCompute.MLCTensor.tensorWithSequenceLengths_sortedSequences_featureChannelCount_batchSize_randomInitializerType_,
            1,
        )
        self.assertArgIsBOOL(
            MLCompute.MLCTensor.tensorWithSequenceLengths_sortedSequences_featureChannelCount_batchSize_data_,
            1,
        )

        self.assertResultIsBOOL(MLCompute.MLCTensor.hasValidNumerics)
        self.assertResultIsBOOL(MLCompute.MLCTensor.synchronizeData)

        self.assertResultIsBOOL(
            MLCompute.MLCTensor.copyDataFromDeviceMemoryToBytes_length_synchronizeWithDevice_
        )
        self.assertArgIsBOOL(
            MLCompute.MLCTensor.copyDataFromDeviceMemoryToBytes_length_synchronizeWithDevice_,
            2,
        )

        self.assertResultIsBOOL(MLCompute.MLCTensor.bindAndWriteData_toDevice_)

        self.assertResultIsBOOL(MLCompute.MLCTensor.synchronizeOptimizerData)
        self.assertResultIsBOOL(MLCompute.MLCTensor.bindOptimizerData_deviceData_)
