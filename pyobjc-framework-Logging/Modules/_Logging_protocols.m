static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1015
    p = PyObjC_IdToPython(@protocol(OSLogEntryFromProcess)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(OSLogEntryWithPayload)); Py_XDECREF(p);
#endif
}
