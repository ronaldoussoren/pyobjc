static void __attribute__((__used__)) use_protocols(void)
{
#if PyObjC_BUILD_RELEASE >= 1200
    PyObject* p;
    p = PyObjC_IdToPython(@protocol(MXMetricManagerSubscriber));
    Py_XDECREF(p);
#endif
}
