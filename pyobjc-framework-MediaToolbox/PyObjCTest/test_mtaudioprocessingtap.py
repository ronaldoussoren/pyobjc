from PyObjCTools.TestSupport import *

import MediaToolbox

class TestMTAudioProcessingTap (TestCase):
    def test_cftypes(self):
        self.assertIsCFType(MediaToolbox.MTAudioProcessingTapRef)

    def test_functions(self):
        self.assertIsInstance(MediaToolbox.MTAudioProcessingTapGetTypeID(), (int, long))

        self.fail("Need manual wrappers for most functions")

    def test_constants(self):
        self.assertEqual(MediaToolbox.kMTAudioProcessingTapCreationFlag_PreEffects, 1 << 0)
        self.assertEqual(MediaToolbox.kMTAudioProcessingTapCreationFlag_PostEffects, 1 << 1)

        self.assertEqual(MediaToolbox.kMTAudioProcessingTapFlag_StartOfStream, 1 << 8)
        self.assertEqual(MediaToolbox.kMTAudioProcessingTapFlag_EndOfStream, 1 << 9)

        self.assertEqual(MediaToolbox.kMTAudioProcessingTapCallbacksVersion_0, 0)


if __name__ == "__main__":
    main()
