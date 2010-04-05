
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGDisplayConfiguration (TestCase):

    def testTypes(self):
        self.assertIsOpaquePointer(CGDisplayConfigRef)

        err, config = CGBeginDisplayConfiguration(None)
        self.assertEqual(err, 0)
        self.assertIsInstance(config, CGDisplayConfigRef)

        err = CGConfigureDisplayOrigin(config,
                CGMainDisplayID(), 0, 0)
        self.assertEqual(err, 0)

        err = CGConfigureDisplayMode(config,
                CGMainDisplayID(), CGDisplayAvailableModes(CGMainDisplayID())[0])
        self.assertEqual(err, 0)

        err = CGConfigureDisplayStereoOperation(config,
                CGMainDisplayID(), False, False)
        self.assertEqual(err, 0)

        err = CGConfigureDisplayMirrorOfDisplay(config,
                CGMainDisplayID(), CGMainDisplayID())
        self.assertIsInstance(err, (int, long))

        err = CGCancelDisplayConfiguration(config)
        self.assertEqual(err, 0)
        config = None

        myInfo = object()
        info = []
        def reconfig(display, flags, userInfo):
            self.assertIsInstance(display, (int, long))
            self.assertIsInstance(flags, (int, long))
            self.assertTrue(userInfo is myInfo)
            info.append((display, flags, userInfo))

        try:
            err, config = CGBeginDisplayConfiguration(None)
            self.assertEqual(err, 0)
            self.assertIsInstance(config, CGDisplayConfigRef)

            err = CGConfigureDisplayMode(config,
                    CGMainDisplayID(), CGDisplayAvailableModes(CGMainDisplayID())[0])

            err = CGDisplayRegisterReconfigurationCallback(reconfig, myInfo)
            self.assertEqual(err, 0)

            CGCompleteDisplayConfiguration(config, kCGConfigureForAppOnly)

            self.assertTrue(len(info) > 0)
      
        finally:
            err = CGDisplayRemoveReconfigurationCallback(reconfig, myInfo)
            self.assertEqual(err, 0)
            l = len(info)

            CGRestorePermanentDisplayConfiguration()

            self.assertEqual(len(info), l)

        err = CGDisplaySetStereoOperation(CGMainDisplayID(), False, False, kCGConfigureForAppOnly)
        self.assertIsInstance(err, (int, long))

        v = CGDisplayIsActive(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))
        
        v = CGDisplayIsAsleep(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))

        v = CGDisplayIsOnline(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))

        v = CGDisplayIsMain(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))

        v = CGDisplayIsBuiltin(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))

        v = CGDisplayIsInMirrorSet(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))

        v = CGDisplayIsAlwaysInMirrorSet(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))

        v = CGDisplayIsInHWMirrorSet(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))

        v = CGDisplayMirrorsDisplay(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))

        v = CGDisplayIsStereo(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))

        v = CGDisplayPrimaryDisplay(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))

        v = CGDisplayUnitNumber(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))

        v = CGDisplayVendorNumber(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))

        v = CGDisplayModelNumber(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))

        v = CGDisplaySerialNumber(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))

        v = CGDisplayIOServicePort(CGMainDisplayID())
        self.assertIsInstance(v, (int, long))

        v = CGDisplayScreenSize(CGMainDisplayID())
        self.assertIsInstance(v, CGSize)

        v = CGDisplayRotation(CGMainDisplayID())
        self.assertIsInstance(v, float)

        v = CGDisplayCopyColorSpace(CGMainDisplayID())
        self.assertIsInstance(v, CGColorSpaceRef)


    def testContents(self):
        self.assertEqual(kCGConfigureForAppOnly, 0)
        self.assertEqual(kCGConfigureForSession, 1)
        self.assertEqual(kCGConfigurePermanently, 2)

        self.assertEqual(kCGDisplayBeginConfigurationFlag, (1 << 0))
        self.assertEqual(kCGDisplayMovedFlag, (1 << 1))
        self.assertEqual(kCGDisplaySetMainFlag, (1 << 2))
        self.assertEqual(kCGDisplaySetModeFlag, (1 << 3))
        self.assertEqual(kCGDisplayAddFlag, (1 << 4))
        self.assertEqual(kCGDisplayRemoveFlag, (1 << 5))
        self.assertEqual(kCGDisplayEnabledFlag, (1 << 8))
        self.assertEqual(kCGDisplayDisabledFlag, (1 << 9))
        self.assertEqual(kCGDisplayMirrorFlag, (1 << 10))
        self.assertEqual(kCGDisplayUnMirrorFlag, (1 << 11))
        self.assertEqual(kCGDisplayDesktopShapeChangedFlag, (1 << 12))

    @min_os_level('10.6')
    def testFunctions10_6(self):
        self.assertResultHasType(CGConfigureDisplayWithDisplayMode, b'i')
        self.assertArgHasType(CGConfigureDisplayWithDisplayMode, 0,
                    b'^{_CGDisplayConfigRef=}')
        self.assertArgHasType(CGConfigureDisplayWithDisplayMode, 1,
                        b'I')
        self.assertArgHasType(CGConfigureDisplayWithDisplayMode, 2,
                            b'^{CGDisplayMode}')
        self.assertArgHasType(CGConfigureDisplayWithDisplayMode, 3,
                                b'^{__CFDictionary=}')


if __name__ == "__main__":
    main()
