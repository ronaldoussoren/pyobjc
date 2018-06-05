from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Photos

    class TestPHProject (TestCase):
        @min_os_level('10.14')
        def test_methods(self):
            self.assertResultIsBOOL(Photos.PHProject.hasProjectPreview)

if __name__ == "__main__":
    main()
