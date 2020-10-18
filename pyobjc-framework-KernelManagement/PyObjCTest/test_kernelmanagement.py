from PyObjCTools.TestSupport import TestCase

import KernelManagement


class TestKernelManagement(TestCase):
    def test_constants(self):
        self.assertIsInstance(KernelManagement.KernelManagementVersionNumber, float)
        self.assertIsInstance(KernelManagement.KernelManagementVersionString, bytes)

        self.assertIsInstance(KernelManagement.OSKernelManagementErrorDomain, str)
