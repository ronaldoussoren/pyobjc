from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSUserActivity (TestCase):
    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(NSUserActivityDocumentURLKey, unicode)
        self.assertIsInstance(NSUserActivityTypeBrowsingWeb, unicode)

    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertIsInstance(NSUserActivityContentUserActionPlay, unicode)
        self.assertIsInstance(NSUserActivityContentUserActionRecord, unicode)
        self.assertIsInstance(NSUserActivityContentUserActionCall, unicode)
        self.assertIsInstance(NSUserActivityContentUserActionNavigate, unicode)
        self.assertIsInstance(NSUserActivityContentUserActionMessage, unicode)
        self.assertIsInstance(NSUserActivityContentUserActionFacetime, unicode)
        self.assertIsInstance(NSUserActivityContentUserActionSchedule, unicode)


    @min_os_level('10.10')
    def testMethods_10(self):
        self.assertResultIsBOOL(NSUserActivity.needsSave)
        self.assertArgIsBOOL(NSUserActivity.setNeedsSave_, 0)

        self.assertResultIsBOOL(NSUserActivity.supportsContinuationStreams)
        self.assertArgIsBOOL(NSUserActivity.setSupportsContinuationStreams_, 0)

        self.assertArgIsBlock(NSUserActivity.getContinuationStreamsWithCompletionHandler_, 0, b'v@@@')

    @min_os_level('10.11')
    def testMethods_11(self):
        self.assertResultIsBOOL(NSUserActivity.isEligibleForHandoff)
        self.assertArgIsBOOL(NSUserActivity.setEligibleForHandoff_, 0)

        self.assertResultIsBOOL(NSUserActivity.isEligibleForSearch)
        self.assertArgIsBOOL(NSUserActivity.setEligibleForSearch_, 0)

        self.assertResultIsBOOL(NSUserActivity.isEligibleForPublicIndexing)
        self.assertArgIsBOOL(NSUserActivity.setEligibleForPublicIndexing_, 0)

    @min_os_level('10.10')
    def testProtocols(self):
        objc.protocolNamed('NSUserActivityDelegate')

if __name__ == "__main__":
    main()
