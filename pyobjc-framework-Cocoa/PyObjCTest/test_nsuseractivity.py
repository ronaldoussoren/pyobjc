from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSUserActivity (TestCase):
    @min_os_level('10.10')
    @onlyOn64Bit
    def testConstants10_10(self):
        self.assertIsInstance(NSUserActivityDocumentURLKey, unicode)
        self.assertIsInstance(NSUserActivityTypeBrowsingWeb, unicode)

    @min_os_level('10.10')
    @onlyOn64Bit
    def testMethods10_10(self):
        self.assertResultIsBOOL(NSUserActivity.needsSave)
        self.assertArgIsBOOL(NSUserActivity.setNeedsSave_, 0)

        self.assertResultIsBOOL(NSUserActivity.supportsContinuationStreams)
        self.assertArgIsBOOL(NSUserActivity.setSupportsContinuationStreams_, 0)

        self.assertArgIsBlock(NSUserActivity.getContinuationStreamsWithCompletionHandler_, 0, b'v@@@')

    @min_os_level('10.11')
    @onlyOn64Bit
    def testMethods10_11(self):
        self.assertResultIsBOOL(NSUserActivity.isEligibleForHandoff)
        self.assertArgIsBOOL(NSUserActivity.setEligibleForHandoff_, 0)

        self.assertResultIsBOOL(NSUserActivity.isEligibleForSearch)
        self.assertArgIsBOOL(NSUserActivity.setEligibleForSearch_, 0)

        self.assertResultIsBOOL(NSUserActivity.isEligibleForPublicIndexing)
        self.assertArgIsBOOL(NSUserActivity.setEligibleForPublicIndexing_, 0)

    @min_os_level('10.10')
    @onlyOn64Bit
    def testProtocols(self):
        objc.protocolNamed('NSUserActivityDelegate')

if __name__ == "__main__":
    main()
