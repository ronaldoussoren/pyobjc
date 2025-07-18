/*
 * This file is generated by objective.metadata
 *
 * Last update: Wed Jan 16 13:10:52 2013
 */

static void __attribute__((__used__))
use_protocols(void)
{
#if PyObjC_BUILD_RELEASE >= 1012
    PyObject* p;
    p = PyObjC_IdToPython(@protocol(INSearchCallHistoryIntentHandling));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(INSearchForMessagesIntentHandling));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(INSendMessageIntentHandling));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(INSpeakable));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(INStartAudioCallIntentHandling));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(INStartVideoCallIntentHandling));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1200
    p = PyObjC_IdToPython(@protocol(INStartCallIntentHandling));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(INShareFocusStatusIntentHandling));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1301
    p = PyObjC_IdToPython(@protocol(INHangUpCallIntentHandling));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(INAnswerCallIntentHandling));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1400
    p = PyObjC_IdToPython(@protocol(INUnsendMessagesIntentHandling));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(INEditMessageIntentHandling));
    Py_XDECREF(p);
#endif
}
