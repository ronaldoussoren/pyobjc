from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import PhotosUI

    class TestPHProjectTypeDescription (TestCase):
        @min_os_level('10.14')
        def testMethods(self):
            self.assertResultIsBOOL(PhotosUI.PHProjectTypeDescription.canProvideSubtypes)

if __name__ == "__main__":
    main()
