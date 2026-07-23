// LCOV_EXCL_START
// This function is only present to ensure protocols are
// available at runtime.

static void __attribute__((__used__))
use_protocols(void)
{
#if PyObjC_BUILD_RELEASE >= 1012
    PyObject* p __attribute__((__unused__));
    p = PyObjC_IdToPython(@protocol(PHLivePhotoFrame));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1013
    p = PyObjC_IdToPython(@protocol(PHPhotoLibraryChangeObserver));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1015
    p = PyObjC_IdToPython(@protocol(PHPhotoLibraryAvailabilityObserver));
    Py_XDECREF(p);
#endif
}

// LCOV_EXCL_STOP
