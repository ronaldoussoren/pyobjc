from PyObjCTools.TestSupport import *
from Quartz import *

class TestCVMetalTextureCache (TestCase):

    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertIsInstance(kCVMetalTextureCacheMaximumTextureAgeKey, unicode)


    @min_os_level('10.11')
    def testFunctions10_11(self):
        self.assertIsInstance(CVMetalTextureCacheGetTypeID(), (int, long))

        CVMetalTextureCacheCreate
        self.assertArgIsOut(CVMetalTextureCacheCreateTextureFromImage, 8)
        CVMetalTextureCacheFlush


if __name__ == "__main__":
    main()
