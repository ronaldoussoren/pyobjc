static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1015
    p = PyObjC_IdToPython(@protocol(ASAuthorizationControllerDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(
        @protocol(ASAuthorizationControllerPresentationContextProviding));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(ASAuthorizationCredential));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(ASAuthorizationProvider));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(ASWebAuthenticationPresentationContextProviding));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(ASWebAuthenticationSessionRequestDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(ASWebAuthenticationSessionWebBrowserSessionHandling));
    Py_XDECREF(p);
#endif
}
