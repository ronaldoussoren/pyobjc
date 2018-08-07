import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import SafariServices

    class TestSFContentBlockerManager (TestCase):
        @min_os_level('10.12')
        def testConstants(self):
            self.assertEqual(SafariServices.SFSafariServicesVersion10_0, 0)
            self.assertEqual(SafariServices.SFSafariServicesVersion10_1, 1)
            self.assertEqual(SafariServices.SFSafariServicesVersion11_0, 2)
            self.assertEqual(SafariServices.SFSafariServicesVersion12_0, 3)

if __name__ == "__main__":
    main()

