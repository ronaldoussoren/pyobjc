import Collaboration
from PyObjCTools.TestSupport import TestCase, expectedFailure


class TestCBIdentity(TestCase):
    @expectedFailure
    def testMethods(self):
        with self.subTest("isHidden"):
            self.assertResultIsBOOL(Collaboration.CBIdentity.isHidden)
        with self.subTest("isMemberOfGroup:"):
            self.assertResultIsBOOL(Collaboration.CBIdentity.isMemberOfGroup_)
        with self.subTest("isEnabled"):
            self.assertResultIsBOOL(Collaboration.CBUserIdentity.isEnabled)
        with self.subTest("authenticateWithPassword:"):
            self.assertResultIsBOOL(
                Collaboration.CBUserIdentity.authenticateWithPassword_
            )
