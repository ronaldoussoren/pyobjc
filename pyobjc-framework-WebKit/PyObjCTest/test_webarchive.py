from PyObjCTools.TestSupport import TestCase
import WebKit


class TestWebArchive(TestCase):
    def testConstants(self):
        self.assertIsInstance(WebKit.WebArchivePboardType, str)
