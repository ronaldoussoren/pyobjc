from PyObjCTools.TestSupport import TestCase

import SafariServices


class TestSFContentBlockerState(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(SafariServices.SFContentBlockerState.isEnabled)
        self.assertArgIsBOOL(SafariServices.SFContentBlockerState.setEnabled_, 0)
