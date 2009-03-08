
from PyObjCTools.TestSupport import *
from Message import *

class TestNSMailDelivery (TestCase):
    def testClasses(self):
        self.failUnlessResultIsBOOL(NSMailDelivery.hasDeliveryClassBeenConfigured)
        self.failUnlessResultIsBOOL(NSMailDelivery.deliverMessage_headers_format_protocol_)
        self.failUnlessResultIsBOOL(NSMailDelivery.deliverMessage_subject_to_)

    def testConstants(self):
        self.failUnlessIsInstance(NSMIMEMailFormat, unicode)
        self.failUnlessIsInstance(NSASCIIMailFormat, unicode)
        self.failUnlessIsInstance(NSSMTPDeliveryProtocol, unicode)
        self.failUnlessIsInstance(NSSendmailDeliveryProtocol, unicode)


if __name__ == "__main__":
    main()
