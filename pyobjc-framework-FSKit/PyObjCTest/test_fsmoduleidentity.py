from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSModuleIdentity(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(FSKit.FSModuleIdentity.isSystem)
