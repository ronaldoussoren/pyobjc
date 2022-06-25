import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTLBinaryArchiveHelper(Metal.NSObject):
    def addComputePipelineFunctionsWithDescriptor_error_(self, a, b):
        return 1

    def addRenderPipelineFunctionsWithDescriptor_error_(self, a, b):
        return 1

    def addTileRenderPipelineFunctionsWithDescriptor_error_(self, a, b):
        return 1

    def serializeToURL_error_(self, a, b):
        pass

    def addFunctionWithDescriptor_library_error_(self, a, b, c):
        return 1


class TestMTLBinaryArchive(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Metal.MTLBinaryArchiveError)

    def test_constants(self):
        self.assertEqual(Metal.MTLBinaryArchiveErrorNone, 0)
        self.assertEqual(Metal.MTLBinaryArchiveErrorInvalidFile, 1)
        self.assertEqual(Metal.MTLBinaryArchiveErrorUnexpectedElement, 2)
        self.assertEqual(Metal.MTLBinaryArchiveErrorCompilationFailure, 3)
        self.assertEqual(Metal.MTLBinaryArchiveErrorInternalError, 4)

    @min_sdk_level("11.0")
    def test_protocols11_0(self):
        self.assertProtocolExists("MTLBinaryArchive")

    def test_methods(self):
        self.assertResultIsBOOL(
            TestMTLBinaryArchiveHelper.addComputePipelineFunctionsWithDescriptor_error_
        )
        self.assertArgHasType(
            TestMTLBinaryArchiveHelper.addComputePipelineFunctionsWithDescriptor_error_,
            1,
            b"o^@",
        )
        self.assertResultIsBOOL(
            TestMTLBinaryArchiveHelper.addRenderPipelineFunctionsWithDescriptor_error_
        )
        self.assertArgHasType(
            TestMTLBinaryArchiveHelper.addRenderPipelineFunctionsWithDescriptor_error_,
            1,
            b"o^@",
        )
        self.assertResultIsBOOL(
            TestMTLBinaryArchiveHelper.addTileRenderPipelineFunctionsWithDescriptor_error_
        )
        self.assertArgHasType(
            TestMTLBinaryArchiveHelper.addTileRenderPipelineFunctionsWithDescriptor_error_,
            1,
            b"o^@",
        )
        self.assertArgHasType(
            TestMTLBinaryArchiveHelper.serializeToURL_error_, 1, b"o^@"
        )
        self.assertResultIsBOOL(
            TestMTLBinaryArchiveHelper.addFunctionWithDescriptor_library_error_
        )
        self.assertArgHasType(
            TestMTLBinaryArchiveHelper.addFunctionWithDescriptor_library_error_,
            2,
            b"o^@",
        )
