
from PyObjCTools.TestSupport import *
import LaunchServices

class TestLSQuarantine (TestCase):
    def testConstants(self):
        self.assertIsInstance(LaunchServices.kLSQuarantineAgentNameKey, unicode)
        self.assertIsInstance(LaunchServices.kLSQuarantineAgentBundleIdentifierKey, unicode)
        self.assertIsInstance(LaunchServices.kLSQuarantineTimeStampKey, unicode)
        self.assertIsInstance(LaunchServices.kLSQuarantineTypeKey, unicode)
        self.assertIsInstance(LaunchServices.kLSQuarantineTypeWebDownload, unicode)
        self.assertIsInstance(LaunchServices.kLSQuarantineTypeOtherDownload, unicode)
        self.assertIsInstance(LaunchServices.kLSQuarantineTypeEmailAttachment, unicode)
        self.assertIsInstance(LaunchServices.kLSQuarantineTypeInstantMessageAttachment, unicode)
        self.assertIsInstance(LaunchServices.kLSQuarantineTypeCalendarEventAttachment, unicode)
        self.assertIsInstance(LaunchServices.kLSQuarantineTypeOtherAttachment, unicode)
        self.assertIsInstance(LaunchServices.kLSQuarantineOriginURLKey, unicode)
        self.assertIsInstance(LaunchServices.kLSQuarantineDataURLKey, unicode)

if __name__ == "__main__":
    main()
