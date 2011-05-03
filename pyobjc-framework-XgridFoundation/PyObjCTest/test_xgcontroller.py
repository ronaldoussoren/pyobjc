
from PyObjCTools.TestSupport import *
from XgridFoundation import *

class TestXGController (TestCase):
    def testConstants(self):
        self.assertIsInstance(XGControllerWillDeallocNotification, unicode)


if __name__ == "__main__":
    main()
