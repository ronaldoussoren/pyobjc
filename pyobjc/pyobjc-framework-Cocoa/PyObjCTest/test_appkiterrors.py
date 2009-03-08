
from PyObjCTools.TestSupport import *
from AppKit import *

class TestAppKitErrors (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSTextReadInapplicableDocumentTypeError, 65806)
        self.failUnlessEqual(NSTextWriteInapplicableDocumentTypeError, 66062)
        self.failUnlessEqual(NSTextReadWriteErrorMinimum, 65792)
        self.failUnlessEqual(NSTextReadWriteErrorMaximum, 66303)
        self.failUnlessEqual(NSServiceApplicationNotFoundError, 66560)
        self.failUnlessEqual(NSServiceApplicationLaunchFailedError, 66561)
        self.failUnlessEqual(NSServiceRequestTimedOutError, 66562)
        self.failUnlessEqual(NSServiceInvalidPasteboardDataError, 66563)
        self.failUnlessEqual(NSServiceMalformedServiceDictionaryError, 66564)
        self.failUnlessEqual(NSServiceMiscellaneousError, 66800)
        self.failUnlessEqual(NSServiceErrorMinimum, 66560)
        self.failUnlessEqual(NSServiceErrorMaximum, 66817)


if __name__ == "__main__":
    main()
