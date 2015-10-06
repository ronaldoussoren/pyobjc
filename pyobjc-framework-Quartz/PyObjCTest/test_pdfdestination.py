from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFDestination (TestCase):
    def testConstants(self):
        self.assertEqual(kPDFDestinationUnspecifiedValue, objc._FLT_MAX)

if __name__ == "__main__":
    main()
