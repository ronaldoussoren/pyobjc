from PyObjCTools.TestSupport import TestCase, min_os_level
import MediaPlayer


class TestMPNowPlayingInfoLanguageOption(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MediaPlayer.MPNowPlayingInfoLanguageOptionType)

    @min_os_level("10.12")
    def testConstants(self):
        self.assertIsInstance(
            MediaPlayer.MPLanguageOptionCharacteristicIsMainProgramContent, str
        )
        self.assertIsInstance(
            MediaPlayer.MPLanguageOptionCharacteristicIsAuxiliaryContent, str
        )
        self.assertIsInstance(
            MediaPlayer.MPLanguageOptionCharacteristicContainsOnlyForcedSubtitles, str
        )
        self.assertIsInstance(
            MediaPlayer.MPLanguageOptionCharacteristicTranscribesSpokenDialog, str
        )
        self.assertIsInstance(
            MediaPlayer.MPLanguageOptionCharacteristicDescribesMusicAndSound, str
        )
        self.assertIsInstance(MediaPlayer.MPLanguageOptionCharacteristicEasyToRead, str)
        self.assertIsInstance(
            MediaPlayer.MPLanguageOptionCharacteristicDescribesVideo, str
        )
        self.assertIsInstance(
            MediaPlayer.MPLanguageOptionCharacteristicLanguageTranslation, str
        )
        self.assertIsInstance(
            MediaPlayer.MPLanguageOptionCharacteristicDubbedTranslation, str
        )
        self.assertIsInstance(
            MediaPlayer.MPLanguageOptionCharacteristicVoiceOverTranslation, str
        )

        self.assertEqual(MediaPlayer.MPNowPlayingInfoLanguageOptionTypeAudible, 0)
        self.assertEqual(MediaPlayer.MPNowPlayingInfoLanguageOptionTypeLegible, 1)

    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultIsBOOL(
            MediaPlayer.MPNowPlayingInfoLanguageOption.isAutomaticLegibleLanguageOption
        )
        self.assertResultIsBOOL(
            MediaPlayer.MPNowPlayingInfoLanguageOption.isAutomaticAudibleLanguageOption
        )

        self.assertArgIsBOOL(
            MediaPlayer.MPNowPlayingInfoLanguageOptionGroup.initWithLanguageOptions_defaultLanguageOption_allowEmptySelection_,  # noqa: B950
            2,
        )
        self.assertResultIsBOOL(
            MediaPlayer.MPNowPlayingInfoLanguageOptionGroup.allowEmptySelection
        )
