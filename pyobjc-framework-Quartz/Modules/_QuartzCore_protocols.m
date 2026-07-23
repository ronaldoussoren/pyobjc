// LCOV_EXCL_START
// This function is only present to ensure protocols are
// available at runtime.

static void __attribute__((__used__))
use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1012
    p = PyObjC_IdToPython(@protocol(CIPlugInRegistration));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CAAnimationDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CALayerDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CALayoutManager));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIImageProcessorInput));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIImageProcessorOutput));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1012 */
#if PyObjC_BUILD_RELEASE >= 1400
    p = PyObjC_IdToPython(@protocol(CAMetalDisplayLinkDelegate));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1400 */
#if PyObjC_BUILD_RELEASE >= 1500
    p = PyObjC_IdToPython(@protocol(CIMaximumScaleTransform));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIToneMapHeadroom));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIAreaBoundsRed));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1400 */
}

// LCOV_EXCL_STOP
