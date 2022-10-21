static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p;
    p = PyObjC_IdToPython(@protocol(SACrashDetectionDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(SAEmergencyResponseDelegate));
    Py_XDECREF(p);
}
