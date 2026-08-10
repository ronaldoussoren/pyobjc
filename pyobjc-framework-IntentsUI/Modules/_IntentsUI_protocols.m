// LCOV_EXCL_START
// This function is only present to ensure protocols are
// available at runtime.
NS_ASSUME_NONNULL_BEGIN

static void __attribute__((__used__))
use_protocols(void)
{
#if PyObjC_BUILD_RELEASE >= 1200
    PyObject* p;
    p = PyObjC_IdToPython(@protocol(INUIEditVoiceShortcutViewControllerDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(INUIAddVoiceShortcutButtonDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(INUIAddVoiceShortcutViewControllerDelegate));
    Py_XDECREF(p);
#endif
}

NS_ASSUME_NONNULL_END
// LCOV_EXCL_STOP
