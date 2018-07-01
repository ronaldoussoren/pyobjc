from PyObjCTools.TestSupport import *

import DiscRecording

class TestDRContentFolder (TestCase):
    @expectedFailure
    def testCFTypes(self):
        self.assertIsCFType(DiscRecording.DRFolderRef)


    def testFunctions(self):
        self.assertIsInstance(DiscRecording.DRFolderGetTypeID(), (int, long))

        self.assertResultIsCFRetained(DiscRecording.DRFolderCreateReal)
        self.assertArgIsIn(DiscRecording.DRFolderCreateReal, 0)

        self.assertResultIsCFRetained(DiscRecording.DRFolderCreateRealWithURL)

        self.assertResultIsCFRetained(DiscRecording.DRFolderCreateVirtual)

        DiscRecording.DRFolderConvertRealToVirtual
        DiscRecording.DRFolderAddChild
        DiscRecording.DRFolderRemoveChild
        DiscRecording.DRFolderCountChildren

        self.assertResultIsCFRetained(DiscRecording.DRFolderCopyChildren)


if __name__ == "__main__":
    main()
