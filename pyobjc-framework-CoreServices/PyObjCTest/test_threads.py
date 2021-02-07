import CoreServices
from PyObjCTools.TestSupport import TestCase


class TestThreads(TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(
            not hasattr(CoreServices, name), "%r exposed in bindings" % (name,)
        )

    def test_not_wrapped(self):
        self.assert_not_wrapped("kReadyThreadState")
        self.assert_not_wrapped("kStoppedThreadState")
        self.assert_not_wrapped("kRunningThreadState")
        self.assert_not_wrapped("kCooperativeThread")
        self.assert_not_wrapped("kPreemptiveThread")
        self.assert_not_wrapped("kNoThreadID")
        self.assert_not_wrapped("kCurrentThreadID")
        self.assert_not_wrapped("kApplicationThreadID")
        self.assert_not_wrapped("kNewSuspend")
        self.assert_not_wrapped("kUsePremadeThread")
        self.assert_not_wrapped("kCreateIfNeeded")
        self.assert_not_wrapped("kFPUNotNeeded")
        self.assert_not_wrapped("kExactMatchThread")
        self.assert_not_wrapped("SchedulerInfoRec")
        self.assert_not_wrapped("NewThreadEntryUPP")
        self.assert_not_wrapped("NewThreadSchedulerUPP")
        self.assert_not_wrapped("NewThreadSwitchUPP")
        self.assert_not_wrapped("NewThreadTerminationUPP")
        self.assert_not_wrapped("NewDebuggerNewThreadUPP")
        self.assert_not_wrapped("NewDebuggerDisposeThreadUPP")
        self.assert_not_wrapped("NewDebuggerThreadSchedulerUPP")
        self.assert_not_wrapped("DisposeThreadEntryUPP")
        self.assert_not_wrapped("DisposeThreadSchedulerUPP")
        self.assert_not_wrapped("DisposeThreadSwitchUPP")
        self.assert_not_wrapped("DisposeThreadTerminationUPP")
        self.assert_not_wrapped("DisposeDebuggerNewThreadUPP")
        self.assert_not_wrapped("DisposeDebuggerDisposeThreadUPP")
        self.assert_not_wrapped("DisposeDebuggerThreadSchedulerUPP")
        self.assert_not_wrapped("InvokeThreadEntryUPP")
        self.assert_not_wrapped("InvokeThreadSchedulerUPP")
        self.assert_not_wrapped("InvokeThreadSwitchUPP")
        self.assert_not_wrapped("InvokeThreadTerminationUPP")
        self.assert_not_wrapped("InvokeDebuggerNewThreadUPP")
        self.assert_not_wrapped("InvokeDebuggerDisposeThreadUPP")
        self.assert_not_wrapped("InvokeDebuggerThreadSchedulerUPP")
        self.assert_not_wrapped("NewThread")
        self.assert_not_wrapped("SetThreadScheduler")
        self.assert_not_wrapped("SetThreadSwitcher")
        self.assert_not_wrapped("SetThreadTerminator")
        self.assert_not_wrapped("SetDebuggerNotificationProcs")
        self.assert_not_wrapped("CreateThreadPool")
        self.assert_not_wrapped("GetDefaultThreadStackSize")
        self.assert_not_wrapped("ThreadCurrentStackSpace")
        self.assert_not_wrapped("DisposeThread")
        self.assert_not_wrapped("YieldToThread")
        self.assert_not_wrapped("YieldToAnyThread")
        self.assert_not_wrapped("GetCurrentThread")
        self.assert_not_wrapped("MacGetCurrentThread")
        self.assert_not_wrapped("GetThreadState")
        self.assert_not_wrapped("SetThreadState")
        self.assert_not_wrapped("SetThreadStateEndCritical")
        self.assert_not_wrapped("ThreadBeginCritical")
        self.assert_not_wrapped("ThreadEndCritical")
        self.assert_not_wrapped("GetThreadCurrentTaskRef")
        self.assert_not_wrapped("GetThreadStateGivenTaskRef")
        self.assert_not_wrapped("SetThreadReadyGivenTaskRef")
        self.assert_not_wrapped("GetFreeThreadCount")
        self.assert_not_wrapped("GetSpecificFreeThreadCount")
