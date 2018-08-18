from PyObjCTools.TestSupport import *

import MediaToolbox

class TestMTFormatNames (TestCase):
    def test_functions(self):
        self.assertResultIsCFRetained(MediaToolbox.MTCopyLocalizedNameForMediaType)
        self.assertResultIsCFRetained(MediaToolbox.MTCopyLocalizedNameForMediaSubType)

if __name__ == "__main__":
    main()
