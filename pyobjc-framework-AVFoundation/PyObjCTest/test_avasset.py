from PyObjCTools.TestSupport import *

import AVFoundation

try:
    unicode
except NameError:
    unicode = str

class TestAVAsset (TestCase):
    @min_os_level('10.7')
    def test_methods10_7(self):
        self.assertResultIsBOOL(AVFoundation.AVAsset.providesPreciseDurationAndTiming)
        self.assertResultIsBOOL(AVFoundation.AVAsset.hasProtectedContent)
        self.assertResultIsBOOL(AVFoundation.AVAsset.isPlayable)
        self.assertResultIsBOOL(AVFoundation.AVAsset.isExportable)
        self.assertResultIsBOOL(AVFoundation.AVAsset.isReadable)
        self.assertResultIsBOOL(AVFoundation.AVAsset.isComposable)

        self.assertResultIsBOOL(AVFoundation.AVURLAsset.isPlayableExtendedMIMEType_)

    def test_constants(self):
        self.assertEqual(AVFoundation.AVAssetReferenceRestrictionForbidNone, 0)
        self.assertEqual(AVFoundation.AVAssetReferenceRestrictionForbidRemoteReferenceToLocal, 1 << 0)
        self.assertEqual(AVFoundation.AVAssetReferenceRestrictionForbidLocalReferenceToRemote, 1 << 1)
        self.assertEqual(AVFoundation.AVAssetReferenceRestrictionForbidCrossSiteReference, 1 << 2)
        self.assertEqual(AVFoundation.AVAssetReferenceRestrictionForbidLocalReferenceToLocal, 1 << 3)
        self.assertEqual(AVFoundation.AVAssetReferenceRestrictionForbidAll, 0xFFFF)

        self.assertIsInstance(AVFoundation.AVURLAssetPreferPreciseDurationAndTimingKey, unicode)
        self.assertIsInstance(AVFoundation.AVURLAssetReferenceRestrictionsKey, unicode)

if __name__ == "__main__":
    main()
