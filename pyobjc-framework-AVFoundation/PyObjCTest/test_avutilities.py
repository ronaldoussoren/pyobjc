from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVUtilities (TestCase):
    @min_os_level('10.7')
    def testFunctions(self):
        AVFoundation.AVMakeRectWithAspectRatioInsideRect # No further testing needed


if __name__ == "__main__":
    main()
