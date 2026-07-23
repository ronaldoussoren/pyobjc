// LCOV_EXCL_START
// This function is only present to ensure protocols are
// available at runtime.

static void __attribute__((__used__))
use_protocols(void)
{
#if PyObjC_BUILD_RELEASE >= 1012
    PyObject* p;
    p = PyObjC_IdToPython(@protocol(NSFetchedResultsControllerDelegate));
    Py_XDECREF(p);
#endif
}

// LCOV_EXCL_STOP
