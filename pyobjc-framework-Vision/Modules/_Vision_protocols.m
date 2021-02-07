static void __attribute__((__used__)) use_protocols(void)
{
#if PyObjC_BUILD_RELEASE >= 1013
    PyObject* p;
    p = PyObjC_IdToPython(@protocol(VNFaceObservationAccepting));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1014
    p = PyObjC_IdToPython(@protocol(VNRequestRevisionProviding));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1015
    p = PyObjC_IdToPython(@protocol(VNRequestProgressProviding));
    Py_XDECREF(p);
#endif
}
