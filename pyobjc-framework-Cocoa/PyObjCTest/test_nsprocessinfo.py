from __future__ import with_statement
from PyObjCTools.TestSupport import *

from Foundation import *



class TestNSProcessInfo (TestCase):
    def testConvenience(self):
        # This doesn't actually test anything...
        with NSDisabledSuddenTermination():
            pass

        with NSDisabledAutomaticTermination('something'):
            pass


    def testStructs(self):
        v = NSOperatingSystemVersion()
        self.assertIsInstance(v.majorVersion, (int, long))
        self.assertIsInstance(v.minorVersion, (int, long))
        self.assertIsInstance(v.patchVersion, (int, long))

    def testConstants(self):
        self.assertEqual(NSWindowsNTOperatingSystem, 1)
        self.assertEqual(NSWindows95OperatingSystem, 2)
        self.assertEqual(NSSolarisOperatingSystem, 3)
        self.assertEqual(NSHPUXOperatingSystem, 4)
        self.assertEqual(NSMACHOperatingSystem, 5)
        self.assertEqual(NSSunOSOperatingSystem, 6)
        self.assertEqual(NSOSF1OperatingSystem, 7)

    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertEqual(NSActivityIdleDisplaySleepDisabled, 1 << 40)
        self.assertEqual(NSActivityIdleSystemSleepDisabled, 1 << 20)
        self.assertEqual(NSActivitySuddenTerminationDisabled, 1 << 14)
        self.assertEqual(NSActivityAutomaticTerminationDisabled, 1 << 15)
        self.assertEqual(NSActivityUserInitiated,
                0x00FFFFFF | NSActivityIdleSystemSleepDisabled)
        self.assertEqual(NSActivityUserInitiatedAllowingIdleSystemSleep,
                NSActivityUserInitiated & ~NSActivityIdleSystemSleepDisabled)
        self.assertEqual(NSActivityBackground, 0x000000FF)
        self.assertEqual(NSActivityLatencyCritical, 0xFF00000000)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertEqual(NSProcessInfoThermalStateNominal, 0)
        self.assertEqual(NSProcessInfoThermalStateFair, 1)
        self.assertEqual(NSProcessInfoThermalStateSerious, 2)
        self.assertEqual(NSProcessInfoThermalStateCritical, 3)

        self.assertIsInstance(NSProcessInfoThermalStateDidChangeNotification, unicode)

    @min_os_level('10.6')
    def testNSDisabledSuddenTermination(self):
        # annoyingly we cannot easily test if this has an effect, but
        # this at least guards against typos.
        with NSDisabledSuddenTermination():
            pass

        class TestException (Exception):
            pass
        try:
            with NSDisabledSuddenTermination():
                raise TestException(1)

        except TestException:
            pass


    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertArgIsBOOL(NSProcessInfo.setAutomaticTerminationSupportEnabled_, 0)
        self.assertResultIsBOOL(NSProcessInfo.automaticTerminationSupportEnabled)

        with NSDisabledAutomaticTermination("reason"):
            pass

        class TestException (Exception):
            pass
        try:
            with NSDisabledAutomaticTermination("reason"):
                raise TestException(1)

        except TestException:
            pass

    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertArgIsBlock(NSProcessInfo.performActivityWithOptions_reason_usingBlock_, 2, b'v')

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(NSProcessInfo.isOperatingSystemAtLeastVersion_)

if __name__ == "__main__":
    main()
