
from PyObjCTools.TestSupport import *
from AppKit import *

class TestAppKitErrors (TestCase):
    def testConstants(self):
        self.assertEqual(NSTextReadInapplicableDocumentTypeError, 65806)
        self.assertEqual(NSTextWriteInapplicableDocumentTypeError, 66062)
        self.assertEqual(NSTextReadWriteErrorMinimum, 65792)
        self.assertEqual(NSTextReadWriteErrorMaximum, 66303)
        self.assertEqual(NSServiceApplicationNotFoundError, 66560)
        self.assertEqual(NSServiceApplicationLaunchFailedError, 66561)
        self.assertEqual(NSServiceRequestTimedOutError, 66562)
        self.assertEqual(NSServiceInvalidPasteboardDataError, 66563)
        self.assertEqual(NSServiceMalformedServiceDictionaryError, 66564)
        self.assertEqual(NSServiceMiscellaneousError, 66800)
        self.assertEqual(NSServiceErrorMinimum, 66560)
        self.assertEqual(NSServiceErrorMaximum, 66817)


if __name__ == "__main__":
    main()
