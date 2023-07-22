static void __attribute__((__used__)) use_protocols(void)
{
#if PyObjC_BUILD_RELEASE >= 1300
    PyObject* p;
    p = PyObjC_IdToPython(@protocol(CMWaterSubmersionManagerDelegate));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1400
    p = PyObjC_IdToPython(@protocol(CMHeadphoneMotionManagerDelegate));
    Py_XDECREF(p);
#endif
}
