// LCOV_EXCL_START
// This function is only present to ensure protocols are
// available at runtime.
NS_ASSUME_NONNULL_BEGIN
static void __attribute__((__used__))
use_protocols(void)
{
#if PyObjC_BUILD_RELEASE >= 1300
    PyObject* p __attribute__((__unused__));
    p = PyObjC_IdToPython(@protocol(PDEPanel));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(PDEPlugInCallbackProtocol));
    Py_XDECREF(p);
#endif
}
NS_ASSUME_NONNULL_END
// LCOV_EXCL_STOP
