#import <AddressBook/ABPersonPickerDelegate.h>

static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
    p = PyObjC_IdToPython(@protocol(GKAchievementViewControllerDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(GKChallengeEventHandlerDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(GKChallengesViewControllerDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(GKChallengeListener)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(GKFriendRequestComposeViewControllerDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(GKGameCenterControllerDelegate)); Py_XDECREF(p);

#if PyObjC_BUILD_RELEASE >= 1012
    p = PyObjC_IdToPython(@protocol(GKGameSessionEventListener)); Py_XDECREF(p);
#endif
    p = PyObjC_IdToPython(@protocol(GKLeaderboardViewControllerDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(GKLocalPlayerListener)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(GKMatchDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(GKInviteEventListener)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(GKMatchmakerViewControllerDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(GKSessionDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(GKVoiceChatClient)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(GKSavedGameListener)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(GKTurnBasedEventListener)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(GKTurnBasedMatchmakerViewControllerDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(GKTurnBasedEventHandlerDelegate)); Py_XDECREF(p);
}
