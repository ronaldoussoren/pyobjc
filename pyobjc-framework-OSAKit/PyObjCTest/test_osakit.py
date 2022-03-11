import OSAKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestOSAScript(TestCase):
    def testConstants(self):
        self.assertIsInstance(OSAKit.OSAScriptErrorMessageKey, str)
        self.assertIsInstance(OSAKit.OSAScriptErrorBriefMessageKey, str)
        self.assertIsInstance(OSAKit.OSAScriptErrorNumberKey, str)
        self.assertIsInstance(OSAKit.OSAScriptErrorPartialResultKey, str)
        self.assertIsInstance(OSAKit.OSAScriptErrorOffendingObjectKey, str)
        self.assertIsInstance(OSAKit.OSAScriptErrorExpectedTypeKey, str)
        self.assertIsInstance(OSAKit.OSAScriptErrorAppAddressKey, str)
        self.assertIsInstance(OSAKit.OSAScriptErrorAppNameKey, str)
        self.assertIsInstance(OSAKit.OSAScriptErrorRangeKey, str)
        self.assertIsInstance(OSAKit.OSAScriptErrorMessage, str)
        self.assertIsInstance(OSAKit.OSAScriptErrorNumber, str)
        self.assertIsInstance(OSAKit.OSAScriptErrorAppName, str)
        self.assertIsInstance(OSAKit.OSAScriptErrorBriefMessage, str)
        self.assertIsInstance(OSAKit.OSAScriptErrorRange, str)
        self.assertIsInstance(OSAKit.OSAStorageScriptType, str)
        self.assertIsInstance(OSAKit.OSAStorageScriptBundleType, str)
        self.assertIsInstance(OSAKit.OSAStorageApplicationType, str)
        self.assertIsInstance(OSAKit.OSAStorageApplicationBundleType, str)
        self.assertIsInstance(OSAKit.OSAStorageTextType, str)

        self.assertEqual(OSAKit.OSANull, 0x00000000)
        self.assertEqual(OSAKit.OSAPreventGetSource, 0x00000001)
        self.assertEqual(OSAKit.OSACompileIntoContext, 0x00000002)
        self.assertEqual(OSAKit.OSADontSetScriptLocation, 0x01000000)
        self.assertEqual(OSAKit.OSAStayOpenApplet, 0x10000000)
        self.assertEqual(OSAKit.OSAShowStartupScreen, 0x20000000)

    def testMethods(self):
        self.assertArgIsOut(OSAKit.OSAScript.initWithCompiledData_error_, 1)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgIsOut(OSAKit.OSAScript.initWithContentsOfURL_error_, 1)
        self.assertArgIsOut(
            OSAKit.OSAScript.initWithContentsOfURL_languageInstance_usingStorageOptions_error_,
            3,
        )
        self.assertArgIsOut(
            OSAKit.OSAScript.initWithCompiledData_fromURL_usingStorageOptions_error_, 3
        )
        self.assertArgIsOut(
            OSAKit.OSAScript.initWithScriptDataDescriptor_fromURL_languageInstance_usingStorageOptions_error_,  # noqa: B950
            4,
        )

        self.assertResultIsBOOL(OSAKit.OSAScript.isCompiled)

        self.assertResultIsBOOL(OSAKit.OSAScript.compileAndReturnError_)
        self.assertArgIsOut(OSAKit.OSAScript.compileAndReturnError_, 0)

        self.assertArgIsOut(OSAKit.OSAScript.executeAndReturnError_, 0)
        self.assertArgIsOut(OSAKit.OSAScript.executeAppleEvent_error_, 1)

        self.assertArgIsOut(OSAKit.OSAScript.executeAndReturnDisplayValue_error_, 0)
        self.assertArgIsOut(OSAKit.OSAScript.executeAndReturnDisplayValue_error_, 1)

        self.assertArgIsOut(OSAKit.OSAScript.executeHandlerWithName_arguments_error_, 2)

        self.assertResultIsBOOL(OSAKit.OSAScript.writeToURL_ofType_error_)
        self.assertArgIsOut(OSAKit.OSAScript.writeToURL_ofType_error_, 2)

        self.assertResultIsBOOL(
            OSAKit.OSAScript.writeToURL_ofType_usingStorageOptions_error_
        )
        self.assertArgIsOut(
            OSAKit.OSAScript.writeToURL_ofType_usingStorageOptions_error_, 3
        )

        self.assertArgIsOut(
            OSAKit.OSAScript.compiledDataForType_usingStorageOptions_error_, 2
        )


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(OSAKit)
