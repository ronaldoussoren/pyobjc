from PyObjCTools.TestSupport import TestCase

import MediaExtension
import objc


class TestMEFormatReaderHelper(MediaExtension.NSObject):
    def formatReaderWithByteSource_options_error_(self, a, b, c):
        return 1

    def loadFileInfoWithCompletionHandler_(self, a):
        return 1

    def loadMetadataWithCompletionHandler_(self, a):
        return 1

    def loadTrackReadersWithCompletionHandler_(self, a):
        return 1

    def parseAdditionalFragmentsWithCompletionHandler_(self, a):
        return 1

    def loadTrackInfoWithCompletionHandler_(self, a):
        return 1

    def generateSampleCursorAtPresentationTimeStamp_completionHandler_(self, a, b):
        pass

    def generateSampleCursorAtFirstSampleInDecodeOrderWithCompletionHandler_(self, a):
        pass

    def generateSampleCursorAtLastSampleInDecodeOrderWithCompletionHandler_(self, a):
        pass

    def loadUneditedDurationWithCompletionHandler_(self, a):
        return 1

    def loadTotalSampleDataLengthWithCompletionHandler_(self, a):
        return 1

    def loadEstimatedDataRateWithCompletionHandler_(self, a):
        return 1

    def presentationTimeStamp(self):
        return 1

    def decodeTimeStamp(self):
        return 1

    def currentSampleDuration(self):
        return 1

    def currentSampleFormatDescription(self):
        return 1

    def stepInDecodeOrderByCount_completionHandler_(self, a, b):
        pass

    def stepInPresentationOrderByCount_completionHandler_(self, a, b):
        pass

    def stepByDecodeTime_completionHandler_(self, a, b):
        pass

    def stepByPresentationTime_completionHandler_(self, a, b):
        pass

    def syncInfo(self):
        return 1

    def dependencyInfo(self):
        return 1

    def hevcDependencyInfo(self):
        return 1

    def decodeTimeOfLastSampleReachableByForwardSteppingThatIsAlreadyLoadedByByteSource(
        self,
    ):
        return 1

    def samplesWithEarlierDTSsMayHaveLaterPTSsThanCursor_(self, a):
        return 1

    def samplesWithLaterDTSsMayHaveEarlierPTSsThanCursor_(self, a):
        return 1

    def chunkDetailsReturningError_(self, a):
        return 1

    def sampleLocationReturningError_(self, a):
        return 1

    def estimatedSampleLocationReturningError_(self, a):
        return 1

    def refineSampleLocation_refinementData_refinementDataLength_refinedLocation_error_(
        self, a, b, c, d, e
    ):
        return 1

    def loadSampleBufferContainingSamplesToEndCursor_completionHandler_(self, a, b):
        pass


