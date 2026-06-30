from PyObjCTools.TestSupport import TestCase
import objc
import Quartz


class TestCIImageProviderHelper(Quartz.NSObject):
    @objc.namedSelector(b"provideImageData:bytesPerRow:origin::size::userInfo:")
    def provideImageData_bytesPerRow_origin__size__userInfo_(
        self, data, rowbytes, x, y, width, height, userInfo
    ):
        pass


class TestCIImageProvider(TestCase):
    def test_constants(self):
        self.assertIsInstance(Quartz.kCIImageProviderTileSize, str)
        self.assertIsInstance(Quartz.kCIImageProviderUserInfo, str)
        self.assertIsInstance(Quartz.kCIOutputNativeSizeKey, str)

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestCIImageProviderHelper.provideImageData_bytesPerRow_origin__size__userInfo_,
            0,
            b"o^v",
        )
        self.assertArgIsVariableSize(
            TestCIImageProviderHelper.provideImageData_bytesPerRow_origin__size__userInfo_,
            0,
            b"o^v",
        )
        self.assertArgHasType(
            TestCIImageProviderHelper.provideImageData_bytesPerRow_origin__size__userInfo_,
            1,
            objc._C_ULNG,
        )
        self.assertArgHasType(
            TestCIImageProviderHelper.provideImageData_bytesPerRow_origin__size__userInfo_,
            2,
            objc._C_ULNG,
        )
        self.assertArgHasType(
            TestCIImageProviderHelper.provideImageData_bytesPerRow_origin__size__userInfo_,
            3,
            objc._C_ULNG,
        )
        self.assertArgHasType(
            TestCIImageProviderHelper.provideImageData_bytesPerRow_origin__size__userInfo_,
            4,
            objc._C_ULNG,
        )
        self.assertArgHasType(
            TestCIImageProviderHelper.provideImageData_bytesPerRow_origin__size__userInfo_,
            5,
            objc._C_ULNG,
        )
        self.assertArgHasType(
            TestCIImageProviderHelper.provideImageData_bytesPerRow_origin__size__userInfo_,
            6,
            objc._C_ID,
        )
