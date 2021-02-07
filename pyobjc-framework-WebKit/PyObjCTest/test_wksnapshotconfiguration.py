from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKSnapshotConfiguration(TestCase):
    @min_os_level("10.15")
    def testMethods(self):
        self.assertResultIsBOOL(WebKit.WKSnapshotConfiguration.afterScreenUpdates)
        self.assertArgIsBOOL(WebKit.WKSnapshotConfiguration.setAfterScreenUpdates_, 0)
