
from PyObjCTools.TestSupport import *
import CoreServices

class TestLSQuarantine (TestCase):
    def testConstants(self):
        self.assertIsInstance(CoreServices.kLSQuarantineAgentNameKey, unicode)
        self.assertIsInstance(CoreServices.kLSQuarantineAgentBundleIdentifierKey, unicode)
        self.assertIsInstance(CoreServices.kLSQuarantineTimeStampKey, unicode)
        self.assertIsInstance(CoreServices.kLSQuarantineTypeKey, unicode)
        self.assertIsInstance(CoreServices.kLSQuarantineTypeWebDownload, unicode)
        self.assertIsInstance(CoreServices.kLSQuarantineTypeOtherDownload, unicode)
        self.assertIsInstance(CoreServices.kLSQuarantineTypeEmailAttachment, unicode)
        self.assertIsInstance(CoreServices.kLSQuarantineTypeInstantMessageAttachment, unicode)
        self.assertIsInstance(CoreServices.kLSQuarantineTypeCalendarEventAttachment, unicode)
        self.assertIsInstance(CoreServices.kLSQuarantineTypeOtherAttachment, unicode)
        self.assertIsInstance(CoreServices.kLSQuarantineOriginURLKey, unicode)
        self.assertIsInstance(CoreServices.kLSQuarantineDataURLKey, unicode)

if __name__ == "__main__":
    main()
