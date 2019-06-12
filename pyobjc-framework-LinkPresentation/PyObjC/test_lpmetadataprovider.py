import sys
from PyObjCTest import *

if sys.maxsize > 2 ** 32:
    import LinkPresentation

    class TestLPMetadataProvider (TestCase):
        def test_methods(self):
            LinkPresentation.LPMetadataProvider



