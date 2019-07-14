import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Logging

    class TestMessageComponent (TestCase):
        def test_constants(self):
            self.assertEqual(Logging.OSLogMessageComponentArgumentCategoryUndefined, 0)
            self.assertEqual(Logging.OSLogMessageComponentArgumentCategoryData, 1)
            self.assertEqual(Logging.OSLogMessageComponentArgumentCategoryDouble, 2)
            self.assertEqual(Logging.OSLogMessageComponentArgumentCategoryInt64, 3)
            self.assertEqual(Logging.OSLogMessageComponentArgumentCategoryString, 4)
            self.assertEqual(Logging.OSLogMessageComponentArgumentCategoryUInt64, 5)
