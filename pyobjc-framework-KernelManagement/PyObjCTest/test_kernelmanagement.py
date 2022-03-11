from PyObjCTools.TestSupport import TestCase

import KernelManagement


class TestKernelManagement(TestCase):
    def test_constants(self):
        self.assertIsInstance(KernelManagement.KernelManagementVersionNumber, float)
        self.assertIsInstance(KernelManagement.KernelManagementVersionString, bytes)

        self.assertIsInstance(KernelManagement.OSKernelManagementErrorDomain, str)


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(KernelManagement)
