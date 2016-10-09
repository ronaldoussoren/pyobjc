import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import SafariServices

    class TestSFError (TestCase):
        @min_os_level('10.12')
        def testConstants(self):
            self.assertEqual(SafariServices.SFErrorNoExtensionFound, 1)
            self.assertEqual(SafariServices.SFErrorNoAttachmentFound, 2)
            self.assertEqual(SafariServices.SFErrorLoadingInterrupted, 3)



if __name__ == "__main__":
    main()

