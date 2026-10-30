// LCOV_EXCL_START
// This function is only present to ensure protocols are
// available at runtime.

#import <CryptoTokenKit/CryptoTokenKit.h>
NS_ASSUME_NONNULL_BEGIN
static void __attribute__((__used__))
use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1011
    p = PyObjC_IdToPython(@protocol(TKSmartCardUserInteractionDelegate));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1012
    p = PyObjC_IdToPython(@protocol(TKSmartCardTokenDriverDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(TKTokenSessionDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(TKTokenDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(TKTokenDriverDelegate));
    Py_XDECREF(p);
#endif
}
NS_ASSUME_NONNULL_END
// LCOV_EXCL_STOP
