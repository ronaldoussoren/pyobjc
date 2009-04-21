
from PyObjCTools.TestSupport import *
from LaunchServices import *

class TestLSQuarantine (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(kLSQuarantineAgentNameKey, unicode)
        self.failUnlessIsInstance(kLSQuarantineAgentBundleIdentifierKey, unicode)
        self.failUnlessIsInstance(kLSQuarantineTimeStampKey, unicode)
        self.failUnlessIsInstance(kLSQuarantineTypeKey, unicode)
        self.failUnlessIsInstance(kLSQuarantineTypeWebDownload, unicode)
        self.failUnlessIsInstance(kLSQuarantineTypeOtherDownload, unicode)
        self.failUnlessIsInstance(kLSQuarantineTypeEmailAttachment, unicode)
        self.failUnlessIsInstance(kLSQuarantineTypeInstantMessageAttachment, unicode)
        self.failUnlessIsInstance(kLSQuarantineTypeCalendarEventAttachment, unicode)
        self.failUnlessIsInstance(kLSQuarantineTypeOtherAttachment, unicode)
        self.failUnlessIsInstance(kLSQuarantineOriginURLKey, unicode)
        self.failUnlessIsInstance(kLSQuarantineDataURLKey, unicode)

if __name__ == "__main__":
    main()
