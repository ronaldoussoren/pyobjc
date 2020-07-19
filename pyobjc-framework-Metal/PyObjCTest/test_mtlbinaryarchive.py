import Metal
import objc
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


class TestMTLBinaryArchive(TestCase):
    def test_constants(self):
        self.assertEqual(Metal.MTLBinaryArchiveErrorNone, 0)
        self.assertEqual(Metal.MTLBinaryArchiveErrorInvalidFile, 1)
        self.assertEqual(Metal.MTLBinaryArchiveErrorUnexpectedElement, 2)
        self.assertEqual(Metal.MTLBinaryArchiveErrorCompilationFailure, 3)

    @min_sdk_level("10.16")
    def test_protocols(self):
        objc.protocolNamed("MTLBinaryArchive")

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
