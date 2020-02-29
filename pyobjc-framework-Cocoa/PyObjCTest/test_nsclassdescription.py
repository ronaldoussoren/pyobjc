from Foundation import *
from PyObjCTools.TestSupport import *


class TestNSClassDescription(TestCase):
    def testConstants(self):
        self.assertIsInstance(NSClassDescriptionNeededForClassNotification, unicode)


if __name__ == "__main__":
    main()
