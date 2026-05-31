import CoreAudio
from PyObjCTools.TestSupport import TestCase, max_os_level


class TestAudioHardwarePlugIn(TestCase):
    def testUnavailable(self):
        self.assertNotHasAttr(CoreAudio, "AudioHardwarePlugInInterface")

        self.assertNotHasAttr(CoreAudio, "kAudioHardwarePlugInTypeID")
        self.assertNotHasAttr(CoreAudio, "kAudioHardwarePlugInInterfaceID")
        self.assertNotHasAttr(CoreAudio, "kAudioHardwarePlugInInterface2ID")
        self.assertNotHasAttr(CoreAudio, "kAudioHardwarePlugInInterface3ID")
        self.assertNotHasAttr(CoreAudio, "kAudioHardwarePlugInInterface4ID")
        self.assertNotHasAttr(CoreAudio, "kAudioHardwarePlugInInterface5ID")

    def testCFTypes(self):
        self.assertIsOpaquePointer(CoreAudio.AudioHardwarePlugInRef)

    @max_os_level("10.15.9")  # API removed in macOS 11
    def testFunctions(self):
        self.assertArgIsOut(CoreAudio.AudioObjectCreate, 3)

        self.assertArgIsIn(CoreAudio.AudioObjectsPublishedAndDied, 3)
        self.assertArgSizeInArg(CoreAudio.AudioObjectsPublishedAndDied, 3, 2)
        self.assertArgIsIn(CoreAudio.AudioObjectsPublishedAndDied, 5)
        self.assertArgSizeInArg(CoreAudio.AudioObjectsPublishedAndDied, 5, 4)

        self.assertArgIsIn(CoreAudio.AudioObjectPropertiesChanged, 3)
        self.assertArgSizeInArg(CoreAudio.AudioObjectPropertiesChanged, 3, 2)

        self.assertArgIsOut(CoreAudio.AudioHardwareClaimAudioDeviceID, 1)

        self.assertArgIsIn(CoreAudio.AudioHardwareDevicesCreated, 2)
        self.assertArgSizeInArg(CoreAudio.AudioHardwareDevicesCreated, 2, 1)

        self.assertArgIsIn(CoreAudio.AudioHardwareDevicesDied, 2)
        self.assertArgSizeInArg(CoreAudio.AudioHardwareDevicesDied, 2, 1)

        self.assertArgIsBOOL(CoreAudio.AudioHardwareDevicePropertyChanged, 3)

        self.assertArgIsOut(CoreAudio.AudioHardwareClaimAudioStreamID, 2)

        self.assertArgIsIn(CoreAudio.AudioHardwareStreamsCreated, 3)
        self.assertArgSizeInArg(CoreAudio.AudioHardwareStreamsCreated, 3, 2)

        self.assertArgIsIn(CoreAudio.AudioHardwareStreamsDied, 3)
        self.assertArgSizeInArg(CoreAudio.AudioHardwareStreamsDied, 3, 2)

        CoreAudio.AudioHardwareStreamPropertyChanged
