from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import PhotosUI

    class TestPHProjectExtensionContext (TestCase):
        @min_os_level('10.14')
        def testMethods(self):
            self.assertArgIsBlock(PhotosUI.PHProjectExtensionContext.updatedProjectInfoFromProjectInfo_completion_, 1, b'v@')

if __name__ == "__main__":
    main()
