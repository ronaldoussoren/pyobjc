// LCOV_EXCL_START
// This function is only present to ensure protocols are
// available at runtime.

static void __attribute__((__used__))
use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1016
    p = PyObjC_IdToPython(@protocol(CXCallDirectoryExtensionContextDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CXCallObserverDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CXProviderDelegate));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1016 */
}

// LCOV_EXCL_STOP
