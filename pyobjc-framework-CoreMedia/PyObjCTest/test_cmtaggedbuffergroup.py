import CoreMedia
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCMTaggedBufferGroup(TestCase):
    def test_constants(self):
        self.assertIsEnumType(CoreMedia.CMTaggedBufferGroupError)
        self.assertEqual(CoreMedia.kCMTaggedBufferGroupError_ParamErr, -15780)
        self.assertEqual(CoreMedia.kCMTaggedBufferGroupError_AllocationFailed, -15781)
        self.assertEqual(CoreMedia.kCMTaggedBufferGroupError_InternalError, -15782)

    @min_os_level("14.0")
    def test_types(self):
        self.assertIsCFType(CoreMedia.CMTaggedBufferGroupRef)

    @min_os_level("14.0")
    def test_functions(self):
        CoreMedia.CMTaggedBufferGroupGetTypeID

        self.assertArgIsOut(CoreMedia.CMTaggedBufferGroupCreate, 3)
        self.assertArgIsCFRetained(CoreMedia.CMTaggedBufferGroupCreate, 3)

        self.assertArgIsOut(CoreMedia.CMTaggedBufferGroupCreateCombined, 2)
        self.assertArgIsCFRetained(CoreMedia.CMTaggedBufferGroupCreateCombined, 2)

        CoreMedia.CMTaggedBufferGroupGetCount

        CoreMedia.CMTaggedBufferGroupGetTagCollectionAtIndex

        CoreMedia.CMTaggedBufferGroupGetCVPixelBufferAtIndex

        self.assertArgIsOut(CoreMedia.CMTaggedBufferGroupGetCVPixelBufferForTag, 2)

        self.assertArgIsOut(
            CoreMedia.CMTaggedBufferGroupGetCVPixelBufferForTagCollection, 2
        )

        CoreMedia.CMTaggedBufferGroupGetCMSampleBufferAtIndex

        self.assertArgIsOut(CoreMedia.CMTaggedBufferGroupGetCMSampleBufferForTag, 2)

        self.assertArgIsOut(
            CoreMedia.CMTaggedBufferGroupGetCMSampleBufferForTagCollection, 2
        )

        CoreMedia.CMTaggedBufferGroupGetNumberOfMatchesForTagCollection

        self.assertArgIsOut(
            CoreMedia.CMTaggedBufferGroupFormatDescriptionCreateForTaggedBufferGroup, 2
        )
        self.assertArgIsCFRetained(
            CoreMedia.CMTaggedBufferGroupFormatDescriptionCreateForTaggedBufferGroup, 2
        )

        self.assertResultIsBOOL(
            CoreMedia.CMTaggedBufferGroupFormatDescriptionMatchesTaggedBufferGroup
        )

        self.assertArgIsOut(CoreMedia.CMSampleBufferCreateForTaggedBufferGroup, 5)
        self.assertArgIsCFRetained(
            CoreMedia.CMSampleBufferCreateForTaggedBufferGroup, 5
        )

        CoreMedia.CMSampleBufferGetTaggedBufferGroup
