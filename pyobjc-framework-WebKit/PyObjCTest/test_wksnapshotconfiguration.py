from PyObjCTools.TestSupport import *
from WebKit import *


class TestWKSnapshotConfiguration(TestCase):
    @onlyOn64Bit
    @min_os_level("10.15")
    def testMethods(self):
        self.assertResultIsBOOL(WKSnapshotConfiguration.afterScreenUpdates)
        self.assertArgIsBOOL(WKSnapshotConfiguration.setAfterScreenUpdates_, 0)


if __name__ == "__main__":
    main()
