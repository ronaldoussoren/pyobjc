import Collaboration
from PyObjCTools.TestSupport import TestCase


class TestCBIdentity(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(Collaboration.CBIdentity.isHidden)
        self.assertResultIsBOOL(Collaboration.CBIdentity.isMemberOfGroup_)
        self.assertResultIsBOOL(Collaboration.CBUserIdentity.isEnabled)
        self.assertResultIsBOOL(Collaboration.CBUserIdentity.authenticateWithPassword_)
