from PyObjCTools.TestSupport import TestCase

import ScreenTime


class TestSTScreenTimeConfiguration(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            ScreenTime.STScreenTimeConfiguration.enforcesChildRestrictions
        )
