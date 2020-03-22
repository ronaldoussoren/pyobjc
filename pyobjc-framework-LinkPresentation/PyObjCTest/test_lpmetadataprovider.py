import sys

from PyObjCTools.TestSupport import TestCase

if sys.maxsize > 2 ** 32:
    import LinkPresentation

    class TestLPMetadataProvider(TestCase):
        def test_methods(self):
            LinkPresentation.LPMetadataProvider
