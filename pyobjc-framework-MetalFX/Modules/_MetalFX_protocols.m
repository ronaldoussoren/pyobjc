// LCOV_EXCL_START
// This function is only present to ensure protocols are
// available at runtime.

static void __attribute__((__used__))
use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1300
    p = PyObjC_IdToPython(@protocol(MTLFXSpatialScaler));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLFXTemporalScaler));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1300 */
#if PyObjC_BUILD_RELEASE >= 2600
    p = PyObjC_IdToPython(@protocol(MTL4FXFrameInterpolator));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTL4FXSpatialScaler));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTL4FXTemporalDenoisedScaler));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTL4FXTemporalScaler));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLFXFrameInterpolatorBase));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLFXFrameInterpolator));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLFXSpatialScalerBase));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLFXTemporalDenoisedScalerBase));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLFXTemporalDenoisedScaler));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLFXTemporalScalerBase));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 2600 */
}

// LCOV_EXCL_STOP
