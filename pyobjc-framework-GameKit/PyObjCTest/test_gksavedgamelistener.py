import GameKit
from PyObjCTools.TestSupport import *


class TestGKSavedGameListener(TestCase):
    def testProtocols(self):
        objc.protocolNamed("GKSavedGameListener")


if __name__ == "__main__":
    main()
