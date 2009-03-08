
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGDisplayConfiguration (TestCase):

    def testTypes(self):
        self.failUnlessIsOpaquePointer(CGDisplayConfigRef)

        err, config = CGBeginDisplayConfiguration(None)
        self.failUnlessEqual(err, 0)
        self.failUnlessIsInstance(config, CGDisplayConfigRef)

        err = CGConfigureDisplayOrigin(config,
                CGMainDisplayID(), 0, 0)
        self.failUnlessEqual(err, 0)

        err = CGConfigureDisplayMode(config,
                CGMainDisplayID(), CGDisplayAvailableModes(CGMainDisplayID())[0])
        self.failUnlessEqual(err, 0)

        err = CGConfigureDisplayStereoOperation(config,
                CGMainDisplayID(), False, False)
        self.failUnlessEqual(err, 0)

        err = CGConfigureDisplayMirrorOfDisplay(config,
                CGMainDisplayID(), CGMainDisplayID())
        self.failUnlessIsInstance(err, (int, long))

        err = CGCancelDisplayConfiguration(config)
        self.failUnlessEqual(err, 0)
        config = None

        myInfo = object()
        info = []
        def reconfig(display, flags, userInfo):
            self.failUnlessIsInstance(display, (int, long))
            self.failUnlessIsInstance(flags, (int, long))
            self.failUnless(userInfo is myInfo)
            info.append((display, flags, userInfo))

        try:
            err, config = CGBeginDisplayConfiguration(None)
            self.failUnlessEqual(err, 0)
            self.failUnlessIsInstance(config, CGDisplayConfigRef)

            err = CGConfigureDisplayMode(config,
                    CGMainDisplayID(), CGDisplayAvailableModes(CGMainDisplayID())[0])

            err = CGDisplayRegisterReconfigurationCallback(reconfig, myInfo)
            self.failUnlessEqual(err, 0)

            CGCompleteDisplayConfiguration(config, kCGConfigureForAppOnly)

            self.failUnless(len(info) > 0)
      
        finally:
            err = CGDisplayRemoveReconfigurationCallback(reconfig, myInfo)
            self.failUnlessEqual(err, 0)
            l = len(info)

            CGRestorePermanentDisplayConfiguration()

            self.failUnlessEqual(len(info), l)

        err = CGDisplaySetStereoOperation(CGMainDisplayID(), False, False, kCGConfigureForAppOnly)
        self.failUnlessIsInstance(err, (int, long))

        v = CGDisplayIsActive(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))
        
        v = CGDisplayIsAsleep(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))

        v = CGDisplayIsOnline(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))

        v = CGDisplayIsMain(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))

        v = CGDisplayIsBuiltin(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))

        v = CGDisplayIsInMirrorSet(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))

        v = CGDisplayIsAlwaysInMirrorSet(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))

        v = CGDisplayIsInHWMirrorSet(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))

        v = CGDisplayMirrorsDisplay(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))

        v = CGDisplayIsStereo(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))

        v = CGDisplayPrimaryDisplay(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))

        v = CGDisplayUnitNumber(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))

        v = CGDisplayVendorNumber(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))

        v = CGDisplayModelNumber(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))

        v = CGDisplaySerialNumber(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))

        v = CGDisplayIOServicePort(CGMainDisplayID())
        self.failUnlessIsInstance(v, (int, long))

        v = CGDisplayScreenSize(CGMainDisplayID())
        self.failUnlessIsInstance(v, CGSize)

        v = CGDisplayRotation(CGMainDisplayID())
        self.failUnlessIsInstance(v, float)

        v = CGDisplayCopyColorSpace(CGMainDisplayID())
        self.failUnlessIsInstance(v, CGColorSpaceRef)


    def testContents(self):
        self.failUnlessEqual(kCGConfigureForAppOnly, 0)
        self.failUnlessEqual(kCGConfigureForSession, 1)
        self.failUnlessEqual(kCGConfigurePermanently, 2)

        self.failUnlessEqual(kCGDisplayBeginConfigurationFlag, (1 << 0))
        self.failUnlessEqual(kCGDisplayMovedFlag, (1 << 1))
        self.failUnlessEqual(kCGDisplaySetMainFlag, (1 << 2))
        self.failUnlessEqual(kCGDisplaySetModeFlag, (1 << 3))
        self.failUnlessEqual(kCGDisplayAddFlag, (1 << 4))
        self.failUnlessEqual(kCGDisplayRemoveFlag, (1 << 5))
        self.failUnlessEqual(kCGDisplayEnabledFlag, (1 << 8))
        self.failUnlessEqual(kCGDisplayDisabledFlag, (1 << 9))
        self.failUnlessEqual(kCGDisplayMirrorFlag, (1 << 10))
        self.failUnlessEqual(kCGDisplayUnMirrorFlag, (1 << 11))
        self.failUnlessEqual(kCGDisplayDesktopShapeChangedFlag, (1 << 12))

if __name__ == "__main__":
    main()
