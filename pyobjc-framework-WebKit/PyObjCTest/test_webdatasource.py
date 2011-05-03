
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebDataSource (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(WebDataSource.isLoading)

if __name__ == "__main__":
    main()
