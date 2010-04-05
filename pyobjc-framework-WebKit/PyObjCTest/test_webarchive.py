
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebArchive (TestCase):
    def testConstants(self):
        self.assertIsInstance(WebArchivePboardType, unicode)

if __name__ == "__main__":
    main()
