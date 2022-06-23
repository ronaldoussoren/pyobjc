static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1012
    p = PyObjC_IdToPython(@protocol(PDFViewDelegate));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1013
    p = PyObjC_IdToPython(@protocol(PDFDocumentDelegate));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1300
    // p = PyObjC_IdToPython(@protocol(PDFPageOverlayViewProvider));
    // Py_XDECREF(p);
#endif
}
