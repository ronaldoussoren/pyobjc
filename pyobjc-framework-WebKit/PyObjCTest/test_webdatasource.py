from PyObjCTools.TestSupport import TestCase
import WebKit


class TestWebDataSource(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.WebDataSource.isLoading)
