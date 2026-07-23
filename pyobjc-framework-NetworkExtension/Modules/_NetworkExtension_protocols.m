// LCOV_EXCL_START
// This function is only present to ensure protocols are
// available at runtime.

static void __attribute__((__used__))
use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1011
    p = PyObjC_IdToPython(@protocol(NWTCPConnectionAuthenticationDelegate));
    Py_XDECREF(p);
#endif
}

// LCOV_EXCL_STOP
