from PyObjCTools.TestSupport import *

import AVFoundation

try:
    unicode
except NameError:
    unicode = str


class TestAVMediaSelection (TestCase):
    @min_os_level('10.11')
    def testMethodsself):
        self.assertResultIsBOOL(AVFoundation.AVMediaSelection.mediaSelectionCriteriaCanBeAppliedAutomaticallyToMediaSelectionGroup_)

if __name__ == "__main__":
    main()
