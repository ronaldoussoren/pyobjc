import ApplicationServices
import HIServices
from PyObjCTools.TestSupport import *

class TestApplicationServices (TestCase):
    def testTrivial(self):
        ApplicationServices.kAXErrorSuccess

if __name__ == "__main__":
    main()
