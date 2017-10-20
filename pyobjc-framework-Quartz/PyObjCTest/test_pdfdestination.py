from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFDestination (TestCase):
    def testConstants(self):
        # XXX: In the 10.13 SDK this is een "extern" defintion istead of an
        # #define.
        self.assertEqual(kPDFDestinationUnspecifiedValue, objc._FLT_MAX)

if __name__ == "__main__":
    main()
