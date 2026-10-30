import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVProVideoStorage(TestCase):
    def test_typed_enums(self):
        self.assertIsTypedEnum(AVFoundation.AVProVideoStorageBusyReason, str)

    @min_os_level("27.0")
    def test_constants(self):
        self.assertIsInstance(
            AVFoundation.AVProVideoStorageBusyReasonAdjustingCapacity, str
        )
        self.assertIsInstance(AVFoundation.AVProVideoStorageBusyReasonReplenishing, str)
        self.assertIsInstance(AVFoundation.AVProVideoStorageBusyReasonCapturing, str)

    @min_os_level("27.0")
    def test_methods(self):
        self.assertResultIsBOOL(AVFoundation.AVProVideoStorage.isSupported)
