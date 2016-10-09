import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import SafariServices

    class TestSFContentBlockerState (TestCase):
        def testMethods(self):
            self.assertResultIsBOOL(SafariServices.SFContentBlockerState.isEnabled)
            self.assertArgIsBOOL(SafariServices.SFContentBlockerState.setEnabled_, 0)


if __name__ == "__main__":
    main()

