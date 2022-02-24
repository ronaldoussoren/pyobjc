import CoreMediaIO
from PyObjCTools.TestSupport import TestCase, fourcc


class TestCMIOHardware(TestCase):
    def testConstants(self):
        self.assertEqual(CoreMediaIO.kCMIOHardwareNoError, 0)
        self.assertEqual(CoreMediaIO.kCMIOHardwareNotStoppedError, fourcc(b"run "))
        self.assertEqual(CoreMediaIO.kCMIOHardwareNotRunningError, fourcc(b"stop"))
        self.assertEqual(CoreMediaIO.kCMIOHardwareUnspecifiedError, fourcc(b"what"))
        self.assertEqual(CoreMediaIO.kCMIOHardwareUnknownPropertyError, fourcc(b"who?"))
        self.assertEqual(CoreMediaIO.kCMIOHardwareBadPropertySizeError, fourcc(b"!siz"))
        self.assertEqual(
            CoreMediaIO.kCMIOHardwareIllegalOperationError, fourcc(b"nope")
        )
        self.assertEqual(CoreMediaIO.kCMIOHardwareBadObjectError, fourcc(b"!obj"))
        self.assertEqual(CoreMediaIO.kCMIOHardwareBadDeviceError, fourcc(b"!dev"))
        self.assertEqual(CoreMediaIO.kCMIOHardwareBadStreamError, fourcc(b"!str"))
        self.assertEqual(
            CoreMediaIO.kCMIOHardwareUnsupportedOperationError, fourcc(b"unop")
        )
        self.assertEqual(
            CoreMediaIO.kCMIOHardwareSuspendedBySystemError, fourcc(b"deny")
        )
        self.assertEqual(CoreMediaIO.kCMIODeviceUnsupportedFormatError, fourcc(b"!dat"))
        self.assertEqual(CoreMediaIO.kCMIODevicePermissionsError, fourcc(b"!hog"))

        self.assertEqual(CoreMediaIO.kCMIOPlugInClassID, fourcc(b"aplg"))

        self.assertEqual(CoreMediaIO.kCMIOPlugInPropertyBundleID, fourcc(b"piid"))
        self.assertEqual(CoreMediaIO.kCMIOPlugInPropertyIsExtension, fourcc(b"piie"))
