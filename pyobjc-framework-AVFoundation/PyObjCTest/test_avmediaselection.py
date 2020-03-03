import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVMediaSelection(TestCase):
    @min_os_level("10.11")
    def testMethods(self):
        self.assertResultIsBOOL(
            AVFoundation.AVMediaSelection.mediaSelectionCriteriaCanBeAppliedAutomaticallyToMediaSelectionGroup_  # noqa: B950
        )
