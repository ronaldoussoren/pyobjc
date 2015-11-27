from PyObjCTools.TestSupport import *
from Quartz import *

class TestCVMetalTexture (TestCase):


    @min_os_level('10.11')
    def testFunctions10_11(self):
        self.assertIsInstance(CVMetalTextureGetTypeID(), (int, long))

        CVMetalTextureGetTexture
        self.assertResultIsBOOL(CVMetalTextureIsFlipped)

        self.assertArgIsOut(CVMetalTextureGetCleanTexCoords, 1)
        self.assertArgIsOut(CVMetalTextureGetCleanTexCoords, 2)
        self.assertArgIsOut(CVMetalTextureGetCleanTexCoords, 3)
        self.assertArgIsOut(CVMetalTextureGetCleanTexCoords, 4)

        self.assertArgIsFixedSize(CVMetalTextureGetCleanTexCoords, 1, 2)
        self.assertArgIsFixedSize(CVMetalTextureGetCleanTexCoords, 2, 2)
        self.assertArgIsFixedSize(CVMetalTextureGetCleanTexCoords, 3, 2)
        self.assertArgIsFixedSize(CVMetalTextureGetCleanTexCoords, 4, 2)


if __name__ == "__main__":
    main()
