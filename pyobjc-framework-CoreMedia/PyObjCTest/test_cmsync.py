from PyObjCTools.TestSupport import *

import CoreMedia

class TestCMSync (TestCase):
    def test_types(self):
        self.assertIsCFType(CoreMedia.CMClockRef)
        self.assertIsCFType(CoreMedia.CMTimebaseRef)

    def test_constants(self):
        self.assertEqual(CoreMedia.kCMClockError_MissingRequiredParameter, -12745)
        self.assertEqual(CoreMedia.kCMClockError_InvalidParameter, -12746)
        self.assertEqual(CoreMedia.kCMClockError_AllocationFailed, -12747)
        self.assertEqual(CoreMedia.kCMClockError_UnsupportedOperation, -12756)

        self.assertEqual(CoreMedia.kCMTimebaseError_MissingRequiredParameter, -12748)
        self.assertEqual(CoreMedia.kCMTimebaseError_InvalidParameter, -12749)
        self.assertEqual(CoreMedia.kCMTimebaseError_AllocationFailed, -12750)
        self.assertEqual(CoreMedia.kCMTimebaseError_TimerIntervalTooShort, -12751)
        self.assertEqual(CoreMedia.kCMTimebaseError_ReadOnly, -12757)

        self.assertEqual(CoreMedia.kCMSyncError_MissingRequiredParameter, -12752)
        self.assertEqual(CoreMedia.kCMSyncError_InvalidParameter, -12753)
        self.assertEqual(CoreMedia.kCMSyncError_AllocationFailed, -12754)
        self.assertEqual(CoreMedia.kCMSyncError_RateMustBeNonZero, -12755)

        self.assertEqual(CoreMedia.kCMTimebaseVeryLongCFTimeInterval, 256.0 * 365.0 * 24.0 * 60.0 * 60.0)
        self.assertEqual(CoreMedia.kCMTimebaseFarFutureCFAbsoluteTime, CoreMedia.kCMTimebaseVeryLongCFTimeInterval)

    @min_os_level('10.8')
    def test_constants10_8(self):
        self.assertIsInstance(CoreMedia.kCMTimebaseNotification_EffectiveRateChanged, unicode)
        self.assertIsInstance(CoreMedia.kCMTimebaseNotification_TimeJumped, unicode)

    @min_os_level('10.9')
    def test_constants10_9(self):
        self.assertIsInstance(CoreMedia.kCMTimebaseNotificationKey_EventTime, unicode)

    @min_os_level('10.8')
    def test_functions(self):
        CoreMedia.CMClockGetTypeID
        CoreMedia.CMClockGetHostTimeClock
        CoreMedia.CMClockConvertHostTimeToSystemUnits
        CoreMedia.CMClockMakeHostTimeFromSystemUnits
        CoreMedia.CMClockGetTime

        self.assertArgIsOut(CoreMedia.CMClockGetAnchorTime, 1)
        self.assertArgIsOut(CoreMedia.CMClockGetAnchorTime, 2)

        CoreMedia.CMClockMightDrift
        CoreMedia.CMClockInvalidate
        CoreMedia.CMTimebaseGetTypeID

        self.assertArgIsOut(CoreMedia.CMTimebaseCreateWithMasterClock, 2)
        self.assertArgIsCFRetained(CoreMedia.CMTimebaseCreateWithMasterClock, 2)

        self.assertArgIsOut(CoreMedia.CMTimebaseCreateWithMasterTimebase, 2)
        self.assertArgIsCFRetained(CoreMedia.CMTimebaseCreateWithMasterTimebase, 2)


        CoreMedia.CMTimebaseGetMasterTimebase
        CoreMedia.CMTimebaseGetMasterClock
        CoreMedia.CMTimebaseGetMaster
        CoreMedia.CMTimebaseGetUltimateMasterClock
        CoreMedia.CMTimebaseGetTime
        CoreMedia.CMTimebaseGetTimeWithTimeScale
        CoreMedia.CMTimebaseSetTime
        CoreMedia.CMTimebaseSetAnchorTime
        CoreMedia.CMTimebaseGetRate
        CoreMedia.CMTimebaseGetTimeAndRate
        CoreMedia.CMTimebaseSetRate
        CoreMedia.CMTimebaseSetRateAndAnchorTime
        CoreMedia.CMTimebaseGetEffectiveRate
        CoreMedia.CMTimebaseAddTimer
        CoreMedia.CMTimebaseRemoveTimer
        CoreMedia.CMTimebaseSetTimerNextFireTime
        CoreMedia.CMTimebaseSetTimerToFireImmediately
        CoreMedia.CMTimebaseAddTimerDispatchSource
        CoreMedia.CMTimebaseRemoveTimerDispatchSource
        CoreMedia.CMTimebaseSetTimerDispatchSourceNextFireTime
        CoreMedia.CMTimebaseSetTimerDispatchSourceToFireImmediately
        CoreMedia.CMSyncGetRelativeRate

        self.assertArgIsOut(CoreMedia.CMSyncGetRelativeRateAndAnchorTime, 2)
        self.assertArgIsOut(CoreMedia.CMSyncGetRelativeRateAndAnchorTime, 3)
        self.assertArgIsOut(CoreMedia.CMSyncGetRelativeRateAndAnchorTime, 4)

        CoreMedia.CMSyncConvertTime
        CoreMedia.CMSyncMightDrift
        CoreMedia.CMSyncGetTime
        CoreMedia.CMTimebaseNotificationBarrier

    @min_os_level('10.11')
    def test_functions10_11(self):
        self.assertResultIsCFRetained(CoreMedia.CMTimebaseCopyMasterTimebase)
        self.assertResultIsCFRetained(CoreMedia.CMTimebaseCopyMasterClock)
        self.assertResultIsCFRetained(CoreMedia.CMTimebaseCopyMaster)
        self.assertResultIsCFRetained(CoreMedia.CMTimebaseCopyUltimateMasterClock)

if __name__ == "__main__":
    main()
