// LCOV_EXCL_START
// This function is only present to ensure protocols are
// available at runtime.
NS_ASSUME_NONNULL_BEGIN

static void __attribute__((__used__))
use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1011
    p = PyObjC_IdToPython(@protocol(PHContentEditingController));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1011 */
#if PyObjC_BUILD_RELEASE >= 1012
    p = PyObjC_IdToPython(@protocol(PHLivePhotoViewDelegate));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1012 */
#if PyObjC_BUILD_RELEASE >= 1013
    p = PyObjC_IdToPython(@protocol(PHProjectExtensionController));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1013 */
#if PyObjC_BUILD_RELEASE >= 1014
    p = PyObjC_IdToPython(@protocol(PHProjectTypeDescriptionDataSource));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(PHProjectTypeDescriptionInvalidator));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1014 */
#if PyObjC_BUILD_RELEASE >= 1300
    p = PyObjC_IdToPython(@protocol(PHPickerViewControllerDelegate));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1300 */
#if PyObjC_BUILD_RELEASE >= 2700
    p = PyObjC_IdToPython(@protocol(PHSharedAlbumCreationViewControllerDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(PHSharedAlbumCustomizationViewControllerDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(PHSharedAlbumPostingViewControllerDelegate));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 2700 */
}

NS_ASSUME_NONNULL_END
// LCOV_EXCL_STOP
