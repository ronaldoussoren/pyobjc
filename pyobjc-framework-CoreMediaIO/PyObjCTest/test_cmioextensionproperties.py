import CoreMediaIO
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCMIOExtensionProperties(TestCase):
    def test_enum_types(self):
        self.assertIsTypedEnum(CoreMediaIO.CMIOExtensionProperty, str)

    @min_os_level("12.3")
    def test_constants(self):
        self.assertIsInstance(CoreMediaIO.CMIOExtensionPropertyProviderName, str)
        self.assertIsInstance(
            CoreMediaIO.CMIOExtensionPropertyProviderManufacturer, str
        )
        self.assertIsInstance(CoreMediaIO.CMIOExtensionPropertyDeviceModel, str)
        self.assertIsInstance(CoreMediaIO.CMIOExtensionPropertyDeviceIsSuspended, str)
        self.assertIsInstance(CoreMediaIO.CMIOExtensionPropertyDeviceTransportType, str)
        self.assertIsInstance(
            CoreMediaIO.CMIOExtensionPropertyDeviceLinkedCoreAudioDeviceUID, str
        )
        self.assertIsInstance(
            CoreMediaIO.CMIOExtensionPropertyDeviceCanBeDefaultInputDevice, str
        )
        self.assertIsInstance(
            CoreMediaIO.CMIOExtensionPropertyDeviceCanBeDefaultOutputDevice, str
        )
        self.assertIsInstance(
            CoreMediaIO.CMIOExtensionPropertyStreamActiveFormatIndex, str
        )
        self.assertIsInstance(CoreMediaIO.CMIOExtensionPropertyStreamFrameDuration, str)
        self.assertIsInstance(
            CoreMediaIO.CMIOExtensionPropertyStreamMaxFrameDuration, str
        )
        self.assertIsInstance(
            CoreMediaIO.CMIOExtensionPropertyStreamSinkBufferQueueSize, str
        )
        self.assertIsInstance(
            CoreMediaIO.CMIOExtensionPropertyStreamSinkBuffersRequiredForStartup, str
        )
        self.assertIsInstance(
            CoreMediaIO.CMIOExtensionPropertyStreamSinkBufferUnderrunCount, str
        )
        self.assertIsInstance(CoreMediaIO.CMIOExtensionPropertyStreamSinkEndOfData, str)

    @min_os_level("14.4")
    def test_constants14_4(self):
        self.assertIsInstance(CoreMediaIO.CMIOExtensionPropertyDeviceLatency, str)
        self.assertIsInstance(CoreMediaIO.CMIOExtensionPropertyStreamLatency, str)

    @min_os_level("12.3")
    def test_methods(self):
        self.assertArgIsBOOL(
            CoreMediaIO.CMIOExtensionPropertyAttributes.propertyAttributesWithMinValue_maxValue_validValues_readOnly_,
            3,
        )
        self.assertArgIsBOOL(
            CoreMediaIO.CMIOExtensionPropertyAttributes.initWithMinValue_maxValue_validValues_readOnly_,
            3,
        )
        self.assertResultIsBOOL(CoreMediaIO.CMIOExtensionPropertyAttributes.isReadOnly)