class TestMEFormatReader(TestCase):
    def test_constants(self):
        self.assertIsEnumType(MediaExtension.MEFileInfoFragmentsStatus)
        self.assertEqual(MediaExtension.MEFileInfoCouldNotContainFragments, 0)
        self.assertEqual(MediaExtension.MEFileInfoContainsFragments, 1)
        self.assertEqual(
            MediaExtension.MEFileInfoCouldContainButDoesNotContainFragments, 2
        )

        self.assertIsEnumType(
            MediaExtension.MEFormatReaderParseAdditionalFragmentsStatus
        )
        self.assertEqual(
            MediaExtension.MEFormatReaderParseAdditionalFragmentsStatusSizeIncreased,
            1 << 0,
        )
        self.assertEqual(
            MediaExtension.MEFormatReaderParseAdditionalFragmentsStatusFragmentAdded,
            1 << 1,
        )
        self.assertEqual(
            MediaExtension.MEFormatReaderParseAdditionalFragmentsStatusFragmentsComplete,
            1 << 2,
        )

    def test_protocols(self):
        self.assertProtocolExists("MEFormatReaderExtension")
        self.assertProtocolExists("MEFormatReader")
        self.assertProtocolExists("METrackReader")
        self.assertProtocolExists("MESampleCursor")

    def test_methods(self):
        self.assertResultIsBOOL(
            MediaExtension.MEFormatReaderInstantiationOptions.allowIncrementalFragmentParsing
        )

        self.assertResultIsBOOL(MediaExtension.METrackInfo.isEnabled)
        self.assertArgIsBOOL(MediaExtension.METrackInfo.setEnabled_, 0)

        self.assertResultIsBOOL(MediaExtension.METrackInfo.requiresFrameReordering)
        self.assertArgIsBOOL(MediaExtension.METrackInfo.setRequiresFrameReordering_, 0)

        self.assertResultIsBOOL(
            MediaExtension.MEHEVCDependencyInfo.hasTemporalSubLayerAccess
        )
        self.assertArgIsBOOL(
            MediaExtension.MEHEVCDependencyInfo.setTemporalSubLayerAccess_, 0
        )

        self.assertResultIsBOOL(
            MediaExtension.MEHEVCDependencyInfo.hasStepwiseTemporalSubLayerAccess
        )
        self.assertArgIsBOOL(
            MediaExtension.MEHEVCDependencyInfo.setStepwiseTemporalSubLayerAccess_, 0
        )

        self.assertArgIsBlock(
            MediaExtension.MEByteSource.readDataOfLength_fromOffset_toDestination_completionHandler_,
            3,
            b"Q@",
        )
        self.assertArgIsBlock(
            MediaExtension.MEByteSource.readDataOfLength_fromOffset_completionHandler_,
            2,
            b"@@",
        )

        self.assertResultIsBOOL(
            MediaExtension.MEByteSource.readDataOfLength_fromOffset_toDestination_bytesRead_error_
        )
        self.assertArgIsOut(
            MediaExtension.MEByteSource.readDataOfLength_fromOffset_toDestination_bytesRead_error_,
            3,
        )
        self.assertArgIsOut(
            MediaExtension.MEByteSource.readDataOfLength_fromOffset_toDestination_bytesRead_error_,
            4,
        )

        self.assertArgIsOut(
            MediaExtension.MEByteSource.byteSourceForRelatedFileName_error_, 1
        )

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestMEFormatReaderHelper.formatReaderWithByteSource_options_error_, 2, "o^@"
        )

        self.assertArgIsBlock(
            TestMEFormatReaderHelper.loadFileInfoWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            TestMEFormatReaderHelper.loadMetadataWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            TestMEFormatReaderHelper.loadTrackReadersWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            TestMEFormatReaderHelper.parseAdditionalFragmentsWithCompletionHandler_,
            0,
            b"vQ@",
        )
        self.assertArgIsBlock(
            TestMEFormatReaderHelper.loadTrackInfoWithCompletionHandler_, 0, b"v@@"
        )

        self.assertArgHasType(
            TestMEFormatReaderHelper.generateSampleCursorAtPresentationTimeStamp_completionHandler_,
            0,
            MediaExtension.CMTime.__typestr__,
        )
        self.assertArgIsBlock(
            TestMEFormatReaderHelper.generateSampleCursorAtPresentationTimeStamp_completionHandler_,
            1,
            b"v@@",
        )

        self.assertArgIsBlock(
            TestMEFormatReaderHelper.generateSampleCursorAtFirstSampleInDecodeOrderWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            TestMEFormatReaderHelper.generateSampleCursorAtLastSampleInDecodeOrderWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            TestMEFormatReaderHelper.loadUneditedDurationWithCompletionHandler_,
            0,
            b"v" + MediaExtension.CMTime.__typestr__ + b"@",
        )
        self.assertArgIsBlock(
            TestMEFormatReaderHelper.loadTotalSampleDataLengthWithCompletionHandler_,
            0,
            b"vQ@",
        )
        self.assertArgIsBlock(
            TestMEFormatReaderHelper.loadEstimatedDataRateWithCompletionHandler_,
            0,
            b"vf@",
        )
        self.assertArgIsBlock(
            TestMEFormatReaderHelper.loadMetadataWithCompletionHandler_, 0, b"v@@"
        )
        self.assertResultHasType(
            TestMEFormatReaderHelper.presentationTimeStamp,
            MediaExtension.CMTime.__typestr__,
        )
        self.assertResultHasType(
            TestMEFormatReaderHelper.decodeTimeStamp, MediaExtension.CMTime.__typestr__
        )
        self.assertResultHasType(
            TestMEFormatReaderHelper.currentSampleDuration,
            MediaExtension.CMTime.__typestr__,
        )
        self.assertResultHasType(
            TestMEFormatReaderHelper.currentSampleFormatDescription, objc._C_ID
        )

        self.assertArgHasType(
            TestMEFormatReaderHelper.stepInDecodeOrderByCount_completionHandler_,
            0,
            b"Q",
        )
        self.assertArgIsBlock(
            TestMEFormatReaderHelper.stepInDecodeOrderByCount_completionHandler_,
            1,
            b"vQ@",
        )

        self.assertArgHasType(
            TestMEFormatReaderHelper.stepInPresentationOrderByCount_completionHandler_,
            0,
            b"Q",
        )
        self.assertArgIsBlock(
            TestMEFormatReaderHelper.stepInPresentationOrderByCount_completionHandler_,
            1,
            b"vQ@",
        )

        self.assertArgHasType(
            TestMEFormatReaderHelper.stepByDecodeTime_completionHandler_,
            0,
            MediaExtension.CMTime.__typestr__,
        )
        self.assertArgIsBlock(
            TestMEFormatReaderHelper.stepByDecodeTime_completionHandler_,
            1,
            b"v" + MediaExtension.CMTime.__typestr__ + b"Z@",
        )

        self.assertArgHasType(
            TestMEFormatReaderHelper.stepByPresentationTime_completionHandler_,
            0,
            MediaExtension.CMTime.__typestr__,
        )
        self.assertArgIsBlock(
            TestMEFormatReaderHelper.stepByPresentationTime_completionHandler_,
            1,
            b"v" + MediaExtension.CMTime.__typestr__ + b"Z@",
        )

        self.assertResultHasType(TestMEFormatReaderHelper.syncInfo, objc._C_NSUInteger)
        self.assertResultHasType(
            TestMEFormatReaderHelper.dependencyInfo, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMEFormatReaderHelper.hevcDependencyInfo, objc._C_ID
        )
        self.assertResultHasType(
            TestMEFormatReaderHelper.decodeTimeOfLastSampleReachableByForwardSteppingThatIsAlreadyLoadedByByteSource,
            MediaExtension.CMTime.__typestr__,
        )
        self.assertResultIsBOOL(
            TestMEFormatReaderHelper.samplesWithEarlierDTSsMayHaveLaterPTSsThanCursor_
        )
        self.assertResultIsBOOL(
            TestMEFormatReaderHelper.samplesWithLaterDTSsMayHaveEarlierPTSsThanCursor_
        )
        self.assertArgHasType(
            TestMEFormatReaderHelper.chunkDetailsReturningError_, 0, b"o^@"
        )
        self.assertArgHasType(
            TestMEFormatReaderHelper.sampleLocationReturningError_, 0, b"o^@"
        )
        self.assertArgHasType(
            TestMEFormatReaderHelper.estimatedSampleLocationReturningError_, 0, b"o^@"
        )

        self.assertResultIsBOOL(
            TestMEFormatReaderHelper.refineSampleLocation_refinementData_refinementDataLength_refinedLocation_error_
        )
        self.assertArgHasType(
            TestMEFormatReaderHelper.refineSampleLocation_refinementData_refinementDataLength_refinedLocation_error_,
            0,
            MediaExtension.AVSampleCursorStorageRange.__typestr__,
        )
        self.assertArgHasType(
            TestMEFormatReaderHelper.refineSampleLocation_refinementData_refinementDataLength_refinedLocation_error_,
            1,
            b"n^v",
        )
        self.assertArgHasType(
            TestMEFormatReaderHelper.refineSampleLocation_refinementData_refinementDataLength_refinedLocation_error_,
            2,
            b"Q",
        )
        self.assertArgHasType(
            TestMEFormatReaderHelper.refineSampleLocation_refinementData_refinementDataLength_refinedLocation_error_,
            3,
            b"o^" + MediaExtension.AVSampleCursorStorageRange.__typestr__,
        )
        self.assertArgHasType(
            TestMEFormatReaderHelper.refineSampleLocation_refinementData_refinementDataLength_refinedLocation_error_,
            4,
            b"o^@",
        )

        self.assertIsBlock(
            TestMEFormatReaderHelper.loadSampleBufferContainingSamplesToEndCursor_completionHandler_,
            1,
            b"v@@",
        )
