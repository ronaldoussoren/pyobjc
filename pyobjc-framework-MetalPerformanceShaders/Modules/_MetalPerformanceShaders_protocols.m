// LCOV_EXCL_START
// This function is only present to ensure protocols are
// available at runtime.
NS_ASSUME_NONNULL_BEGIN

static void __attribute__((__used__))
use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1013
    p = PyObjC_IdToPython(@protocol(MPSCNNBatchNormalizationDataSource));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MPSCNNInstanceNormalizationDataSource));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MPSHandle));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1015
    p = PyObjC_IdToPython(@protocol(MPSNDArrayAllocator));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MPSCNNGroupNormalizationDataSource));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MPSHeapProvider));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MPSNNGramMatrixCallback));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MPSNNLossCallback));
    Py_XDECREF(p);
#endif
}

NS_ASSUME_NONNULL_END
// LCOV_EXCL_STOP
