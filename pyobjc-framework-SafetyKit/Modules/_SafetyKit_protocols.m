// LCOV_EXCL_START
// This function is only present to ensure protocols are
// available at runtime.
NS_ASSUME_NONNULL_BEGIN

static void __attribute__((__used__))
use_protocols(void)
{
    PyObject* p;
    p = PyObjC_IdToPython(@protocol(SACrashDetectionDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(SAEmergencyResponseDelegate));
    Py_XDECREF(p);
}

NS_ASSUME_NONNULL_END
// LCOV_EXCL_STOP
