import warnings

from PyObjCTools.TestSupport import TestCase

with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
    import LaunchServices


class TestLSQuarantine(TestCase):
    def testConstants(self):
        self.assertIsInstance(LaunchServices.kLSQuarantineAgentNameKey, str)
        self.assertIsInstance(LaunchServices.kLSQuarantineAgentBundleIdentifierKey, str)
        self.assertIsInstance(LaunchServices.kLSQuarantineTimeStampKey, str)
        self.assertIsInstance(LaunchServices.kLSQuarantineTypeKey, str)
        self.assertIsInstance(LaunchServices.kLSQuarantineTypeWebDownload, str)
        self.assertIsInstance(LaunchServices.kLSQuarantineTypeOtherDownload, str)
        self.assertIsInstance(LaunchServices.kLSQuarantineTypeEmailAttachment, str)
        self.assertIsInstance(
            LaunchServices.kLSQuarantineTypeInstantMessageAttachment, str
        )
        self.assertIsInstance(
            LaunchServices.kLSQuarantineTypeCalendarEventAttachment, str
        )
        self.assertIsInstance(LaunchServices.kLSQuarantineTypeOtherAttachment, str)
        self.assertIsInstance(LaunchServices.kLSQuarantineOriginURLKey, str)
        self.assertIsInstance(LaunchServices.kLSQuarantineDataURLKey, str)
