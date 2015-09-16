from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSAlignmentFeedbackFilter (TestCase):
    @min_os_level('10.11')
    def testProtocols(self):
        objc.protocolNamed('NSAlignmentFeedbackToken')

if __name__ == "__main__":
    main()
