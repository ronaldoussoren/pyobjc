from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSClassDescription (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSClassDescriptionNeededForClassNotification, unicode)
if __name__ == "__main__":
    main()
