import CoreAudioKit
from PyObjCTools.TestSupport import *


class TestAUCustomViewPersistentData(TestCase):
    def testProtocols(self):
        objc.protocolNamed("AUCustomViewPersistentData")


if __name__ == "__main__":
    main()
