from PyObjCTools.TestSupport import *

import OpenDirectory

try:
    unicode
except NameError:
    unicode = str

class TestOpenDirectory (TestCase):
    def testConstants(self):
        self.assertIsInstance(OpenDirectory.ODFrameworkErrorDomain, unicode)


if __name__ == "__main__":
    main()
