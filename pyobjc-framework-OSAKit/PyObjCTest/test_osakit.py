from PyObjCTools.TestSupport import *

import OSAKit

class TestOSAScript (TestCase):
    def testConstants(self):
        self.assertIsInstance(OSAKit.OSAScriptErrorMessageKey, unicode)
        self.assertIsInstance(OSAKit.OSAScriptErrorBriefMessageKey, unicode)
        self.assertIsInstance(OSAKit.OSAScriptErrorNumberKey, unicode)
        self.assertIsInstance(OSAKit.OSAScriptErrorPartialResultKey, unicode)
        self.assertIsInstance(OSAKit.OSAScriptErrorOffendingObjectKey, unicode)
        self.assertIsInstance(OSAKit.OSAScriptErrorExpectedTypeKey, unicode)
        self.assertIsInstance(OSAKit.OSAScriptErrorAppAddressKey, unicode)
        self.assertIsInstance(OSAKit.OSAScriptErrorAppNameKey, unicode)
        self.assertIsInstance(OSAKit.OSAScriptErrorRangeKey, unicode)
        self.assertIsInstance(OSAKit.OSAScriptErrorMessage, unicode)
        self.assertIsInstance(OSAKit.OSAScriptErrorNumber, unicode)
        self.assertIsInstance(OSAKit.OSAScriptErrorAppName, unicode)
        self.assertIsInstance(OSAKit.OSAScriptErrorBriefMessage, unicode)
        self.assertIsInstance(OSAKit.OSAScriptErrorRange, unicode)
        self.assertIsInstance(OSAKit.OSAStorageScriptType, unicode)
        self.assertIsInstance(OSAKit.OSAStorageScriptBundleType, unicode)
        self.assertIsInstance(OSAKit.OSAStorageApplicationType, unicode)
        self.assertIsInstance(OSAKit.OSAStorageApplicationBundleType, unicode)
        self.assertIsInstance(OSAKit.OSAStorageTextType, unicode)

        self.assertEqual(OSAKit.OSANull, 0x00000000)
        self.assertEqual(OSAKit.OSAPreventGetSource, 0x00000001)
        self.assertEqual(OSAKit.OSACompileIntoContext, 0x00000002)
        self.assertEqual(OSAKit.OSADontSetScriptLocation, 0x01000000)
        self.assertEqual(OSAKit.OSAStayOpenApplet, 0x10000000)
        self.assertEqual(OSAKit.OSAShowStartupScreen, 0x20000000)

    def testMethods(self):
        self.assertArgIsOut(OSAKit.OSAScript.initWithCompiledData_error_, 1)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgIsOut(OSAKit.OSAScript.initWithContentsOfURL_error_, 1)
        self.assertArgIsOut(OSAKit.OSAScript.initWithContentsOfURL_languageInstance_usingStorageOptions_error_, 3)
        self.assertArgIsOut(OSAKit.OSAScript.initWithCompiledData_fromURL_usingStorageOptions_error_, 3)
        self.assertArgIsOut(OSAKit.OSAScript.initWithScriptDataDescriptor_fromURL_languageInstance_usingStorageOptions_error_, 4)

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

        self.assertResultIsBOOL(OSAKit.OSAScript.writeToURL_ofType_usingStorageOptions_error_)
        self.assertArgIsOut(OSAKit.OSAScript.writeToURL_ofType_usingStorageOptions_error_, 3)

        self.assertArgIsOut(OSAKit.OSAScript.compiledDataForType_usingStorageOptions_error_, 2)


if __name__ == "__main__":
    main()
