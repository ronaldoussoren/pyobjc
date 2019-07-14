import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import PencilKit

    class TestPKInkingTool (TestCase):
        @min_os_level('10.15')
        def test_constants(self):
            self.assertIsInstance(PencilKit.PKInkTypePen, unicode)
            self.assertIsInstance(PencilKit.PKInkTypePencil, unicode)
            self.assertIsInstance(PencilKit.PKInkTypeMarker, unicode)
