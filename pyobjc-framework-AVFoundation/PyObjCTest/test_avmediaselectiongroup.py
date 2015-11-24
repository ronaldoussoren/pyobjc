from PyObjCTools.TestSupport import *

import AVFoundation

try:
    unicode
except NameError:
    unicode = str


class TestAVMediaSelectionGroup (TestCase):
    @min_os_level('10.8')
    def testMethodsself):
        self.assertResultIsBOOL(AVFoundation.AVMediaSelectionGroup.allowsEmptySelection)

        self.assertResultIsBOOL(AVFoundation.AVMediaSelectionOption.hasMediaCharacteristic)
        self.assertResultIsBOOL(AVFoundation.AVMediaSelectionOption.isPlayable)

if __name__ == "__main__":
    main()
