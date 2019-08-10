import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import LinkPresentation

    class TestLPError(TestCase):
        def test_constants(self):
            self.assertIsInstance(LinkPresentation.LPErrorDomain, unicode)

            self.assertEqual(LinkPresentation.LPErrorUnknown, 1)
            self.assertEqual(LinkPresentation.LPErrorMetadataFetchFailed, 2)
            self.assertEqual(LinkPresentation.LPErrorMetadataFetchCancelled, 3)
            self.assertEqual(LinkPresentation.LPErrorMetadataFetchTimedOut, 4)
