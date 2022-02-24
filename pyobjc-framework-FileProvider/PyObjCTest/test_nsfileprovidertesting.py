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
    def test_enum_types(self):
        self.assertIsEnumType(FileProvider.NSFileProviderTestingOperationSide)
        self.assertIsEnumType(FileProvider.NSFileProviderTestingOperationType)

    def test_constants(self):
        self.assertEqual(FileProvider.NSFileProviderTestingOperationSideDisk, 0)
        self.assertEqual(FileProvider.NSFileProviderTestingOperationSideFileProvider, 1)

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
        objc.protocolNamed("NSFileProviderTestingOperation")
        objc.protocolNamed("NSFileProviderTestingIngestion")
        objc.protocolNamed("NSFileProviderTestingLookup")
        objc.protocolNamed("NSFileProviderTestingContentFetch")
        objc.protocolNamed("NSFileProviderTestingChildrenEnumeration")
        objc.protocolNamed("NSFileProviderTestingCreation")
        objc.protocolNamed("NSFileProviderTestingModification")
        objc.protocolNamed("NSFileProviderTestingDeletion")
        objc.protocolNamed("NSFileProviderTestingCollisionResolution")

    def test_proto_methods(self):
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
