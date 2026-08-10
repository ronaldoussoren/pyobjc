// LCOV_EXCL_START
// This function is only present to ensure protocols are
// available at runtime.
NS_ASSUME_NONNULL_BEGIN
static void __attribute__((__used__))
use_protocols(void)
{
#if PyObjC_BUILD_RELEASE >= 1300
    PyObject* p;
    p = PyObjC_IdToPython(@protocol(CMWaterSubmersionManagerDelegate));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1400
    p = PyObjC_IdToPython(@protocol(CMHeadphoneMotionManagerDelegate));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 2700
    p = PyObjC_IdToPython(@protocol(CMBodyIdentifiable));
    Py_XDECREF(p);
#endif
}
NS_ASSUME_NONNULL_END
// LCOV_EXCL_STOP
