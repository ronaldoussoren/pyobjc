import AVFoundation
from PyObjCTools.TestSupport import *


class TestAVMediaSelection(TestCase):
    @min_os_level("10.11")
    def testMethods(self):
        self.assertResultIsBOOL(
            AVFoundation.AVMediaSelection.mediaSelectionCriteriaCanBeAppliedAutomaticallyToMediaSelectionGroup_
        )


if __name__ == "__main__":
    main()
