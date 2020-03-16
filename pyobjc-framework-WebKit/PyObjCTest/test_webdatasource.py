from PyObjCTools.TestSupport import TestCase
import WebKit


class TestWebDataSource(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(WebKit.WebDataSource.isLoading)
