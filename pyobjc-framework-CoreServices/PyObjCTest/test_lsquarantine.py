import CoreServices
from PyObjCTools.TestSupport import TestCase


class TestLSQuarantine(TestCase):
    def testConstants(self):
        self.assertIsInstance(CoreServices.kLSQuarantineAgentNameKey, str)
        self.assertIsInstance(CoreServices.kLSQuarantineAgentBundleIdentifierKey, str)
        self.assertIsInstance(CoreServices.kLSQuarantineTimeStampKey, str)
        self.assertIsInstance(CoreServices.kLSQuarantineTypeKey, str)
        self.assertIsInstance(CoreServices.kLSQuarantineTypeWebDownload, str)
        self.assertIsInstance(CoreServices.kLSQuarantineTypeOtherDownload, str)
        self.assertIsInstance(CoreServices.kLSQuarantineTypeEmailAttachment, str)
        self.assertIsInstance(
            CoreServices.kLSQuarantineTypeInstantMessageAttachment, str
        )
        self.assertIsInstance(
            CoreServices.kLSQuarantineTypeCalendarEventAttachment, str
        )
        self.assertIsInstance(CoreServices.kLSQuarantineTypeOtherAttachment, str)
        self.assertIsInstance(CoreServices.kLSQuarantineOriginURLKey, str)
        self.assertIsInstance(CoreServices.kLSQuarantineDataURLKey, str)
