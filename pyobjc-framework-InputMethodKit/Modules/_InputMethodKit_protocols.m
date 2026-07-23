// LCOV_EXCL_START
// This function is only present to ensure protocols are
// available at runtime.

static void __attribute__((__used__))
use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
    p = PyObjC_IdToPython(@protocol(IMKMouseHandling));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(IMKStateSetting));
    Py_XDECREF(p);
}

// LCOV_EXCL_STOP
