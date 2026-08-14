from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCGDisplayConfiguration(TestCase):
    def test_constants(self):
        self.assertEqual(Quartz.kCGConfigureForAppOnly, 0)
        self.assertEqual(Quartz.kCGConfigureForSession, 1)
        self.assertEqual(Quartz.kCGConfigurePermanently, 2)

        self.assertEqual(Quartz.kCGDisplayBeginConfigurationFlag, (1 << 0))
        self.assertEqual(Quartz.kCGDisplayMovedFlag, (1 << 1))
        self.assertEqual(Quartz.kCGDisplaySetMainFlag, (1 << 2))
        self.assertEqual(Quartz.kCGDisplaySetModeFlag, (1 << 3))
        self.assertEqual(Quartz.kCGDisplayAddFlag, (1 << 4))
        self.assertEqual(Quartz.kCGDisplayRemoveFlag, (1 << 5))
        self.assertEqual(Quartz.kCGDisplayEnabledFlag, (1 << 8))
        self.assertEqual(Quartz.kCGDisplayDisabledFlag, (1 << 9))
        self.assertEqual(Quartz.kCGDisplayMirrorFlag, (1 << 10))
        self.assertEqual(Quartz.kCGDisplayUnMirrorFlag, (1 << 11))
        self.assertEqual(Quartz.kCGDisplayDesktopShapeChangedFlag, (1 << 12))

    def test_functions(self):
        self.assertResultHasType(Quartz.CGConfigureDisplayWithDisplayMode, b"i")
        self.assertArgHasType(
            Quartz.CGConfigureDisplayWithDisplayMode, 0, b"^{_CGDisplayConfigRef=}"
        )
        self.assertArgHasType(Quartz.CGConfigureDisplayWithDisplayMode, 1, b"I")
        self.assertArgHasType(
            Quartz.CGConfigureDisplayWithDisplayMode, 2, b"^{CGDisplayMode=}"
        )
        self.assertArgHasType(
            Quartz.CGConfigureDisplayWithDisplayMode, 3, b"^{__CFDictionary=}"
        )


class TestCGDisplayConfigurationUsage(TestCase):
    def test_usage(self):
        self.assertIsOpaquePointer(Quartz.CGDisplayConfigRef)

        err, config = Quartz.CGBeginDisplayConfiguration(None)
        self.assertEqual(err, 0)
        self.assertIsInstance(config, Quartz.CGDisplayConfigRef)

        err = Quartz.CGConfigureDisplayOrigin(config, Quartz.CGMainDisplayID(), 0, 0)
        self.assertEqual(err, 0)

        err = Quartz.CGConfigureDisplayMode(
            config,
            Quartz.CGMainDisplayID(),
            Quartz.CGDisplayAvailableModes(Quartz.CGMainDisplayID())[0],
        )
        self.assertEqual(err, 0)

        err = Quartz.CGConfigureDisplayStereoOperation(
            config, Quartz.CGMainDisplayID(), False, False
        )
        self.assertEqual(err, 0)

        err = Quartz.CGConfigureDisplayMirrorOfDisplay(
            config, Quartz.CGMainDisplayID(), Quartz.CGMainDisplayID()
        )
        self.assertIsInstance(err, int)

        err = Quartz.CGCancelDisplayConfiguration(config)
        self.assertEqual(err, 0)
        config = None

        myInfo = object()
        info = []

        def reconfig(display, flags, userInfo):
            self.assertIsInstance(display, int)
            self.assertIsInstance(flags, int)
            self.assertTrue(userInfo is myInfo)
            info.append((display, flags, userInfo))

        def reconfig_raises(display, flags, userInfo):
            print("reconfig_raises called")
            raise RuntimeError("reconfig raises")

        with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 0"):
            Quartz.CGDisplayRegisterReconfigurationCallback()

        with self.assertRaisesRegex(TypeError, "callback not callable"):
            Quartz.CGDisplayRegisterReconfigurationCallback(42, myInfo)

        for callback in (reconfig_raises, reconfig):
            with self.subTest(callback=callback):
                info[:] = []

                try:
                    err, config = Quartz.CGBeginDisplayConfiguration(None)
                    self.assertEqual(err, 0)
                    self.assertIsInstance(config, Quartz.CGDisplayConfigRef)

                    err = Quartz.CGDisplayRegisterReconfigurationCallback(
                        callback, myInfo
                    )
                    self.assertEqual(err, 0)

                    err = Quartz.CGConfigureDisplayMode(
                        config,
                        Quartz.CGMainDisplayID(),
                        Quartz.CGDisplayAvailableModes(Quartz.CGMainDisplayID())[0],
                    )

                    if callback == reconfig_raises:
                        with self.assertRaisesRegex(RuntimeError, "reconfig raises"):
                            Quartz.CGCompleteDisplayConfiguration(
                                config, Quartz.kCGConfigureForAppOnly
                            )
                    else:
                        Quartz.CGCompleteDisplayConfiguration(
                            config, Quartz.kCGConfigureForAppOnly
                        )

                finally:
                    err = Quartz.CGDisplayRemoveReconfigurationCallback(
                        callback, myInfo
                    )
                    try:
                        with self.assertRaisesRegex(
                            TypeError, "expected 2 arguments, got 0"
                        ):
                            Quartz.CGDisplayRemoveReconfigurationCallback()
                        with self.assertRaisesRegex(
                            ValueError, "Cannot find callback info"
                        ):
                            Quartz.CGDisplayRemoveReconfigurationCallback(42, myInfo)

                        self.assertEqual(err, 0)
                        if callback == reconfig:
                            self.assertGreater(len(info), 0)
                            for item in info:
                                self.assertIsInstance(item[0], int)
                                self.assertIsInstance(item[1], int)
                                self.assertIs(item[2], myInfo)

                        else:
                            self.assertEqual(info, [])
                    finally:
                        # Quartz.CGCancelDisplayConfiguration(config)
                        Quartz.CGRestorePermanentDisplayConfiguration()

        err = Quartz.CGDisplaySetStereoOperation(
            Quartz.CGMainDisplayID(), False, False, Quartz.kCGConfigureForAppOnly
        )
        self.assertIsInstance(err, int)

        v = Quartz.CGDisplayIsActive(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        v = Quartz.CGDisplayIsAsleep(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        v = Quartz.CGDisplayIsOnline(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        v = Quartz.CGDisplayIsMain(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        v = Quartz.CGDisplayIsBuiltin(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        v = Quartz.CGDisplayIsInMirrorSet(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        v = Quartz.CGDisplayIsAlwaysInMirrorSet(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        v = Quartz.CGDisplayIsInHWMirrorSet(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        v = Quartz.CGDisplayUsesOpenGLAcceleration(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        v = Quartz.CGDisplayMirrorsDisplay(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        v = Quartz.CGDisplayIsStereo(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        v = Quartz.CGDisplayPrimaryDisplay(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        v = Quartz.CGDisplayUnitNumber(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        v = Quartz.CGDisplayVendorNumber(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        v = Quartz.CGDisplayModelNumber(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        v = Quartz.CGDisplaySerialNumber(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        v = Quartz.CGDisplayIOServicePort(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, int)

        v = Quartz.CGDisplayScreenSize(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, Quartz.CGSize)

        v = Quartz.CGDisplayRotation(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, float)

        v = Quartz.CGDisplayCopyColorSpace(Quartz.CGMainDisplayID())
        self.assertIsInstance(v, Quartz.CGColorSpaceRef)
