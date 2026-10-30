from PyObjCTools.TestSupport import TestCase
import WebKit


class TestWebArchive(TestCase):
    def test_constants(self):
        self.assertIsInstance(WebKit.WebArchivePboardType, str)
