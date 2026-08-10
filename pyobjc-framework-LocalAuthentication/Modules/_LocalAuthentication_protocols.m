// LCOV_EXCL_START
// This function is only present to ensure protocols are
// available at runtime.
NS_ASSUME_NONNULL_BEGIN

static void __attribute__((__used__))
use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1500
    p = PyObjC_IdToPython(@protocol(LAEnvironmentObserver));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1500 */
}

NS_ASSUME_NONNULL_END
// LCOV_EXCL_STOP
