from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import MediaPlayer

    class TestMPNowPlayingInfoLanguageOption (TestCase):
        @min_os_level('10.12')
        def testConstants(self):
            self.assertIsInstance(MediaPlayer.MPLanguageOptionCharacteristicIsMainProgramContent, unicode)
            self.assertIsInstance(MediaPlayer.MPLanguageOptionCharacteristicIsAuxiliaryContent, unicode)
            self.assertIsInstance(MediaPlayer.MPLanguageOptionCharacteristicContainsOnlyForcedSubtitles, unicode)
            self.assertIsInstance(MediaPlayer.MPLanguageOptionCharacteristicTranscribesSpokenDialog, unicode)
            self.assertIsInstance(MediaPlayer.MPLanguageOptionCharacteristicDescribesMusicAndSound, unicode)
            self.assertIsInstance(MediaPlayer.MPLanguageOptionCharacteristicEasyToRead, unicode)
            self.assertIsInstance(MediaPlayer.MPLanguageOptionCharacteristicDescribesVideo, unicode)
            self.assertIsInstance(MediaPlayer.MPLanguageOptionCharacteristicLanguageTranslation, unicode)
            self.assertIsInstance(MediaPlayer.MPLanguageOptionCharacteristicDubbedTranslation, unicode)
            self.assertIsInstance(MediaPlayer.MPLanguageOptionCharacteristicVoiceOverTranslation, unicode)

            self.assertEqual(MediaPlayer.MPNowPlayingInfoLanguageOptionTypeAudible, 0)
            self.assertEqual(MediaPlayer.MPNowPlayingInfoLanguageOptionTypeLegible, 1)

        @min_os_level('10.12')
        def testMethods(self):
            self.assertResultIsBOOL(MediaPlayer.MPNowPlayingInfoLanguageOption.isAutomaticLegibleLanguageOption)
            self.assertResultIsBOOL(MediaPlayer.MPNowPlayingInfoLanguageOption.isAutomaticAudibleLanguageOption)

            self.assertArgIsBOOL(MediaPlayer.MPNowPlayingInfoLanguageOptionGroup.initWithLanguageOptions_defaultLanguageOption_allowEmptySelection_, 2)
            self.assertResultIsBOOL(MediaPlayer.MPNowPlayingInfoLanguageOptionGroup.allowEmptySelection)

if __name__ == "__main__":
    main()
