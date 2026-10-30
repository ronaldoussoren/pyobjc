// LCOV_EXCL_START
// This function is only present to ensure protocols are
// available at runtime.
NS_ASSUME_NONNULL_BEGIN

static void __attribute__((__used__))
use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1300
    p = PyObjC_IdToPython(@protocol(HKLiveWorkoutBuilderDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(HKWorkoutSessionDelegate));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1300 */
}

NS_ASSUME_NONNULL_END
// LCOV_EXCL_STOP
