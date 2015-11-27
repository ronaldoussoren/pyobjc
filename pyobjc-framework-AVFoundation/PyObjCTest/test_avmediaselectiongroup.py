from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVMediaSelectionGroup (TestCase):
    @min_os_level('10.8')
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVMediaSelectionGroup.allowsEmptySelection)

        self.assertResultIsBOOL(AVFoundation.AVMediaSelectionOption.hasMediaCharacteristic_)
        self.assertResultIsBOOL(AVFoundation.AVMediaSelectionOption.isPlayable)

if __name__ == "__main__":
    main()
