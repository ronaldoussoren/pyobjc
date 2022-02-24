import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


import SceneKit

SCNSceneSourceStatusHandler = b"vf" + objc._C_NSInteger + b"@o^Z"


class TestSCNSceneSource(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(SceneKit.SCNSceneSourceAnimationImportPolicy, str)
        self.assertIsTypedEnum(SceneKit.SCNSceneSourceLoadingOption, str)

    def test_enum_types(self):
        self.assertIsEnumType(SceneKit.SCNSceneSourceStatus)

    def test_constants(self):
        self.assertIsInstance(SceneKit.SCNSceneSourceAssetContributorsKey, str)
        self.assertIsInstance(SceneKit.SCNSceneSourceAssetCreatedDateKey, str)
        self.assertIsInstance(SceneKit.SCNSceneSourceAssetModifiedDateKey, str)
        self.assertIsInstance(SceneKit.SCNSceneSourceAssetUpAxisKey, str)
        self.assertIsInstance(SceneKit.SCNSceneSourceAssetUnitKey, str)
        self.assertIsInstance(SceneKit.SCNSceneSourceAssetAuthoringToolKey, str)
        self.assertIsInstance(SceneKit.SCNSceneSourceAssetAuthorKey, str)
        self.assertIsInstance(SceneKit.SCNSceneSourceAssetUnitNameKey, str)
        self.assertIsInstance(SceneKit.SCNSceneSourceAssetUnitMeterKey, str)
        self.assertIsInstance(SceneKit.SCNSceneSourceCreateNormalsIfAbsentKey, str)
        self.assertIsInstance(SceneKit.SCNSceneSourceCheckConsistencyKey, str)
        self.assertIsInstance(SceneKit.SCNSceneSourceFlattenSceneKey, str)
        self.assertIsInstance(SceneKit.SCNSceneSourceUseSafeModeKey, str)
        self.assertIsInstance(SceneKit.SCNSceneSourceAssetDirectoryURLsKey, str)
        self.assertIsInstance(SceneKit.SCNSceneSourceOverrideAssetURLsKey, str)
        self.assertIsInstance(SceneKit.SCNSceneSourceStrictConformanceKey, str)
        self.assertIsInstance(SceneKit.SCNDetailedErrorsKey, str)
        self.assertIsInstance(SceneKit.SCNConsistencyElementIDErrorKey, str)
        self.assertIsInstance(SceneKit.SCNConsistencyElementTypeErrorKey, str)
        self.assertIsInstance(SceneKit.SCNConsistencyLineNumberErrorKey, str)

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

        self.assertIs(
            SceneKit.SCNSceneSourceLoadingOptionCreateNormalsIfAbsent,
            SceneKit.SCNSceneSourceCreateNormalsIfAbsentKey,
        )
        self.assertIs(
            SceneKit.SCNSceneSourceLoadingOptionCheckConsistency,
            SceneKit.SCNSceneSourceCheckConsistencyKey,
        )
        self.assertIs(
            SceneKit.SCNSceneSourceLoadingOptionFlattenScene,
            SceneKit.SCNSceneSourceFlattenSceneKey,
        )
        self.assertIs(
            SceneKit.SCNSceneSourceLoadingOptionUseSafeMode,
            SceneKit.SCNSceneSourceUseSafeModeKey,
        )
        self.assertIs(
            SceneKit.SCNSceneSourceLoadingOptionAssetDirectoryURLs,
            SceneKit.SCNSceneSourceAssetDirectoryURLsKey,
        )
        self.assertIs(
            SceneKit.SCNSceneSourceLoadingOptionOverrideAssetURLs,
            SceneKit.SCNSceneSourceOverrideAssetURLsKey,
        )
        self.assertIs(
            SceneKit.SCNSceneSourceLoadingOptionStrictConformance,
            SceneKit.SCNSceneSourceStrictConformanceKey,
        )

    @min_os_level("10.10")
    def test_constants10_10(self):
        self.assertIsInstance(SceneKit.SCNSceneSourceConvertUnitsToMetersKey, str)
        self.assertIsInstance(SceneKit.SCNSceneSourceConvertToYUpKey, str)
        self.assertIsInstance(SceneKit.SCNSceneSourceAnimationImportPolicyKey, str)
        self.assertIsInstance(SceneKit.SCNSceneSourceAnimationImportPolicyPlay, str)
        self.assertIsInstance(SceneKit.SCNSceneSourceAnimationImportPolicyPlay, str)
        self.assertIsInstance(
            SceneKit.SCNSceneSourceAnimationImportPolicyPlayRepeatedly, str
        )
        self.assertIsInstance(
            SceneKit.SCNSceneSourceAnimationImportPolicyDoNotPlay, str
        )
        self.assertIsInstance(
            SceneKit.SCNSceneSourceAnimationImportPolicyPlayUsingSceneTimeBase, str
        )

        self.assertIs(
            SceneKit.SCNSceneSourceLoadingOptionConvertUnitsToMeters,
            SceneKit.SCNSceneSourceConvertUnitsToMetersKey,
        )
        self.assertIs(
            SceneKit.SCNSceneSourceLoadingOptionConvertToYUp,
            SceneKit.SCNSceneSourceConvertToYUpKey,
        )
        self.assertIs(
            SceneKit.SCNSceneSourceLoadingOptionAnimationImportPolicy,
            SceneKit.SCNSceneSourceAnimationImportPolicyKey,
        )

    @min_os_level("10.12")
    def test_constants10_12(self):
        self.assertIsInstance(
            SceneKit.SCNSceneSourceLoadingOptionPreserveOriginalTopology, str
        )

    def testMethods(self):
        self.assertArgIsBlock(
            SceneKit.SCNSceneSource.sceneWithOptions_statusHandler_,
            1,
            SCNSceneSourceStatusHandler,
        )
        self.assertArgIsOut(SceneKit.SCNSceneSource.sceneWithOptions_error_, 1)
        self.assertArgIsBlock(SceneKit.SCNSceneSource.entriesPassingTest_, 0, b"Z@@o^Z")
