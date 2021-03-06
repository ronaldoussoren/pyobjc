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


class TestNSFileProviderTesting(TestCase):
    def test_constants(self):
        self.assertEqual(FileProvider.NSFileProviderTestingOperationSideDisk, 0)
        self.assertEqual(FileProvider.NSFileProviderTestingOperationSideFileProvider, 1)

    @min_sdk_level("11.3")
    def test_protocols(self):
        objc.protocolNamed("NSFileProviderTestingOperation")
        objc.protocolNamed("NSFileProviderTestingIngestion")
        objc.protocolNamed("NSFileProviderTestingLookup")
        objc.protocolNamed("NSFileProviderTestingPropagation")
        objc.protocolNamed("NSFileProviderTestingContentFetch")
        objc.protocolNamed("NSFileProviderTestingChildrenEnumeration")
        objc.protocolNamed("NSFileProviderTestingBounce")

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

    @min_os_level("11.3")
    def test_methods11_3(self):
        self.assertArgIsOut(
            FileProvider.NSFileProviderManager.listAvailableTestingOperationsWithError_,
            0,
        )
        self.assertArgIsOut(
            FileProvider.NSFileProviderManager.runTestingOperations_error_, 1
        )
