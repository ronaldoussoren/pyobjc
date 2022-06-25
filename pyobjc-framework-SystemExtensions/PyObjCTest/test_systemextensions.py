import SystemExtensions
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestSystemExtensions(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(SystemExtensions.OSSystemExtensionReplacementAction)
        self.assertIsEnumType(SystemExtensions.OSSystemExtensionRequestResult)

    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertIsInstance(SystemExtensions.OSRelatedKernelExtensionKey, str)

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(SystemExtensions.OSSystemExtensionErrorDomain, str)
        self.assertIsInstance(SystemExtensions.OSBundleUsageDescriptionKey, str)
        self.assertIsInstance(
            SystemExtensions.NSSystemExtensionUsageDescriptionKey, str
        )

        self.assertEqual(SystemExtensions.OSSystemExtensionErrorUnknown, 1)
        self.assertEqual(SystemExtensions.OSSystemExtensionErrorMissingEntitlement, 2)
        self.assertEqual(
            SystemExtensions.OSSystemExtensionErrorUnsupportedParentBundleLocation, 3
        )
        self.assertEqual(SystemExtensions.OSSystemExtensionErrorExtensionNotFound, 4)
        self.assertEqual(
            SystemExtensions.OSSystemExtensionErrorExtensionMissingIdentifier, 5
        )
        self.assertEqual(
            SystemExtensions.OSSystemExtensionErrorDuplicateExtensionIdentifer, 6
        )
        self.assertEqual(
            SystemExtensions.OSSystemExtensionErrorUnknownExtensionCategory, 7
        )
        self.assertEqual(SystemExtensions.OSSystemExtensionErrorCodeSignatureInvalid, 8)
        self.assertEqual(SystemExtensions.OSSystemExtensionErrorValidationFailed, 9)
        self.assertEqual(
            SystemExtensions.OSSystemExtensionErrorForbiddenBySystemPolicy, 10
        )
        self.assertEqual(SystemExtensions.OSSystemExtensionErrorRequestCanceled, 11)
        self.assertEqual(SystemExtensions.OSSystemExtensionErrorRequestSuperseded, 12)
        self.assertEqual(
            SystemExtensions.OSSystemExtensionErrorAuthorizationRequired, 13
        )

        self.assertEqual(SystemExtensions.OSSystemExtensionReplacementActionCancel, 0)
        self.assertEqual(SystemExtensions.OSSystemExtensionReplacementActionReplace, 1)

        self.assertEqual(SystemExtensions.OSSystemExtensionRequestCompleted, 0)
        self.assertEqual(
            SystemExtensions.OSSystemExtensionRequestWillCompleteAfterReboot, 1
        )

    @min_sdk_level("10.15")
    def test_protocols(self):
        self.assertProtocolExists("OSSystemExtensionRequestDelegate")

    @min_os_level("10.15")
    def test_classes(self):
        # Explictly test for classes because the API doesn't require any
        # other testing
        SystemExtensions.OSSystemExtensionRequest
        SystemExtensions.OSSystemExtensionProperties
        SystemExtensions.OSSystemExtensionManager

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBOOL(SystemExtensions.OSSystemExtensionProperties.isEnabled)
        self.assertResultIsBOOL(
            SystemExtensions.OSSystemExtensionProperties.isAwaitingUserApproval
        )
        self.assertResultIsBOOL(
            SystemExtensions.OSSystemExtensionProperties.isUninstalling
        )


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(SystemExtensions)
