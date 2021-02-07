import Metal
import objc
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTLAccelerationStructureHelper(Metal.NSObject):
    def serializeToURL_error_(self, a, b):
        pass


class TestMTLAccelerationStructure(TestCase):
    def test_constants(self):
        self.assertEqual(Metal.MTLDynamicLibraryErrorNone, 0)
        self.assertEqual(Metal.MTLDynamicLibraryErrorInvalidFile, 1)
        self.assertEqual(Metal.MTLDynamicLibraryErrorCompilationFailure, 2)
        self.assertEqual(Metal.MTLDynamicLibraryErrorUnresolvedInstallName, 3)
        self.assertEqual(Metal.MTLDynamicLibraryErrorDependencyLoadFailure, 4)
        self.assertEqual(Metal.MTLDynamicLibraryErrorUnsupported, 5)

    @min_sdk_level("10.16")
    def test_protocols(self):
        objc.protocolNamed("MTLDynamicLibrary")

    def test_methods(self):
        self.assertResultIsBOOL(
            TestMTLAccelerationStructureHelper.serializeToURL_error_
        )
        self.assertArgHasType(
            TestMTLAccelerationStructureHelper.serializeToURL_error_, 1, b"o^@"
        )
