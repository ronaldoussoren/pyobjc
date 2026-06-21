import MediaToolbox
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestMTAudioProcessingTap(TestCase):
    def test_cftypess(self):
        self.assertIsCFType(MediaToolbox.MTAudioProcessingTapRef)

    def test_functions(self):
        self.assertIsInstance(MediaToolbox.MTAudioProcessingTapGetTypeID(), int)

        self.assertArgIsOut(MediaToolbox.MTAudioProcessingTapGetSourceAudio, 3)
        self.assertArgIsOut(MediaToolbox.MTAudioProcessingTapGetSourceAudio, 4)
        self.assertArgIsOut(MediaToolbox.MTAudioProcessingTapGetSourceAudio, 5)

        # XXX: These two funtions should be tested manually:
        self.assertNotIsInstance(
            MediaToolbox.MTAudioProcessingTapGetStorage, objc.function
        )
        self.assertNotIsInstance(MediaToolbox.MTAudioProcessingTapCreate, objc.function)

    @min_os_level("27.0")
    def test_functions27_0(self):
        # XXX: This funtion should be tested manually:
        self.assertNotIsInstance(
            MediaToolbox.MTAudioProcessingTapCreateWithPreferredFormat, objc.function
        )

    def test_constants(self):
        self.assertEqual(
            MediaToolbox.kMTAudioProcessingTapCreationFlag_PreEffects, 1 << 0
        )
        self.assertEqual(
            MediaToolbox.kMTAudioProcessingTapCreationFlag_PostEffects, 1 << 1
        )

        self.assertEqual(MediaToolbox.kMTAudioProcessingTapFlag_StartOfStream, 1 << 8)
        self.assertEqual(MediaToolbox.kMTAudioProcessingTapFlag_EndOfStream, 1 << 9)

        self.assertEqual(MediaToolbox.kMTAudioProcessingTapCallbacksVersion_0, 0)
