import CoreMedia
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCMTextMarkup(TestCase):
    @min_os_level("10.9")
    def test_constants10_9(self):
        self.assertIsInstance(CoreMedia.kCMTextMarkupAttribute_ForegroundColorARGB, str)
        self.assertIsInstance(CoreMedia.kCMTextMarkupAttribute_BackgroundColorARGB, str)
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupAttribute_CharacterBackgroundColorARGB, str
        )
        self.assertIsInstance(CoreMedia.kCMTextMarkupAttribute_BoldStyle, str)
        self.assertIsInstance(CoreMedia.kCMTextMarkupAttribute_ItalicStyle, str)
        self.assertIsInstance(CoreMedia.kCMTextMarkupAttribute_UnderlineStyle, str)
        self.assertIsInstance(CoreMedia.kCMTextMarkupAttribute_FontFamilyName, str)
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupAttribute_GenericFontFamilyName, str
        )
        self.assertIsInstance(CoreMedia.kCMTextMarkupGenericFontName_Default, str)
        self.assertIsInstance(CoreMedia.kCMTextMarkupGenericFontName_Serif, str)
        self.assertIsInstance(CoreMedia.kCMTextMarkupGenericFontName_SansSerif, str)
        self.assertIsInstance(CoreMedia.kCMTextMarkupGenericFontName_Monospace, str)
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupGenericFontName_ProportionalSerif, str
        )
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupGenericFontName_ProportionalSansSerif, str
        )
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupGenericFontName_MonospaceSerif, str
        )
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupGenericFontName_MonospaceSansSerif, str
        )
        self.assertIsInstance(CoreMedia.kCMTextMarkupGenericFontName_Casual, str)
        self.assertIsInstance(CoreMedia.kCMTextMarkupGenericFontName_Cursive, str)
        self.assertIsInstance(CoreMedia.kCMTextMarkupGenericFontName_Fantasy, str)
        self.assertIsInstance(CoreMedia.kCMTextMarkupGenericFontName_SmallCapital, str)
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupAttribute_BaseFontSizePercentageRelativeToVideoHeight,
            str,
        )
        self.assertIsInstance(CoreMedia.kCMTextMarkupAttribute_RelativeFontSize, str)
        self.assertIsInstance(CoreMedia.kCMTextMarkupAttribute_VerticalLayout, str)
        self.assertIsInstance(CoreMedia.kCMTextVerticalLayout_LeftToRight, str)
        self.assertIsInstance(CoreMedia.kCMTextVerticalLayout_RightToLeft, str)
        self.assertIsInstance(CoreMedia.kCMTextMarkupAttribute_Alignment, str)
        self.assertIsInstance(CoreMedia.kCMTextMarkupAlignmentType_Start, str)
        self.assertIsInstance(CoreMedia.kCMTextMarkupAlignmentType_Middle, str)
        self.assertIsInstance(CoreMedia.kCMTextMarkupAlignmentType_End, str)
        self.assertIsInstance(CoreMedia.kCMTextMarkupAlignmentType_Left, str)
        self.assertIsInstance(CoreMedia.kCMTextMarkupAlignmentType_Right, str)
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupAttribute_TextPositionPercentageRelativeToWritingDirection,
            str,
        )
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupAttribute_OrthogonalLinePositionPercentageRelativeToWritingDirection,
            str,
        )
        self.assertIsInstance(
            CoreMedia.kCMTextMarkupAttribute_WritingDirectionSizePercentage, str
        )
        self.assertIsInstance(CoreMedia.kCMTextMarkupAttribute_CharacterEdgeStyle, str)
        self.assertIsInstance(CoreMedia.kCMTextMarkupCharacterEdgeStyle_None, str)
        self.assertIsInstance(CoreMedia.kCMTextMarkupCharacterEdgeStyle_Raised, str)
        self.assertIsInstance(CoreMedia.kCMTextMarkupCharacterEdgeStyle_Depressed, str)
        self.assertIsInstance(CoreMedia.kCMTextMarkupCharacterEdgeStyle_Uniform, str)
        self.assertIsInstance(CoreMedia.kCMTextMarkupCharacterEdgeStyle_DropShadow, str)

    @min_os_level("13.0")
    def test_constants13_0(self):
        self.assertIsInstance(CoreMedia.kCMTextMarkupAttribute_FontFamilyNameList, str)
