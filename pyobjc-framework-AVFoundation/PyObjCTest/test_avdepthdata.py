from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVDepthData (TestCase):
    def testConstants(self):
        self.assertEqual(AVFoundation.AVDepthDataQualityLow, 0)
        self.assertEqual(AVFoundation.AVDepthDataQualityHigh, 1)

        self.assertEqual(AVFoundation.AVDepthDataAccuracyRelative, 0)
        self.assertEqual(AVFoundation.AVDepthDataAccuracyAbsolute, 1)

    @min_os_level('10.13')
    def testMethods10_13(self):
        self.assertArgIsOut(AVFoundation.AVDepthData.depthDataFromDictionaryRepresentation_error_, 1)
        self.assertArgIsOut(AVFoundation.AVDepthData.depthDataByReplacingDepthDataMapWithPixelBuffer_error_, 1)
        self.assertArgIsOut(AVFoundation.AVDepthData.dictionaryRepresentationForAuxiliaryDataType_, 0)
        self.assertResultIsBOOL(AVFoundation.AVDepthData.isDepthDataFiltered)


if __name__ == "__main__":
    main()
