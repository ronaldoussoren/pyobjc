
from PyObjCTools.TestSupport import *
from LaunchServices import *

try:
    unicode
except NameError:
    unicode = str

class TestLSQuarantine (TestCase):
    def testConstants(self):
        self.assertIsInstance(kLSQuarantineAgentNameKey, unicode)
        self.assertIsInstance(kLSQuarantineAgentBundleIdentifierKey, unicode)
        self.assertIsInstance(kLSQuarantineTimeStampKey, unicode)
        self.assertIsInstance(kLSQuarantineTypeKey, unicode)
        self.assertIsInstance(kLSQuarantineTypeWebDownload, unicode)
        self.assertIsInstance(kLSQuarantineTypeOtherDownload, unicode)
        self.assertIsInstance(kLSQuarantineTypeEmailAttachment, unicode)
        self.assertIsInstance(kLSQuarantineTypeInstantMessageAttachment, unicode)
        self.assertIsInstance(kLSQuarantineTypeCalendarEventAttachment, unicode)
        self.assertIsInstance(kLSQuarantineTypeOtherAttachment, unicode)
        self.assertIsInstance(kLSQuarantineOriginURLKey, unicode)
        self.assertIsInstance(kLSQuarantineDataURLKey, unicode)

if __name__ == "__main__":
    main()
