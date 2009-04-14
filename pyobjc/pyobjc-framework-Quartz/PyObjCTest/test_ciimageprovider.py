
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCIImageProviderHelper (NSObject):
    def provideImageData_bytesPerRow_origin__size__userInfo_(self,
            data, rowbytes, x, y, width, height, userInfo):
        pass

class TestCIImageProvider (TestCase):
    def testMethods(self):
        self.failUnlessArgHasType(TestCIImageProviderHelper.provideImageData_bytesPerRow_origin__size__userInfo_, 0, 'o^v')
        self.failUnlessArgIsVariableSize(TestCIImageProviderHelper.provideImageData_bytesPerRow_origin__size__userInfo_, 0, 'o^v')
        self.failUnlessArgHasType(TestCIImageProviderHelper.provideImageData_bytesPerRow_origin__size__userInfo_, 1, objc._C_ULNG)
        self.failUnlessArgHasType(TestCIImageProviderHelper.provideImageData_bytesPerRow_origin__size__userInfo_, 2, objc._C_ULNG)
        self.failUnlessArgHasType(TestCIImageProviderHelper.provideImageData_bytesPerRow_origin__size__userInfo_, 3, objc._C_ULNG)
        self.failUnlessArgHasType(TestCIImageProviderHelper.provideImageData_bytesPerRow_origin__size__userInfo_, 4, objc._C_ULNG)
        self.failUnlessArgHasType(TestCIImageProviderHelper.provideImageData_bytesPerRow_origin__size__userInfo_, 5, objc._C_ULNG)
        self.failUnlessArgHasType(TestCIImageProviderHelper.provideImageData_bytesPerRow_origin__size__userInfo_, 6, objc._C_ID)

    def testConstants(self):
        self.failUnlessIsInstance(kCIImageProviderTileSize, unicode)
        self.failUnlessIsInstance(kCIImageProviderUserInfo, unicode)


if __name__ == "__main__":
    main()
