from PyObjCTools.TestSupport import *

import DiscRecording

class TestDRCoreObject (TestCase):
    def testFunctions(self):
        # A manual wrapper is not needed with the current apinotes
        #self.assertNotIsInstance(DiscRecording.DRSetRefCon, objc.function)

        DiscRecording.DRSetRefCon
        DiscRecording.DRGetRefCon

        self.assertResultIsCFRetained(DiscRecording.DRCopyLocalizedStringForValue)



if __name__ == "__main__":
    main()
