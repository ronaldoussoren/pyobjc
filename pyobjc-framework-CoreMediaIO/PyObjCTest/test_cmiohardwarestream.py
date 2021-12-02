import CoreMediaIO
from PyObjCTools.TestSupport import TestCase, fourcc

MIODeviceStreamQueueAlteredProc = b"vI^v^v"

CMIOStreamScheduledOutputNotificationProc = b"vQQ^v"


class TestCMIOHardwareStream(TestCase):
    def testConstants(self):
        self.assertEqual(CoreMediaIO.kCMIOStreamClassID, fourcc(b"astr"))
        self.assertEqual(CoreMediaIO.kCMIOStreamUnknown, CoreMediaIO.kCMIOObjectUnknown)

        self.assertEqual(CoreMediaIO.kCMIODeckStatusBusy, 1)
        self.assertEqual(CoreMediaIO.kCMIODeckStatusLocal, 2)
        self.assertEqual(CoreMediaIO.kCMIODeckStatusNotThreaded, 3)
        self.assertEqual(CoreMediaIO.kCMIODeckStatusTapeInserted, 4)
        self.assertEqual(CoreMediaIO.kCMIODeckStatusOpcode, 5)
        self.assertEqual(CoreMediaIO.kCMIODeckStatusSearchingForDevice, 6)
        self.assertEqual(CoreMediaIO.kCMIODeckStatusNoDevice, 7)

        self.assertEqual(CoreMediaIO.kCMIODeckStateStop, 0)
        self.assertEqual(CoreMediaIO.kCMIODeckStatePlay, 1)
        self.assertEqual(CoreMediaIO.kCMIODeckStatePause, 2)
        self.assertEqual(CoreMediaIO.kCMIODeckStatePlaySlow, 3)
        self.assertEqual(CoreMediaIO.kCMIODeckStateReverseSlow, 4)
        self.assertEqual(CoreMediaIO.kCMIODeckStatePlayReverse, 5)
        self.assertEqual(CoreMediaIO.kCMIODeckStateFastForward, 6)
        self.assertEqual(CoreMediaIO.kCMIODeckStateFastRewind, 7)

        self.assertEqual(CoreMediaIO.kCMIODeckShuttleReverseHighSpeed, -10)
        self.assertEqual(CoreMediaIO.kCMIODeckShuttleReverseFastest, -9)
        self.assertEqual(CoreMediaIO.kCMIODeckShuttleReverseFaster, -8)
        self.assertEqual(CoreMediaIO.kCMIODeckShuttleReverseFast, -7)
        self.assertEqual(CoreMediaIO.kCMIODeckShuttleReverse1x, -6)
        self.assertEqual(CoreMediaIO.kCMIODeckShuttleReverseSlow3, -5)
        self.assertEqual(CoreMediaIO.kCMIODeckShuttleReverseSlow2, -4)
        self.assertEqual(CoreMediaIO.kCMIODeckShuttleReverseSlow1, -3)
        self.assertEqual(CoreMediaIO.kCMIODeckShuttleReverseSlowest, -2)
        self.assertEqual(CoreMediaIO.kCMIODeckShuttlePlayPreviousFrame, -1)
        self.assertEqual(CoreMediaIO.kCMIODeckShuttlePause, 0)
        self.assertEqual(CoreMediaIO.kCMIODeckShuttlePlayNextFrame, 1)
        self.assertEqual(CoreMediaIO.kCMIODeckShuttlePlaySlowest, 2)
        self.assertEqual(CoreMediaIO.kCMIODeckShuttlePlaySlow1, 3)
        self.assertEqual(CoreMediaIO.kCMIODeckShuttlePlaySlow2, 4)
        self.assertEqual(CoreMediaIO.kCMIODeckShuttlePlaySlow3, 5)
        self.assertEqual(CoreMediaIO.kCMIODeckShuttlePlay1x, 6)
        self.assertEqual(CoreMediaIO.kCMIODeckShuttlePlayFast, 7)
        self.assertEqual(CoreMediaIO.kCMIODeckShuttlePlayFaster, 8)
        self.assertEqual(CoreMediaIO.kCMIODeckShuttlePlayFastest, 9)
        self.assertEqual(CoreMediaIO.kCMIODeckShuttlePlayHighSpeed, 10)

        self.assertEqual(CoreMediaIO.kCMIOStreamPropertyDirection, fourcc(b"sdir"))
        self.assertEqual(CoreMediaIO.kCMIOStreamPropertyTerminalType, fourcc(b"term"))
        self.assertEqual(
            CoreMediaIO.kCMIOStreamPropertyStartingChannel, fourcc(b"schn")
        )
        self.assertEqual(CoreMediaIO.kCMIOStreamPropertyLatency, fourcc(b"ltnc"))
        self.assertEqual(
            CoreMediaIO.kCMIOStreamPropertyFormatDescription, fourcc(b"pft ")
        )
        self.assertEqual(
            CoreMediaIO.kCMIOStreamPropertyFormatDescriptions, fourcc(b"pfta")
        )
        self.assertEqual(CoreMediaIO.kCMIOStreamPropertyStillImage, fourcc(b"stmg"))
        self.assertEqual(
            CoreMediaIO.kCMIOStreamPropertyStillImageFormatDescriptions, fourcc(b"stft")
        )
        self.assertEqual(CoreMediaIO.kCMIOStreamPropertyFrameRate, fourcc(b"nfrt"))
        self.assertEqual(
            CoreMediaIO.kCMIOStreamPropertyMinimumFrameRate, fourcc(b"mfrt")
        )
        self.assertEqual(CoreMediaIO.kCMIOStreamPropertyFrameRates, fourcc(b"nfr#"))
        self.assertEqual(
            CoreMediaIO.kCMIOStreamPropertyFrameRateRanges, fourcc(b"frrg")
        )
        self.assertEqual(
            CoreMediaIO.kCMIOStreamPropertyNoDataTimeoutInMSec, fourcc(b"pmn1")
        )
        self.assertEqual(
            CoreMediaIO.kCMIOStreamPropertyDeviceSyncTimeoutInMSec, fourcc(b"pmn2")
        )
        self.assertEqual(
            CoreMediaIO.kCMIOStreamPropertyNoDataEventCount, fourcc(b"pmn3")
        )
        self.assertEqual(
            CoreMediaIO.kCMIOStreamPropertyOutputBufferUnderrunCount, fourcc(b"pmou")
        )
        self.assertEqual(
            CoreMediaIO.kCMIOStreamPropertyOutputBufferRepeatCount, fourcc(b"pmor")
        )
        self.assertEqual(
            CoreMediaIO.kCMIOStreamPropertyOutputBufferQueueSize, fourcc(b"pmoq")
        )
        self.assertEqual(
            CoreMediaIO.kCMIOStreamPropertyOutputBuffersRequiredForStartup,
            fourcc(b"pmos"),
        )
        self.assertEqual(
            CoreMediaIO.kCMIOStreamPropertyOutputBuffersNeededForThrottledPlayback,
            fourcc(b"miff"),
        )
        self.assertEqual(
            CoreMediaIO.kCMIOStreamPropertyFirstOutputPresentationTimeStamp,
            fourcc(b"popt"),
        )
        self.assertEqual(CoreMediaIO.kCMIOStreamPropertyEndOfData, fourcc(b"pmed"))
        self.assertEqual(CoreMediaIO.kCMIOStreamPropertyClock, fourcc(b"pmcl"))
        self.assertEqual(
            CoreMediaIO.kCMIOStreamPropertyCanProcessDeckCommand, fourcc(b"pdcd")
        )
        self.assertEqual(CoreMediaIO.kCMIOStreamPropertyDeck, fourcc(b"deck"))
        self.assertEqual(
            CoreMediaIO.kCMIOStreamPropertyDeckFrameNumber, fourcc(b"tcod")
        )
        self.assertEqual(CoreMediaIO.kCMIOStreamPropertyDeckDropness, fourcc(b"drop"))
        self.assertEqual(CoreMediaIO.kCMIOStreamPropertyDeckThreaded, fourcc(b"thrd"))
        self.assertEqual(CoreMediaIO.kCMIOStreamPropertyDeckLocal, fourcc(b"locl"))
        self.assertEqual(CoreMediaIO.kCMIOStreamPropertyDeckCueing, fourcc(b"cuec"))
        self.assertEqual(
            CoreMediaIO.kCMIOStreamPropertyInitialPresentationTimeStampForLinkedAndSyncedAudio,
            fourcc(b"ipls"),
        )
        self.assertEqual(
            CoreMediaIO.kCMIOStreamPropertyScheduledOutputNotificationProc,
            fourcc(b"sonp"),
        )
        self.assertEqual(
            CoreMediaIO.kCMIOStreamPropertyPreferredFormatDescription, fourcc(b"prfd")
        )
        self.assertEqual(
            CoreMediaIO.kCMIOStreamPropertyPreferredFrameRate, fourcc(b"prfr")
        )

    def testStructs(self):
        v = CoreMediaIO.CMIOStreamDeck()
        self.assertEqual(v.mStatus, 0)
        self.assertEqual(v.mState, 0)
        self.assertEqual(v.mState2, 0)
        self.assertPickleRoundTrips(v)

        v = CoreMediaIO.CMIOStreamScheduledOutputNotificationProcAndRefCon()
        self.assertEqual(v.scheduledOutputNotificationProc, None)
        self.assertEqual(v.scheduledOutputNotificationRefCon, None)
        self.assertPickleRoundTrips(v)

    def testFunctions(self):
        self.assertArgIsOut(CoreMediaIO.CMIOStreamCopyBufferQueue, 3)

        CoreMediaIO.CMIOStreamDeckPlay
        CoreMediaIO.CMIOStreamDeckStop
        CoreMediaIO.CMIOStreamDeckJog

        self.assertArgIsBOOL(CoreMediaIO.CMIOStreamDeckCueTo, 2)

        self.assertArgIsOut(CoreMediaIO.CMIOStreamClockCreate, 6)
        self.assertArgIsCFRetained(CoreMediaIO.CMIOStreamClockCreate, 6)

        CoreMediaIO.CMIOStreamClockPostTimingEvent
        CoreMediaIO.CMIOStreamClockInvalidate
        CoreMediaIO.CMIOStreamClockConvertHostTimeToDeviceTime
