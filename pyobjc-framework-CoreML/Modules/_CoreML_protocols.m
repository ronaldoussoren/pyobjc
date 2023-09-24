static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1013 && defined(__x86_64__)
    p = PyObjC_IdToPython(@protocol(MLFeatureProvider));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MLCustomLayer));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1014 && defined(__x86_64__)
    p = PyObjC_IdToPython(@protocol(MLCustomModel));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MLBatchProvider));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1015 && defined(__x86_64__)
    p = PyObjC_IdToPython(@protocol(MLWritable));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1400
    p = PyObjC_IdToPython(@protocol(MLComputeDeviceProtocol));
    Py_XDECREF(p);
#endif
}
