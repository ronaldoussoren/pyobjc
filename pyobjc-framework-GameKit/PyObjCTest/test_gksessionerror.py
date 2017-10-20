from PyObjCTools.TestSupport import *

import GameKit

class TestGKSessionError (TestCase):

    def testConstants(self):
        self.assertIsInstance(GameKit.GKSessionErrorDomain, unicode)

if __name__ == "__main__":
    main()
