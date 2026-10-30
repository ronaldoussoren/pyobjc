import FileProvider
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSFileProviderTestingHelper(FileProvider.NSObject):
    def side(self):
        return 1

    def targetSide(self):
        return 1

    def changedFields(self):
        return 1

    def type(self):  # noqa: A003
        return 1


class TestNSFileProviderTesting(TestCase):
    def test_enums(self):
        self.assertIsEnumType(FileProvider.NSFileProviderTestingOperationSide)
        self.assertEqual(FileProvider.NSFileProviderTestingOperationSideDisk, 0)
        self.assertEqual(FileProvider.NSFileProviderTestingOperationSideFileProvider, 1)

        self.assertIsEnumType(FileProvider.NSFileProviderTestingOperationType)
        self.assertEqual(FileProvider.NSFileProviderTestingOperationTypeIngestion, 0)
        self.assertEqual(FileProvider.NSFileProviderTestingOperationTypeLookup, 1)
        self.assertEqual(FileProvider.NSFileProviderTestingOperationTypeCreation, 2)
        self.assertEqual(FileProvider.NSFileProviderTestingOperationTypeModification, 3)
        self.assertEqual(FileProvider.NSFileProviderTestingOperationTypeDeletion, 4)
        self.assertEqual(FileProvider.NSFileProviderTestingOperationTypeContentFetch, 5)
        self.assertEqual(
            FileProvider.NSFileProviderTestingOperationTypeChildrenEnumeration, 6
        )
        self.assertEqual(
            FileProvider.NSFileProviderTestingOperationTypeCollisionResolution, 7
        )

    @min_sdk_level("11.3")
    def test_protocols(self):
        self.assertProtocolExists("NSFileProviderTestingOperation", FileProvider)
        self.assertProtocolExists("NSFileProviderTestingIngestion", FileProvider)
        self.assertProtocolExists("NSFileProviderTestingLookup", FileProvider)
        self.assertProtocolExists("NSFileProviderTestingContentFetch", FileProvider)
        self.assertProtocolExists(
            "NSFileProviderTestingChildrenEnumeration", FileProvider
        )
        self.assertProtocolExists("NSFileProviderTestingCreation", FileProvider)
        self.assertProtocolExists("NSFileProviderTestingModification", FileProvider)
        self.assertProtocolExists("NSFileProviderTestingDeletion", FileProvider)
        self.assertProtocolExists(
            "NSFileProviderTestingCollisionResolution", FileProvider
        )

    def test_protocol_methods(self):
        self.assertResultHasType(
            TestNSFileProviderTestingHelper.side, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestNSFileProviderTestingHelper.targetSide, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestNSFileProviderTestingHelper.changedFields, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestNSFileProviderTestingHelper.type, objc._C_NSInteger
        )

    @min_os_level("11.3")
    def test_methods11_3(self):
        self.assertArgIsOut(
            FileProvider.NSFileProviderManager.listAvailableTestingOperationsWithError_,
            0,
        )
        self.assertArgIsOut(
            FileProvider.NSFileProviderManager.runTestingOperations_error_, 1
        )
