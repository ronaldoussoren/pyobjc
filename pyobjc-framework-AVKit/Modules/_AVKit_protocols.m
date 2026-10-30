// LCOV_EXCL_START
// This function is only present to ensure protocols are
// available at runtime.

NS_ASSUME_NONNULL_BEGIN

static void __attribute__((__used__))
use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1010
    p = PyObjC_IdToPython(@protocol(AVCaptureViewDelegate));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1015
    p = PyObjC_IdToPython(@protocol(AVPictureInPictureControllerDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(AVPlayerViewPictureInPictureDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(AVRoutePickerViewDelegate));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1200
    p = PyObjC_IdToPython(@protocol(AVPlayerViewDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(AVPictureInPictureSampleBufferPlaybackDelegate));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 2604
    p = PyObjC_IdToPython(@protocol(AVLegibleMediaOptionsMenuControllerDelegate));
    Py_XDECREF(p);
#endif
}

NS_ASSUME_NONNULL_END

// LCOV_EXCL_STOP
