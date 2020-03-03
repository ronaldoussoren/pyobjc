import Automator
from PyObjCTools.TestSupport import TestCase


class TestAMBundleAction(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(
            Automator.AMBundleAction.initWithDefinition_fromArchive_, 1
        )
        self.assertResultIsBOOL(Automator.AMBundleAction.hasView)
