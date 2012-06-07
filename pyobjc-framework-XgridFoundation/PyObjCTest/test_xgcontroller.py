
from PyObjCTools.TestSupport import *
from XgridFoundation import *

try:
    unicode
except NameError:
    unicode = str

class TestXGController (TestCase):
    def testConstants(self):
        self.assertIsInstance(XGControllerWillDeallocNotification, unicode)


if __name__ == "__main__":
    main()
