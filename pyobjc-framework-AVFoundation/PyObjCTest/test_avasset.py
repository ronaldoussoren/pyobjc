from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAssetHelper (AVFoundation.NSObject):
    def isAssociatedWithFragmentMinder(self): return True

class TestAVAsset (TestCase):
    @min_os_level('10.7')
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVAsset.providesPreciseDurationAndTiming)
        self.assertResultIsBOOL(AVFoundation.AVAsset.hasProtectedContent)
        self.assertResultIsBOOL(AVFoundation.AVAsset.isPlayable)
        self.assertResultIsBOOL(AVFoundation.AVAsset.isExportable)
        self.assertResultIsBOOL(AVFoundation.AVAsset.isReadable)
        self.assertResultIsBOOL(AVFoundation.AVAsset.isComposable)

        self.assertResultIsBOOL(AVFoundation.AVURLAsset.isPlayableExtendedMIMEType_)

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertResultIsBOOL(AVFoundation.AVAsset.canContainFragments)
        self.assertResultIsBOOL(AVFoundation.AVAsset.containsFragments)
        self.assertResultIsBOOL(AVFoundation.AVAsset.isCompatibleWithAirPlayVideo)

    @min_os_level('10.12.4')
    def testMethods10_12_4(self):
        self.assertResultIsBOOL(AVFoundation.AVURLAsset.mayRequireContentKeysForMediaDataProcessing)

    @min_os_level('10.7')
    def testConstants(self):
        self.assertEqual(AVFoundation.AVAssetReferenceRestrictionForbidNone, 0)
        self.assertEqual(AVFoundation.AVAssetReferenceRestrictionForbidRemoteReferenceToLocal, 1 << 0)
        self.assertEqual(AVFoundation.AVAssetReferenceRestrictionForbidLocalReferenceToRemote, 1 << 1)
        self.assertEqual(AVFoundation.AVAssetReferenceRestrictionForbidCrossSiteReference, 1 << 2)
        self.assertEqual(AVFoundation.AVAssetReferenceRestrictionForbidLocalReferenceToLocal, 1 << 3)
        self.assertEqual(AVFoundation.AVAssetReferenceRestrictionForbidAll, 0xFFFF)

        self.assertIsInstance(AVFoundation.AVURLAssetPreferPreciseDurationAndTimingKey, unicode)
        self.assertIsInstance(AVFoundation.AVURLAssetReferenceRestrictionsKey, unicode)

    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertIsInstance(AVFoundation.AVAssetDurationDidChangeNotification, unicode)
        self.assertIsInstance(AVFoundation.AVAssetContainsFragmentsDidChangeNotification, unicode)
        self.assertIsInstance(AVFoundation.AVAssetWasDefragmentedNotification, unicode)
        self.assertIsInstance(AVFoundation.AVAssetChapterMetadataGroupsDidChangeNotification, unicode)
        self.assertIsInstance(AVFoundation.AVAssetMediaSelectionGroupsDidChangeNotification, unicode)


    @min_sdk_level('10.11')
    def testProtocols(self):
        objc.protocolNamed('AVFragmentMinding')

    @min_sdk_level('10.11')
    def testProtocolMethods(self):
        self.assertResultIsBOOL(TestAVAssetHelper.isAssociatedWithFragmentMinder)

if __name__ == "__main__":
    main()
