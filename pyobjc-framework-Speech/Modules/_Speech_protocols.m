// LCOV_EXCL_START
// This function is only present to ensure protocols are
// available at runtime.
NS_ASSUME_NONNULL_BEGIN

static void __attribute__((__used__))
use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
    p = PyObjC_IdToPython(@protocol(SFSpeechRecognitionTaskDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(SFSpeechRecognizerDelegate));
    Py_XDECREF(p);
}

NS_ASSUME_NONNULL_END
// LCOV_EXCL_STOP
