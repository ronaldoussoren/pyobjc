import CoreMediaIO
from PyObjCTools.TestSupport import TestCase, fourcc


class TestCMIOHardwareSystem(TestCase):
    def testConstants(self):
        self.assertEqual(CoreMediaIO.kCMIOSystemObjectClassID, fourcc(b"asys"))
        self.assertEqual(CoreMediaIO.kCMIOObjectSystemObject, 1)

        self.assertEqual(
            CoreMediaIO.kCMIOHardwarePropertyProcessIsMaster, fourcc(b"mast")
        )
        self.assertEqual(
            CoreMediaIO.kCMIOHardwarePropertyIsInitingOrExiting, fourcc(b"inot")
        )
        self.assertEqual(CoreMediaIO.kCMIOHardwarePropertyDevices, fourcc(b"dev#"))
        self.assertEqual(
            CoreMediaIO.kCMIOHardwarePropertyDefaultInputDevice, fourcc(b"dIn ")
        )
        self.assertEqual(
            CoreMediaIO.kCMIOHardwarePropertyDefaultOutputDevice, fourcc(b"dOut")
        )
        self.assertEqual(CoreMediaIO.kCMIOHardwarePropertyDeviceForUID, fourcc(b"duid"))
        self.assertEqual(
            CoreMediaIO.kCMIOHardwarePropertySleepingIsAllowed, fourcc(b"slep")
        )
        self.assertEqual(
            CoreMediaIO.kCMIOHardwarePropertyUnloadingIsAllowed, fourcc(b"unld")
        )
        self.assertEqual(
            CoreMediaIO.kCMIOHardwarePropertyPlugInForBundleID, fourcc(b"pibi")
        )
        self.assertEqual(
            CoreMediaIO.kCMIOHardwarePropertyUserSessionIsActiveOrHeadless,
            fourcc(b"user"),
        )
        self.assertEqual(
            CoreMediaIO.kCMIOHardwarePropertySuspendedBySystem, fourcc(b"sbys")
        )
        self.assertEqual(
            CoreMediaIO.kCMIOHardwarePropertyAllowScreenCaptureDevices, fourcc(b"yes ")
        )
        self.assertEqual(
            CoreMediaIO.kCMIOHardwarePropertyAllowWirelessScreenCaptureDevices,
            fourcc(b"wscd"),
        )
