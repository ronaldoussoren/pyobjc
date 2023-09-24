from PyObjCTools.TestSupport import TestCase, min_os_level
import BackgroundAssets


class TestBAError(TestCase):
    def test_constants(self):
        self.assertIsEnumType(BackgroundAssets.BAErrorCode)

        self.assertEqual(BackgroundAssets.BAErrorCodeDownloadInvalid, 0)
        self.assertEqual(BackgroundAssets.BAErrorCodeCallFromExtensionNotAllowed, 50)
        self.assertEqual(
            BackgroundAssets.BAErrorCodeCallFromInactiveProcessNotAllowed, 51
        )
        self.assertEqual(BackgroundAssets.BAErrorCodeCallerConnectionNotAccepted, 55)
        self.assertEqual(BackgroundAssets.BAErrorCodeCallerConnectionInvalid, 56)
        self.assertEqual(BackgroundAssets.BAErrorCodeDownloadAlreadyScheduled, 100)
        self.assertEqual(BackgroundAssets.BAErrorCodeDownloadNotScheduled, 101)
        self.assertEqual(BackgroundAssets.BAErrorCodeDownloadFailedToStart, 102)
        self.assertEqual(BackgroundAssets.BAErrorCodeDownloadAlreadyFailed, 103)
        self.assertEqual(
            BackgroundAssets.BAErrorCodeDownloadEssentialDownloadNotPermitted, 109
        )
        self.assertEqual(
            BackgroundAssets.BAErrorCodeDownloadBackgroundActivityProhibited, 111
        )
        self.assertEqual(BackgroundAssets.BAErrorCodeDownloadWouldExceedAllowance, 112)
        self.assertEqual(
            BackgroundAssets.BAErrorCodeSessionDownloadDisallowedByDomain, 202
        )
        self.assertEqual(
            BackgroundAssets.BAErrorCodeSessionDownloadDisallowedByAllowance, 203
        )
        self.assertEqual(
            BackgroundAssets.BAErrorCodeSessionDownloadAllowanceExceeded, 204
        )
        self.assertEqual(
            BackgroundAssets.BAErrorCodeSessionDownloadNotPermittedBeforeAppLaunch, 206
        )

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(BackgroundAssets.BAErrorDomain, str)
