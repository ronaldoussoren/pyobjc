
from PyObjCTools.TestSupport import *
from Message import *

class TestNSMailDelivery (TestCase):
    def testClasses(self):
        self.assertResultIsBOOL(NSMailDelivery.hasDeliveryClassBeenConfigured)
        self.assertResultIsBOOL(NSMailDelivery.deliverMessage_headers_format_protocol_)
        self.assertResultIsBOOL(NSMailDelivery.deliverMessage_subject_to_)

    def testConstants(self):
        self.assertIsInstance(NSMIMEMailFormat, unicode)
        self.assertIsInstance(NSASCIIMailFormat, unicode)
        self.assertIsInstance(NSSMTPDeliveryProtocol, unicode)
        self.assertIsInstance(NSSendmailDeliveryProtocol, unicode)


if __name__ == "__main__":
    main()
