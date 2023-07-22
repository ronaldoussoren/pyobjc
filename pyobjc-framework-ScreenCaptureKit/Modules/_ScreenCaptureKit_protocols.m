static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
    p = PyObjC_IdToPython(@protocol(SCStreamDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(SCStreamOutput));
    Py_XDECREF(p);
#if PyObjC_BUILD_RELEASE >= 1400
    p = PyObjC_IdToPython(@protocol(SCContentSharingPickerObserver));
    Py_XDECREF(p);
#endif
}
