from PyObjCTools.TestSupport import TestCase

import KernelManagement


class TestKernelManagement(TestCase):
    def test_constants(self):
        self.assertIsInstance(KernelManagement.KernelManagementVersionNumber, float)
        self.assertIsInstance(KernelManagement.KernelManagementVersionString, bytes)

        self.assertIsInstance(KernelManagement.OSKernelManagementErrorDomain, str)

    def test_methods(self):
        self.assertResultIsBOOL(
            KernelManagement.KernelManagementClient.loadExtensionsWithPaths_withError_
        )
        self.assertArgIsOut(
            KernelManagement.KernelManagementClient.loadExtensionsWithPaths_withError_,
            1,
        )

        self.assertResultIsBOOL(
            KernelManagement.KernelManagementClient.loadExtensionsWithPaths_withNoAuth_withError_
        )
        self.assertArgIsBOOL(
            KernelManagement.KernelManagementClient.loadExtensionsWithPaths_withNoAuth_withError_,
            1,
        )
        self.assertArgIsOut(
            KernelManagement.KernelManagementClient.loadExtensionsWithPaths_withNoAuth_withError_,
            2,
        )

        self.assertResultIsBOOL(
            KernelManagement.KernelManagementClient.loadExtensionsWithPaths_withIdentifiers_withPersonalityNames_withNoAuth_withError_  # noqa: B950
        )
        self.assertArgIsBOOL(
            KernelManagement.KernelManagementClient.loadExtensionsWithPaths_withIdentifiers_withPersonalityNames_withNoAuth_withError_,  # noqa: B950
            3,
        )
        self.assertArgIsOut(
            KernelManagement.KernelManagementClient.loadExtensionsWithPaths_withIdentifiers_withPersonalityNames_withNoAuth_withError_,  # noqa: B950
            4,
        )
