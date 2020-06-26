static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if 0
    p = PyObjC_IdToPython(@protocol(MTKViewDelegate));
    Py_XDECREF(p);
#endif

#if PyObjC_BUILD_RELEASE >= 1015
    p = PyObjC_IdToPython(@protocol(MTLCounter));
    Py_XDECREF(p);

    p = PyObjC_IdToPython(@protocol(MTLCounterSet));
    Py_XDECREF(p);

    p = PyObjC_IdToPython(@protocol(MTLCounterSampleBuffer));
    Py_XDECREF(p);

#endif
#if PyObjC_BUILD_RELEASE >= 1016
    p = PyObjC_IdToPython(@protocol(MTLBinaryArchive));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLDynamicLibrary));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLFunctionHandle));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLFunctionLogContainer));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLFunctionLogDebugLocation));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLFunctionLog));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLIntersectionFunctionTable));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLVisibleFunctionTable));
    Py_XDECREF(p);
#endif
}
