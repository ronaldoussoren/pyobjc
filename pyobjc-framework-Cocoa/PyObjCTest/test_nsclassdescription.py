from PyObjCTools.TestSupport import *

from Foundation import *

try:
    unicode
except NameError:
    unicode = str

class TestNSClassDescription (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSClassDescriptionNeededForClassNotification, unicode)

if __name__ == "__main__":
    main()
