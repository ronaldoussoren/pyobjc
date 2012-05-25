from PyObjCTools.TestSupport import *
from Foundation import *

try:
    unicode
except NameError:
    unicode = str

class TestNSURLCredentialStorage (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSURLCredentialStorageChangedNotification, unicode)


if __name__ == "__main__":
    main()
