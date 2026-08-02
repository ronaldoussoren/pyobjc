from PyObjCTools.TestSupport import TestCase, min_os_level

import SafariServices


class SFSafariSettings(TestCase):
    def test_constants(self):
        self.assertIsEnumType(SafariServices.SFSafariSettingsError)
        self.assertEqual(SafariServices.SFSafariSettingsErrorNotAllowed, 0)
        self.assertEqual(SafariServices.SFSafariSettingsErrorFailed, 1)

    @min_os_level("27.0")
    def test_methods(self):
        self.assertArgIsBlock(
            SafariServices.SFSafariSettings.checkAutoFillUserNamesAndPasswordsEnabledWithCompletionHandler_,
            0,
            b"vZ@",
        )
