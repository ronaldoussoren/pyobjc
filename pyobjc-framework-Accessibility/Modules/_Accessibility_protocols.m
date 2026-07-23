// LCOV_EXCL_START
// This function is only present to ensure protocols are
// available at runtime.

static void __attribute__((__used__))
use_protocols(void)
{
    PyObject* p;
#if PyObjC_BUILD_RELEASE >= 1016
    p = PyObjC_IdToPython(@protocol(AXCustomContentProvider));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1200
    p = PyObjC_IdToPython(@protocol(AXChart));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(AXDataAxisDescriptor));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 2600
    p = PyObjC_IdToPython(@protocol(AXBrailleMapRenderer));
    Py_XDECREF(p);
#endif
}

// LCOV_EXCL_STOP
