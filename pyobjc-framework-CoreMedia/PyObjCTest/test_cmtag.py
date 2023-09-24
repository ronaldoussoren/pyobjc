import CoreMedia
from PyObjCTools.TestSupport import TestCase, min_os_level, fourcc


class TestCMTag(TestCase):
    def test_constants(self):
        self.assertIsEnumType(CoreMedia.CMTagError)
        self.assertEqual(CoreMedia.kCMTagError_ParamErr, -15730)
        self.assertEqual(CoreMedia.kCMTagError_AllocationFailed, -15731)

        self.assertIsEnumType(CoreMedia.CMTagCategory)
        self.assertEqual(CoreMedia.kCMTagCategory_Undefined, 0)
        self.assertEqual(CoreMedia.kCMTagCategory_MediaType, fourcc(b"mdia"))
        self.assertEqual(CoreMedia.kCMTagCategory_MediaSubType, fourcc(b"msub"))
        self.assertEqual(CoreMedia.kCMTagCategory_TrackID, fourcc(b"trak"))
        self.assertEqual(CoreMedia.kCMTagCategory_ChannelID, fourcc(b"vchn"))
        self.assertEqual(CoreMedia.kCMTagCategory_VideoLayerID, fourcc(b"vlay"))
        self.assertEqual(CoreMedia.kCMTagCategory_PixelFormat, fourcc(b"pixf"))
        self.assertEqual(CoreMedia.kCMTagCategory_PackingType, fourcc(b"pack"))
        self.assertEqual(CoreMedia.kCMTagCategory_ProjectionType, fourcc(b"proj"))
        self.assertEqual(CoreMedia.kCMTagCategory_StereoView, fourcc(b"eyes"))
        self.assertEqual(
            CoreMedia.kCMTagCategory_StereoViewInterpretation, fourcc(b"eyip")
        )

        self.assertIsEnumType(CoreMedia.CMTagDataType)
        self.assertEqual(CoreMedia.kCMTagDataType_Invalid, 0)
        self.assertEqual(CoreMedia.kCMTagDataType_SInt64, 2)
        self.assertEqual(CoreMedia.kCMTagDataType_Float64, 3)
        self.assertEqual(CoreMedia.kCMTagDataType_OSType, 5)
        self.assertEqual(CoreMedia.kCMTagDataType_Flags, 7)

        self.assertIsEnumType(CoreMedia.CMStereoViewComponents)
        self.assertEqual(CoreMedia.kCMStereoView_None, 0)
        self.assertEqual(CoreMedia.kCMStereoView_LeftEye, 1 << 0)
        self.assertEqual(CoreMedia.kCMStereoView_RightEye, 1 << 1)

        self.assertIsEnumType(CoreMedia.CMStereoViewInterpretationOptions)
        self.assertEqual(CoreMedia.kCMStereoViewInterpretation_Default, 0)
        self.assertEqual(
            CoreMedia.kCMStereoViewInterpretation_StereoOrderReversed, 1 << 0
        )
        self.assertEqual(CoreMedia.kCMStereoViewInterpretation_AdditionalViews, 1 << 1)

        self.assertIsEnumType(CoreMedia.CMProjectionType)
        self.assertEqual(CoreMedia.kCMProjectionType_Rectangular, fourcc(b"rect"))
        self.assertEqual(CoreMedia.kCMProjectionType_Equirectangular, fourcc(b"equi"))
        self.assertEqual(
            CoreMedia.kCMProjectionType_HalfEquirectangular, fourcc(b"hequ")
        )
        self.assertEqual(CoreMedia.kCMProjectionType_Fisheye, fourcc(b"fish"))

        self.assertIsEnumType(CoreMedia.CMPackingType)
        self.assertEqual(CoreMedia.kCMPackingType_None, fourcc(b"none"))
        self.assertEqual(CoreMedia.kCMPackingType_SideBySide, fourcc(b"side"))
        self.assertEqual(CoreMedia.kCMPackingType_OverUnder, fourcc(b"over"))

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(CoreMedia.kCMTagInvalid, CoreMedia.CMTag)
        self.assertIsInstance(CoreMedia.kCMTagMediaTypeVideo, CoreMedia.CMTag)
        self.assertIsInstance(CoreMedia.kCMTagMediaSubTypeMebx, CoreMedia.CMTag)
        self.assertIsInstance(CoreMedia.kCMTagMediaTypeAudio, CoreMedia.CMTag)
        self.assertIsInstance(CoreMedia.kCMTagMediaTypeMetadata, CoreMedia.CMTag)
        self.assertIsInstance(CoreMedia.kCMTagStereoLeftEye, CoreMedia.CMTag)
        self.assertIsInstance(CoreMedia.kCMTagStereoRightEye, CoreMedia.CMTag)
        self.assertIsInstance(CoreMedia.kCMTagStereoLeftAndRightEye, CoreMedia.CMTag)
        self.assertIsInstance(CoreMedia.kCMTagStereoNone, CoreMedia.CMTag)
        self.assertIsInstance(
            CoreMedia.kCMTagStereoInterpretationOrderReversed, CoreMedia.CMTag
        )
        self.assertIsInstance(
            CoreMedia.kCMTagProjectionTypeRectangular, CoreMedia.CMTag
        )
        self.assertIsInstance(
            CoreMedia.kCMTagProjectionTypeEquirectangular, CoreMedia.CMTag
        )
        self.assertIsInstance(CoreMedia.kCMTagProjectionTypeFisheye, CoreMedia.CMTag)
        self.assertIsInstance(CoreMedia.kCMTagPackingTypeNone, CoreMedia.CMTag)
        self.assertIsInstance(CoreMedia.kCMTagPackingTypeSideBySide, CoreMedia.CMTag)

        self.assertIsInstance(CoreMedia.kCMTagValueKey, str)
        self.assertIsInstance(CoreMedia.kCMTagCategoryKey, str)
        self.assertIsInstance(CoreMedia.kCMTagDataTypeKey, str)

    def test_structs(self):
        v = CoreMedia.CMTag()
        self.assertIsInstance(v.category, int)
        self.assertIsInstance(v.dataType, int)
        self.assertIsInstance(v.value, int)

    @min_os_level("14.0")
    def test_functions(self):
        self.assertResultIsBOOL(CoreMedia.CMTagIsValid)
        CoreMedia.CMTagGetCategory
        self.assertResultIsBOOL(CoreMedia.CMTagCategoryEqualToTagCategory)
        CoreMedia.CMTagGetValue
        self.assertResultIsBOOL(CoreMedia.CMTagHasCategory)
        self.assertResultIsBOOL(CoreMedia.CMTagHasSInt64Value)
        CoreMedia.CMTagGetSInt64Value
        self.assertResultIsBOOL(CoreMedia.CMTagHasFloat64Value)
        CoreMedia.CMTagGetFloat64Value
        self.assertResultIsBOOL(CoreMedia.CMTagHasOSTypeValue)
        CoreMedia.CMTagGetOSTypeValue
        self.assertResultIsBOOL(CoreMedia.CMTagHasFlagsValue)
        CoreMedia.CMTagGetFlagsValue
        CoreMedia.CMTagMakeWithSInt64Value
        CoreMedia.CMTagMakeWithFloat64Value
        CoreMedia.CMTagMakeWithOSTypeValue
        CoreMedia.CMTagMakeWithFlagsValue
        self.assertResultIsBOOL(CoreMedia.CMTagEqualToTag)
        CoreMedia.CMTagCompare
        self.assertResultIsBOOL(CoreMedia.CMTagCategoryValueEqualToValue)
        CoreMedia.CMTagHash
        self.assertResultIsCFRetained(CoreMedia.CMTagCopyDescription)
        self.assertResultIsCFRetained(CoreMedia.CMTagCopyAsDictionary)
        CoreMedia.CMTagMakeFromDictionary

        CoreMedia.CMTAG_IS_VALID
        CoreMedia.CMTAG_IS_INVALID
