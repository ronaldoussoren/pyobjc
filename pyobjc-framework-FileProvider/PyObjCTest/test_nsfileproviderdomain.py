import FileProvider
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFileProviderDomain(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(FileProvider.NSFileProviderDomainTestingModes)

    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(FileProvider.NSFileProviderDomainDidChange, str)

        self.assertEqual(
            FileProvider.NSFileProviderDomainTestingModeAlwaysEnabled, 1 << 0
        )
        self.assertEqual(
            FileProvider.NSFileProviderDomainTestingModeInteractive, 1 << 1
        )

        self.assertIsEnumType(FileProvider.NSFileProviderKnownFolders)
        self.assertEqual(FileProvider.NSFileProviderDesktop, 1 << 0)
        self.assertEqual(FileProvider.NSFileProviderDocuments, 1 << 1)

    @min_os_level("26.0")
    def test_constants26_0(self):
        self.assertIsInstance(FileProvider.NSFileProviderUserInfoKey, str)
        self.assertIsInstance(FileProvider.NSFileProviderUserInfoExperimentIDKey, str)

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBOOL(FileProvider.NSFileProviderDomain.isDisconnected)
        self.assertResultIsBOOL(FileProvider.NSFileProviderDomain.userEnabled)
        self.assertResultIsBOOL(FileProvider.NSFileProviderDomain.isHidden)

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(FileProvider.NSFileProviderDomain.supportsSyncingTrash)
        self.assertArgIsBOOL(
            FileProvider.NSFileProviderDomain.setSupportsSyncingTrash_, 0
        )

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertResultIsBOOL(
            FileProvider.NSFileProviderDomain.supportsStringSearchRequest
        )
        self.assertArgIsBOOL(
            FileProvider.NSFileProviderDomain.setSupportsStringSearchRequest_, 0
        )
