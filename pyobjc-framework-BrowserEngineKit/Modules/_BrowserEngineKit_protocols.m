// LCOV_EXCL_START
// This function is only present to ensure protocols are
// available at runtime.
NS_ASSUME_NONNULL_BEGIN
static void __attribute__((__used__))
use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1404
    p = PyObjC_IdToPython(@protocol(BEProcessCapabilityGrant));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(BETextInputDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(BETextInteractionDelegate));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1404 */
#if PyObjC_BUILD_RELEASE >= 1502
    // Not exposed on macOS
    // p = PyObjC_IdToPython(@protocol(BEAccessibilityTextMarker)); Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1502 */
#if PyObjC_BUILD_RELEASE >= 2600
    p = PyObjC_IdToPython(@protocol(BEExtensionProcess));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 2600 */
}
NS_ASSUME_NONNULL_END
// LCOV_EXCL_STOP
