from PyObjCTools.TestSupport import TestCase, min_os_level

import MediaExtension


class TestMERawProcessorHelper(MediaExtension.NSObject):
    def processorWithFormatDescription_extensionPixelBufferManager_error_(
        self, a, b, c
    ):
        return 1

    def metalDeviceRegistryID(self):
        return 1

    def setMetalDeviceRegistryID_(self, a):
        pass

    def isReadyForMoreMediaData(self):
        return 1

    def processFrameFromImageBuffer_completionHandler_(self, a, b):
        pass


class TestMERawProcessor(TestCase):
    @min_os_level("15.0")
    def test_constants(self):
        self.assertIsInstance(
            MediaExtension.MERAWProcessorValuesDidChangeNotification, str
        )
        self.assertIsInstance(
            MediaExtension.MERAWProcessorReadyForMoreMediaDataDidChangeNotification, str
        )

    def test_protocols(self):
        self.assertProtocolExists("MERAWProcessorExtension")
        self.assertProtocolExists("MERAWProcessor")

    def test_protocol_methods(self):
        self.assertArgIsOut(
            TestMERawProcessorHelper.processorWithFormatDescription_extensionPixelBufferManager_error_,
            2,
        )
        self.assertResultHasType(TestMERawProcessorHelper.metalDeviceRegistryID, b"Q")
        self.assertArgHasType(
            TestMERawProcessorHelper.setMetalDeviceRegistryID_, 0, b"Q"
        )
        self.assertResultIsBOOL(TestMERawProcessorHelper.processFrameFromImageBuffer)
        self.assertArgIsBlock(
            TestMERawProcessorHelper.processFrameFromImageBuffer_completionHandler_,
            0,
            b"v@@",
        )

    @min_os_level("15.0")
    def test_methods(self):
        self.assertArgIsOut(
            MediaExtension.MERAWProcessorPixelBufferManager.createPixelBufferAndReturnError_,
            0,
        )

        self.assertResultIsBOOL(MediaExtension.MERAWProcessingParameter.enabled)
        self.assertArgIsBOOL(MediaExtension.MERAWProcessingParameter.setEnabled_, 0)

        self.assertArgIsBOOL(
            MediaExtension.MERAWProcessingBooleanParameter.initWithName_key_description_initialValue_,
            4,
        )

        self.assertArgIsBOOL(
            MediaExtension.MERAWProcessingBooleanParameter.initWithName_key_description_initialValue_neutralValue_cameraValue_,
            4,
        )
        self.assertArgIsBOOL(
            MediaExtension.MERAWProcessingBooleanParameter.initWithName_key_description_initialValue_neutralValue_cameraValue_,
            5,
        )
        self.assertArgIsBOOL(
            MediaExtension.MERAWProcessingBooleanParameter.initWithName_key_description_initialValue_neutralValue_cameraValue_,
            6,
        )

        self.assertResultIsBOOL(
            MediaExtension.MERAWProcessingBooleanParameter.initialValue
        )
        self.assertResultIsBOOL(
            MediaExtension.MERAWProcessingBooleanParameter.currentValue
        )
        self.assertResultIsBOOL(
            MediaExtension.MERAWProcessingBooleanParameter.neutralValue
        )
        self.assertResultIsBOOL(
            MediaExtension.MERAWProcessingBooleanParameter.cameraValue
        )
