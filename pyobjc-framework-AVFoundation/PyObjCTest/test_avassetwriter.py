import AVFoundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestAVAssetWriterHelper(AVFoundation.NSObject):
    def assetWriter_didOutputSegmentData_segmentType_segmentReport_(self, a, b, c, d):
        pass

    def assetWriter_didOutputSegmentData_segmentType_(self, a, b, c):
        pass


class TestAVAssetWriter(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVAssetWriterStatus)

    @min_os_level("10.7")
    def testConstants(self):
        self.assertEqual(AVFoundation.AVAssetWriterStatusUnknown, 0)
        self.assertEqual(AVFoundation.AVAssetWriterStatusWriting, 1)
        self.assertEqual(AVFoundation.AVAssetWriterStatusCompleted, 2)
        self.assertEqual(AVFoundation.AVAssetWriterStatusFailed, 3)
        self.assertEqual(AVFoundation.AVAssetWriterStatusCancelled, 4)

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertArgIsBlock(
            AVFoundation.AVAssetWriter.finishWritingWithCompletionHandler_, 0, b"v"
        )
        self.assertResultIsBOOL(AVFoundation.AVAssetWriter.canAddInputGroup_)

    @min_os_level("10.7")
    def testMethods(self):
        self.assertArgIsOut(
            AVFoundation.AVAssetWriter.assetWriterWithURL_fileType_error_, 2
        )
        self.assertArgIsOut(AVFoundation.AVAssetWriter.initWithURL_fileType_error_, 2)

        self.assertResultIsBOOL(AVFoundation.AVAssetWriter.shouldOptimizeForNetworkUse)
        self.assertArgIsBOOL(
            AVFoundation.AVAssetWriter.setShouldOptimizeForNetworkUse_, 0
        )

        self.assertResultIsBOOL(
            AVFoundation.AVAssetWriter.canApplyOutputSettings_forMediaType_
        )
        self.assertResultIsBOOL(AVFoundation.AVAssetWriter.canAddInput_)
        self.assertResultIsBOOL(AVFoundation.AVAssetWriter.startWriting)
        self.assertResultIsBOOL(AVFoundation.AVAssetWriter.finishWriting)

    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetWriter.producesCombinableFragments)
        self.assertArgIsBOOL(
            AVFoundation.AVAssetWriter.setProducesCombinableFragments_, 0
        )

    @min_sdk_level("11.0")
    def test_protocols(self):
        self.assertProtocolExists("AVAssetWriterDelegate")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestAVAssetWriterHelper.assetWriter_didOutputSegmentData_segmentType_segmentReport_,
            2,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestAVAssetWriterHelper.assetWriter_didOutputSegmentData_segmentType_,
            2,
            objc._C_NSInteger,
        )
