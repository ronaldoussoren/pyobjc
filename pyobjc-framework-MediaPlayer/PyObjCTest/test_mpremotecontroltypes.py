from PyObjCTools.TestSupport import TestCase
import MediaPlayer


class TestMPRemoteControlTypes(TestCase):
    def test_enums(self):
        self.assertIsEnumType(MediaPlayer.MPChangeLanguageOptionSetting)
        self.assertEqual(MediaPlayer.MPChangeLanguageOptionSettingNone, 0)
        self.assertEqual(MediaPlayer.MPChangeLanguageOptionSettingNowPlayingItemOnly, 1)
        self.assertEqual(MediaPlayer.MPChangeLanguageOptionSettingPermanent, 2)

        self.assertIsEnumType(MediaPlayer.MPRepeatType)
        self.assertEqual(MediaPlayer.MPRepeatTypeOff, 0)
        self.assertEqual(MediaPlayer.MPRepeatTypeOne, 1)
        self.assertEqual(MediaPlayer.MPRepeatTypeAll, 2)

        self.assertIsEnumType(MediaPlayer.MPShuffleType)
        self.assertEqual(MediaPlayer.MPShuffleTypeOff, 0)
        self.assertEqual(MediaPlayer.MPShuffleTypeItems, 1)
        self.assertEqual(MediaPlayer.MPShuffleTypeCollections, 2)
