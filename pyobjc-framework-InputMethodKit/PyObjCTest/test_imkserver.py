
from PyObjCTools.TestSupport import *
from InputMethodKit import *

class TestIMKServer (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(IMKControllerClass, unicode)
        self.failUnlessIsInstance(IMKDelegateClass, unicode)


if __name__ == "__main__":
    main()
