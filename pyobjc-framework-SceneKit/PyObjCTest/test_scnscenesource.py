from PyObjCTools.TestSupport import *
import objc
import sys

if os_level_key(os_release()) < os_level_key('10.12') or sys.maxsize >= 2**32:

    import SceneKit


    SCNSceneSourceStatusHandler = b'vf' + objc._C_NSInteger + b'@o^Z'

    class TestSCNSceneSource (TestCase):
        def test_constants(self):
            self.assertIsInstance(SceneKit.SCNSceneSourceAssetContributorsKey, unicode)
            self.assertIsInstance(SceneKit.SCNSceneSourceAssetCreatedDateKey, unicode)
            self.assertIsInstance(SceneKit.SCNSceneSourceAssetModifiedDateKey, unicode)
            self.assertIsInstance(SceneKit.SCNSceneSourceAssetUpAxisKey, unicode)
            self.assertIsInstance(SceneKit.SCNSceneSourceAssetUnitKey, unicode)
            self.assertIsInstance(SceneKit.SCNSceneSourceAssetAuthoringToolKey, unicode)
            self.assertIsInstance(SceneKit.SCNSceneSourceAssetAuthorKey, unicode)
            self.assertIsInstance(SceneKit.SCNSceneSourceAssetUnitNameKey, unicode)
            self.assertIsInstance(SceneKit.SCNSceneSourceAssetUnitMeterKey, unicode)
            self.assertIsInstance(SceneKit.SCNSceneSourceCreateNormalsIfAbsentKey, unicode)
            self.assertIsInstance(SceneKit.SCNSceneSourceCheckConsistencyKey, unicode)
            self.assertIsInstance(SceneKit.SCNSceneSourceFlattenSceneKey, unicode)
            self.assertIsInstance(SceneKit.SCNSceneSourceUseSafeModeKey, unicode)
            self.assertIsInstance(SceneKit.SCNSceneSourceAssetDirectoryURLsKey, unicode)
            self.assertIsInstance(SceneKit.SCNSceneSourceOverrideAssetURLsKey, unicode)
            self.assertIsInstance(SceneKit.SCNSceneSourceStrictConformanceKey, unicode)
            self.assertIsInstance(SceneKit.SCNDetailedErrorsKey, unicode)
            self.assertIsInstance(SceneKit.SCNConsistencyElementIDErrorKey, unicode)
            self.assertIsInstance(SceneKit.SCNConsistencyElementTypeErrorKey, unicode)
            self.assertIsInstance(SceneKit.SCNConsistencyLineNumberErrorKey, unicode)

            self.assertEqual(SceneKit.SCNConsistencyInvalidURIError, 1000)
            self.assertEqual(SceneKit.SCNConsistencyInvalidCountError, 1001)
            self.assertEqual(SceneKit.SCNConsistencyInvalidArgumentError, 1002)
            self.assertEqual(SceneKit.SCNConsistencyMissingElementError, 1003)
            self.assertEqual(SceneKit.SCNConsistencyMissingAttributeError, 1004)
            self.assertEqual(SceneKit.SCNConsistencyXMLSchemaValidationError, 1005)

            self.assertEqual(SceneKit.SCNSceneSourceStatusError, -1)
            self.assertEqual(SceneKit.SCNSceneSourceStatusParsing, 4)
            self.assertEqual(SceneKit.SCNSceneSourceStatusValidating, 8)
            self.assertEqual(SceneKit.SCNSceneSourceStatusProcessing, 12)
            self.assertEqual(SceneKit.SCNSceneSourceStatusComplete, 16)

            self.assertIs(SceneKit.SCNSceneSourceLoadingOptionCreateNormalsIfAbsent, SceneKit.SCNSceneSourceCreateNormalsIfAbsentKey)
            self.assertIs(SceneKit.SCNSceneSourceLoadingOptionCheckConsistency, SceneKit.SCNSceneSourceCheckConsistencyKey)
            self.assertIs(SceneKit.SCNSceneSourceLoadingOptionFlattenScene, SceneKit.SCNSceneSourceFlattenSceneKey)
            self.assertIs(SceneKit.SCNSceneSourceLoadingOptionUseSafeMode, SceneKit.SCNSceneSourceUseSafeModeKey)
            self.assertIs(SceneKit.SCNSceneSourceLoadingOptionAssetDirectoryURLs, SceneKit.SCNSceneSourceAssetDirectoryURLsKey)
            self.assertIs(SceneKit.SCNSceneSourceLoadingOptionOverrideAssetURLs, SceneKit.SCNSceneSourceOverrideAssetURLsKey)
            self.assertIs(SceneKit.SCNSceneSourceLoadingOptionStrictConformance, SceneKit.SCNSceneSourceStrictConformanceKey)


        @min_os_level('10.10')
        def test_constants10_10(self):
            self.assertIsInstance(SceneKit.SCNSceneSourceConvertUnitsToMetersKey, unicode)
            self.assertIsInstance(SceneKit.SCNSceneSourceConvertToYUpKey, unicode)
            self.assertIsInstance(SceneKit.SCNSceneSourceAnimationImportPolicyKey, unicode)
            self.assertIsInstance(SceneKit.SCNSceneSourceAnimationImportPolicyPlay, unicode)
            self.assertIsInstance(SceneKit.SCNSceneSourceAnimationImportPolicyPlay, unicode)
            self.assertIsInstance(SceneKit.SCNSceneSourceAnimationImportPolicyPlayRepeatedly, unicode)
            self.assertIsInstance(SceneKit.SCNSceneSourceAnimationImportPolicyDoNotPlay, unicode)
            self.assertIsInstance(SceneKit.SCNSceneSourceAnimationImportPolicyPlayUsingSceneTimeBase, unicode)

            self.assertIs(SceneKit.SCNSceneSourceLoadingOptionConvertUnitsToMeters, SceneKit.SCNSceneSourceConvertUnitsToMetersKey)
            self.assertIs(SceneKit.SCNSceneSourceLoadingOptionConvertToYUp, SceneKit.SCNSceneSourceConvertToYUpKey)
            self.assertIs(SceneKit.SCNSceneSourceLoadingOptionAnimationImportPolicy, SceneKit.SCNSceneSourceAnimationImportPolicyKey)

        @min_os_level('10.12')
        def test_constants10_12(self):
            self.assertIsInstance(SceneKit.SCNSceneSourceLoadingOptionPreserveOriginalTopology, unicode)

        def testMethods(self):
            self.assertArgIsBlock(SceneKit.SCNSceneSource.sceneWithOptions_statusHandler_, 1, SCNSceneSourceStatusHandler)
            self.assertArgIsOut(SceneKit.SCNSceneSource.sceneWithOptions_error_, 1)
            self.assertArgIsBlock(SceneKit.SCNSceneSource.entriesPassingTest_, 0, b'Z@@o^Z')


if __name__ == "__main__":
    main()
