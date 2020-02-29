import DiscRecording
from PyObjCTools.TestSupport import *


class TestDRMSF(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DiscRecording.DRMSF.isEqualToMSF_)


if __name__ == "__main__":
    main()
