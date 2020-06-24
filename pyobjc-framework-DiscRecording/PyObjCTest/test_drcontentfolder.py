import DiscRecording
from PyObjCTools.TestSupport import TestCase, expectedFailure


class TestDRContentFolder(TestCase):
    @expectedFailure
    def testCFTypes(self):
        self.assertIsCFType(DiscRecording.DRFolderRef)

    def testFunctions(self):
        self.assertIsInstance(DiscRecording.DRFolderGetTypeID(), int)

        self.assertResultIsCFRetained(DiscRecording.DRFolderCreateReal)
        self.assertArgIsIn(DiscRecording.DRFolderCreateReal, 0)

        self.assertResultIsCFRetained(DiscRecording.DRFolderCreateRealWithURL)

        self.assertResultIsCFRetained(DiscRecording.DRFolderCreateVirtual)

        DiscRecording.DRFolderConvertRealToVirtual
        DiscRecording.DRFolderAddChild
        DiscRecording.DRFolderRemoveChild
        DiscRecording.DRFolderCountChildren

        self.assertResultIsCFRetained(DiscRecording.DRFolderCopyChildren)
