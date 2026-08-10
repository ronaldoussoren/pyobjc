// LCOV_EXCL_START
// This function is only present to ensure protocols are
// available at runtime.
NS_ASSUME_NONNULL_BEGIN

static void __attribute__((__used__))
use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1010

    p = PyObjC_IdToPython(@protocol(IKCameraDeviceViewDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(IKDeviceBrowserViewDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(IKScannerDeviceViewDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(IKFilterCustomUIProvider));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(IKImageEditPanelDataSource));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(IKSlideshowDataSource));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1010 */
}

NS_ASSUME_NONNULL_END
// LCOV_EXCL_STOP
