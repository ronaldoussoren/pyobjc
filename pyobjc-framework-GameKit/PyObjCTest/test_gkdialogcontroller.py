from PyObjCTools.TestSupport import *

import GameKit

class TestGKDialogController (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(GameKit.GKDialogController.presentViewController_)

if __name__ == "__main__":
    main()
