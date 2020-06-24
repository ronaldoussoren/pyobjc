import CFOpenDirectory
from PyObjCTools.TestSupport import TestCase


class TestCFODSession(TestCase):
    def testMethods(self):
        self.assertIsInstance(CFOpenDirectory.ODSessionGetTypeID(), int)

        self.assertResultIsCFRetained(CFOpenDirectory.ODSessionCreate)
        self.assertArgIsOut(CFOpenDirectory.ODSessionCreate, 2)

        self.assertResultIsCFRetained(CFOpenDirectory.ODSessionCopyNodeNames)
        self.assertArgIsOut(CFOpenDirectory.ODSessionCopyNodeNames, 2)

    def testConstants(self):
        self.assertIsInstance(
            CFOpenDirectory.kODSessionDefault,
            (CFOpenDirectory.ODSessionRef, type(None)),
        )
