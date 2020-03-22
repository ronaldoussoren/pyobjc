import CoreHaptics
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc

CHHapticAdvancedPatternPlayerCompletionHandler = b"v@"


class TestCHHapticPatternPlayerHelper(CoreHaptics.NSObject):
    def startAtTime_error_(self, a, b):
        return 1

    def stopAtTime_error_(self, a, b):
        return 1

    def sendParameters_atTime_error_(self, a, b, c):
        return 1

    def scheduleParameterCurve_atTime_error_(self, a, b, c):
        return 1

    def cancelAndReturnError_(self, a):
        return 1

    def isMuted(self):
        return 1

    def setIsMuted_(self, a):
        return 1

    def pauseAtTime_error_(self, a, b):
        return 1

    def resumeAtTime_error_(self, a, b):
        return 1

    def seekToOffset_error_(self, a, b):
        return 1

    def loopEnabled(self):
        return 1

    def setLoopEnabled_(self, a):
        pass

    def loopEnd(self):
        return 1

    def setLoopEnd_(self, a):
        pass

    def playbackRate(self):
        return 1

    def setPlaybackRate_(self, a):
        pass

    # def isMuted(self): return 1
    # def setIsMuted_(self, a): pass
    def completionHandler(self):
        return 1

    def setCompletionHandler_(self, a):
        pass


class TestCHHapticPatternPlayer(TestCase):
    @min_sdk_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("CHHapticPatternPlayer")
        objc.protocolNamed("CHHapticAdvancedPatternPlayer")

    def test_methods(self):
        # CHHapticPatternPlayer
        self.assertResultIsBOOL(TestCHHapticPatternPlayerHelper.startAtTime_error_)
        self.assertArgIsOut(TestCHHapticPatternPlayerHelper.startAtTime_error_, 1)

        self.assertResultIsBOOL(TestCHHapticPatternPlayerHelper.stopAtTime_error_)
        self.assertArgIsOut(TestCHHapticPatternPlayerHelper.stopAtTime_error_, 1)

        self.assertResultIsBOOL(
            TestCHHapticPatternPlayerHelper.sendParameters_atTime_error_
        )
        self.assertArgIsOut(
            TestCHHapticPatternPlayerHelper.sendParameters_atTime_error_, 2
        )

        self.assertResultIsBOOL(
            TestCHHapticPatternPlayerHelper.scheduleParameterCurve_atTime_error_
        )
        self.assertArgIsOut(
            TestCHHapticPatternPlayerHelper.scheduleParameterCurve_atTime_error_, 2
        )

        self.assertResultIsBOOL(TestCHHapticPatternPlayerHelper.cancelAndReturnError_)
        self.assertArgIsOut(TestCHHapticPatternPlayerHelper.cancelAndReturnError_, 0)

        self.assertResultIsBOOL(TestCHHapticPatternPlayerHelper.isMuted)
        self.assertArgIsBOOL(TestCHHapticPatternPlayerHelper.setIsMuted_, 0)

        # CHHapticAdvancedPatternPlayer
        self.assertResultIsBOOL(TestCHHapticPatternPlayerHelper.pauseAtTime_error_)
        self.assertArgHasType(
            TestCHHapticPatternPlayerHelper.pauseAtTime_error_, 0, objc._C_DBL
        )
        self.assertArgIsOut(TestCHHapticPatternPlayerHelper.pauseAtTime_error_, 1)

        self.assertResultIsBOOL(TestCHHapticPatternPlayerHelper.resumeAtTime_error_)
        self.assertArgHasType(
            TestCHHapticPatternPlayerHelper.resumeAtTime_error_, 0, objc._C_DBL
        )
        self.assertArgIsOut(TestCHHapticPatternPlayerHelper.resumeAtTime_error_, 1)

        self.assertResultIsBOOL(TestCHHapticPatternPlayerHelper.seekToOffset_error_)
        self.assertArgHasType(
            TestCHHapticPatternPlayerHelper.seekToOffset_error_, 0, objc._C_DBL
        )
        self.assertArgIsOut(TestCHHapticPatternPlayerHelper.seekToOffset_error_, 1)

        self.assertResultIsBOOL(TestCHHapticPatternPlayerHelper.loopEnabled)
        self.assertArgIsBOOL(TestCHHapticPatternPlayerHelper.setLoopEnabled_, 0)

        self.assertResultHasType(TestCHHapticPatternPlayerHelper.loopEnd, objc._C_DBL)
        self.assertArgHasType(
            TestCHHapticPatternPlayerHelper.setLoopEnd_, 0, objc._C_DBL
        )

        self.assertResultHasType(
            TestCHHapticPatternPlayerHelper.playbackRate, objc._C_FLT
        )
        self.assertArgHasType(
            TestCHHapticPatternPlayerHelper.setPlaybackRate_, 0, objc._C_FLT
        )

        self.assertResultIsBOOL(TestCHHapticPatternPlayerHelper.isMuted)
        self.assertArgIsBOOL(TestCHHapticPatternPlayerHelper.setIsMuted_, 0)

        self.assertResultIsBlock(
            TestCHHapticPatternPlayerHelper.completionHandler,
            CHHapticAdvancedPatternPlayerCompletionHandler,
        )
        self.assertArgIsBlock(
            TestCHHapticPatternPlayerHelper.setCompletionHandler_,
            0,
            CHHapticAdvancedPatternPlayerCompletionHandler,
        )
