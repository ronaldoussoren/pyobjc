
from PyObjCTools.TestSupport import *
from WebKit import *

try:
    unicode
except NameError:
    unicode = str

class TestWebArchive (TestCase):
    def testConstants(self):
        self.assertIsInstance(WebArchivePboardType, unicode)

if __name__ == "__main__":
    main()
