import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSProcessInfo(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSActivityOptions)
        self.assertIsEnumType(Foundation.NSProcessInfoThermalState)

    def testConvenience(self):
        # This doesn't actually test anything...
        with Foundation.NSDisabledSuddenTermination():
            pass

        with Foundation.NSDisabledAutomaticTermination("something"):
            pass

    def testStructs(self):
        v = Foundation.NSOperatingSystemVersion()
        self.assertIsInstance(v.majorVersion, int)
        self.assertIsInstance(v.minorVersion, int)
        self.assertIsInstance(v.patchVersion, int)
        self.assertPickleRoundTrips(v)

    def testConstants(self):
        self.assertEqual(Foundation.NSWindowsNTOperatingSystem, 1)
        self.assertEqual(Foundation.NSWindows95OperatingSystem, 2)
        self.assertEqual(Foundation.NSSolarisOperatingSystem, 3)
        self.assertEqual(Foundation.NSHPUXOperatingSystem, 4)
        self.assertEqual(Foundation.NSMACHOperatingSystem, 5)
        self.assertEqual(Foundation.NSSunOSOperatingSystem, 6)
        self.assertEqual(Foundation.NSOSF1OperatingSystem, 7)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertEqual(Foundation.NSActivityIdleDisplaySleepDisabled, 1 << 40)
        self.assertEqual(Foundation.NSActivityIdleSystemSleepDisabled, 1 << 20)
        self.assertEqual(Foundation.NSActivitySuddenTerminationDisabled, 1 << 14)
        self.assertEqual(Foundation.NSActivityAutomaticTerminationDisabled, 1 << 15)
        self.assertEqual(Foundation.NSActivityAnimationTrackingEnabled, 1 << 45)
        self.assertEqual(Foundation.NSActivityTrackingEnabled, 1 << 46)
        self.assertEqual(
            Foundation.NSActivityUserInitiated,
            0x00FFFFFF | Foundation.NSActivityIdleSystemSleepDisabled,
        )
        self.assertEqual(
            Foundation.NSActivityUserInitiatedAllowingIdleSystemSleep,
            Foundation.NSActivityUserInitiated
            & ~Foundation.NSActivityIdleSystemSleepDisabled,
        )
        self.assertEqual(Foundation.NSActivityBackground, 0x000000FF)
        self.assertEqual(Foundation.NSActivityLatencyCritical, 0xFF00000000)
        self.assertEqual(
            Foundation.NSActivityUserInteractive,
            Foundation.NSActivityUserInitiated | Foundation.NSActivityLatencyCritical,
        )

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertEqual(Foundation.NSProcessInfoThermalStateNominal, 0)
        self.assertEqual(Foundation.NSProcessInfoThermalStateFair, 1)
        self.assertEqual(Foundation.NSProcessInfoThermalStateSerious, 2)
        self.assertEqual(Foundation.NSProcessInfoThermalStateCritical, 3)

        self.assertIsInstance(
            Foundation.NSProcessInfoThermalStateDidChangeNotification, str
        )

    @min_os_level("12.0")
    def testConstants12_0(self):
        self.assertIsInstance(
            Foundation.NSProcessInfoPowerStateDidChangeNotification, str
        )

    @min_os_level("10.6")
    def testNSDisabledSuddenTermination(self):
        # annoyingly we cannot easily test if this has an effect, but
        # this at least guards against typos.
        with Foundation.NSDisabledSuddenTermination():
            pass

        class TestException(Exception):
            pass

        try:
            with Foundation.NSDisabledSuddenTermination():
                raise TestException(1)

        except TestException:
            pass

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgIsBOOL(
            Foundation.NSProcessInfo.setAutomaticTerminationSupportEnabled_, 0
        )
        self.assertResultIsBOOL(
            Foundation.NSProcessInfo.automaticTerminationSupportEnabled
        )

        with Foundation.NSDisabledAutomaticTermination("reason"):
            pass

        class TestException(Exception):
            pass

        try:
            with Foundation.NSDisabledAutomaticTermination("reason"):
                raise TestException(1)

        except TestException:
            pass

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertArgIsBlock(
            Foundation.NSProcessInfo.performActivityWithOptions_reason_usingBlock_,
            2,
            b"v",
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(
            Foundation.NSProcessInfo.isOperatingSystemAtLeastVersion_
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(Foundation.NSProcessInfo.isMacCatalystApp)

    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertResultIsBOOL(Foundation.NSProcessInfo.isiOSAppOnMac)

    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertResultIsBOOL(Foundation.NSProcessInfo.isLowPowerModeEnabled)
