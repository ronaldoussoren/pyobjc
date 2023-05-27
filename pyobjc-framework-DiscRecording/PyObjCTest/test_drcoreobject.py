import DiscRecording
from PyObjCTools.TestSupport import TestCase


class TestDRCoreObject(TestCase):
    def testFunctions(self):
        # A manual wrapper is not needed with the current apinotes
        # self.assertNotIsInstance(DiscRecording.DRSetRefCon, objc.function)

        # DiscRecording.DRSetRefCon
        # DiscRecording.DRGetRefCon

        self.assertResultIsCFRetained(DiscRecording.DRCopyLocalizedStringForValue)
