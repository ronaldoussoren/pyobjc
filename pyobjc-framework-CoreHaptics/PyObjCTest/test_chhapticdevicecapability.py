import CoreHaptics
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestCHHapticDeviceCapabilityHelper(CoreHaptics.NSObject):
    def minValue(self):
        return 1

    def maxValue(self):
        return 1

    def defaultValue(self):
        return 1

    def supportsHaptics(self):
        return 1

    def supportsAudio(self):
        return 1

    def attributesForEventParameter_eventType_error_(self, a, b, c):
        return 1

    def attributesForDynamicParameter_error_(self, a, b):
        return 1


class TestCHHapticDeviceCapability(TestCase):
    @min_sdk_level("10.15")
    def test_protocols(self):
        self.assertProtocolExists("CHHapticParameterAttributes")
        self.assertProtocolExists("CHHapticDeviceCapability")

    def test_methods(self):
        # CHHapticParameterAttributes
        self.assertResultHasType(
            TestCHHapticDeviceCapabilityHelper.minValue, objc._C_FLT
        )
        self.assertResultHasType(
            TestCHHapticDeviceCapabilityHelper.maxValue, objc._C_FLT
        )
        self.assertResultHasType(
            TestCHHapticDeviceCapabilityHelper.defaultValue, objc._C_FLT
        )

        # CHHapticDeviceCapability
        self.assertResultIsBOOL(TestCHHapticDeviceCapabilityHelper.supportsHaptics)
        self.assertResultIsBOOL(TestCHHapticDeviceCapabilityHelper.supportsAudio)

        self.assertArgHasType(
            TestCHHapticDeviceCapabilityHelper.attributesForEventParameter_eventType_error_,
            2,
            b"o^@",
        )
        self.assertArgHasType(
            TestCHHapticDeviceCapabilityHelper.attributesForDynamicParameter_error_,
            1,
            b"o^@",
        )
