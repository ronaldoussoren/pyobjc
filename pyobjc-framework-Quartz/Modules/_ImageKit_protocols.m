// LCOV_EXCL_START
// This function is only present to ensure protocols are
// available at runtime.

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

// LCOV_EXCL_STOP
